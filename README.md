# just-logger

A logging tool is used to record all kinds of logs during program running.

# demo

```python
# Initialize.
logger = Logger('demo', level=LogLevel.DEBUG) # global log-level
logger.add_stream_handler(LogLevel.DEBUG) # log-level for console base on global level
logger.add_file_handler('demo.log', LogLevel.INFO) # log-level for log file base on global level

logger.log('Hello world!', LogLevel.INFO)
logger.log('Caution please!', LogLevel.WARNING)
logger.log('Error was found!', LogLevel.ERROR)
logger.log('Fatal error!', LogLevel.CRITICAL)
logger.log('Debugger!', LogLevel.DEBUG) # Cannot be recorded in log file, but can be showed on console.
obj = {
    'code': 0,
    'message': 'success',
    'data': {
        'content': 'only for testing.'
    }
}
logger.log(json.dumps(obj, ensure_ascii=False, indent=4), LogLevel.INFO)
```
