from translator.core.dictionary import *


# Any operator description.
OPERATOR_DESC = r"Operator."

# For keywords.
KEYWORD_DESC_DICT = dict.fromkeys(DECLARATIONS, r"Declaration keyword.")
KEYWORD_DESC_DICT.update(dict.fromkeys(MODIFIERS, r"Modifier keyword."))
KEYWORD_DESC_DICT.update(dict.fromkeys(TYPES, r"Type keyword."))
KEYWORD_DESC_DICT.update(dict.fromkeys(LOOPS, r"Loop keyword."))
KEYWORD_DESC_DICT.update(dict.fromkeys(CONDITIONS, r"Condition keyword."))

# For punctuation symbols.
PUNCTUATION_DESC_DICT = {
  SEMICOLON: r"Represents an end of an instruction.",
  COMMA: r"Used for enumeration of parameters, arguments, variables, etc.",
  PARENTHESIS_LEFT: r"Represents a start of a group.",
  PARENTHESIS_RIGHT: r"Represents an end of a group.",
  BRACE_LEFT: r"Represents a start of a block.",
  BRACE_RIGHT: r"Represents an end of a block.",
  BRACKET_LEFT: r"Used in pair with ] to hold indexes, attributes.",
  BRACKET_RIGHT: r"Used in pair with [ to hold indexes, attributes."
}

# For literals.
LITERAL_DESC_DICT = {
  INT: r"Represents an integer value.",
  DOUBLE: r"Represents a double precision value.",
  BOOL: r"Represents a logical value.",
  STRING: r"Represents a string."
}

# For identifiers.
IDENTIFIER_DESC_DICT = {
  'UNRESOLVED': r"Unresolved symbols sequence.",
  'USER_DEFINED': r"Identifier defined by user."
}
