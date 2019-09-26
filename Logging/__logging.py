# Latest 26-Sep-2019
# Made by Leni ♡

import logging
import logging.config
import os

# from __LoggingAdapter import Logger4Adapter
import read_config_file


class Logging:
    """
    Logging Class
    """
    def __init__(self, name):
        config = read_config_file.typeYAML(file_name='log_configure.yml')
        logging.config.dictConfig(config)

        self.logger = logging.getLogger(name)

    def debug(self, log_message):
        self.logger.debug(log_message)

    def info(self, log_message):
        self.logger.info(log_message)

    def error(self, log_message):
        error_message = '\n\t{}'.format(log_message)
        self.logger.error(log_message)

if __name__ == "__main__":
    os.chdir('/Users/leni/Coding/Pythoneer/Logging')

    __name = 'byLeni'
    __message = input('\tlog context: ')

    log = Logging(__name)
    log.debug(__message+' debug function')
    log.info(__message+' info function')
    log.error(__message+' error function')
