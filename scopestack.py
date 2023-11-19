class ScopeStack():
    def __init__(self) -> None:
        """
         Inicializa una nueva instancia de ScopeStack.
        """
        self.scope_stack = []

    def push_scope(self, scope):
        """
         Agrega un nuevo ámbito a la pila de ámbitos.
         :param scope: El ámbito que se va a agregar a la pila.
        """
        self.scope_stack.append(scope)

    def pop_scope(self):
        """
          Elimina y devuelve el ámbito superior de la pila de ámbitos.
          Si la pila está vacía, devuelve "Global".
        """
        try:
            return self.scope_stack.pop()
        except Exception:
            return "Global"

    def peek_scope(self):
        """
           Devuelve el ámbito superior de la pila de ámbitos sin eliminarlo.
           Si la pila está vacía, devuelve "Global".
        """
        try:
            return self.scope_stack[-1]
        except Exception:
            return "Global"