class ErrorStack():  # Builder
    def __init__(self) -> None:
        self.error_stack = []

    def add_unknown_variable_error(self, variable_name, line_number):
        self.error_stack.append(f'Unknown variable "{variable_name}" at line {line_number}. Variable not declared')

    def add_already_declared_error(self, name, line_number):
        self.error_stack.append(f'Name "{name}" at line {line_number} is already taken.')

    def add_unknown_datatype_error(self, datatype, line_number):
        self.error_stack.append(f'Invalid datatype "{datatype}" at line {line_number}')

    def add_invalid_return_type_error(self, function_name, expected_datatype, line_number):
        self.error_stack.append(
            f'Return value does not match declaration of "{function_name}", expected "{expected_datatype}" at line {line_number}')

    def add_void_return_type_error(self, function_name):
        self.error_stack.append(f'"{function_name}" is void')

    def get_error_stack(self):
        return self.error_stack