import os
import sys
sys.path.append(os.getcwd())
from just_logger import Logger, LogLevel

if __name__ == '__main__':
    logger = Logger('demo', level=LogLevel.INFO)
    logger.add_stream_handler(LogLevel.INFO)
    logger.add_file_handler('demo.log', LogLevel.INFO)
    logger.log('hello world!', LogLevel.INFO)
    logger.log('caution please!', LogLevel.WARNING)
    logger.log('bad man!', LogLevel.ERROR)
    logger.log('fatal error!', LogLevel.CRITICAL)
    logger.log('debugger!', LogLevel.DEBUG) # Cannot be recorded by level "INFO".
    pass