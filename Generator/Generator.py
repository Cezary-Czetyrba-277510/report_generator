import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

class Generator:
    data_set = pd.DataFrame()
    def __init__(self, relative_path:str, file_name:str):
        self.data_set = pd.read_csv(os.path.join(relative_path, file_name), delimiter=';')
    def print_data(self):
        print(self.data_set.to_latex())