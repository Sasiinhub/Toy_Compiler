# run.py

from lexer import tokenize

code = "x = 10 + 20;\nprint(x);"

for token in tokenize(code):
    print(token)
