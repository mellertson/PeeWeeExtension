# native libs

# 3rd party libs
from playhouse.pool import PooledMySQLDatabase
from peewee import *

# PeeWeeExtension libs
from PeeWeeExtension.Globals import Globals

class Environment(object):
	default     = 'default'
	production  = 'production'
	test        = 'test'

class MySQLConnections(object):
	"""
	Manages database connections for the production and test servers
	"""
	# production database connection
	prod_db = PooledMySQLDatabase(
		database=Globals.prod_schema,
		max_connections=Globals.prod_max_connections,
		stale_timeout=600,
		user=Globals.prod_username,
		passwd=Globals.prod_password,
		host=Globals.prod_host,
		port=Globals.prod_port,
		use_unicode=False
	)

	# test database connection
	test_db = PooledMySQLDatabase(
		database=Globals.test_schema,
		max_connections=Globals.test_max_connections,
		stale_timeout=600,
		user=Globals.test_username,
		passwd=Globals.test_password,
		host=Globals.test_host,
		port=Globals.test_port,
		use_unicode=False
	)

	# the default, "placeholder" database connection
	default_db = PooledMySQLDatabase(None)

	def __init__(self, environment=None):
		self.getDatabasePooler(environment=environment)

	@classmethod
	def getDatabasePooler(cls, environment=None):
		"""
		Gets a reference to the selected database connection pooler.
		:return PooledMySQLDatabase: an class variable to either prod or test database pooler
		"""
		verror = "Unkown database environment selected, it must be value from the 'Environment' class"
		if environment is not None:
			if environment == Environment.production:
				return cls.prod_db
			elif environment == Environment.test:
				return cls.test_db
			elif environment == Environment.default:
				return cls.default_db
			else:
				raise ValueError(verror)

class MySQL_BaseModel(Model):
	"""
	Use this as the base data model for all data in the PeeWeeExtension application.

	This class uses MySQLConnections to dynamically manage a pool of database connections to all environments.
	"""
	class Meta:
		"""
		The database connection.

		We initialize using the generic PooledMySQLDatabase class from the peewee library, it's replaced later
		in the connect method, with the specific database environment connected to it.
		"""
		database = PooledMySQLDatabase(None)

	def __del__(self):
		self.disconnect()

	@classmethod
	def connect(cls, environment):
		# type: (str) -> None
		cls._meta.database = MySQLConnections.getDatabasePooler(environment=environment)
		cls._meta.database.connect()
		cls.create_table_if_not_exists()

	@classmethod
	def disconnect(cls):
		# type: (None) -> None
		"""
		Disconnects from the current database connection, and return it to the pool.

		NOTE: Make sure you call this after you're done with it,
		otherwise it won't be usable until it times out!
		"""
		cls._meta.database.close()

	@classmethod
	def create_table_if_not_exists(cls):
		"""
		Create the model's table in the database, but only if it doesn't exist.
		"""
		if not cls.table_exists():
			cls.create_table()

	@classmethod
	def drop_table_if_exists(cls):
		"""
		Drop the model's table in the databse, but only if it already exists.
		"""
		if cls.table_exists():
			# todo: insert exception handling into TickerData::drop_table_if_exists() method
			cls.drop_table()




























