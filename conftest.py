import logging
import pytest


def pytest_configure(config):
    logging.basicConfig(filename=r'C:\Users\KDesai\Documents\Imagecompare\Results\mypytest.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
