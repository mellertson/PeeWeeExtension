
class ProviderHasNoDataWarning(Exception):
	"""
	Raised when the provider for market data returns no data to us,
	and program execution should continue
	"""

class UnsupportedDataProviderError(Exception):
	"""
	Raised when an unsupported data provider is requested.
	"""

class CantTouchThisError(Exception):
	"""
	Raised when the user attempts to set a property which is read only.
	I had to have a little fun!  :-)
	"""

class RequiredDataMissingError(Exception):
	"""
	Raised when a required object or variable has no data in it.
	For example: if a pandas.DataFrame() needs to have data for a method
	to function correctly, but it has no rows in it
	"""
