"""
Logging configuration for the BioMarket system.
"""

import logging
import os
from datetime import datetime


def setup_logger(log_dir='logs', log_level=logging.INFO):
    """
    Configure and return a logger instance.
    
    Args:
        log_dir (str): Directory for log files
        log_level (int): Logging level (e.g., logging.INFO)
        
    Returns:
        logging.Logger: Configured logger instance
    """
    # Create logs directory if it doesn't exist
    if not os.path.exists(log_dir):
        try:
            os.makedirs(log_dir)
        except OSError:
            pass
    
    # Create logger
    logger = logging.getLogger('BioMarket')
    logger.setLevel(log_level)
    
    # Avoid duplicate handlers
    if logger.handlers:
        return logger
    
    # Create log filename with timestamp
    log_filename = os.path.join(
        log_dir,
        f'biomarket_{datetime.now().strftime("%Y%m%d")}.log'
    )
    
    # Create file handler
    try:
        file_handler = logging.FileHandler(log_filename, encoding='utf-8')
        file_handler.setLevel(log_level)
        
        # Create formatter
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )
        file_handler.setFormatter(formatter)
        
        # Add handler to logger
        logger.addHandler(file_handler)
    except (IOError, OSError):
        # If can't create file handler, continue without it
        pass
    
    return logger
