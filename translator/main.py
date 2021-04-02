if __name__ == '__main__':

    from translator.lexical_analyzer import LexicalAnalyzer

    # filepath = "examples/Program.cs"
    filepath = "examples/QER.cs"

    try:
        with open(filepath, mode = "r", encoding = "utf-8") as file:
            lexemes, unresolved = LexicalAnalyzer.analyze(file)

            for item in lexemes:
                print(item)

            print("==================================================", end = "")
            print("==================================================")

            for item in unresolved:
                print(item)

    except FileNotFoundError:
        print(f"ERROR: source file \"{filepath}\" is not found.")
