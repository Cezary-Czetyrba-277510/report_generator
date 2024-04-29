import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

class Generator:
    def __init__(self, file_name:str):
        self.data_set = pd.read_csv(os.path.join(os.path.dirname(__file__), "data/", file_name), delimiter=';')
    def print_data()