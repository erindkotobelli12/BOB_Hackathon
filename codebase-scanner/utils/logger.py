"""Logging configuration for the codebase scanner."""

import logging
import sys
from datetime import datetime
from pathlib import Path


def setup_logger(name: str = "codebase_scanner", verbose: bool = True, log_file: str | None = None) -> logging.Logger:
    """
    Set up and configure a logger for the application.
    
    Args:
        name: Logger name
        verbose: If True, set level to DEBUG, otherwise INFO
        log_file: Optional path to log file
        
    Returns:
        Configured logger instance
    """
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG if verbose else logging.INFO)
    
    # Remove existing handlers to avoid duplicates
    logger.handlers.clear()
    
    # Console handler
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(logging.DEBUG if verbose else logging.INFO)
    
    # Format with timestamp, level, and message
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)
    
    # File handler if log_file is specified
    if log_file:
        log_path = Path(log_file)
        log_path.parent.mkdir(parents=True, exist_ok=True)
        
        file_handler = logging.FileHandler(log_file, mode='a', encoding='utf-8')
        file_handler.setLevel(logging.DEBUG)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
    
    return logger


def log_scan_summary(logger: logging.Logger, stats: dict) -> None:
    """
    Log a summary of the scan results.
    
    Args:
        logger: Logger instance
        stats: Dictionary containing scan statistics
    """
    logger.info("=" * 60)
    logger.info("SCAN SUMMARY")
    logger.info("=" * 60)
    logger.info(f"Total files scanned: {stats.get('total_files', 0)}")
    logger.info(f"Total functions found: {stats.get('total_functions', 0)}")
    logger.info(f"Total classes found: {stats.get('total_classes', 0)}")
    logger.info(f"Languages detected: {', '.join(stats.get('languages_detected', []))}")
    logger.info(f"Overall documentation coverage: {stats.get('overall_coverage', 0):.2f}%")
    logger.info("=" * 60)

# Made with Bob
