#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@File: logger.py
@Date: 2021/12/24 17:45:59
@Version: 1.0
@Description: A logging tool is used to record all kinds of logs during program running.
'''

from enum import Enum

import datetime
import logging
import logging.handlers
import os
import platform


class LogLevel(Enum):
    DEBUG = logging.DEBUG
    INFO = logging.INFO
    WARNING = logging.WARNING
    ERROR = logging.ERROR
    CRITICAL = logging.CRITICAL


class LogSplitType(Enum):
    Time = 1
    Size = 2


class Logger:
    def __init__(self, logger_name: str, log_dir: str=None, level: LogLevel=LogLevel.INFO, split_type: LogSplitType=LogSplitType.Time) -> None:
        self.__sptr = '/'
        if platform.system() == 'windows':
            self.__sptr = '\\'
        
        if log_dir is None:
            self.__logdir = os.path.join(os.getcwd(), 'logs') 
        else:
            self.__logdir = log_dir

        self.__logger = logging.getLogger(logger_name)
        self.__logger.setLevel(level.value)
        fmt = '[%(asctime)s - %(levelname)s] %(message)s'
        datefmt = '%Y/%m/%d %H:%M:%S %p'
        self.__formatter = logging.Formatter(fmt=fmt, datefmt=datefmt)
        self.__split_type = split_type
        self.__func = logging.handlers.TimedRotatingFileHandler if split_type == LogSplitType.Time else logging.handlers.RotatingFileHandler
    

    def __del__(self) -> None:
        print('Dispose all the resource.')


    def add_stream_handler(self, level: LogLevel=LogLevel.DEBUG) -> None:
        if self.__contains_handler(logging.StreamHandler):
            return

        handler = logging.StreamHandler()
        handler.setLevel(level.value)
        handler.setFormatter(self.__formatter)
        self.__logger.addHandler(handler)

    
    def add_file_handler(self, logfile: str, level: LogLevel=LogLevel.WARNING, options: dict=None) -> None:
        if self.__contains_handler(self.__func):
            return
        
        if options is None:
            options = {}
        if 'storage_days' not in options:
            options['storage_days'] = 30
        if 'backup_count' not in options:
            options['backup_count'] = 30
        if 'max_bytes' not in options:
            options['max_bytes'] = 1024 * 1024

        if not os.path.exists(self.__logdir):
            os.makedirs(self.__logdir)
        logfile = f'{self.__logdir}{self.__sptr}{logfile}'

        if self.__split_type == LogSplitType.Time:
            handler = self.__func(
                logfile, 
                when='MIDNIGHT', 
                interval=1, 
                atTime=datetime.time(0, 0, 0, 0), 
                encoding='utf-8')
        else:
            handler = self.__func(
                logfile,
                maxBytes=options['max_bytes'],
                backupCount=options['backup_count'], # 存储日志的最大数量
                encoding='utf-8')
        
        handler.setLevel(level.value)
        handler.setFormatter(self.__formatter)
        self.__logger.addHandler(handler)

    
    def log(self, message: str, level: LogLevel=LogLevel.WARNING) -> None:
        if '\n' in message:
            msg_parts = message.split('\n')
            for msg in msg_parts:
                self.log(msg, level)
        else:
            if level == LogLevel.DEBUG:
                self.__logger.debug(message)
            elif level == LogLevel.INFO:
                self.__logger.info(message)
            elif level == LogLevel.WARNING:
                self.__logger.warning(message)
            elif level == LogLevel.ERROR:
                self.__logger.error(message)
            else: # level == LogLevel.CRITICAL
                self.__logger.critical(message)
    

    def __contains_handler(self, handler_type: type):
        if not self.__logger.handlers:
            return False
        else:
            for handler in self.__logger.handlers:
                if type(handler) == handler_type:
                    return True
            
            return False