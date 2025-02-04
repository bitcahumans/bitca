import time

from bitca.tools import Toolkit
from bitca.utils.log import logger


class SleepTools(Toolkit):
    def __init__(self):
        super().__init__(name="sleep")

        self.register(self.sleep)

    def sleep(self, seconds: int) -> str:
        """Use this function to sleep for a given number of seconds."""
        logger.info(f"Sleeping for {seconds} seconds")
        time.sleep(seconds)
        logger.info(f"Awake after {seconds} seconds")
        return f"Slept for {seconds} seconds"
