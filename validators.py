VALID_FUNCTION_TYPES = ["void", "int", "float", "string"]
"""
Se define el tipo de datos asociados a la funcion 
"""
VALID_VARIABLE_TYPES = ["int", "float", "string"]
"""
Definicion del tipo de dato de la variable, entero, texto o flotante
"""
KEYWORDS = ["if", "while", "return"]
"""
Definicion de palabras claves dentro de las funciones, ejemplo ciclo while o condicionales if
"""
VALID_CONDITIONERS = ["==", ">", "<"]
"""
Definicion de la simbologia para las diferentes comparaciones que se puedan hacer dentro de una funcion, mayor, igual, menor
"""


def validate_data_type(data_type, is_function: bool):
    """
    Funcion para validar si es una funcion
    :param data_type:  tipo de dato
    :param is_function: mediante la validacion de tipo booleano valida si es funcion
    :return: true or false
    """
    if is_function:  # Si es funcion void es un tipo de dato valido
        return data_type in VALID_FUNCTION_TYPES
    else:
        return data_type in VALID_VARIABLE_TYPES


def valid_return_type(returning_type, function_type):
    """
    Valida que el retorno de la funcion sea igual al de la declaracion de la funcion
    :param returning_type: tipo de dato asociado al return de la funcion
    :param function_type: tipo de dato asociado a la funcion
    :return: true si son iguales
    """
    return returning_type == function_type