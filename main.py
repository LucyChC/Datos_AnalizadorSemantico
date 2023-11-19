from scopestack import ScopeStack
from symboltable import SymbolTable, Symbol
from errorstack import ErrorStack
import re
from reutils import FUNCTION_DECLARATION_RE, VARIABLE_DECLARATION_RE, VARIABLE_ASSIGNATION_RE, CONDITIONS_RE, RETURN_RE
from validators import valid_return_type, validate_data_type

symbol_table = SymbolTable()
error_stack = ErrorStack()
scope_stack = ScopeStack()
