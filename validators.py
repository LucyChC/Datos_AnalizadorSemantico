VALID_FUNCTION_TYPES = ["void", "int", "float", "string"]
VALID_VARIABLE_TYPES = ["int", "float", "string"]
KEYWORDS = ["if", "while", "return"]
VALID_CONDITIONERS = ["==", ">", "<"]


def validate_data_type(data_type, is_function: bool):
    if is_function:  # If is function then void is a valid data type
        return data_type in VALID_FUNCTION_TYPES
    else:
        return data_type in VALID_VARIABLE_TYPES


def valid_return_type(returning_type, function_type):
    return returning_type == function_type