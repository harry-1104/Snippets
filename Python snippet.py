'''
	Author: ------ ---- ----   --/--/----
	Date created: dd/mm/yyyy
'''

import sys

def __FILE(name=None):
	if name is None: pass
	else: 
		try: 
			open(name+".inp", 'r')
			sys.stdin = open(name + ".inp", 'r')
			sys.stdout = open(name + ".out", 'w')
			sys.stderr = open(name + ".err", 'w')
		except FileNotFoundError: pass

## This optional function is for reading variables in files
# def input(arg): return sys.stdin.readline(arg)

# Start here ! __nguyenquan__
__FILE("nq")
#
