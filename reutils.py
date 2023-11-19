VARIABLE_DECLARATION_RE = r"^(\t*|\s*)?(?P<Type>(\w+){1})\s(?P<VariableName>\w+)\s?={1}\s?(\"|\')?(?P<VariableValue>((\d*\.)?\d+)|\w+)+(\"|\')?"
"""
Se construye la estructura que tendra una declaracion de una variable 
Simbologia:/t /s =  validan espacios en blanco
/w= valida cuando un string contiene un caracter alfanumerico
/d=  valida digitos decimales
/.= valida digitos flotantes
? = se utilizan para validar coincidencias
VariableName: asocia al nombre de la variable
VariableValue: asocia el valor de la variable
Type: tipo de dato

"""

VARIABLE_ASSIGNATION_RE = r"^(\t*|\s*)?(?P<VariableName>(\w+){1})(\s={1}\s?(\"|\')?(?P<VariableValue>((\d*\.)?\d+)|\w+)+(\"|\')?)?"
"""
Se construye la estructura que tendra la asignacion de variable
Simbologia:/t /s =  validan espacios en blanco
/w= valida cuando un string contiene un caracter alfanumerico
/d=  valida digitos decimales
/.= valida digitos flotantes
? = se utilizan para validar coincidencias
VariableName: asocia al nombre de la variable
VariableValue: asocia el valor de la variable
{n}= especifica cuantas veces necesitamos que algo se repita en este caso seria {1}
"""

FUNCTION_DECLARATION_RE = r"^(?P<Type>(\w+){1})\s(?P<FunctionName>\w+)\((?P<FunctionParameters>((int|float|string){1}\s\w+(\,\s?)?)*)\)\{$"
"""
Construccion de la estructura para la declaracion de funciones
Simbologia:
/w= valida cuando un string contiene un caracter alfanumerico
? = se utilizan para validar coincidencias
$ = se utiliza para el fin de la funcion con un determinado caracter
FunctionName= se asocia al nombre de la funcion
FunctionParameters: Se define que los parametros de la funcion pueden ser int, float o string
{n}= especifica cuantas veces necesitamos que algo se repita en este caso seria {1}
"""
CONDITIONS_RE = r"(\t*|\s*)?(?P<Operator>(if|while))\s?\((?P<VariableName>\w+)\s?(==|>|<){1}\s?(\"|\')?(?P<Condition>((\d*\.)?\d+|\w*))+(\"|\')?\)\{$"
"""
Se construye la estructura de los condicionales if y while
Simbologia: /t /s =  validan espacios en blanco
/w= valida cuando un string contiene un caracter alfanumerico
/d=  valida digitos decimales
/.= valida digitos flotantes
? = se utilizan para validar coincidencias
$ = se utiliza para el fin de la condicion con un determinado caracter
*= coincide con una o mas apariciones
VariableName: asocia al nombre de la variable
Operator: se asocia a if, while
Condition: condicion evaluativa asociada"""

RETURN_RE = r"(\t*|\s*)?return\s(?P<VariableName>\w+)"
""" 
Se construye la estructura para la declaracion del retorno de una funcion
Simbologia:/t /s =  validan espacios en blanco
/w= valida cuando un string contiene un caracter alfanumerico
VariableName: asocia al nombre de la variable


"""