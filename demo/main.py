import json
import os
import sys
sys.path.append(os.getcwd())
from just_logger import Logger, LogLevel, LogSplitType

def demo_time_based_logger():
    logger = Logger('demo', level=LogLevel.INFO)
    logger.add_stream_handler(LogLevel.INFO)
    logger.add_file_handler('demo.log', LogLevel.INFO)
    logger.log('Hello world!', LogLevel.INFO)
    logger.log('Caution please!', LogLevel.WARNING)
    logger.log('Error was found!', LogLevel.ERROR)
    logger.log('Fatal error!', LogLevel.CRITICAL)
    logger.log('Debugger!', LogLevel.DEBUG) # Cannot be recorded by level "INFO".
    obj = {
        'code': 0,
        'message': 'success',
        'data': {
            'content': 'only for testing.'
        }
    }
    logger.log(json.dumps(obj, ensure_ascii=False, indent=4), LogLevel.INFO)


def demo_size_based_logger():
    logger = Logger('demo_size', level=LogLevel.INFO, split_type=LogSplitType.Size)
    logger.add_stream_handler(LogLevel.INFO)
    logger.add_file_handler('demo_size.log', LogLevel.INFO, options={ 'backup_count': 3 })
    logger.log('Hello world!', LogLevel.INFO)
    logger.log('Caution please!', LogLevel.WARNING)
    logger.log('Error was found!', LogLevel.ERROR)
    logger.log('Fatal error!', LogLevel.CRITICAL)
    logger.log('Debugger!', LogLevel.DEBUG) # Cannot be recorded by level "INFO".
    obj = {
        'code': 0,
        'message': 'success',
        'data': {
            'content': 'only for testing.'
        }
    }
    logger.log(json.dumps(obj, ensure_ascii=False, indent=4), LogLevel.INFO)

    logger2 = Logger('demo_size', level=LogLevel.INFO, split_type=LogSplitType.Size)
    logger2.add_stream_handler(LogLevel.INFO)
    logger2.add_file_handler('demo_size.log', LogLevel.INFO, options={ 'backup_count': 3 })
    logger2.log('Hello world!', LogLevel.INFO)
    logger2.log('Caution please!', LogLevel.WARNING)
    logger2.log('Error was found!', LogLevel.ERROR)
    logger2.log('Fatal error!', LogLevel.CRITICAL)
    logger2.log('Debugger!', LogLevel.DEBUG) # Cannot be recorded by level "INFO".
    obj = {
        'code': 0,
        'message': 'success',
        'data': {
            'content': 'only for testing.'
        }
    }
    logger2.log(json.dumps(obj, ensure_ascii=False, indent=4), LogLevel.INFO)


if __name__ == '__main__':
    demo_size_based_logger()
    pass