import logging
import pytest
import os

def pytest_configure(config):
    logging.basicConfig(filename=os.getcwd()+"\\Results\\Test_Chaos_Image_Task.log", level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
