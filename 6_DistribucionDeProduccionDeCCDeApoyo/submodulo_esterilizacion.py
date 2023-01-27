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

    def extract_autoclave_plasma_data(self, df_month):
        df_tmp = df_month.copy()
        df_tmp = df_tmp.set_index(df_tmp.columns[0])

        litros_prod_autoclave_1 = df_tmp.loc['Litros producción', 'AUTOCLAVE 1']
        litros_prod_autoclave_2 = df_tmp.loc['Litros producción', 'AUTOCLAVE 2']
        litros_prod_plasma = df_tmp.loc['Litros producción', 'PLASMA']

        return litros_prod_autoclave_1, litros_prod_autoclave_2, litros_prod_plasma

    def get_cubic_meters(self, auto_1, auto_2, plasma):
        return round(sum([auto_1, auto_2, plasma]) / 1000, 0)


if __name__ == '__main__':
    instancia = Esterilizacion()
    RUTA_ARCHIVO = 'test_files_input/produccion_esterilizacionDIC2022.xlsx'
    df = instancia.load_esterilizacion_file(RUTA_ARCHIVO)
    print(df)
    df_month = instancia.extract_month_data(df, 'AGOSTO')
    print(df_month)
    auto_1, auto_2, plasma = instancia.extract_autoclave_plasma_data(df_month)
    print(auto_1, auto_2, plasma)
    m3 = instancia.get_cubic_meters(auto_1, auto_2, plasma)
    print(m3)
