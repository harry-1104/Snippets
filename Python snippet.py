'''
	Author: ------ ---- ----   --/--/----
	Date created: dd/mm/yyyy
'''

import sys

def __FILE(name):
	if ( open(name+".inp", 'r') ):
		sys.stdin = open(name + ".inp", 'r')
		sys.stdout = open(name + ".out", 'w')
		sys.stderr = open(name + ".err", 'w')

def input(arg): return sys.stdin.readline(arg)
# Start here !
__FILE()
#
