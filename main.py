#!/usr/bin/env python3
import helpers.logging_setup as logging_setup
import helpers.ebay_search as ebay_search
import helpers.arg_parse_setup as arge_setup
import helpers.export_to_csv as export_to_csv
from helpers.config_reader import ConfigLoader

import logging
import random
import time
import sys

args = arge_setup.getArgs()
logging_setup.setup_logging(verbose=args.verbose)

if args.file:
  config = ConfigLoader(args.file)
  results = []
  brandNum = 1
  for brand in config.brands:
    delayInterval = config.delayInterval + random.randint(1, 10)
    logging.info("(Search #: " + str(brandNum) + " of " + str(len(config.brands)) +
                 ") Brand: " + brand + " - Delay: " + str(delayInterval) + "s")
    brandNum += 1   
    time.sleep(delayInterval)
    result = ebay_search.performSearch(searchTerm=config.searchTerm,
                                       brand=brand,
                                       category=config.category,
                                       condition=config.condition)
    results.append(result)    
  if args.export:
    export_to_csv.exportToCsv(config.exportCsvFileName, results)


if args.interactive:
  while True:
    searchTerm = input("Enter search term ('exit' to quit): ")
    if searchTerm == "exit":
      sys.exit()
    print("Search term entered: " + searchTerm)
    ebay_search.performSearch(searchTerm=searchTerm, category=args.category, condition=args.condition)
    
