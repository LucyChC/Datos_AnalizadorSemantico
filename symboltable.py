from dataclasses import dataclass


@dataclass
class Symbol:

    """
    Se definen los simbolos como atributos que se utilizaran en la tabla de simbolos
    """
    key: str
    declaration_line_number: int
    type: str  # Function or Variable
    finishing_line_numbe: int | None  # None if datatype == Function
    data_type: str
    name: str
    scope: str
    value: str | None


# Keys will be scope+name attempting to hash the values
class SymbolTable():
    """
    Se define la estructura de la tabla de simbolos
    Se utiliza un diccionario para la estructura de la misma
    """
    symbol_table: dict

    def __init__(self) -> None:
        self.symbol_table = {}

    def key_exists(self, key):
        """
        Valida que la entrada exista en la tabla de simbolos
        Retorna True si la entrada con una llave asociada existe en la tabla
        si no se encuentra retorna false
        """
        return key in self.symbol_table  # Returns true if key is in symbol table, else false

    def get_key_attributes(self, key) -> Symbol:
        """
        Retorna atributos que estan asociados a la llave
        Retorna none si la llave no esta registrada
        """
        return self.symbol_table.get(key)

    def update_key_attributes(self, key, new_attr_value: Symbol):
        """
          Actualiza los atributos que estan asociados a la llave
        """
        self.symbol_table[key] = new_attr_value

    def add_new_entry(self, key, attr_value: Symbol):
        """
            Agrega un nuevo simbolo a la tabla, asociado a su llave
        """
        self.symbol_table[key] = attr_value

    def delete_entry(self, key):
        """
            Elimina los atributos asociados a una llave
        """
        self.symbol_table.pop(key)

    def get_symbol_table(self):
        """
        Retorna la tabla con todos los atributos
        """
        return self.symbol_table