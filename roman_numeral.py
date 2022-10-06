#!/usr/bin/env python3

def roman_from_int(t_num):
	MAX_VALUE = 4000
	roman_symbols = {1000: "M",
		900: "CM", 500: "D", 400: "CD", 100: "C",
		90: "XC", 50: "L", 40: "XL", 10: "X",
		9: "IX", 5: "V", 4: "IV", 1: "I",
	}
	roman = ""

	if t_num >= MAX_VALUE:
		raise ValueError(f"input number must be less than {MAX_VALUE}")
		return
	for i in roman_symbols:
		while t_num >= i:
			roman += roman_symbols[i]
			t_num -= i
	return roman


def main(t_argv):
	if len(t_argv) > 1:
		print(roman_from_int(int(sys.argv[1])))
	else:
		print("Usage: roman_numeral.py int")


if __name__ == "__main__":
	import sys

	main(sys.argv)
