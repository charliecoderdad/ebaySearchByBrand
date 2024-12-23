# config_loader.py
import json
import logging


class ConfigLoader:
  def __init__(self, file_path):
    self.file_path = file_path
    self.config = self.get_config()
    self.category = self.config.get('category')
    self.condition = self.config.get('condition')
    self.delayInterval = self.config.get('delayInterval')
    self.exportCsvFileName = self.config.get('exportCsvFileName')
    self.searchTerm = self.config.get('searchTerm')
    self.brands = self.config['brands']

  def get_config(self):
    try:
      with open(self.file_path, "r") as file:
        return json.load(file)
    except Exception as e:
      logging.error(
          f"An error occurred reading json configuration file: {e}")
      return None


# import json, logging

# def get_config(file_path):
#   try:
#     with open(file_path, "r") as file:
#       return json.load(file)
#   except Exception as e:
#     logging.error(f"An error occurred reading json configuration file: {e}")
