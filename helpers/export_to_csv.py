import csv
import logging


def exportToCsv(filename, data):
  # Open the file in write mode
  with open(filename, 'w', newline='') as file:
    # Create a CSV writer object
    csv_writer = csv.writer(file)

    # Write the header row
    header = data[0].keys()
    csv_writer.writerow(header)

    # Write the data rows
    for item in data:
      csv_writer.writerow(item.values())
    
    logging.info("Exported results to " + filename)
