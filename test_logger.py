import unittest
import os
import time
from logger.logger import Logger
import threading

class TestLogger(unittest.TestCase):
    def setUp(self):
        self.log_file_path = 'logs/test.log'
        if not os.path.exists('logs'):
            os.makedirs('logs')
        self.logger = Logger(self.log_file_path)

    def tearDown(self):
        for i in range(11):
            log_file = f'{self.log_file_path}.{i}'
            if os.path.exists(log_file):
                try:
                    os.remove(log_file)
                except PermissionError:
                    pass

    def test_log_rotation(self):
        large_message = "x" * (5 * 1024 * 1024 // 10)
        for _ in range(15):
            self.logger.info(__name__, 'test_log_rotation', threading.get_ident(), large_message)

        # Wait for a moment to ensure all writes are flushed and files are closed
        time.sleep(1)

        log_files = [f for f in os.listdir('logs') if f.startswith('test.log')]
        self.assertEqual(len(log_files), 10)

    def test_thread_safety(self):
        def log_messages():
            for _ in range(100):
                self.logger.info(__name__, 'test_thread_safety', threading.get_ident(), "Thread-safe log message")

        threads = [threading.Thread(target=log_messages) for _ in range(10)]
        for thread in threads:
            thread.start()
        for thread in threads:
            thread.join()

        # Wait for a moment to ensure all writes are flushed and files are closed
        time.sleep(1)

        log_files = [f for f in os.listdir('logs') if f.startswith('test.log')]
        self.assertGreaterEqual(len(log_files), 1)

if __name__ == '__main__':
    unittest.main()