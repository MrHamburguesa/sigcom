import unittest

import pandas as pd

from modulo_cc_apoyo import obtain_proportional_of_whole


class Esterilizacion:
    def __init__(self):
        pass

    def load_file(self, file_name):
        df = pd.read_excel(file_name)
        return df

    def get_cubic_meters(self):
        pass


if __name__ == '__main__':
    instancia = Esterilizacion()
    instancia.load_file()
