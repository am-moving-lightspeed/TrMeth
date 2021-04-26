from typing import List
from typing import Optional
from typing import Tuple

from anytree import Node

from translator.core.lexeme import *
from translator.core.operators_priorities import Priority


class SyntaxAnalyzer:
    #
    EMPTY_TITLE = '$'
    ROOT_TITLE = '$ROOT'
    START_BLOCK_TITLE = '$BLOCK'
    END_BLOCK_TITLE = '$ENDBLOCK'

    _AST_root: Node

    _lexemes_read_by_instruction_parser: int = 0
    _instruction_left_parenthesis_count: int = 0
    _instruction_right_parenthesis_count: int = 0
    _instruction_left_brace_count: int = 0
    _instruction_right_brace_count: int = 0

    _priority_manager: Priority


    @classmethod
    def analyze(cls, stream: List[Lexeme], offset: int = 0) -> Node:
        #
        cls._analyzer_clean_up()
        head = cls._AST_root

        while offset < len(stream):
            node, parsed_lexemes_count = cls._parse_instruction(stream, offset)
            offset += parsed_lexemes_count

            if offset < len(stream) and stream[offset] == BRACE_LEFT_LEXEME:
                cls._instruction_left_brace_count += 1
                offset += 1
                head = Node(cls.START_BLOCK_TITLE, parent = head)

            if node.name != cls.EMPTY_TITLE:
                node.parent = head

            if offset < len(stream) and stream[offset] == BRACE_RIGHT_LEXEME:
                cls._instruction_right_brace_count += 1
                offset += 1
                Node(cls.END_BLOCK_TITLE, parent = head)
                head = head.parent

        return cls._AST_root


    @classmethod
    def _parse_instruction(cls, stream: List[Lexeme], offset: int) -> Tuple[Node, int]:
        #
        cls._instruction_parser_clean_up()

        if stream[offset] == SEMICOLON_LEXEME:
            return Node(cls.EMPTY_TITLE), cls._lexemes_read_by_instruction_parser

        cls._priority_manager = Priority()

        tree = cls._parse_lexemes_recursively(stream, offset)

        if tree is None:
            return Node(cls.EMPTY_TITLE), cls._lexemes_read_by_instruction_parser

        while tree.parent is not None:
            tree = tree.parent

        return tree, cls._lexemes_read_by_instruction_parser


    @classmethod
    def _parse_lexemes_recursively(cls,
                                   stream: List[Lexeme],
                                   offset: int,
                                   parent_node: Optional[Node] = None) -> Optional[Node]:
        #
        if (
          stream[offset] == BRACE_LEFT_LEXEME or
          stream[offset] == BRACE_RIGHT_LEXEME
        ):
            return
        else:
            cls._lexemes_read_by_instruction_parser += 1

        if stream[offset] == SEMICOLON_LEXEME:
            return

        current_node: Optional[Node] = None
        parent_node_lexeme: Optional[Lexeme] = None

        if parent_node is not None:
            parent_node_lexeme = getattr(parent_node, 'lexeme')

        if stream[offset] == PARENTHESIS_LEFT_LEXEME:
            cls._instruction_left_parenthesis_count += 1

            if (
              parent_node_lexeme is not None and
              parent_node_lexeme.type == LexemeType.IDENTIFIER
            ):
                current_node = cls._parse_lexeme_to_node(CALL_LEXEME)
                cls._priority_manager.increase_priority()
            else:
                cls._priority_manager.increase_priority()
                cls._parse_lexemes_recursively(stream, offset + 1, parent_node)
                return

        elif stream[offset] == PARENTHESIS_RIGHT_LEXEME:
            cls._priority_manager.decrease_priority()
            cls._instruction_right_parenthesis_count += 1

            cls._parse_lexemes_recursively(stream, offset + 1, parent_node)
            return

        else:
            current_node = cls._parse_lexeme_to_node(stream[offset])

        #
        cls._set_right_child(parent_node, current_node)

        if (
          parent_node_lexeme is not None and
          (current_node.lexeme.type == LexemeType.OPERATOR or
           current_node.lexeme.type == LexemeType.KEYWORD) and
          parent_node_lexeme.type != LexemeType.OPERATOR
        ):
            current_node = cls._left_rotate_subtree(parent_node)

        cls._parse_lexemes_recursively(stream, offset + 1, current_node)

        return cls._resolve_order_by_priority(current_node)


    @classmethod
    def _resolve_order_by_priority(cls, subtree: Node) -> Node:
        #
        subtree_lexeme: Lexeme = getattr(subtree, 'lexeme')
        if (
          subtree_lexeme.type == LexemeType.OPERATOR or
          subtree_lexeme.type == LexemeType.KEYWORD
        ):

            right_child: Node = subtree.children[1]  # right child of the subtree.
            if right_child.name != cls.EMPTY_TITLE:

                right_child_lexeme: Lexeme = getattr(right_child, 'lexeme')
                if (
                  right_child_lexeme.type == LexemeType.OPERATOR or
                  right_child_lexeme.type == LexemeType.KEYWORD
                ):

                    subtree_priority = getattr(subtree, 'priority')
                    right_child_priority = getattr(right_child, 'priority')

                    if subtree_priority >= right_child_priority:
                        ret = cls._left_rotate_subtree(subtree)
                        # Check for left child of returned result-tree. Necessary once.
                        cls._resolve_order_by_priority(subtree)

                        return ret

        return subtree


    @classmethod
    def _set_right_child(cls, parent_node: Node, right_child_node: Node) -> None:
        #
        if parent_node is not None:
            if len(parent_node.children) == 0:
                parent_node.children = [Node(cls.EMPTY_TITLE), right_child_node]
            else:
                left_child_node: Node = parent_node.children[0]
                parent_node.children = [left_child_node, right_child_node]


    @classmethod
    def _left_rotate_subtree(cls, subtree_root: Node) -> Node:
        #
        right_child: Node = subtree_root.children[1]

        if right_child.name != cls.EMPTY_TITLE:
            subtree_parent: Node = subtree_root.parent

            if subtree_parent is not None:
                if subtree_root.path == subtree_parent.children[0].path:
                    subtree_parent.children = [right_child, subtree_parent.children[1]]
                else:
                    subtree_parent.children = [subtree_parent.children[0], right_child]
            else:
                right_child.parent = subtree_root.parent  # root->right.parent = root.parent

            right_child.children[0].parent = subtree_root  # root->right = root->right->left
            # root->right->left = root
            # root->right->right = root->right->right
            right_child.children = [subtree_root, right_child.children[0]]

            return right_child
        else:
            return subtree_root


    @classmethod
    def _parse_lexeme_to_node(cls, lexeme_: Lexeme) -> Node:
        #
        node = Node(lexeme_.title)
        node.lexeme = lexeme_
        node.children = [Node(cls.EMPTY_TITLE), Node(cls.EMPTY_TITLE)]

        if lexeme_.type == LexemeType.OPERATOR:
            node.priority = cls._priority_manager[node.name]
        elif lexeme_.type == LexemeType.KEYWORD:
            node.priority = cls._priority_manager['KEYWORD']

        return node


    @classmethod
    def _analyzer_clean_up(cls) -> None:
        #
        cls._AST_root = Node(cls.ROOT_TITLE)
        cls._instruction_left_brace_count = 0
        cls._instruction_right_brace_count = 0


    @classmethod
    def _instruction_parser_clean_up(cls) -> None:
        #
        cls._lexemes_read_by_instruction_parser = 0
        cls._instruction_left_parenthesis_count = 0
        cls._instruction_right_parenthesis_count = 0
