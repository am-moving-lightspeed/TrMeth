import enum


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


    def __eq__(self, other: 'LexemeType') -> bool:
        return True if self.name == other.name else False


    def __str__(self) -> str:
        return self.name
