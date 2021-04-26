from anytree import RenderTree
from anytree import ContStyle

from translator.analyzers.lexical_analyzer import LexicalAnalyzer
from translator.analyzers.syntax_analyzer import SyntaxAnalyzer


if __name__ == '__main__':
    with open("../examples/test.cs", encoding = r'utf-8') as file:
        lexemes, _ = LexicalAnalyzer.analyze(file)
        tree = SyntaxAnalyzer.parse_instruction(lexemes, 0)
        for pre, _, node in RenderTree(tree, style = ContStyle()):
            print("%s%s" % (pre, node.name))
