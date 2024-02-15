'''
	Author: ------ ---- ----   --/--/----
	Date created: dd/mm/yyyy
'''

# Functions
def __FILE(name=None):
	if name is None:
		return None, None
	try:
		fi = open(name + ".inp", "r")
		fo = open(name + ".out", "w")
		return fi, fo
	except FileNotFoundError:
		return None, None

fi, fo = __FILE()

# Start here !

#
