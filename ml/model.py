import pandas as pd
import numpy as np
import logging

logger = logging.getLogger("main.model")
logger.setLevel(logging.DEBUG)


class DataHandler:
    """
        Get data from sources
    """
    def __init__(self):
        self.csvfile1 = None
        self.csvfile2 = None
        self.gouped_data = None


class FeatureRecipe:
    """
    Feature processing class
    """
    def __init__(self, data: pd.DataFrame):
        self.data = data
        self.continuous = None
        self.categorical = None
        self.discrete = None
        self.datetime = None


class FeatureExtractor:
    """
    Feature Extractor class
    """
    def __init__(self, data: pd.DataFrame, flist: list):
        """
            Input : pandas.DataFrame, feature list to drop
            Output : X_train, X_test, y_train, y_test according to sklearn.model_selection.train_test_split
        """


class ModelBuilder:
    """
        Class for train and print results of ml model
    """
    def __init__(self, model_path: str = None, save: bool = None):
        pass

    def __repr__(self):
        pass

    def train(self, X, Y):
        pass

    def predict_test(self, X) -> np.ndarray:
        pass

    def predict_from_dump(self, X) -> np.ndarray:
        pass

    def save_model(self, path:str):
        #with the format : ‘model_{}_{}’.format(date)
        pass

    def print_accuracy(self):
        pass

    def load_model(self):
        try:
            #load model
            pass
        except:
            pass
