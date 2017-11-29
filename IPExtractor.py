#!/usr/bin/python
#
# IP Extractor to export IP addresses from the clipboard to be used within Nessus
# Sam Braidley
#
#
# Version History
# 0.1 - Basic clipboard import and export (11:55 29/11/2017)
# 0.2 - Ability to export to file (12:10 29/11/2017)
# 0.3 - Removed trailing comma that was left (12:14 29/11/2017)
# 0.3.1 - Changed stripping to 2 characters due to newline (12:18 29/11/2017)
# 0.3.2 - Fixed space issue, when importing list into Nessus, space is automatically inserted (13:23 29/11/2017)

import pyperclip
import sys

try:
	sys.argv[1]
	output_file = sys.argv[1]
except IndexError:
	output_file = ""
	print('No output file specified, output will be copied to clipboard.')


ip_addresses = pyperclip.paste()

formatted = ip_addresses.replace("\n", ",").replace("\r", ",")
final = formatted[:-2].strip()

if not output_file:
	pyperclip.copy(final)
else:
	file = open(output_file, "w")
	file.write(final)
	file.close()