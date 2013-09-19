#Path Management Imports
from os.path import dirname, abspath

#Absolute path directory valid for whole application's modules.
TEST_DIR = dirname(abspath(__file__))
TEST_SOURCE_REAL_ROME = "{}\Rome_Real_OSM.xml".format(TEST_DIR)
TEST_SOURCE_REAL_PARIOLI = "{}\Parioli_Real_OSM.xml".format(TEST_DIR)
TEST_SOURCE_GENERATED = "{}\RandomOsmGenerator.xml".format(TEST_DIR)