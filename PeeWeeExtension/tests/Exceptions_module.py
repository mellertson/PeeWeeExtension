import unittest

from PeeWeeExtension.Exceptions import *

class Exceptions_case(unittest.TestCase):
	def test_raising_exceptions(self):
		with self.assertRaises(ProviderHasNoDataWarning):
			raise ProviderHasNoDataWarning
		with self.assertRaises(UnsupportedDataProviderError):
			raise UnsupportedDataProviderError
		with self.assertRaises(CantTouchThisError):
			raise CantTouchThisError
		with self.assertRaises(RequiredDataMissingError):
			raise RequiredDataMissingError