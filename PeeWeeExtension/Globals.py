

class Globals(object):
	"""
	The global values shared by the PeeWeeExtension module
	"""
	# date time formatter strings
	date_format_EU 		 = "%Y-%m-%d"
	date_format_EUL 	 = "%Y-%m-%d %H:%M:%S"
	date_format_US 		 = "%m/%d/%y %H:%M"
	date_format_DB 		 = "%m/%d/%Y %I:%M:%S %p"

	# production database credentials
	prod_username 		 = "root"
	prod_password 		 = ""
	prod_schema 		 = "peeweeextensions"
	prod_port            = 3306
	prod_host            = "localhost"
	prod_max_connections = 16

	# test database credentials
	test_schema          = "peeweeextensions_test"
	test_username        = "root"
	test_password        = ""
	test_host            = "localhost"
	test_port            = 3306
	test_max_connections = 16
