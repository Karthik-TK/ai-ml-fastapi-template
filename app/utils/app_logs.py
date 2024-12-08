import logging
import time
import tracemalloc
from enum import Enum
from functools import wraps
from typing import Any, Callable, Optional

import psutil

# Customise the log handler


class LogColor(Enum):
    INFO = "\033[94m"
    WARNING = "\033[93m"
    ERROR = "\033[91m"
    CRITICAL = "\033[95m"
    OKCYAN = "\033[96m"
    OKGREEN = "\033[92m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"
    RESET = "\033[0m"


class LogHandler:
    def __init__(self, logger_name=__name__, log_level=logging.INFO):
        self.logger = logging.getLogger(logger_name)
        self.logger.setLevel(log_level)

        formatter = logging.Formatter(
            "%(levelname)s: %(asctime)s - %(name)s - %(message)s",
            datefmt="%d/%m/%Y %I:%M:%S %p",
        )

        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(formatter)
        self.logger.addHandler(stream_handler)

    def log_message(
        self, level: int, message: str, color: Optional[LogColor] = None
    ) -> None:
        color_code = (
            color.value if color else LogColor[logging.getLevelName(level)].value
        )
        self.logger.log(level, f"{color_code}{message}{LogColor.RESET.value}")

    def log_info(self, message: str, color: Optional[LogColor] = None) -> None:
        self.log_message(logging.INFO, message, color)

    def log_error(self, message: str, color: Optional[LogColor] = None) -> None:
        self.log_message(logging.ERROR, message, color)

    def log_warning(self, message: str, color: Optional[LogColor] = None) -> None:
        self.log_message(logging.WARNING, message, color)

    def log_critical(self, message: str, color: Optional[LogColor] = None) -> None:
        self.log_message(logging.CRITICAL, message, color)

    def log_exception(self, message: str) -> None:
        self.logger.exception(message)

    def print_debug(self, message: str, color: Optional[LogColor] = None) -> None:
        self.log_message(logging.DEBUG, message, color)

    def api_log_stats(self, start_time, request):
        end_time = time.time()
        elapsed_time = end_time - start_time
        process = psutil.Process()
        memory_usage = process.memory_info().rss
        cpu_usage = process.cpu_percent()

        self.log_info(
            f"Memory Usage: {memory_usage / (1024 * 1024):.2f} MB", LogColor.INFO
        )
        self.log_info(f"CPU Usage: {cpu_usage}%", LogColor.INFO)
        self.log_info(f"Elapsed Time: {elapsed_time:.4f} seconds", LogColor.INFO)

    def analyze_complexity(self, func: Callable) -> Callable:
        @wraps(func)
        async def wrapper(*args: Any, **kwargs: Any) -> Any:
            # Start tracking memory
            tracemalloc.start()

            # Record the start time
            start_time = time.perf_counter()

            try:
                result = await func(*args, **kwargs)
            finally:
                # Record the end time
                end_time = time.perf_counter()

                # Stop tracking memory and get the current size
                current, peak = tracemalloc.get_traced_memory()
                tracemalloc.stop()

                # Log the results
                self.log_message(
                    f"Function '{func.__name__}' executed in {end_time - start_time:.4f} seconds "
                    f"and used {current / 1024:.2f} KB of memory (peak {peak / 1024:.2f} KB)."
                )

            return result

        return wrapper


log_handler = LogHandler()
