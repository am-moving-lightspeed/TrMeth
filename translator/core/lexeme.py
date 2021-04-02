import enum


class Lexeme:
    #
    def __init__(self, id_: int, type_: 'LexemeType', title: str, line: int, desc: str):
        self.id = id_
        self.type = type_
        self.title = title
        self.line = line
        self.desc = desc


    def __str__(self) -> str:
        return (
          "%4d | %-15s | %-9s | %5d | %s" %
          (self.id, self.type, self.title, self.line, self.desc)
        )


class LexemeType(enum.Enum):
    #
    INVALID = -1
    KEYWORD = 0
    PUNCTUATION = 1
    OPERATOR = 100
    LITERAL_INT = 200
    LITERAL_DOUBLE = 201
    LITERAL_BOOL = 202
    LITERAL_STRING = 203
    IDENTIFIER = 300


    def __str__(self):
        return self.name


# ==================================================

SPACE_CHARACTER = r" "

# Skippable
NEW_LINE_CHARACTER = r"\n"
NULL_CHARACTER = r""

# Punctuation
SEMICOLON = r";"
COMMA = r","
PARENTHESIS_START = r"("
PARENTHESIS_END = r")"
BRACE_START = r"{"
BRACE_END = r"}"
BRACKET_START = r"["
BRACKET_END = r"]"
DQUOTE = r'"'

# Operator
DOT = r"."
ADD = r"+"
SUB = r"-"
MUL = r"*"
DIV = r"/"
MOD = r"%"
ASSIGN = r"="
EQUAL = r"=="
UNEQUAL = r"!="
GREATER = r">"
LOWER = r"<"

# ==================================================

# Skippable set
SKIPPABLES = {
    NEW_LINE_CHARACTER, NULL_CHARACTER
}

# Punctuation set
PUNCTUATION = {
    SEMICOLON,
    COMMA,
    PARENTHESIS_START,
    PARENTHESIS_END,
    BRACE_START,
    BRACE_END,
    BRACKET_START,
    BRACKET_END
    # DQUOTE -- is resolved with string literal
}

# Operators set
OPERATORS = {
    DOT, ADD, SUB, MUL, DIV, MOD, ASSIGN, EQUAL, UNEQUAL, GREATER, LOWER
}
