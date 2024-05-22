import threading
from logger.logger import Logger
import unittest
import os

def log_messages(logger, level, message, count=10):
    for _ in range(count):
        logger.log(level, __name__, 'log_messages', threading.get_ident(), message)

def main():
    log_file_path = 'logs/app.log'
    logger = Logger(log_file_path)

    # Logging different levels
    logger.debug(__name__, 'main', threading.get_ident(), 'This is a debug message.')
    logger.info(__name__, 'main', threading.get_ident(), 'This is an info message.')
    logger.error(__name__, 'main', threading.get_ident(), 'This is an error message.')

    # Creating threads to test thread safety
    threads = [
        threading.Thread(target=log_messages, args=(logger, 'INFO', 'Thread-safe log message', 100)),
        threading.Thread(target=log_messages, args=(logger, 'ERROR', 'Thread-safe error message', 100))
    ]

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    # Running tests
    print("Running tests...")
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner().run(tests)

if __name__ == '__main__':
    main()