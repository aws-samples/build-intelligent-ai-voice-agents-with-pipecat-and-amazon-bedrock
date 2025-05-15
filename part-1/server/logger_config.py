from loguru import logger
import sys


logger.remove(0)
logger.add(sys.stderr, level="DEBUG")