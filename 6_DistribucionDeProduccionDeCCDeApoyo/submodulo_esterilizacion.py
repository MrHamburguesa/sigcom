import unittest

import pandas as pd

from modulo_cc_apoyo import obtain_proportional_of_whole


class Esterilizacion:
    def __init__(self):
        pass

    def load_esterilizacion_file(self, file_name):
        df = pd.read_excel(file_name)
        return df

    def get_cubic_meters(self):
        pass


if __name__ == '__main__':
    instancia = Esterilizacion()
    RUTA_ARCHIVO = 'test_files_input/produccion_esterilizacionDIC2022.xlsx'
    df = instancia.load_esterilizacion_file(RUTA_ARCHIVO)
    print(df)
