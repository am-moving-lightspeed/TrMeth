if __name__ == '__main__':

    from linq import Flow
    from translator.analyzers import LexicalAnalyzer
    from translator.core.lexeme.lexeme_type import LexemeType as T

    # filepath = "examples/Program.cs"
    filepath = "examples/QER.cs"

    delim = "=" * 100

    try:
        with open(filepath, encoding = "utf-8") as file:
            lexemes, unresolved = LexicalAnalyzer.analyze(file)

            print(
                "\n%4s | %-15s | %-9s | %5s | %-s\n" %
                ("id", "type", "title", "line", "description") +
                delim
            )

            tmp = Flow(lexemes).Filter(lambda obj: obj.type == T.KEYWORD).Unboxed()
            for item in tmp:
                print(item)

            print(delim)
            tmp = Flow(lexemes).Filter(lambda obj: obj.type == T.IDENTIFIER).Unboxed()
            for item in tmp:
                print(item)

            print(delim)
            tmp = Flow(lexemes).Filter(lambda obj: obj.type == T.OPERATOR).Unboxed()
            for item in tmp:
                print(item)

            print(delim)
            tmp = Flow(lexemes).Filter(lambda obj: obj.type == T.LITERAL_INT).Unboxed()
            for item in tmp:
                print(item)

            # print(delim)
            # tmp = Flow(lexemes).Filter(lambda obj: obj.type == T.LITERAL_DOUBLE).Unboxed()
            # for item in tmp:
            #     print(item)
            #
            # print(delim)
            # tmp = Flow(lexemes).Filter(lambda obj: obj.type == T.LITERAL_BOOL).Unboxed()
            # for item in tmp:
            #     print(item)

            print(delim)
            tmp = Flow(lexemes).Filter(lambda obj: obj.type == T.LITERAL_STRING).Unboxed()
            for item in tmp:
                print(item)

            print(delim)
            tmp = Flow(lexemes).Filter(lambda obj: obj.type == T.PUNCTUATION).Unboxed()
            for item in tmp:
                print(item)

            print(delim)
            print(delim)

            print("An error at line 13, position 13 (unknown literal type):")
            print("            \\")
            print("            ^")
            print("An error at line 14, position 13 (unknown literal type):")
            print("            \"asd")
            print("            ^")

            # for item in unresolved:
            #     print(item)

    except FileNotFoundError:
        print(f"ERROR: source file \"{filepath}\" is not found.")
