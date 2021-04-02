from translator.core.lexeme import *
from translator.core.keyword import *


KEYWORD_DESC_DICT = dict.fromkeys(DECLARATIONS, r"Declaration keyword.")
KEYWORD_DESC_DICT.update(dict.fromkeys(MODIFIERS, r"Modifier keyword."))
KEYWORD_DESC_DICT.update(dict.fromkeys(TYPES, r"Type keyword."))
KEYWORD_DESC_DICT.update(dict.fromkeys(LOOPS, r"Loop keyword."))
KEYWORD_DESC_DICT.update(dict.fromkeys(CONDITIONS, r"Condition keyword."))

OPERATOR_DESC = r"Operator."

PUNCTUATION_DESC_DICT = {
    SEMICOLON: r"Represents an end of an instruction.",
    COMMA: r"Used for enumeration of parameters, arguments, variables, etc.",
    PARENTHESIS_START: r"Represents a start of a group.",
    PARENTHESIS_END: r"Represents an end of a group.",
    BRACE_START: r"Represents a start of a block.",
    BRACE_END: r"Represents an end of a block.",
    BRACKET_START: r"Used in pair with ] to hold indexes, attributes.",
    BRACKET_END: r"Used in pair with [ to hold indexes, attributes."
}

LITERAL_DESC_DICT = {
    INT: r"Represents an integer value.",
    DOUBLE: r"Represents a double precision value.",
    BOOL: r"Represents a logical value.",
    STRING: r"Represents a string."
}

IDENTIFIER_DESC_DICT = {
    'UNRESOLVED': "Unresolved identifier.",
    'USER_DEFINED': "Identifier defined by user."
}
