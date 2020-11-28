"""This module contains a code example related to

The Python Workbook, 2nd Edition
by Ben Stephenson
http://thinkpython2.com

Copyright 2020 Giuseppe Marcucci

License: http://creativecommons.org/licenses/by/4.0/
"""

def run_length_deconding_NO_RECU(text_in):
	text_out = []
	for i in range(len(text_in)//2):
		c = text_in[2*i]
		t = text_in[2*i + 1]
		text_out += c*t
	return text_out


def run_length_deconding(text_in):
	# if len(text_in) == 2:
		# out = []
		# c = text_in[0]
		# t = text_in[1]
		# out += [c]*t
		# return out
	if len(text_in) == 0:
		return []
	elif len(text_in) % 2 == 0:
		c = text_in[0]
		t = text_in[1]
		return [c]*t + run_length_deconding(text_in[2:])
	else:
		print('ERROR input')
	return text_out
	

def run_length_coding(text_in):
	if (len(text_in) == 0):
		return []
	else: #(len(text_in) > 0):
		c = text_in[0]
		i = 0
		while (i < len(text_in) and c == text_in[i]):
			i += 1
		return [c, i] + run_length_coding(text_in[i:])


res = run_length_coding(['A', 'A', 'B'])  # OK
print(res)
res = run_length_coding(['A'])  # OK
print(res)

text_in = ["A", 12, "B", 4, "A", 6, "B", 1]
res = run_length_deconding_NO_RECU(text_in)
print(res)
res = run_length_deconding(text_in)
print(res)
res = run_length_coding(res)
print(res)
assert res == text_in
