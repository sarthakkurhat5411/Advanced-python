import logging

# Configure logging
logging.basicConfig(
    filename="app.log",
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Different logging levels
logging.debug("This is a debug message")
logging.info("Program started successfully")
logging.warning("This is a warning message")
logging.error("An error has occurred")
logging.critical("This is a critical error")

# Example of logging in a program
a = 10
b = 0

try:
    result = a / b
except ZeroDivisionError:
    logging.exception("Cannot divide a number by zero")

print("Logging program executed successfully.")
print("Check app.log file for log messages.")
