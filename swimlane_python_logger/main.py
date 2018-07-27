from os import path
import datetime
import logging
import logging.config
import logmatic
import json
import socket


class integration:
    def __init__(self, integration, logPath, configFile, configPath, logger=None):
        self.dateNow = datetime.datetime.now().strftime("%Y-%m-%d")
        self.integration = integration
        self.configDict = {}
        self.configFile = configFile
        self.configPath = path.join(configPath, self.configFile)
        self.logger = logger or logging.getLogger(self.integration)
        self.logPath = path.join(logPath, "{}_{}.log".format(self.integration, self.dateNow))
        self.checkAndCreateFile()
        self.loadLoggingConfig()

    def checkAndCreateFile(self):
        if not path.isfile(self.logPath):
            f = open(self.logPath, 'a+')
            f.close()

    def loadLoggingConfig(self):
        with open(self.configPath, 'r') as configFile:
            self.configDict = json.load(configFile)
        self.configDict['handlers']['critical_file_handler']['filename'] = self.logPath
        self.configDict['handlers']['error_file_handler']['filename'] = self.logPath
        self.configDict['handlers']['warning_file_handler']['filename'] = self.logPath
        self.configDict['handlers']['info_file_handler']['filename'] = self.logPath
        self.configDict['handlers']['debug_file_handler']['filename'] = self.logPath
        self.configDict['handlers']['notset_file_handler']['filename'] = self.logPath
        #logging.config.dictConfig(self.configDict)
        handler = logging.FileHandler(self.logPath)
        handler.setFormatter(logmatic.JsonFormatter(extra={"hostname": socket.gethostname()}))
        self.logger.addHandler(handler)

    def infoLogger(self, message):
        self.logger.info(message)

    def errorLogger(self, message, extra=None):
        if extra is not None:
            self.logger.error(message, exrta=extra, exc_info=True)
        else:
            self.logger.error(message, exc_info=True)


spl = integration("SePollLogRythemEventData", "D:/SwimlanePython/Production/logs/", "config.json", "D:/SwimlanePython/swimlane_python_logger/swimlane_python_logger/")
spl.errorLogger('test')