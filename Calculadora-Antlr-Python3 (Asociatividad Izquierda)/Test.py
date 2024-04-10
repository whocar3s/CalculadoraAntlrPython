import sys
from antlr4 import *
from antlr4.InputStream import InputStream
from SenCosTanLexer import SenCosTanLexer
from SenCosTanParser import SenCosTanParser
from SenCosTanVisitorTest import SenCosTanVisitorTest

if __name__ == '__main__':
    if len(sys.argv) > 1:
        input_stream = FileStream(sys.argv[1])
    else:
        input_stream = InputStream(sys.stdin.readline())

    lexer = SenCosTanLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = SenCosTanParser(token_stream)
    tree = parser.prog()

    #lisp_tree_str = tree.toStringTree(recog=parser)
    #print(lisp_tree_str)

    visitor = SenCosTanVisitorTest()
    visitor.visit(tree)
