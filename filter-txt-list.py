#!/usr/bin/env python3
import re
import argparse


def setup_parser():
  parser = argparse.ArgumentParser(
      description="Cleans up ebay brand text files")
  parser.add_argument("-i", "--input", action="store",
                      help="Input text file to parse")
  parser.add_argument("-o", "--output", action="store",
                      default='output.txt', help="Output file to save results to")
  parser.add_argument("-n", "--number", action="store", default=30,
                      help="Number of items a brand must have to be included in results")
  return parser.parse_args()


def filter_lines(input_file, output_file):
  with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
    for line in infile:
      if (len(line.strip()) > 0):       
        match = re.search(r'\(([\d,]+)\)', line)
        if match:
          number = int(match.group(1).replace(",",""))
          if number >= int(args.number):
              text_before_parentheses = line[:match.start()].strip()
              outfile.write("\"" + text_before_parentheses + "\",\n")


# Main
args = setup_parser()
filter_lines(args.input, args.output)
