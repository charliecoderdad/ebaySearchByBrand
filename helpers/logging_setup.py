import logging, sys

def setup_logging(verbose=None):
	# Set up logging configuration
	level = logging.DEBUG if verbose else logging.INFO
	logging.basicConfig(
			filename='logfile.log',  # Log file name
			# Log level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
			level=level,
			format='%(asctime)s - %(levelname)s - %(message)s',  # Log format
			datefmt='%Y-%m-%d %H:%M:%S'  # Date format
	)
	console_handler = logging.StreamHandler()
	console_handler.setFormatter(logging.Formatter(
		'%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S'))
	logging.getLogger().addHandler(console_handler)

# Example usage of logging
# logging.debug('This is a debug message')
# logging.info('This is an info message')
# logging.warning('This is a warning message')
# logging.error('This is an error message')
# logging.critical('This is a critical message')