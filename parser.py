# parser.py

from lexer import tokenize

class ASTNode:
    def __init__(self, type, value=None, children=None):
        self.type = type          # e.g. 'ASSIGN', 'PRINT', 'BINOP'
        self.value = value        # e.g. '+', variable name, number
        self.children = children or []  # sub-nodes

    def __repr__(self):
        return f"{self.type}({self.value}, {self.children})"

class Parser:
    def __init__(self, tokens):
        self.tokens = list(tokens)
        self.pos = 0

    def peek(self):
        return self.tokens[self.pos] if self.pos < len(self.tokens) else (None, None)

    def consume(self, expected_type=None):
        token = self.peek()
        if expected_type and token[0] != expected_type:
            raise SyntaxError(f"Expected {expected_type}, got {token}")
        self.pos += 1
        return token

    # Grammar:
    # program   -> stmt*
    # stmt      -> ID '=' expr ';' | 'print' '(' expr ')' ';'
    # expr      -> term (('+'|'-') term)*
    # term      -> factor (('*'|'/') factor)*
    # factor    -> NUMBER | ID | '(' expr ')'

    def parse(self):
        stmts = []
        while self.peek()[0] is not None:
            stmts.append(self.stmt())
        return ASTNode("PROGRAM", children=stmts)

    def stmt(self):
        kind, value = self.peek()
        if kind == 'ID':
            # assignment
            name = self.consume('ID')[1]
            self.consume('ASSIGN')
            expr = self.expr()
            self.consume('SEMI')
            return ASTNode("ASSIGN", value=name, children=[expr])
        elif kind == 'ID' and value == 'print':
            # print statement
            self.consume('ID')   # consume "print"
            self.consume('LPAREN')
            expr = self.expr()
            self.consume('RPAREN')
            self.consume('SEMI')
            return ASTNode("PRINT", children=[expr])
        elif kind == 'ID' and value != 'print':
            raise SyntaxError("Unknown identifier")
        elif kind is None:
            return None
        else:
            raise SyntaxError(f"Unexpected token {self.peek()}")

    def expr(self):
        node = self.term()
        while self.peek()[0] in ('PLUS', 'MINUS'):
            op = self.consume()[1]
            right = self.term()
            node = ASTNode("BINOP", value=op, children=[node, right])
        return node

    def term(self):
        node = self.factor()
        while self.peek()[0] in ('MULT', 'DIV'):
            op = self.consume()[1]
            right = self.factor()
            node = ASTNode("BINOP", value=op, children=[node, right])
        return node

    def factor(self):
        kind, value = self.peek()
        if kind == 'NUMBER':
            self.consume('NUMBER')
            return ASTNode("NUMBER", value=value)
        elif kind == 'ID':
            self.consume('ID')
            return ASTNode("VAR", value=value)
        elif kind == 'LPAREN':
            self.consume('LPAREN')
            node = self.expr()
            self.consume('RPAREN')
            return node
        else:
            raise SyntaxError(f"Unexpected factor {self.peek()}")
