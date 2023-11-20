from scopestack import ScopeStack
from symboltable import SymbolTable, Symbol
from errorstack import ErrorStack
import re
from reutils import FUNCTION_DECLARATION_RE, VARIABLE_DECLARATION_RE, VARIABLE_ASSIGNATION_RE, CONDITIONS_RE, RETURN_RE
from validators import valid_return_type, validate_data_type

symbol_table = SymbolTable()
error_stack = ErrorStack()
scope_stack = ScopeStack()

if __name__ == "__main__":


    with open("./code_error.txt", "r", encoding="utf-8") as file:
        code = file.readlines()
        for line in code:
            if len(line) > 0: # Ignore empty lines
                line_number = code.index(line) + 1
                if re.match(VARIABLE_DECLARATION_RE, line) is not None: # A variable is being declared
                    re_match = re.search(VARIABLE_DECLARATION_RE, line)
                    scope = scope_stack.peek_scope()
                    scope_key = re_match.group('VariableName')
                    variable_data_type = re_match.group("Type")
                    if not validate_data_type(variable_data_type, False):
                        error_stack.add_unknown_datatype_error(variable_data_type, line_number)
                    symbol = Symbol(scope_key, line_number, "variable", None, variable_data_type, re_match.group("VariableName"), scope, re_match.group("VariableValue"))
                    symbol_table.add_new_entry(symbol.key, symbol)
                elif re.match(FUNCTION_DECLARATION_RE, line) is not None: # There is a function being declared
                    re_match = re.search(FUNCTION_DECLARATION_RE, line)
                    scope = 'global' # By default all functions must have global scopes
                    scope_key = re_match.group('FunctionName')
                    function_data_type = re_match.group("Type")
                    if not validate_data_type(function_data_type, True):
                        error_stack.add_unknown_datatype_error(function_data_type, line_number)
                    symbol = Symbol(scope_key, line_number, "function", None, function_data_type, re_match.group("FunctionName"), scope, None)
                    symbol_table.add_new_entry(symbol.key, symbol)
                    scope_stack.push_scope(re_match.group("FunctionName"))
                    parameters = re_match.group("FunctionParameters")
                    if len(parameters) > 0: # Process function parameters
                        for param in parameters.split(", "):
                            p = param.split(" ")
                            scope_key = p[1]
                            symbol = Symbol(scope_key, line_number, "parameter", None, p[0], p[1], scope_stack.peek_scope(), None)
                            symbol_table.add_new_entry(symbol.key, symbol)
                elif (re.match(VARIABLE_ASSIGNATION_RE, line) is not None
                            and 'if' not in line
                            and 'while' not in line
                            and 'return' not in line): # A variable is being assigned
                    re_match = re.search(VARIABLE_ASSIGNATION_RE, line)
                    variable_key = re_match.group('VariableName')
                    if not symbol_table.key_exists(variable_key): # Variable hasn't been declared, add error
                        error_stack.add_unknown_variable_error(variable_key, line_number)
                    else: # Update value of declared variable
                        variable_symbol = symbol_table.get_key_attributes(variable_key)
                        variable_symbol.value = re_match.group('VariableValue')
                elif re.match(CONDITIONS_RE, line) is not None: # Assuming that there are not special conditions
                    re_match = re.search(CONDITIONS_RE, line)
                    scope_key =  scope_stack.peek_scope()
                    scope_key = f'{scope_key};{re_match.group("Operator")}'
                    variable = re_match.group("VariableName")
                    scope_stack.push_scope(scope_key)
                    if not symbol_table.key_exists(variable):
                        error_stack.add_unknown_variable_error(variable, line_number)
                elif re.match(RETURN_RE, line) is not None: # Assuming that there are not special conditions
                    re_match = re.search(RETURN_RE, line)
                    returned_variable_key = re_match.group('VariableName')
                    if not symbol_table.key_exists(returned_variable_key):
                        error_stack.add_unknown_variable_error(returned_variable_key, line_number)
                    else:
                        current_scope_key = scope_stack.peek_scope().split(';')[0]
                        current_scope = symbol_table.get_key_attributes(current_scope_key)
                        if current_scope.data_type == 'void':
                            error_stack.add_void_return_type_error(current_scope.name)
                            continue
                        returned_variable = symbol_table.get_key_attributes(returned_variable_key)
                        if not valid_return_type(returned_variable.data_type, current_scope.data_type):
                            error_stack.add_invalid_return_type_error(current_scope.name, current_scope.data_type, line_number)
                elif '}' in line: # Exit the function scope or condition
                    scope_stack.pop_scope()


    final_error_stack = error_stack.get_error_stack()
    if len(final_error_stack) > 0:
        for error in final_error_stack:
            print(f'[ERROR] - {error}')
    else:
        print("Code has no errors!!")