import os
import threading
from datetime import datetime

class LogFile:
    def __init__(self, log_file_path, max_size, backup_count):
        self.log_file_path = log_file_path
        self.max_size = max_size
        self.backup_count = backup_count
        self.current_size = 0
        self.lock = threading.Lock()
        self.current_file_index = 0
        self._open_new_file()

    def _open_new_file(self):
        self.current_file_path = f"{self.log_file_path}.{self.current_file_index}"
        self.file = open(self.current_file_path, 'a')
        self.current_size = os.path.getsize(self.current_file_path)

    def _rotate_files(self):
        self.file.close()  # Close the current log file
        with self.lock:
            for i in range(self.backup_count - 1, 0, -1):
                old_file = f"{self.log_file_path}.{i}"
                new_file = f"{self.log_file_path}.{i+1}"
                if os.path.exists(old_file):
                    os.rename(old_file, new_file)
            os.rename(self.current_file_path, f"{self.log_file_path}.1")
        self.current_file_index = 0
        self._open_new_file()  # Open a new log file for writing

    def write(self, message):
        with self.lock:
            if self.current_size + len(message) > self.max_size:
                self._rotate_files()
            self.file.write(message)
            self.file.flush()
            self.current_size += len(message)

    def __del__(self):
        self.file.close()


class Logger:
    def __init__(self, log_file_path):
        self.log_file = LogFile(log_file_path, max_size=5 * 1024 * 1024, backup_count=10)

    def log(self, level, filename, funcname, thread_id, message):
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        log_message = f"{timestamp} - {level} - {filename} - {funcname} - {thread_id} - {message}\n"
        self.log_file.write(log_message)

    def debug(self, filename, funcname, thread_id, message):
        self.log('DEBUG', filename, funcname, thread_id, message)

    def info(self, filename, funcname, thread_id, message):
        self.log('INFO', filename, funcname, thread_id, message)

    def error(self, filename, funcname, thread_id, message):
        self.log('ERROR', filename, funcname, thread_id, message)