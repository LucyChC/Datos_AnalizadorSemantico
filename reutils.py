VARIABLE_DECLARATION_RE = r"^(\t*|\s*)?(?P<Type>(\w+){1})\s(?P<VariableName>\w+)\s?={1}\s?(\"|\')?(?P<VariableValue>((\d*\.)?\d+)|\w+)+(\"|\')?"
VARIABLE_ASSIGNATION_RE = r"^(\t*|\s*)?(?P<VariableName>(\w+){1})(\s={1}\s?(\"|\')?(?P<VariableValue>((\d*\.)?\d+)|\w+)+(\"|\')?)?"
FUNCTION_DECLARATION_RE = r"^(?P<Type>(\w+){1})\s(?P<FunctionName>\w+)\((?P<FunctionParameters>((int|float|string){1}\s\w+(\,\s?)?)*)\)\{$"
CONDITIONS_RE = r"(\t*|\s*)?(?P<Operator>(if|while))\s?\((?P<VariableName>\w+)\s?(==|>|<){1}\s?(\"|\')?(?P<Condition>((\d*\.)?\d+|\w*))+(\"|\')?\)\{$"
RETURN_RE = r"(\t*|\s*)?return\s(?P<VariableName>\w+)"