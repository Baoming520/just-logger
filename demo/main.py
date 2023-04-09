import os
import sys
sys.path.append(os.getcwd())
from just_logger import Logger, LogLevel

if __name__ == '__main__':
    logger = Logger('demo', LogLevel.INFO)
    logger.add_stream_handler(LogLevel.INFO)
    logger.add_file_handler('demo.log', LogLevel.INFO)
    logger.log('hello world!', LogLevel.INFO)
    logger.log('bad man!', LogLevel.ERROR)
    pass