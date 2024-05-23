# Overview
- This project implements a custom logger with log rotation, designed to be thread-safe and easily integrable into any codebase. 
# Features
- Logs messages with timestamp, log level, file name, function name, and thread ID.
- Rotates log files after they reach 5 MB, maintaining up to 10 backups.
- Thread-safe logging.

# Approach Used To Solve The Problem

  # The task was to create a robust logging system that supports:
      - Log Rotation: Automatically rotate log files when they exceed a specified size.
      - Thread Safety: Ensure that the logging operations are safe for concurrent access by multiple threads.
      - Configurable Backup Management: Maintain a configurable number of backup log files.
      - Support for Different Log Levels: Allow logging of messages with different severity levels (DEBUG, INFO, ERROR).

  # Design Decisions 

     # LogFile Class:
      - Handles the actual file operations, including writing messages, checking file sizes, and rotating log files.
      - Uses a lock (threading.Lock) to ensure that file operations are thread-safe.
      - Keeps track of the current file size to determine when rotation is necessary.
      
    # Logger Class:
      - Provides a high-level interface for logging messages.
      - Formats log messages with relevant information such as timestamp, log level, filename, function name, and thread ID.
      - Delegates the actual writing and rotation logic to the LogFile class.
      
# How to Test the Code
    1. Set Up Your Environment
      Ensure you have a directory structure similar to the following:
         logger-library/
         │
         ├── logger/
         │   └── logger.py
         ├── tests/
         │   └── test_logger.py
         └── main.py
    2. Prepare the Test Script
         -Create the test script test_logger.py in the tests directory. This script will use the unittest framework to test the Logger class.
    3. Prepare the Logger Class
    4. Running the Tests
         -To run the tests, execute the following command in your terminal from the root directory of your project (logger-library/):
                  python -m unittest discover -s tests
    5. Running the Main Application
          -You can also create a main script to use the logger and verify its behavior interactively. Place this in a file named main.py
          -Run the main application using the following command:
                  python main.py
          -This script will create log entries, spawn threads to test thread safety, and run the unit tests to ensure everything works correctly.









      
