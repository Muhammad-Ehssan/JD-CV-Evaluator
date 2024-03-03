# logger_config.py
import logging
from logging.handlers import RotatingFileHandler

def configure_logger():
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)

    log_file = './logs/upload.log'
    file_handler = RotatingFileHandler(log_file, maxBytes=10240, backupCount=10)
    file_handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))

    logger.addHandler(file_handler)

    return logger

def app_configure_logger():
    log_file_path = "./logs/app.log"
    max_file_size_bytes = 10240  # Set the maximum file size (adjust as needed)
    backup_count = 5 
    # logging.basicConfig(filename="./logs/app.log", level=logging.INFO,format=('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
    file_handler = RotatingFileHandler(log_file_path, maxBytes=max_file_size_bytes, backupCount=backup_count)
    file_handler.setLevel(logging.INFO)

    # Create a formatter and add it to the handler
    formatter = logging.Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]')
    file_handler.setFormatter(formatter)

    # Add the rotating file handler to the root logger
    return file_handler
