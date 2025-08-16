import re

# Token specification as regex patterns
token_spec = [
    ('NUMBER',  r'\d+'),
    ('ID',      r'[a-zA-Z_][a-zA-Z_0-9]*'),
    ('ASSIGN',  r'='),
    ('PLUS',    r'\+'),
    ('MINUS',   r'-'),
    ('MULT',    r'\*'),
    ('DIV',     r'/'),
    ('LPAREN',  r'\('),
    ('RPAREN',  r'\)'),
    ('SEMI',    r';'),
    ('SKIP',    r'[ \t]+'),
    ('NEWLINE', r'\n'),
]

# Join all regex into a single pattern
token_re = '|'.join(f'(?P<{name}>{pattern})' for name, pattern in token_spec)

# Tokenizer function
def tokenize(code):
    for mo in re.finditer(token_re, code):
        kind = mo.lastgroup
        value = mo.group()
        if kind == 'SKIP' or kind == 'NEWLINE':
            continue
        yield (kind, value)
