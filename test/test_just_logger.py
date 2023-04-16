#!python
# -*- coding: utf-8 -*-
'''
@File: test_just_logger.py
@Date: 2023/04/16 11:01:19
@Version: 1.0
@Description: Unit-test on just-logger
'''

from datetime import datetime
from just_logger import Logger, LogLevel
from unittest.case import TestCase

import re
import time


class VerifyJustLogger(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        return super().setUpClass()


    @classmethod
    def tearDownClass(cls) -> None:
        return super().tearDownClass()
    

    def setUp(self) -> None:
        self.datetime_pattern = '[0-9]{4}/[0-9]{2}/[0-9]{2} [0-9]{2}:[0-9]{2}:[0-9]{2}'
        self.logger_name = 'test'
        return super().setUp()
    

    def tearDown(self) -> None:
        return super().tearDown()
    

    def test_just_logger(self) -> None:
        # Initialize.
        logger = Logger(self.logger_name, level=LogLevel.DEBUG) # set log-level globally
        logger.add_stream_handler(LogLevel.DEBUG) # set log-level for console only base on global settings
        logger.add_file_handler(f"{self.logger_name}.log", LogLevel.INFO) # set log-level for log file base on global settings

        current = datetime.now().strftime('%Y/%m/%d %H:%M:%S')
        logger.log('Hello world!', LogLevel.INFO)
        log_recs = self.__search_logs(current)
        self.assertTrue(log_recs[0].endswith('- INFO] Hello world!\n'))
        time.sleep(1)

        current = datetime.now().strftime('%Y/%m/%d %H:%M:%S')
        logger.log('Caution please!', LogLevel.WARNING)
        log_recs = self.__search_logs(current)
        self.assertTrue(log_recs[0].endswith('- WARNING] Caution please!\n'))
        time.sleep(1)

        current = datetime.now().strftime('%Y/%m/%d %H:%M:%S')
        logger.log('Error was found!', LogLevel.ERROR)
        log_recs = self.__search_logs(current)
        self.assertTrue(log_recs[0].endswith('- ERROR] Error was found!\n'))
        time.sleep(1)

        current = datetime.now().strftime('%Y/%m/%d %H:%M:%S')
        logger.log('Fatal error!', LogLevel.CRITICAL)
        log_recs = self.__search_logs(current)
        self.assertTrue(log_recs[0].endswith('- CRITICAL] Fatal error!\n'))
        time.sleep(1)

        current = datetime.now().strftime('%Y/%m/%d %H:%M:%S')
        logger.log('Debugger!', LogLevel.DEBUG) # it will show on console, but will not record it in log file
        log_recs = self.__search_logs(current)
        self.assertEquals(0, len(log_recs))
    

    def __search_logs(self, curr_time: str) -> list[str]:
        lines = None
        with open(f"logs/{self.logger_name}.log", 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        log_recs = []
        if lines is not None:
            for line in lines:
                res = re.search(self.datetime_pattern, line)
                fnd = res.group() if res is not None else ''
                if fnd >= curr_time:
                    log_recs.append(line)
        
        return log_recs