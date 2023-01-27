import unittest

import pandas as pd

from modulo_cc_apoyo import obtain_proportional_of_whole


class Esterilizacion:
    def __init__(self):
        pass

    def load_esterilizacion_file(self, file_name):
        df = pd.read_excel(file_name)
        return df

    def extract_month_data(self, df, month_to_extract):
        df_tmp = df.copy()

        first_column = list(df_tmp.iloc[:, 0])
        first_column_parsed = list(map(lambda x: str(x).strip(), first_column))
        index_of_month = first_column_parsed.index(month_to_extract)

        df_month = df_tmp.iloc[index_of_month: index_of_month +
                               5, :8].reset_index(drop=True)
        df_month.columns = df_month.iloc[0, :]
        df_month = df_month.iloc[1:, :]

        return df_month

    def get_cubic_meters(self):
        pass


if __name__ == '__main__':
    instancia = Esterilizacion()
    RUTA_ARCHIVO = 'test_files_input/produccion_esterilizacionDIC2022.xlsx'
    df = instancia.load_esterilizacion_file(RUTA_ARCHIVO)
    index = instancia.extract_esterilizacion_data(df, 'AGOSTO')
    print(index)
