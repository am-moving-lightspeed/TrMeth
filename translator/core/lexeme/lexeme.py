from translator.core.dictionary import *
from .lexeme_type import LexemeType


__all__ = [
  'Lexeme',
  'SEMICOLON_LEXEME',
  'PARENTHESIS_LEFT_LEXEME',
  'PARENTHESIS_RIGHT_LEXEME',
  'CALL_LEXEME'
]


class Lexeme:
    #
    def __init__(self, id_: int = -1,
                 type_: 'LexemeType' = LexemeType.INVALID,
                 title: str = "",
                 line: int = -1,
                 desc: str = ""):
        #
        self.id = id_
        self.type = type_
        self.title = title
        self.line = line
        self.desc = desc


    def __eq__(self, other: 'Lexeme') -> bool:
        #
        return True if self.title == other.title and self.type == other.type else False


    def __str__(self) -> str:
        #
        return (
          "%4d | %-15s | %-9s | %5d | %s" %
          (self.id, self.type, self.title, self.line, self.desc)
        )


# Punctuation
SEMICOLON_LEXEME = Lexeme(type_ = LexemeType.PUNCTUATION,
                          title = SEMICOLON)

PARENTHESIS_LEFT_LEXEME = Lexeme(type_ = LexemeType.PUNCTUATION,
                                 title = PARENTHESIS_LEFT)

PARENTHESIS_RIGHT_LEXEME = Lexeme(type_ = LexemeType.PUNCTUATION,
                                  title = PARENTHESIS_RIGHT)

BRACE_LEFT_LEXEME = Lexeme(type_ = LexemeType.PUNCTUATION,
                           title = BRACE_LEFT)

BRACE_RIGHT_LEXEME = Lexeme(type_ = LexemeType.PUNCTUATION,
                            title = BRACE_RIGHT)

# Operators
CALL_LEXEME = Lexeme(type_ = LexemeType.OPERATOR,
                            title = CALL)
