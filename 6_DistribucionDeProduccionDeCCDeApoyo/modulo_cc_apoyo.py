import pandas as pd

FILAS_FORMATO_SIGCOM = ["15022_1-PROCEDIMIENTO DE NEUMOLOGÍA | Procedimiento",
                        "245_1-PROCEDIMIENTOS ASISTENCIA VENTRICULAR | Procedimiento",
                        "15026_1-PROCEDIMIENTOS DE CARDIOLOGÍA | Procedimiento",
                        "253_1-PROCEDIMIENTOS DE HEMODINAMIA | Procedimiento",
                        "15038_1-PROCEDIMIENTO ONCOLOGÍA | Procedimiento",
                        "262_1-PROCEDIMIENTOS DE TRAUMATOLOGÍA | Procedimiento",
                        "264_1-PROCEDIMIENTOS EBUS | Procedimiento",
                        "265_1-PROCEDIMIENTOS ECMO | Procedimiento",
                        "267_1-PROCEDIMIENTOS ENDOSCÓPICOS | Procedimiento",
                        "270_1-PROCEDIMIENTOS TAVI | Procedimiento",
                        "518_1-LABORATORIO CLÍNICO | Exámen",
                        "537_1-ECOCARDIOGRAFÍA | Estudio",
                        "41107_1-TOMOGRAFÍA | Estudio",
                        "41108_1-IMAGENOLOGÍA | Exámen",
                        "544_1-ANATOMÍA PATOLÓGICA | Estudio",
                        "51001_1-BANCO DE SANGRE | Exámen",
                        "55101_1-SERVICIO FARMACEUTICO | Prescripción",
                        "95301_1-CENTRAL DE ESTERILIZACIÓN | Metro cúbico",
                        "652_1-SERVICIO DE ALIMENTACIÓN | Ración paciente",
                        "652_2-SERVICIO DE ALIMENTACIÓN | Ración funcionario",
                        "95501_1-MANTENIMIENTO | Órden"
                        ]

COLUMNAS_FORMATO_SIGCOM = ['66-HOSPITALIZACIÓN MEDICINA INTERNA',
                           '90-HOSPITALIZACIÓN QUIRÚRGICA',
                           '102-HOSPITALIZACIÓN CARDIOVASCULAR',
                           '464-QUIRÓFANOS CARDIOVASCULAR',
                           '484-QUIRÓFANOS TORACICA',
                           '166-UNIDAD DE CUIDADOS INTENSIVOS',
                           '195-UNIDAD DE TRATAMIENTO INTENSIVO ADULTO',
                           '15105-CONSULTA CARDIOLOGÍA',
                           '15107-CONSULTA ONCOLOGÍA',
                           '15111-CONSULTA NEUMOLOGÍA',
                           '15123-PROGRAMA MANEJO DEL DOLOR',
                           '15201-CONSULTA CIRUGÍA GENERAL',
                           '15220-CONSULTA CIRUGIA CARDIACA',
                           '15008-CONSULTA NUTRICIÓN',
                           '15010-CONSULTA OTROS PROFESIONALES',
                           '631-CENTRO DE COSTOS EXTERNO',
                           '15022-PROCEDIMIENTO DE NEUMOLOGÍA',
                           '245-PROCEDIMIENTOS ASISTENCIA VENTRICULAR',
                           '15026-PROCEDIMIENTOS DE CARDIOLOGÍA',
                           '253-PROCEDIMIENTOS DE HEMODINAMIA',
                           '15038-PROCEDIMIENTO ONCOLOGÍA',
                           '262-PROCEDIMIENTOS DE TRAUMATOLOGÍA',
                           '264-PROCEDIMIENTOS EBUS',
                           '265-PROCEDIMIENTOS ECMO',
                           '267-PROCEDIMIENTOS ENDOSCÓPICOS',
                           '270-PROCEDIMIENTOS TAVI',
                           '518-LABORATORIO CLÍNICO',
                           '537-ECOCARDIOGRAFÍA',
                           '41107-TOMOGRAFÍA',
                           '41108-IMAGENOLOGÍA',
                           '544-ANATOMÍA PATOLÓGICA',
                           '51001-BANCO DE SANGRE',
                           '55101-SERVICIO FARMACEUTICO',
                           '95301-CENTRAL DE ESTERILIZACIÓN',
                           '652-SERVICIO DE ALIMENTACIÓN',
                           '95501-MANTENIMIENTO',
                           '670-ADMINISTRACIÓN']

TOMOGRAFIA_PROPORTIONS = [0.169636964,
                          0.057425743,
                          0.020462046,
                          0,
                          0,
                          0.17689769,
                          0.211221122,
                          0.044884488,
                          0,
                          0.231023102,
                          0,
                          0.047524752,
                          0,
                          0,
                          0.040924092,
                          0,
                          0,
                          0,
                          0,
                          0,
                          0,
                          0,
                          0,
                          0,
                          0,
                          0,
                          0,
                          0,
                          0,
                          0,
                          0,
                          0,
                          0,
                          0,
                          0,
                          0,
                          0]

IMAGENOLOGIA_PROPORTIONS = [0.171507607,
                            0.055325035,
                            0.042876902,
                            0,
                            0,
                            0.047026279,
                            0.096818811,
                            0.070539419,
                            0,
                            0.373443983,
                            0,
                            0.067773167,
                            0,
                            0,
                            0.074688797,
                            0,
                            0,
                            0,
                            0,
                            0,
                            0,
                            0,
                            0,
                            0,
                            0,
                            0,
                            0,
                            0,
                            0,
                            0,
                            0,
                            0,
                            0,
                            0,
                            0,
                            0,
                            0]


def rename_rows(df):
    '''Funcion para renombrar las filas del DataFrame obtenidos de la tabla Distribucion de la planilla CC de Apoyo
    de Enrique

    :param df: Es el DataFrame con los datos
    :type df: pd.DataFrame

    :returns: El DataFrame con los nombres de las filas cambiadas
    :rtype: pd.DataFrame
    '''
    diccionario_a_cambiar = {'244_1-PROCEDIMIENTO DE NEUMOLOGÍA | Procedimiento': '15022_1-PROCEDIMIENTO DE NEUMOLOGÍA | Procedimiento',
                             '248_1-PROCEDIMIENTOS DE CARDIOLOGÍA | Procedimiento': '15026_1-PROCEDIMIENTOS DE CARDIOLOGÍA | Procedimiento',
                             '260_1-PROCEDIMIENTO ONCOLOGÍA | Procedimiento': '15038_1-PROCEDIMIENTO ONCOLOGÍA | Procedimiento',
                             '541_1-TOMOGRAFÍA | Estudio': '41107_1-TOMOGRAFÍA | Estudio',
                             '542_1-IMAGENOLOGÍA | Estudio': '41108_1-IMAGENOLOGÍA | Exámen',
                             '543_1-ANGIOGRAFÍA | Estudio': None,
                             '575_1-BANCO DE SANGRE | Unidad': None,
                             '575_2-BANCO DE SANGRE | Exámen': '51001_1-BANCO DE SANGRE | Exámen',
                             '593_1-SERVICIO FARMACEUTICO | Receta': '55101_1-SERVICIO FARMACEUTICO | Prescripción',
                             '662_1-CENTRAL DE ESTERILIZACIÓN | Paquete': None,
                             '662_2-CENTRAL DE ESTERILIZACIÓN | Metro cúbico': '95301_1-CENTRAL DE ESTERILIZACIÓN | Metro cúbico',
                             '665_1-MANTENIMIENTO | Órden': '95501_1-MANTENIMIENTO | Órden'}

    df_cambiada = df.copy()
    df_cambiada = df_cambiada.replace(
        diccionario_a_cambiar).dropna(subset=df.columns[0])
    return df_cambiada


def rename_cols(df):
    '''Funcion para renombrar las columnas (son los Centros de Costo) del DataFrame obtenidos 
    de la tabla Distribucion de la planilla CC de Apoyo de Enrique

    :param df: Es el DataFrame con los datos
    :type df: pd.DataFrame

    :returns: El DataFrame con los nombres de las columnas cambiadas
    :rtype: pd.DataFrame
    '''
    diccionario_a_cambiar = {'HOSPITALIZACION MEDICINA INTERNA': '66-HOSPITALIZACIÓN MEDICINA INTERNA',
                             'HOSPITALIZACION QUIRURGICA ': '90-HOSPITALIZACIÓN QUIRÚRGICA',
                             'HOSPITALIZACION CARDIOVASCULAR ': '102-HOSPITALIZACIÓN CARDIOVASCULAR',
                             'UNIDAD DE CUIDADOS INTENSIVOS ': '166-UNIDAD DE CUIDADOS INTENSIVOS',
                             'UNIDAD DE TRATAMIENTO INTENSIVO ADULTO ': '195-UNIDAD DE TRATAMIENTO INTENSIVO ADULTO',
                             'CONSULTA NUTRICION ': '15008-CONSULTA NUTRICIÓN',
                             'CONSULTA OTROS PROgESIONALES ': '15010-CONSULTA OTROS PROFESIONALES',
                             'CONSULTA CARDIOLOGIA ': '15105-CONSULTA CARDIOLOGÍA',
                             'CONSULTA ONCOLOGIA ': '15107-CONSULTA ONCOLOGÍA',
                             'CONSULTA NEUMOLOGIA ': '15111-CONSULTA NEUMOLOGÍA',
                             'CONSULTA MANEJO DEL DOLOR ': '15123-PROGRAMA MANEJO DEL DOLOR',
                             'CONSULTA CIRUGIA GENERAL ': '15201-CONSULTA CIRUGÍA GENERAL',
                             'CONSULTA CIRUGIA CARDIACA ': '15220-CONSULTA CIRUGIA CARDIACA',
                             'QUIRÓgANOS CARDIOVASCULAR ': '464-QUIRÓFANOS CARDIOVASCULAR',
                             'QUIROgANOS CIRUGIA TORACICA ': '484-QUIRÓFANOS TORACICA',
                             'CENTRO DE COSTOS EXTERNO ': '631-CENTRO DE COSTOS EXTERNO',
                             'PROCEDIMIENTO DE NEUMOLOGIA ': '15022-PROCEDIMIENTO DE NEUMOLOGÍA',
                             'PROCEDIMIENTO ASISTENCIA VENTRICULAR ': '245-PROCEDIMIENTOS ASISTENCIA VENTRICULAR',
                             'PROCEDIMIENTO DE CARDIOLOGIA ': '15026-PROCEDIMIENTOS DE CARDIOLOGÍA',
                             'PROCEDIMIENTOS DE HEMODINAMIA ': '253-PROCEDIMIENTOS DE HEMODINAMIA',
                             'PROCEDIMIENTO ONCOLOGIA ': '15038-PROCEDIMIENTO ONCOLOGÍA',
                             'PROCEDIMIENTO EBUS ': '264-PROCEDIMIENTOS EBUS',
                             'PROCEDIMIENTO ECMO ': '265-PROCEDIMIENTOS ECMO',
                             'PROCEDIMIENTOS ENDOSCÓPICOS ': '267-PROCEDIMIENTOS ENDOSCÓPICOS',
                             'PROCEDIMIENTO TAVI ': '270-PROCEDIMIENTOS TAVI',
                             'LABORATORIO CLINICO ': '518-LABORATORIO CLÍNICO',
                             'ECOCARDIOGRAgIA ': '537-ECOCARDIOGRAFÍA',
                             'TOMOGRAgIA ': '41107-TOMOGRAFÍA',
                             'IMAGENOLOGIA ': '41108-IMAGENOLOGÍA',
                             'ANGIOGRAgIA ': None,
                             'ANATOMIA PATOLOGICA ': '544-ANATOMÍA PATOLÓGICA',
                             'BANCO DE SANGRE ': '51001-BANCO DE SANGRE',
                             'SERVICIO gARMACEUTICO ': '55101-SERVICIO FARMACEUTICO',
                             'CENTRAL DE ESTERILIZACION ': '95301-CENTRAL DE ESTERILIZACIÓN',
                             'SERVICIO DE ALIMENTACION ': '652-SERVICIO DE ALIMENTACIÓN',
                             'MANTENIMIENTO ': '95501-MANTENIMIENTO',
                             'ADMINISTRACION ': '670-ADMINISTRACIÓN'}

    df_cambiada = df.copy()
    df_cambiada = df_cambiada.rename(diccionario_a_cambiar, axis=1)
    return df_cambiada


def order_cols(df):
    '''Funcion que permite reordenar las columnas de un DataFrame segun la constante
    COLUMNAS_FORMATO_SIGCOM

    :param df: Es el DataFrame con los datos y que se le quieren cambiar las columnas
    :type df: pd.DataFrame

    :returns: El DataFrame con las columnas reordenadas
    :rtype: pd.DataFrame
    '''
    df_tmp = df.copy()
    df_tmp = df_tmp[COLUMNAS_FORMATO_SIGCOM]

    return df_tmp


def order_rows(df):
    '''Funcion que permite reordenar las filas de un DataFrame segun la constante
    FILAS_FORMATO_SIGCOM.

    :param df: Es el DataFrame con los datos y que se le quieren cambiar las filas. Su
    indice debe ser la columna con los tipos de gastos.
    :type df: pd.DataFrame

    :returns: El DataFrame con las filas reordenadas
    :rtype: pd.DataFrame
    '''
    df_tmp = df.copy()
    df_tmp = df_tmp.loc[FILAS_FORMATO_SIGCOM]
    return df_tmp


def obtain_proportional_of_whole(total, coefs):
    '''Funcion que distribuir un valor a lo largo de una lista con coeficientes. Los
    coeficientes deben sumar 1

    :param total: Es el valor total que se quiere distribuir
    :type total: int, float

    :param coefs: Es la lista que contiene diversos coeficientes como elementos. Los coeficientes
    deben sumar 1
    :type coefs: list

    :returns: Una lista con el valor total distribuido a lo largo de los coeficientes
    :rtype: list
    '''
    return list(map(lambda x: x * total, coefs))


def change_row_with_proportional(df, row_to_change, total_of_row, coeffs_of_row):
    '''Funcion que permite cambiar una fila de un DataFrame con una distribucion nueva de un total.

    :param df: Es el DataFrame que se quiere cambiar. El indice del DataFrame debe tener la fila que se quiere
    cambiar
    :type df: pd.DataFrame

    :param row_to_change: Es la fila que se quiere cambiar del DataFrame
    :type row_to_change: str

    :param total_of_row: Es el valor total que se le asignara a la fila a cambiar
    :type total_of_row: int, float

    :param coeffs_of_row: Es una lista que contiene los coeficientes para distribuir el valor total
    :type coeffs_of_row: list

    :returns: El DataFrame con la fila cambiada por el proporcional
    :rtype: pd.DataFrame
    '''
    proportional = obtain_proportional_of_whole(total_of_row, coeffs_of_row)
    tmp_df = df.copy()
    tmp_df.loc[row_to_change] = proportional

    return tmp_df


def obtain_value_to_add(df, column_name_to_fill):
    '''Funcion que permite extraer un valor de una celda basado en la columna que se quiere rellenar

    :param df: Es el DataFrame que contiene los datos
    :type df: pd.DataFrame

    :param column_name_to_fill: Es el nombre de la columna que se quiere agregar un valor
    :type column_name_to_fill: str

    :returns: El valor que se tiene que agregar a la columna que se quiere rellenar
    :rtype: int, float
    '''
    if column_name_to_fill == '15022-PROCEDIMIENTO DE NEUMOLOGÍA':
        return df.loc['15022_1-PROCEDIMIENTO DE NEUMOLOGÍA | Procedimiento', '66-HOSPITALIZACIÓN MEDICINA INTERNA']

    elif column_name_to_fill == '15038-PROCEDIMIENTO ONCOLOGÍA':
        return df.loc['15038_1-PROCEDIMIENTO ONCOLOGÍA | Procedimiento', '15107-CONSULTA ONCOLOGÍA']

    elif column_name_to_fill == '264-PROCEDIMIENTOS EBUS':
        return df.loc['264_1-PROCEDIMIENTOS EBUS | Procedimiento', '267-PROCEDIMIENTOS ENDOSCÓPICOS']

    elif column_name_to_fill == '265-PROCEDIMIENTOS ECMO':
        return df.loc['265_1-PROCEDIMIENTOS ECMO | Procedimiento', '166-UNIDAD DE CUIDADOS INTENSIVOS']

    elif column_name_to_fill == '270-PROCEDIMIENTOS TAVI':
        return df.loc['270_1-PROCEDIMIENTOS TAVI | Procedimiento', '253-PROCEDIMIENTOS DE HEMODINAMIA']


def fill_serv_farmaceutico(df):
    '''Funcion que permite rellenar la fila de SERVICIO FARMACEUTICO en el formato 6 de CC Apoyo de
    SIGCOM

    :param df: Es el DataFrame con el formato del SIGCOM
    :type df: pd.DataFrame

    :returns: El DataFrame con la fila SERVICIO FARMACEUTICO rellenado
    :rtype: pd.DataFrame
    '''
    columnas_a_imputar = ['15022-PROCEDIMIENTO DE NEUMOLOGÍA', '15038-PROCEDIMIENTO ONCOLOGÍA',
                          '264-PROCEDIMIENTOS EBUS', '265-PROCEDIMIENTOS ECMO', '270-PROCEDIMIENTOS TAVI']
    df_tmp = df.copy()

    for columna in columnas_a_imputar:
        value = obtain_value_to_add(df_tmp, columna)
        df_tmp.loc['55101_1-SERVICIO FARMACEUTICO | Prescripción',
                   columna] = value

    return df_tmp


def obtain_sigcom_format(total_imagenologia, total_tomografia):
    '''Funcion que permite obtener el formato 6_DistribucionDeProduccionDeCCDeApoyo para el SIGCOM

    :param total_imagenologia: Son la cantidad de prestaciones que se realizaron en imagenologia para
    el periodo analizado
    :type total_imagenologia: int

    :param total_tomografia: Son la cantidad de prestaciones que se realizaron en tomografia para
    el periodo analizado
    :type total_tomografia: int

    :returns: El DataFrame con el formato 6_DistribucionDeProduccionDeCCDeApoyo completamente rellenado y listo
    :rtype: pd.DataFrame
    '''
    df_resultado = pd.read_excel(
        'test_files_input/Tabla_resultado_diciembre.xlsx')
    df_tmp = rename_rows(df_resultado)
    df_tmp = rename_cols(df_tmp)

    df_tmp = df_tmp.set_index(df_tmp.columns[0])
    df_tmp['262-PROCEDIMIENTOS DE TRAUMATOLOGÍA'] = None
    df_tmp.loc['262_1-PROCEDIMIENTOS DE TRAUMATOLOGÍA | Procedimiento', :] = None

    df_tmp = order_cols(df_tmp)
    df_tmp = order_rows(df_tmp)

    df_tmp = change_row_with_proportional(
        df_tmp, '41108_1-IMAGENOLOGÍA | Exámen', total_imagenologia, IMAGENOLOGIA_PROPORTIONS)
    df_tmp = change_row_with_proportional(
        df_tmp, '41107_1-TOMOGRAFÍA | Estudio', total_tomografia, TOMOGRAFIA_PROPORTIONS)

    df_tmp = fill_serv_farmaceutico(df_tmp)

    return df_tmp


if __name__ == '__main__':
    formato = obtain_sigcom_format(
        total_imagenologia=1224, total_tomografia=870)
    formato.to_excel('test_files_output/output.xlsx')
