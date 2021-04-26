class LiteralRegex:
    #
    INT_LITERAL_RE = r"\d+"
    DOUBLE_LITERAL_RE = r"\d+\.?\d+((e|E){1}(\+|-)?\d+)?"
    BOOL_LITERAL_RE = r"(true|false)"
    STRING_LITERAL_RE = r"^(\"|'){1}.*(\"|'){1}$"


class IdentifierRegex:
    #
    IDENTIFIER = r"\b[A-Za-z_]\w*\b"
