from .dictionary import *
from .lexeme_type import LexemeType


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


LEXEME_SEMICOLON = Lexeme(type_ = LexemeType.PUNCTUATION,
                          title = SEMICOLON)

LEXEME_BRACE_LEFT = Lexeme(type_ = LexemeType.PUNCTUATION,
                           title = BRACE_LEFT)

LEXEME_BRACE_RIGHT = Lexeme(type_ = LexemeType.PUNCTUATION,
                            title = BRACE_RIGHT)
