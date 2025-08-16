# Toy_Compiler
Try to creating a simple compiler to understand how the compiler works.. may be own language syntax..





Absolutely, I’d love to help you build a **compiler** step by step for learning purposes! It’s a great way to understand how programming languages work from the inside out — and it also improves your knowledge of **parsing, grammars, tokens, assembly/code generation**, and sometimes **virtual machines**.

---

### ✅ **One Best Book to Follow**

**Book:**
📘 **"Crafting a Compiler" by Charles N. Fischer, Ron K. Cytron, and Richard J. LeBlanc**

* 📌 Why this book?

  * Starts from basics: Lexical analysis → Parsing → Semantic analysis → Code generation → Optimization
  * Clear structure and practical examples
  * Focus on building an actual compiler
  * Recommended for learners

---

### 🛠️ What You'll Learn (Compiler Stages)

| Stage | Topic                                          | Tool/Language                                              |
| ----- | ---------------------------------------------- | ---------------------------------------------------------- |
| 1.    | **Lexical Analysis** (splits code into tokens) | Build or use tools like **Lex** / **Flex**                 |
| 2.    | **Syntax Analysis** (parse grammar)            | Use **Yacc** / **Bison** or write recursive-descent parser |
| 3.    | **Semantic Analysis** (meaning, type checking) | Write code to manage symbol tables and type info           |
| 4.    | **Intermediate Code Generation**               | Generate code like three-address code (TAC)                |
| 5.    | **Optimization** (optional)                    | Remove redundancy, improve code                            |
| 6.    | **Target Code Generation**                     | Output Assembly, JVM Bytecode, or LLVM IR                  |

---

### 🚧 Language You Can Use

* **C/C++** → Traditional and widely used for compiler projects
* **Java** → Good for beginners + many parser generators
* **Python** → Simple syntax, perfect for learning (e.g. using `ply`, `lark`, or `antlr`)

---

### 🚀 Suggested Project Plan

| Phase   | Goal                                                         |
| ------- | ------------------------------------------------------------ |
| Week 1  | Learn tokens, grammar (BNF, EBNF), write a tokenizer         |
| Week 2  | Build parser for simple expressions (like `a + b * c`)       |
| Week 3  | Add support for variables and simple statements              |
| Week 4  | Translate parsed expressions into a basic stack machine code |
| Week 5+ | Add functions, conditionals, loops, then try optimization    |

---

### 👶 Start Small: Toy Language Example

Design a mini-language like:

```c
int x = 5 + 10;
print(x);
```

And build a compiler that turns this into:

```
PUSH 5
PUSH 10
ADD
STORE x
LOAD x
PRINT
```

---

### 💡 Tools That Might Help

* **Flex & Bison** (C/C++)
* **ANTLR** (Java / Python / C++)
* **PLY** (Python Lex-Yacc)
* **LLVM** (for backend code generation)

---

Would you like me to help you:

* Pick a language like Python/C/Java first?
* Start designing a simple grammar and tokenizer?
* Or share step-by-step exercises with example code?

Let’s build this compiler together — just like creating your own mini C or Python interpreter! 🔧💡

query:
Great. Is it the same components for all compilers used in most of the top languages? If yes means, why I am asking means, I think after compiler building, or while compiler building, I want to make virtual machine like JVM. Is it possible? Is it make any uncontrolled flows?

result:
Great thinking! Yes — you're absolutely on the right track. Let's break this into parts and answer your insightful question clearly.

---

## ✅ Is it the Same Components for All Compilers?

**Yes, most modern compilers share the same core components:**

| Stage                                | Purpose                                     | Universally Used? |
| ------------------------------------ | ------------------------------------------- | ----------------- |
| **Lexical Analysis**                 | Break code into tokens                      | ✅ Yes             |
| **Syntax Analysis**                  | Check grammar using parsing                 | ✅ Yes             |
| **Semantic Analysis**                | Type checking, symbol table                 | ✅ Yes             |
| **Intermediate Representation (IR)** | Code in a format between source and machine | ✅ Yes             |
| **Optimization (optional)**          | Improve performance or size                 | ✅ Yes             |
| **Code Generation**                  | Produce assembly or VM bytecode             | ✅ Yes             |

So, **whether you're building a C compiler, Java compiler, or even a custom DSL**, the structure is very similar. The difference lies in **syntax, semantics, and the target (machine code or bytecode).**

---

## 💡 Is Building a Virtual Machine (Like JVM) Possible?

**Yes, absolutely — and it's a brilliant idea.**

A **Virtual Machine (VM)** is a software program that:

* Executes **intermediate bytecode** (not raw machine code)
* Acts like a CPU + Memory + Stack Frame handler
* Offers **platform independence**, like Java

You can definitely build your own VM **after or along with** your compiler.

### 🔧 How It Connects:

| Step                 | Output                                                |
| -------------------- | ----------------------------------------------------- |
| Your Compiler        | Converts source code → bytecode (for your custom VM)  |
| Your Virtual Machine | Reads bytecode → executes using stack/register/memory |

Think of it like:

```
[Your Language] --(Compiler)--> [Your Bytecode] --(Your VM)--> Output
```

---

## ⚠️ Will It Cause Uncontrolled Flows?

If you **design your VM properly**, the control flow will be completely in your hands. But a few risks are:

### Potential Challenges (and how to solve them):

| Problem                | Risk                   | Solution                                |
| ---------------------- | ---------------------- | --------------------------------------- |
| Infinite loops         | VM gets stuck          | Add timeout or instruction limits       |
| Memory overflow        | Stack/memory crash     | Use bounds and heap management          |
| Security risks         | If accepting user code | Sandbox the VM                          |
| Unhandled instructions | Crash                  | Build proper error handling for opcodes |

As long as:

* You define **clear bytecode instructions**
* Build a **stack/register-based VM**
* Handle **branches, loops, and function calls properly**

→ You’ll stay in full control.

---

## 🎯 Your Learning Path Can Be:

1. ✅ Build Compiler (Stage 1–4):

   * Parse code
   * Output intermediate bytecode
   * Keep it simple like: `LOAD`, `ADD`, `JMP`, `CALL`

2. 🔁 Build a Stack-Based VM:

   * Read your bytecode line by line
   * Maintain a stack
   * Execute instructions like `PUSH`, `POP`, `ADD`, `PRINT`

3. ⚙️ Connect Both:

   * Compile any code into bytecode
   * Feed bytecode to your VM
   * Observe how real languages work underneath!

---

## 🧠 Bonus Motivation:

➡️ You’re basically creating your own version of:

* **Java (with JVM)**
* **Python (with CPython VM)**
* **Lua (with Lua VM)**

All those real-world interpreters use the same concepts you’re trying to build. 👏

---

Would you like me to:

* Help design your own VM instruction set?
* Show a real example of how to implement the VM?
* Or first help you build your compiler's tokenizer and parser?

Let’s pick the next step!

query:
Can we start from begging,  the compiler first then we move to vm!

result:
Perfect! Starting from the **compiler** first is the best approach — it gives you full control over how your custom language is parsed, and later you can decide how the **virtual machine** should execute it.

Let’s go step by step in a beginner-friendly and practical way.

---

## 🧭 Step-by-Step Plan to Build a Compiler

We'll build a **simple compiler** for a toy programming language, like:

```txt
x = 10 + 20;
print(x);
```

This will go through:

1. **Tokenization** → Break input into tokens
2. **Parsing** → Build a tree from tokens (syntax structure)
3. **Semantic Analysis** → Validate variable names, etc.
4. **Code Generation** → Output bytecode for your future VM

---

## 🧰 Step 1: Environment & Language Setup

### ✅ Language We’ll Use: **Python**

Why?

* Easy syntax
* Lots of libraries for text processing
* Good for learning fast

> If you prefer C, Java, or C++ instead, I can adapt everything accordingly.

---

## 📦 Step 2: Project Folder Structure

```
mycompiler/
│
├── lexer.py        ← Tokenizer
├── parser.py       ← Grammar rules and parser
├── node.py         ← AST (Abstract Syntax Tree)
├── codegen.py      ← Bytecode or intermediate code
├── run.py          ← Main driver
└── test.code       ← Example program to compile
```

---

## ✏️ Step 3: Design the Language Syntax

We will design a mini-language:

```text
x = 5 + 10;
y = x * 2;
print(y);
```

Supports:

* Arithmetic: `+`, `-`, `*`, `/`
* Assignment: `=`
* Print: `print(...)`
* Integers and variables

---

## 🚀 Step 4: Start with the **Lexer** (Tokenizer)

A lexer turns source code into tokens:

```python
# lexer.py

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

token_re = '|'.join(f'(?P<{name}>{pattern})' for name, pattern in token_spec)

def tokenize(code):
    for mo in re.finditer(token_re, code):
        kind = mo.lastgroup
        value = mo.group()
        if kind == 'SKIP' or kind == 'NEWLINE':
            continue
        yield (kind, value)
```

### 🧪 Example usage:

```python
# run.py

from lexer import tokenize

code = "x = 10 + 20;\nprint(x);"

for token in tokenize(code):
    print(token)
```

Output:

```
('ID', 'x')
('ASSIGN', '=')
('NUMBER', '10')
('PLUS', '+')
('NUMBER', '20')
('SEMI', ';')
('ID', 'print')
('LPAREN', '(')
('ID', 'x')
('RPAREN', ')')
('SEMI', ';')
```

---

## ✅ Next Step?

Would you like me to continue by writing the **Parser** (step 2) that builds a syntax tree from these tokens?

After the parser, we’ll move to code generation → then VM!

Let me know if:

* You're okay with Python for now
* You want the next step: the **Parser**
* Or if you want to try running the lexer first and explore it a bit



query:
can you explain the lexer program line by line to understand how you make tokeniser and how the tokeniser works!  

result: 
Absolutely! Let's **break down the `lexer.py` program** line by line. This will help you understand how a **tokenizer (lexer)** works — how it reads source code and turns it into meaningful pieces (tokens) like `NUMBER`, `ID`, `PLUS`, etc.

---

## 🔍 Full Code Recap

```python
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
```

---

## 🔍 Line-by-Line Explanation

---

### 🔹 `import re`

We import Python’s **`re`** module (regular expressions). Regex is used to **match patterns in text** — perfect for scanning code for tokens.

---

### 🔹 `token_spec = [...]`

This is a list of **token definitions**, each one is:

```python
('TOKEN_NAME', 'regex-pattern')
```

#### Explanation of Some Tokens:

| Token Name  | Pattern                  | Meaning                                                                    |
| ----------- | ------------------------ | -------------------------------------------------------------------------- |
| `'NUMBER'`  | `\d+`                    | One or more digits (e.g. `10`, `42`)                                       |
| `'ID'`      | `[a-zA-Z_][a-zA-Z_0-9]*` | A variable name (starts with letter or `_`, followed by letters/digits/\_) |
| `'ASSIGN'`  | `=`                      | Assignment operator                                                        |
| `'PLUS'`    | `\+`                     | Plus sign (escaped `+` because it's special in regex)                      |
| `'SKIP'`    | `[ \t]+`                 | Spaces or tabs (we ignore them)                                            |
| `'NEWLINE'` | `\n`                     | Line breaks (ignored too)                                                  |

So this list says:
➡️ “If you see digits → that’s a `NUMBER`.
If you see `print`, `x`, etc. → that’s an `ID` (identifier),
If you see `+` → it's a `PLUS`, and so on.”

---

### 🔹 `token_re = '|'.join(...)`

We combine all regexes into **one big pattern** using the `|` symbol (means "OR" in regex):

```python
(?P<NAME>pattern)
```

This is a **named group** — tells Python to remember which pattern matched.

✅ So the final regex looks like:

```regex
(?P<NUMBER>\d+)|(?P<ID>[a-zA-Z_][a-zA-Z_0-9]*)|(?P<ASSIGN>=)|...
```

Now Python knows:

* If `\d+` matches, label it `NUMBER`
* If `[a-zA-Z_][a-zA-Z_0-9]*` matches, label it `ID`
* and so on…

---

### 🔹 `def tokenize(code):`

This function takes your source code (e.g. `x = 10 + 5;`) and splits it into tokens.

---

### 🔹 `for mo in re.finditer(token_re, code):`

`re.finditer(...)` goes through your source code **one match at a time** using the big `token_re`.

It returns a **Match Object (mo)** each time something matches.

---

### 🔹 `kind = mo.lastgroup`

This gets the **name of the matching token** — e.g., `NUMBER`, `PLUS`, etc.

It uses the name from our `(?P<NAME>...)` part.

---

### 🔹 `value = mo.group()`

This gets the actual **text matched** — e.g., `10`, `+`, or `x`.

---

### 🔹 `if kind == 'SKIP' or kind == 'NEWLINE': continue`

We **ignore spaces, tabs, and newlines** because they don't matter in our language grammar.

---

### 🔹 `yield (kind, value)`

This gives back a tuple like:

```python
('ID', 'x')
('ASSIGN', '=')
('NUMBER', '10')
```

It doesn't return all tokens at once. Instead, it **yields one at a time**, so you can loop through them using:

```python
for token in tokenize(code):
    print(token)
```

---

## 🧪 Sample Input and Output

Input:

```python
x = 5 + 3;
print(x);
```

Output:

```
('ID', 'x')
('ASSIGN', '=')
('NUMBER', '5')
('PLUS', '+')
('NUMBER', '3')
('SEMI', ';')
('ID', 'print')
('LPAREN', '(')
('ID', 'x')
('RPAREN', ')')
('SEMI', ';')
```

---

## 🧠 Summary: What This Lexer Does

✅ Scans input from left to right
✅ Matches using patterns (regex)
✅ Skips whitespace and newlines
✅ Returns a stream of meaningful tokens
✅ Forms the **first step of your compiler**!

---

## ✅ Next Step?

Would you like to:

1. Try modifying this lexer to add new tokens (like `if`, `else`)?
2. Move to the **Parser**, where we’ll build an Abstract Syntax Tree (AST)?
3. Or want a small assignment to test your understanding of the lexer?

Let me know how you’d like to continue!


query:
1. r before pattern dinotes?
2.  2. F' and ?p  
3. Why the for loop looks like  This? I mean if possible or my question is valid, compare for statement with java for

result:
Your question is **absolutely valid** and very thoughtful. You're asking about:

1. `r` before regex patterns like `r'\d+'`
2. `f'...'` and `(?P<...)` in regex
3. Python's `for` loop (especially `for mo in re.finditer(...)`) vs Java's `for` loop

Let’s answer each clearly:

---

## ✅ 1. What does `r'...'` (raw string) mean in Python?

This is called a **raw string**.

### 🔹 Problem:

In normal strings:

* `\n` → newline
* `\t` → tab
* `\\` → backslash

So writing regex like `"\d+"` would be **confusing** because `\d` might be treated as a special escape (but `\d` is a regex symbol for digit).

### ✅ Solution: Use `r'...'` → raw string

It tells Python:

> “Don’t treat backslashes as special. Keep them as-is.”

### Example:

```python
print("\n")    # newline
print(r"\n")   # prints \n as plain text
```

### In our Lexer:

```python
r'\d+'   # match digits like 1, 23, 999 — REGEX for "digit one or more times"
```

So `r'\d+'` is cleaner and safer to use in regular expressions.

---

## ✅ 2. What is `f'...'` and `(?P<...>)` in the code?

### 🔹 A) `f'...'` → Python f-string (formatted string)

It allows **string interpolation** (like Java's `String.format` or `+`).

```python
name = "x"
print(f"Hello {name}")   # Hello x
```

In our lexer:

```python
f'(?P<{name}>{pattern})'
```

This becomes:

```python
'(?P<NUMBER>\\d+)'     # if name = "NUMBER", pattern = "\\d+"
```

---

### 🔹 B) `(?P<NAME>...)` in Regex

This is **named capturing group** in regex.

```regex
(?P<ID>[a-zA-Z_][a-zA-Z_0-9]*)
```

Means:

* Match any valid identifier like `print`, `x`, `myVar`
* Assign the name `ID` to this match

Then later, in the loop:

```python
kind = mo.lastgroup   # gives "ID"
value = mo.group()    # gives matched text, like "x"
```

So you know what kind of token it is.

> 🔑 Without `(?P<NAME>...)`, we wouldn’t know **which pattern matched**.

---

## ✅ 3. Why the `for` loop looks like that in Python? How is it different from Java?

Let’s compare:

### 🔹 Python:

```python
for mo in re.finditer(token_re, code):
    # mo = match object
    ...
```

### 🔹 Java equivalent:

```java
Pattern p = Pattern.compile(token_re);
Matcher m = p.matcher(code);

while (m.find()) {
    // process match m.group()
}
```

#### 🔄 Similarities:

* Python uses `for item in iterable` instead of `while`.
* `re.finditer()` returns an **iterator** of Match objects (like `Matcher.find()` in Java).
* In Python, this `for` is common when dealing with sequences, files, matches, etc.

---

### 🔍 Python `for` syntax compared to Java:

| Concept       | Java                          | Python                          |
| ------------- | ----------------------------- | ------------------------------- |
| For-each loop | `for (Type item : list)`      | `for item in list:`             |
| Indexed loop  | `for (int i = 0; i < n; i++)` | `for i in range(n):`            |
| While loop    | `while (condition)`           | `while condition:`              |
| Iterators     | `while (matcher.find())`      | `for match in re.finditer(...)` |

So Python's `for` is **more flexible** — it works with any "iterable" (list, file, generator, regex matcher).

---

## ✅ Summary

| Concept             | Meaning                                                                   |
| ------------------- | ------------------------------------------------------------------------- |
| `r'...'`            | Raw string — keep backslashes literal (`\d`, `\n`, etc.)                  |
| `f'...'`            | Formatted string — insert variables (`f"{name}"`)                         |
| `(?P<name>pattern)` | Named regex group — used to get which pattern matched                     |
| `for ... in ...`    | Python's clean, flexible loop over iterables (vs Java's `while` or `for`) |

---

Would you like to try modifying the lexer, or shall we move to the **parser**, which builds the syntax tree from tokens?

I'm happy to walk line by line again in the parser too.

query: 
Again explain in detail (?P<{name}>{pattern})'

result:
Absolutely! The expression `(?P<{name}>{pattern})` is a key part of how we build a **custom tokenizer (lexer)** using **Python’s regular expressions**.

Let’s **break it down fully and slowly**, and even include **examples** so it becomes super clear.

---

## ✅ Goal: What Are We Trying to Do?

We're trying to create a **big regex** that can match **different types of tokens**, such as:

* Identifiers (`x`, `print`)
* Numbers (`10`, `999`)
* Operators (`+`, `=`)
* Punctuation (`;`, `(`)

But also we want to **label** each part with a **name**, so when it matches something, we know **what kind of token** it is.

---

## ✅ The Format: `(?P<name>pattern)`

This is called a **named capturing group** in Python’s regular expressions.

### 🔹 General form:

```python
(?P<NAME>REGEX_PATTERN)
```

* `?P<NAME>`: Assigns a **name** to this pattern
* `REGEX_PATTERN`: The regex pattern to match

---

### 🔧 Example 1: Matching an identifier

```python
pattern = r'(?P<ID>[a-zA-Z_][a-zA-Z_0-9]*)'
```

This matches:

* `x`
* `my_var1`
* `Print`

And it **names** the match as `ID`.

So if you write:

```python
import re

regex = r'(?P<ID>[a-zA-Z_][a-zA-Z_0-9]*)'
match = re.match(regex, 'hello123')

print(match.group())          # hello123
print(match.lastgroup)        # ID
```

✅ Output:

```
hello123
ID
```

Now you know both:

* The **value** matched: `'hello123'`
* The **type** of token: `'ID'`

---

## 🔁 Back to `f'(?P<{name}>{pattern})'`

In our code, we want to dynamically create this string for **many different token types**, not just one.

Here’s the full line from our lexer again:

```python
token_re = '|'.join(f'(?P<{name}>{pattern})' for name, pattern in token_spec)
```

Let’s see what this does step-by-step.

### 🔹 Suppose `token_spec` contains:

```python
[
  ('NUMBER', r'\d+'),
  ('ID', r'[a-zA-Z_][a-zA-Z_0-9]*'),
  ('PLUS', r'\+')
]
```

The `f-string`:

```python
f'(?P<{name}>{pattern})'
```

becomes:

```python
'(?P<NUMBER>\\d+)'        # for name='NUMBER', pattern='\\d+'
'(?P<ID>[a-zA-Z_][a-zA-Z_0-9]*)'
'(?P<PLUS>\\+)'
```

So the `token_re` string becomes:

```regex
(?P<NUMBER>\d+)|(?P<ID>[a-zA-Z_][a-zA-Z_0-9]*)|(?P<PLUS>\+)
```

This is a single **combined regex** that matches:

* Digits
* Identifiers
* Plus signs

And labels each match with a name like `NUMBER`, `ID`, or `PLUS`.

---

## 🔍 Why We Use `(?P<NAME>...)` Instead of Just `(...)`?

With unnamed groups, you'd just get the value (like `10`), but **not the type**.

But we want both:

* The value (`10`)
* And what kind of token it is (`NUMBER`)

That's what `(?P<name>...)` gives us.

---

## ✅ How It Helps in Code

Inside our tokenizer:

```python
for mo in re.finditer(token_re, code):
    kind = mo.lastgroup   # gets the name from (?P<NAME>...)
    value = mo.group()    # gets the matched text
```

So you get output like:

```
('NUMBER', '10')
('PLUS', '+')
('NUMBER', '20')
```

Which is exactly what we need for the parser!

---

## ✅ Summary

| Syntax                     | Meaning                                                 |                                                         |
| -------------------------- | ------------------------------------------------------- | ------------------------------------------------------- |
| `(?P<NAME>...)`            | A **named group** in regex — stores what kind of match  |                                                         |
| `f'(?P<{name}>{pattern})'` | Builds this named group dynamically for each token type |                                                         |
| \`token\_re = '            | '.join(...)\`                                           | Joins all patterns into one big regex with named groups |
| `mo.lastgroup`             | Tells you **which token type matched**                  |                                                         |
| `mo.group()`               | Tells you **what actual text matched**                  |                                                         |

---

Would you like to:

* See how this all looks visually (diagram of how regex finds tokens)?
* Or move on to the **parser**, the next compiler step?
* Or want a small assignment to practice writing your own token rule?

Let me know — we’ll keep it smooth and exciting!

query:
what about match objests? is it defines on the code as mo?

result:
Great question! Let's clarify this — you're right to notice the term **`mo`** in this line:

```python
for mo in re.finditer(token_re, code):
```

---

## ✅ What is `mo`?

`mo` is just a **variable name** we chose — it stands for **Match Object**.

In Python, when using `re.finditer(...)`, you get back an **iterator of `MatchObject` instances**, each one representing a single match of a token from the source code.

So:

```python
for mo in re.finditer(token_re, code):
```

means:

➡️ “Loop through every match of the combined regex pattern in the code, and for each **match object**, call it `mo`.”

---

## 🧪 What is a MatchObject?

A `MatchObject` is created whenever a regex finds a match. It contains **methods and properties** to access:

* What was matched
* Which pattern matched it
* Where in the string it was found

### 📘 Key `MatchObject` methods we use:

| Method                    | What It Does                          | Example       |
| ------------------------- | ------------------------------------- | ------------- |
| `mo.group()`              | The actual text matched               | `"42"`        |
| `mo.lastgroup`            | Name of the pattern that matched      | `"NUMBER"`    |
| `mo.start()` / `mo.end()` | Start and end positions in the string | For debugging |

---

### 🔍 Example of `MatchObject`

Let’s say your input is:

```python
code = "x = 10"
```

Your combined regex sees this:

* `x` matches `'ID'`
* `=` matches `'ASSIGN'`
* `10` matches `'NUMBER'`

When this line runs:

```python
for mo in re.finditer(token_re, code):
```

It gives three MatchObjects — one for each token.

So on first iteration:

```python
mo.group()     → 'x'
mo.lastgroup   → 'ID'
```

And so on.

---

## 💡 So, to answer your question:

> ❓ **"Is `mo` defined in the code?"**

✅ **Yes, it's a variable name in the `for` loop**, and its value is **each MatchObject** returned by `re.finditer(...)`.

You could rename it to anything like `match` or `m`, for example:

```python
for match in re.finditer(token_re, code):
    kind = match.lastgroup
    value = match.group()
```

But `mo` is short and common shorthand in regex-based code for **Match Object**.

---

Would you like me to:

* Show how to debug or visualize these MatchObjects live?
* Add `mo.start()` / `mo.end()` to show where the token occurs in the code?
* Or move to writing the parser next?


query:
why we join?

result:
Excellent question! Let’s break this down clearly:

---

## 🔗 Why Do We **Join All Patterns** into One Regex?

In this line:

```python
token_re = '|'.join(f'(?P<{name}>{pattern})' for name, pattern in token_spec)
```

We are creating **one big regular expression** that matches **any one of the tokens**.

---

### ✅ Purpose of Joining:

We want to scan the source code **from left to right** and match **the first valid token** at each step.

By combining all patterns into a single regex, we can:

* Use `re.finditer(...)` just once
* Let the regex engine automatically figure out **which token matched**
* Retrieve the **token type (name)** using `.lastgroup`
* Avoid writing a manual "check for each token type" loop

---

### 🧠 What does the joined regex look like?

If your `token_spec` includes:

```python
[
    ('NUMBER',  r'\d+'),
    ('ID',      r'[a-zA-Z_][a-zA-Z_0-9]*'),
    ('PLUS',    r'\+'),
]
```

Then the joined regex becomes:

```regex
(?P<NUMBER>\d+)|(?P<ID>[a-zA-Z_][a-zA-Z_0-9]*)|(?P<PLUS>\+)
```

* The `(?P<NAME>...)` part is a **named group** — it labels the match.
* The `|` is the **OR** operator, so it tries to match any one of the token patterns.

---

### ⚙️ Why Not Match One-by-One?

If we didn’t join them, we’d have to write code like:

```python
for each character:
    try match NUMBER
    else try match ID
    else try match PLUS
    ...
```

That would be slow, messy, and error-prone.
Instead, with one joined regex:

* Python’s `re` module efficiently matches the **first valid pattern**
* You get both the **matched string** and **which type it is**

---

### ✅ Summary: Why We Join Patterns

| Reason      | Benefit                             |
| ----------- | ----------------------------------- |
| Simplicity  | One pattern handles all token types |
| Speed       | Regex engine is optimized           |
| Clarity     | Easy to manage token types          |
| Flexibility | Add/remove token types in one list  |

---

Would you like to **print out the actual full regex string** to see what it looks like? I can help you try that.

Or shall we now move to **writing the parser** that uses these tokens?


query:
Again explain in detail (?P<{name}>{pattern})'

result:
Absolutely! The expression `(?P<{name}>{pattern})` is a key part of how we build a **custom tokenizer (lexer)** using **Python’s regular expressions**.

Let’s **break it down fully and slowly**, and even include **examples** so it becomes super clear.

---

## ✅ Goal: What Are We Trying to Do?

We're trying to create a **big regex** that can match **different types of tokens**, such as:

* Identifiers (`x`, `print`)
* Numbers (`10`, `999`)
* Operators (`+`, `=`)
* Punctuation (`;`, `(`)

But also we want to **label** each part with a **name**, so when it matches something, we know **what kind of token** it is.

---

## ✅ The Format: `(?P<name>pattern)`

This is called a **named capturing group** in Python’s regular expressions.

### 🔹 General form:

```python
(?P<NAME>REGEX_PATTERN)
```

* `?P<NAME>`: Assigns a **name** to this pattern
* `REGEX_PATTERN`: The regex pattern to match

---

### 🔧 Example 1: Matching an identifier

```python
pattern = r'(?P<ID>[a-zA-Z_][a-zA-Z_0-9]*)'
```

This matches:

* `x`
* `my_var1`
* `Print`

And it **names** the match as `ID`.

So if you write:

```python
import re

regex = r'(?P<ID>[a-zA-Z_][a-zA-Z_0-9]*)'
match = re.match(regex, 'hello123')

print(match.group())          # hello123
print(match.lastgroup)        # ID
```

✅ Output:

```
hello123
ID
```

Now you know both:

* The **value** matched: `'hello123'`
* The **type** of token: `'ID'`

---

## 🔁 Back to `f'(?P<{name}>{pattern})'`

In our code, we want to dynamically create this string for **many different token types**, not just one.

Here’s the full line from our lexer again:

```python
token_re = '|'.join(f'(?P<{name}>{pattern})' for name, pattern in token_spec)
```

Let’s see what this does step-by-step.

### 🔹 Suppose `token_spec` contains:

```python
[
  ('NUMBER', r'\d+'),
  ('ID', r'[a-zA-Z_][a-zA-Z_0-9]*'),
  ('PLUS', r'\+')
]
```

The `f-string`:

```python
f'(?P<{name}>{pattern})'
```

becomes:

```python
'(?P<NUMBER>\\d+)'        # for name='NUMBER', pattern='\\d+'
'(?P<ID>[a-zA-Z_][a-zA-Z_0-9]*)'
'(?P<PLUS>\\+)'
```

So the `token_re` string becomes:

```regex
(?P<NUMBER>\d+)|(?P<ID>[a-zA-Z_][a-zA-Z_0-9]*)|(?P<PLUS>\+)
```

This is a single **combined regex** that matches:

* Digits
* Identifiers
* Plus signs

And labels each match with a name like `NUMBER`, `ID`, or `PLUS`.

---

## 🔍 Why We Use `(?P<NAME>...)` Instead of Just `(...)`?

With unnamed groups, you'd just get the value (like `10`), but **not the type**.

But we want both:

* The value (`10`)
* And what kind of token it is (`NUMBER`)

That's what `(?P<name>...)` gives us.

---

## ✅ How It Helps in Code

Inside our tokenizer:

```python
for mo in re.finditer(token_re, code):
    kind = mo.lastgroup   # gets the name from (?P<NAME>...)
    value = mo.group()    # gets the matched text
```

So you get output like:

```
('NUMBER', '10')
('PLUS', '+')
('NUMBER', '20')
```

Which is exactly what we need for the parser!

---

## ✅ Summary

| Syntax                     | Meaning                                                 |                                                         |
| -------------------------- | ------------------------------------------------------- | ------------------------------------------------------- |
| `(?P<NAME>...)`            | A **named group** in regex — stores what kind of match  |                                                         |
| `f'(?P<{name}>{pattern})'` | Builds this named group dynamically for each token type |                                                         |
| \`token\_re = '            | '.join(...)\`                                           | Joins all patterns into one big regex with named groups |
| `mo.lastgroup`             | Tells you **which token type matched**                  |                                                         |
| `mo.group()`               | Tells you **what actual text matched**                  |                                                         |

---

Would you like to:

* See how this all looks visually (diagram of how regex finds tokens)?
* Or move on to the **parser**, the next compiler step?
* Or want a small assignment to practice writing your own token rule?

Let me know — we’ll keep it smooth and exciting!






