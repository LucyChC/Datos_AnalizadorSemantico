class ScopeStack():
    def __init__(self) -> None:
        self.scope_stack = []

    def push_scope(self, scope):
        self.scope_stack.append(scope)

    def pop_scope(self):
        try:
            return self.scope_stack.pop()
        except Exception:
            return "Global"

    def peek_scope(self):
        try:
            return self.scope_stack[-1]
        except Exception:
            return "Global"