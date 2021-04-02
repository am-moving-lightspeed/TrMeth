class BasicRegex:
    #
    ANY_ACCESS_MODIFIER = r"(protected\s+internal|" \
                          r"internal\s+protected|" \
                          r"private\s+protected|" \
                          r"protected\s+private|" \
                          r"public|protected|private|internal)"

    CLASS_ACCESS_MODIFIER = r"(public|internal)"

    ANY_TYPE = r"(void|string|bool|int|double)"
    ANY_NONVOID_TYPE = r"(string|bool|int|double)"

    USING_STATEMENT = r"using\s+\w+(\.[\s\t]*\w+)*"


BR = BasicRegex


class LiteralRegex:
    #
    INT_LITERAL_RE = r"\d+"
    DOUBLE_LITERAL_RE = r"\d+\.?\d+((e|E){1}(\+|-)?\d+)?"
    BOOL_LITERAL_RE = r"(true|false)"
    STRING_LITERAL_RE = r"^(\"|'){1}.*(\"|'){1}$"


class DeclarationRegex:
    #
    CLASS = (
        rf"(\b{BR.CLASS_ACCESS_MODIFIER}\s+)?"
        rf"(\bstatic\s+)?"
        rf"\bclass\s+\w+(\s*{{\s*}}?)?"
    )

    METHOD = (
        rf"(\b{BR.ANY_ACCESS_MODIFIER}\s+)?"
        rf"(\bstatic\s+)?"
        rf"\b{BR.ANY_TYPE}{{1}}\s+\w+\s*"
        rf"\(\s*"
        rf"({BR.ANY_NONVOID_TYPE}{{1}}(\s*\[\s*\])?(\s+\w+){{1}}\s*,?\s*)*"
        rf"\)"
        rf"(\s*{{\s*}}?)?"
    )


class IdentifierRegex:
    #
    IDENTIFIER = r"\b[A-Za-z_]\w*\b"
