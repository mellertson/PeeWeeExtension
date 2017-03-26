import unittest
from datetime import datetime
from peewee import *
from PeeWeeExtension.Database import Environment, MySQL_BaseModel

# The one and only database connection
db = Environment.test

class PorkAndBeans(MySQL_BaseModel):
	"""Model for testing purposes only!!!"""
	id = PrimaryKeyField()
	porks_name = TextField()
	beans_name = TextField()
	porked_at = DateTimeField(default=datetime.now)

class PorkAndBeansTwo(MySQL_BaseModel):
	"""Model for testing purposes only!!!"""
	id = PrimaryKeyField()
	porks_name = TextField()
	beans_name = TextField()
	porked_at = DateTimeField(default=datetime.now)

class MySQL_BaseModel_case(unittest.TestCase):
	"""
	Tests the MysQL class, using the PorkAndBeans data model (above)
	"""
	def test_app_to_model_connection_using_class_directly(self):
		PorkAndBeans.connect(db)

		# drop it like it's hot!
		PorkAndBeans.drop_table_if_exists()

		# create the table if it doesn't exist
		PorkAndBeans.create_table_if_not_exists()

		# insert 20 records
		PorkAndBeans.create(porks_name="Porky Pig", beans_name="Chili Bean")
		PorkAndBeans.create(porks_name="Porky Pig", beans_name="Chili Bean")
		PorkAndBeans.create(porks_name="Porky Pig", beans_name="Chili Bean")
		PorkAndBeans.create(porks_name="Porky Pig", beans_name="Chili Bean")
		PorkAndBeans.create(porks_name="Ms. Piggy", beans_name="Chili Bean")
		PorkAndBeans.create(porks_name="Ms. Piggy", beans_name="Chili Bean")
		PorkAndBeans.create(porks_name="Ms. Piggy", beans_name="Chili Bean")
		PorkAndBeans.create(porks_name="Ms. Piggy", beans_name="Chili Bean")
		PorkAndBeans.create(porks_name="Ms. Piggy", beans_name="Chili Bean")
		PorkAndBeans.create(porks_name="Ms. Piggy", beans_name="Chili Bean")
		PorkAndBeans.create(porks_name="Ms. Piggy", beans_name="Chili Bean")
		PorkAndBeans.create(porks_name="Ms. Piggy", beans_name="Chili Bean")
		PorkAndBeans.create(porks_name="Ms. Piggy", beans_name="Chili Bean")
		PorkAndBeans.create(porks_name="Porky Pig", beans_name="Chili Bean")
		PorkAndBeans.create(porks_name="Porky Pig", beans_name="Chili Bean")
		PorkAndBeans.create(porks_name="Porky Pig", beans_name="Chili Bean")
		PorkAndBeans.create(porks_name="Porky Pig", beans_name="Chili Bean")
		PorkAndBeans.create(porks_name="Porky Pig", beans_name="Chili Bean")
		PorkAndBeans.create(porks_name="Porky Pig", beans_name="Chili Bean")
		PorkAndBeans.create(porks_name="Porky Pig", beans_name="Chili Bean")

		# select and loop all records
		i = 0
		for row in PorkAndBeans.select().where((PorkAndBeans.beans_name == "Chili Bean")):
			i += 1
			# I should probably test contents of each row, but I'm trusting the PeeWee API
		PorkAndBeans.disconnect()
		self.assertEqual(i, 20, "Wrong number of records returned by select statement.")

	def test_app_to_model_connection_using_an_object(self):
		pb = PorkAndBeansTwo()
		pb.connect(Environment.test)

		# drop it like it's hot!
		pb.drop_table_if_exists()

		# re-create the table since it was just deleted
		pb.create_table_if_not_exists()

		# insert 20 records
		PorkAndBeansTwo.create(porks_name="Porky Pig", beans_name="Chili Bean")
		PorkAndBeansTwo.create(porks_name="Porky Pig", beans_name="Chili Bean")
		PorkAndBeansTwo.create(porks_name="Porky Pig", beans_name="Chili Bean")
		PorkAndBeansTwo.create(porks_name="Porky Pig", beans_name="Chili Bean")
		PorkAndBeansTwo.create(porks_name="Ms. Piggy", beans_name="Chili Bean")
		PorkAndBeansTwo.create(porks_name="Ms. Piggy", beans_name="Chili Bean")
		PorkAndBeansTwo.create(porks_name="Ms. Piggy", beans_name="Chili Bean")
		PorkAndBeansTwo.create(porks_name="Ms. Piggy", beans_name="Chili Bean")
		PorkAndBeansTwo.create(porks_name="Ms. Piggy", beans_name="Chili Bean")
		PorkAndBeansTwo.create(porks_name="Ms. Piggy", beans_name="Chili Bean")
		PorkAndBeansTwo.create(porks_name="Ms. Piggy", beans_name="Chili Bean")
		PorkAndBeansTwo.create(porks_name="Ms. Piggy", beans_name="Chili Bean")
		PorkAndBeansTwo.create(porks_name="Ms. Piggy", beans_name="Chili Bean")
		PorkAndBeansTwo.create(porks_name="Porky Pig", beans_name="Chili Bean")
		PorkAndBeansTwo.create(porks_name="Porky Pig", beans_name="Chili Bean")
		PorkAndBeansTwo.create(porks_name="Porky Pig", beans_name="Chili Bean")
		PorkAndBeansTwo.create(porks_name="Porky Pig", beans_name="Chili Bean")
		PorkAndBeansTwo.create(porks_name="Porky Pig", beans_name="Chili Bean")
		PorkAndBeansTwo.create(porks_name="Porky Pig", beans_name="Chili Bean")
		PorkAndBeansTwo.create(porks_name="Porky Pig", beans_name="Chili Bean")

		# insert 1 more record, making 21
		pb.porks_name = "Ms. Piggy"
		pb.beans_name = "Chili Bean"
		pb.save()

		# select and loop through all records
		i = 0
		for row in PorkAndBeansTwo.select().where((PorkAndBeansTwo.beans_name == "Chili Bean") |
		                            ((PorkAndBeansTwo.beans_name == "Chili Bean"))):
			i += 1
			# I should probably test contents of each row, but I'm trusting the PeeWee API
		self.assertEqual(i, 21, "Wrong number of records returned by select statement, {} were returned.".format(i))
		PorkAndBeansTwo.disconnect()

