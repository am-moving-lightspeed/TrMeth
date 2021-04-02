if __name__ == '__main__':

    from translator.lexical_analyzer import LexicalAnalyzer
    from translator.templates.regex import DeclarationRegex as A

    # TODO: allow to enter filename
    filepath = "examples/Program.cs"

    # print(str(A.METHOD))

    try:
        with open(filepath, mode = "r", encoding = "utf-8") as file:
            a = LexicalAnalyzer.analyze(file)
            for i in a:
                print(i)

    except FileNotFoundError:
        print(f"ERROR: source file \"{filepath}\" is not found.")
