#!/usr/bin/env python3
import re

def filter_lines(input_file, output_file):
  with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
    for line in infile:
      match = re.search(r'\((\d+)\)', line)
      if match:
        number = int(match.group(1))
        if number >= 30:
          text_before_parentheses = line[:match.start()].strip()
          print(line.strip())
          outfile.write(text_before_parentheses + "\n")


# Example usage
input_file = 'necktie-brands.txt'
output_file = 'output.txt'
filter_lines(input_file, output_file)
