import unittest
import os
from datetime import datetime
from MoneyMaker.Database import Environment
from MoneyMaker.HTMModel import HTMModel

class HTMModel_case(unittest.TestCase):
    def setUp(self):
        #############################################################################
        # WARNING! Exercise extreme caution with this setting, you might            #
        # blow something up!!                                                       #
        # The database environment these test cases will use                        #
        self.db = Environment.test  #
        #                                                                           #
        #############################################################################
        self.dir = os.path.dirname(__file__)

        realPath = os.path.realpath(__file__)   # /home/user/test/my_script.py
        dirPath = os.path.dirname(realPath)     # /home/user/test
    def test_save_records(self):
        # delete and re-create the table, so we have a known number of records
        HTMModel.connect(Environment.test)
        HTMModel.drop_table_if_exists()
        HTMModel.disconnect()
        HTMModel.connect(Environment.test)

        # TODO: HIGH: Before running this test case, add an HTM model to the 'models_directory'
        # model uwt-close-feb-03-2017
        dir = self.dir + '/test_models/models_directory'
        HTMModel.createModel(name="model1",
                             base_description_filename=dir + '/description.py',
                             permutations_filename=dir + '/permutations.py',
                             description_filename=dir + '/model_0/description.py',
                             model_params_filename=dir + '/model_0/model_params.py',
                             params_filename=dir + '/model_0/params.csv')

        # TODO: HIGH: update test case so it verifies data was saved correctly in the database

        # disconnect from the database
        HTMModel.disconnect()

if __name__ == '__main__':
    unittest.main()
