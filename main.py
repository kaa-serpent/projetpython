import logging

logger = logging.getLogger("main")
logger.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
ch.setLevel(logging.WARNING)
fh = logging.handlers.RotatingFileHandler("./main.log", maxBytes=100000000, backupCount=5)
fh.setLevel(logging.DEBUG)
formatter = logging.Formatter("%(asctime)s - %(name)-20s - %(levelname)-8s - %(message)s")
ch.setFormatter(formatter)
fh.setFormatter(formatter)
logger.addHandler(ch)
logger.addHandler(fh)


def DataManager(d:DataHandler=None, fr: FeatureRecipe=None, fe:FeatureExtractor=None):
    """
        Fonction qui lie les 3 premières classes de la pipeline et qui return FeatureExtractor.split(0.1)
    """
    pass
#on appelera la fonction DataManager() de la facon suivante :
X_train, X_test, y_train, y_test = DataManager()


if __name__ == '__main__':
    DataManager()