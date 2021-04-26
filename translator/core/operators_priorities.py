from .dictionary.operators import *


__all__ = [
  'Priority'
]


class Priority:
    """
    This class is used to resolve priorities of operators in syntax analysis.
    """

    _PRIORITIES_DICT = {
      # Arithmetic operators
      ASSIGN:    200,
      ADD:       1200,
      SUB:       1200,  # Same as ADD.
      MUL:       1300,
      DIV:       1301,  # A bit higher than MUL, executes before MUL.
      MOD:       1301,  # Same as DIV.

      # Comparison operators
      EQUAL:     900,
      UNEQUAL:   900,  # Same as EQUAL.
      GREATER:   1000,
      LOWER:     1000,  # Same as GREATER.

      # Access operators
      DOT:       1500,

      # Call or decl. operator ()
      CALL:      1500,

      COMMA:     100,

      # Keyword
      'KEYWORD': 50  # Same as ASSIGN.
    }

    # Only used to increase priority of the operator, if it is located between parentheses.
    _parenthesis_adjustment: int = 0


    def __getitem__(self, item: str) -> int:
        #
        try:
            return self._PRIORITIES_DICT[item] + self._parenthesis_adjustment
        except KeyError:
            return 0


    def increase_priority(self):
        #
        self._parenthesis_adjustment += 100_000


    def decrease_priority(self):
        #
        self._parenthesis_adjustment -= 100_000 if self._parenthesis_adjustment >= 100_000 else 0
