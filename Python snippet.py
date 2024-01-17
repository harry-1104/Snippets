'''
	Author: ------ ---- ----   --/--/----
	Date created: dd/mm/yyyy
'''

# Functions
def __FILE(name):
	try:
		fi = open(name + ".inp", "r")
		fo = open(name + ".out", "w")
		return fi, fo
	except FileNotFoundError:
		return None, None

# Start here !
__FILE()

