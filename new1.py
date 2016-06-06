import random
n = 14
def digital_root(n):
	if n > 9:
		d = 0
		for i in str(n): d += int(i)
		n = d
		digital_root(n)
	else:
		return


digital_root(n)
