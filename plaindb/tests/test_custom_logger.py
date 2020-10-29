__author__ = "Smruti Mohanty"

from ..plaindb.core import customlogger
import logging




def test_Logging_Function():
    logger = customlogger(logging.INFO, "plaindb-unit-test.log")
    logger.info("This function tests Custom Logger Object.")
    assert logger is not None, "Logger object could not be created."
    logger.info("THREAD - plaindb - This is info level logging.")
    logger.debug("THREAD - plaindb - This is debug level logging.")
    logger.warning("THREAD - plaindb - This is warning level logging.")
