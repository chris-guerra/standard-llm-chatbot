# src/utils/logging_config.py
import logging

def setup_logging() -> None:
    """
    Configures logging for the application.
    """
    logging.basicConfig(
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        level=logging.INFO  # Set to DEBUG, WARNING, ERROR as per environment needs
    )
