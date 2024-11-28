import logging

logging.basicConfig(
    filename="app.log",
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s"  # Define the log format
)

logging.debug("This is a debug message.")
logging.info("This is an info message.")
logging.warning("This is a warning message.")
logging.error("This is an error message.")
logging.critical("This is a critical message.")


# Configure logging
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

# Custom logger
logger = logging.getLogger("MyLogger")

# Log messages
logger.debug("Debugging details.")
logger.info("Informational message.")
logger.warning("This is a warning!")
logger.error("An error has occurred!")
logger.critical("Critical issue!")


logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger("MyLogger")


logger.debug("Debugging details.")
logger.info("Log in successful.")
logger.warning("This is a warning!")
logger.error("An error has occurred!")
logger.critical("Critical issue!")