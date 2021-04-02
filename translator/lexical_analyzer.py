import re as regex
from typing import List
from typing import TextIO
from typing import Tuple

from translator.core.lexeme import *
from translator.core.lexeme import LexemeType as Type
from translator.core.keyword import *
from translator.core.desc import OPERATOR_DESC
from translator.core.desc import PUNCTUATION_DESC_DICT as PDD
from translator.core.desc import KEYWORD_DESC_DICT as KDD
from translator.core.desc import LITERAL_DESC_DICT as LDD
from translator.core.desc import IDENTIFIER_DESC_DICT as IDD
from translator.templates.regex import LiteralRegex as Lr
from translator.templates.regex import IdentifierRegex as Ir


class LexicalAnalyzer:
    #
    _lexemes: List[Lexeme] = []
    _unresolved_sequences: List[Lexeme] = []
    _current_line: int = 0


    @classmethod
    def analyze(cls, file: TextIO) -> Tuple[List[Lexeme], List[Lexeme]]:
        #
        if len(cls._lexemes) != 0:
            cls._lexemes = []

        try:
            for line in file:
                cls._current_line += 1
                cls._resolve_line(line)

            return cls._lexemes, cls._unresolved_sequences

        except IOError:
            return [], []

        finally:
            file.close()


    @classmethod
    def _resolve_line(cls, plain_text: str) -> None:
        #
        tokens: List[str] = (
            regex.split(r"([^\w.])", plain_text.replace("\t", " ").strip())
        )

        tokens = cls._remove_skippables(tokens)
        tokens = cls._preprocess_special_cases(tokens)

        for token in tokens:
            if token != SPACE_CHARACTER:
                cls._resolve_token(token)


    @classmethod
    def _resolve_token(cls, token: str) -> None:
        #
        if (
          token in DECLARATIONS or
          token in MODIFIERS or
          token in TYPES or
          token in LOOPS or
          token in CONDITIONS
        ):
            cls._add_lexeme(token, Type.KEYWORD, KDD[token])
        elif token in OPERATORS:
            cls._add_lexeme(token, Type.OPERATOR, OPERATOR_DESC)
        elif token in PUNCTUATION:
            cls._add_lexeme(token, Type.PUNCTUATION, PDD[token])
        elif cls._try_resolve_literal(token):
            pass
        else:
            identifiers: List[str] = regex.split(r"(\b[A-Za-z_]\w*\b)", token)
            identifiers = cls._remove_skippables(identifiers)

            for id_ in identifiers:
                if id_ in TYPES:
                    cls._add_lexeme(id_, Type.KEYWORD, KDD[id_])
                elif cls._try_resolve_identifier(id_):
                    pass
                else:
                    cls._unresolved_sequences.append(
                        Lexeme(-1, Type.INVALID, id_, cls._current_line, IDD['UNRESOLVED'])
                    )


    @classmethod
    def _try_resolve_literal(cls, token: str) -> bool:
        #
        success = True

        if regex.fullmatch(Lr.STRING_LITERAL_RE, token):
            cls._add_lexeme(token, Type.LITERAL_STRING, LDD[STRING])
        elif regex.fullmatch(Lr.BOOL_LITERAL_RE, token):
            cls._add_lexeme(token, Type.LITERAL_BOOL, LDD[BOOL])
        elif regex.fullmatch(Lr.INT_LITERAL_RE, token):
            cls._add_lexeme(token, Type.LITERAL_INT, LDD[INT])
        elif regex.fullmatch(Lr.DOUBLE_LITERAL_RE, token):
            cls._add_lexeme(token, Type.LITERAL_DOUBLE, LDD[DOUBLE])
        else:
            success = False

        return success


    @classmethod
    def _try_resolve_identifier(cls, token: str) -> bool:
        #
        success = True

        if token == DOT:
            cls._add_lexeme(token, Type.OPERATOR, OPERATOR_DESC)
        elif regex.fullmatch(Ir.IDENTIFIER, token):
            cls._add_lexeme(token, Type.IDENTIFIER, IDD['USER_DEFINED'])
        else:
            success = False

        return success


    @classmethod
    def _remove_skippables(cls, tokens: List[str]) -> List[str]:
        out = []

        for i in range(len(tokens)):
            if tokens[i] not in SKIPPABLES:
                out.append(tokens[i])

        return out


    @classmethod
    def _preprocess_special_cases(cls, tokens: List[str]) -> List[str]:
        #
        out = []

        i = 0
        size = len(tokens)
        while i < size:
            # Case when a double is represented as 1.95e+05, or 2.10E-03, or etc.
            if tokens[i] == ADD or tokens[i] == SUB:
                i = cls._check_if_double_and_compose(tokens, out, i)

            # Case when string literal encountered.
            elif tokens[i] == DQUOTE:
                i = cls._check_if_string_and_compose(tokens, out, i)

            # Case when != or == encountered.
            elif tokens[i] == ASSIGN:
                i = cls._check_if_assignment_operator_and_compose(tokens, out, i)

            # Regular.
            else:
                out.append(tokens[i])

            i += 1

        return out


    @classmethod
    def _add_lexeme(cls, lexeme: str, type_: LexemeType, desc: str) -> None:
        #
        cls._lexemes.append(
            Lexeme(
                len(cls._lexemes),
                type_,
                lexeme,
                cls._current_line,
                desc
            )
        )


    @staticmethod
    def _check_if_string_and_compose(src: List[str], dest: List[str], offset: int) -> int:
        #
        tmp = [src[offset]]
        offset += 1

        while offset < len(src):
            tmp.append(src[offset])

            if src[offset] == "\"":
                break

            if (
              src[offset] == "\\" and
              offset != len(src) - 1 and
              src[offset + 1] == "\""
            ):
                tmp.append(src[offset])
                tmp.append(src[offset + 1])
                offset += 1

            offset += 1

        dest.append("".join(tmp))

        return offset


    @staticmethod
    def _check_if_double_and_compose(src: List[str], dest: List[str], offset: int) -> int:
        #
        if offset - 1 >= 0 and offset + 1 < len(src):
            tmp: str = src[offset - 1] + src[offset] + src[offset + 1]

            if regex.fullmatch(Lr.DOUBLE_LITERAL_RE, tmp):
                dest.pop(len(dest) - 1)
                dest.append(tmp)
                offset += 1
            else:
                dest.append(src[offset])

        return offset


    @staticmethod
    def _check_if_assignment_operator_and_compose(src: List[str],
                                                  dest: List[str],
                                                  offset: int) -> int:
        #
        if offset - 1 >= 0:
            tmp: str = src[offset - 1] + src[offset]

            if tmp == EQUAL or tmp == UNEQUAL:
                dest.pop(len(dest) - 1)
                dest.append(tmp)
            else:
                dest.append(src[offset])

        return offset
