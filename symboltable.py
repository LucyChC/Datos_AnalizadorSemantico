from dataclasses import dataclass


@dataclass
class Symbol:
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
    symbol_table: dict

    def __init__(self) -> None:
        self.symbol_table = {}

    def key_exists(self, key):
        """
        Valida que la entrada exista en la tabla de simbolos
        :param key: Valor del item en la tabla de simbolos
        :return: true or false
        """
        return key in self.symbol_table  # Returns true if key is in symbol table, else false

    def get_key_attributes(self, key) -> Symbol:
        return self.symbol_table.get(key)  # Returns none if key has not been registered

    def update_key_attributes(self, key, new_attr_value: Symbol):
        self.symbol_table[key] = new_attr_value

    def add_new_entry(self, key, attr_value: Symbol):
        self.symbol_table[key] = attr_value

    def delete_entry(self, key):
        self.symbol_table.pop(key)

    def get_symbol_table(self):
        return self.symbol_table