#
# key.py by Grant Weaver
#
# a class for key presses that way keys can easily be created
# and searched without the need for a big if/elif branch

class Key():

	def __init__(self, entry, symbol):
		self.entry = entry
		self.symbol = symbol
