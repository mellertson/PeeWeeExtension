import unittest
from PeeWeeExtension.Database import MySQL_BaseModel, Environment, MySQLConnections
from PeeWeeExtension.Globals import Globals

class MySQLConnection_Initialization_case(unittest.TestCase):
	def test_raise_if_unkown_environment(self):
		"""
		Tests constructor for valie args, and asserts no exceptions are thrown.
		Tests constructor for invalid args, and asserts exceptions are thrown.
		:return:
		"""
		# call consturctor for all known environments
		MySQL_BaseModel(environment=Environment.production)
		MySQL_BaseModel(environment=Environment.test)

		# these should raise ValueError
		with self.assertRaises(ValueError):
			MySQLConnections("unknown_environment")
		with self.assertRaises(ValueError):
			MySQLConnections("")
		with self.assertRaises(ValueError):
			MySQLConnections(environment=5)
		with self.assertRaises(ValueError):
			MySQLConnections(environment="unknown_environment")
		with self.assertRaises(ValueError):
			MySQLConnections(environment="")
		with self.assertRaises(ValueError):
			MySQLConnections("unknown_environment")

	def test_getDatabasePooler_method(self):
		MySQLConnections.getDatabasePooler(environment=Environment.default)
		MySQLConnections.getDatabasePooler(environment=Environment.production)
		MySQLConnections.getDatabasePooler(environment=Environment.test)

	def test_limits_of_max_connections(self):
		"""
		Creates the max number of connections, and asserts no exceptions are thrown while doing so.
		Then, creates more than the max number of connections, and asserts an exception is thrown.
		Then, destroys all the connections using the deconstructor, and asserts no exception is thrown.
		"""
		connections = []
		for i in range(0, (Globals.prod_max_connections + 1)):
			if i < Globals.prod_max_connections:
				db = MySQL_BaseModel()
				db.connect(Environment.test)
				connections.append(db)
			else:
				with self.assertRaises(ValueError):
					connections.append(MySQL_BaseModel.connect(environment="unknown"))

		# Close the connections we just opened, no exceptions should be thrown.
		for i in range(0, Globals.prod_max_connections-8):
			connections[i].__del__()


