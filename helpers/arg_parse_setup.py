import argparse

def getArgs():
	parser = argparse.ArgumentParser(
			description="A simple script that handles command-line arguments.")
	parser.add_argument("-i", "--interactive", action="store_true",
											help="Enter interactive mode to search on the fly")
	parser.add_argument("-c", "--condition", action="store",
                     choices=['any', 'new', 'used'], default='any', help="Condition of item")
	parser.add_argument("-cat","--category", action="store", help="Category as # used by ebay")
	parser.add_argument("-f", "--file", action="store",
											help="Configuration json file to use")
	parser.add_argument("-x", "--export", action="store_true", help="Export to csv file")
	parser.add_argument("-v", "--verbose", action="store_true", help="Run with verbose debugging")
	return parser.parse_args()
