import json
import os
import sys
sys.path.append(os.getcwd())
from just_logger import Logger, LogLevel

if __name__ == '__main__':
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
    pass