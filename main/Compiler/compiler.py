import sys
from antlr4 import FileStream, CommonTokenStream
from antlr4.tree.Tree import TerminalNodeImpl
from antlr4.tree.Trees import Trees

from out.SlangLexer import SlangLexer
from out.SlangParser import SlangParser
from out.SlangVisitor import SlangVisitor

from abstractTree import getProg
from transformAST import flattenBlock, optimizeBlock
#from gba import GBAconverter
from gba import buildMain

if len(sys.argv)!=3:
    print("usage: python3 compiler.py <InPath> <OutPath>")
    exit(1)
INFILE = sys.argv[1]
OUTFILE = sys.argv[2]


def main():


    print("\n------ Code ------")
    print(open(INFILE,"r").read())
    # get concrete tree for prog


    print("\n------ Parser ------")
    input_stream = FileStream(INFILE, encoding="UTF-8")
    lexer = SlangLexer(input_stream)
    tokenStream = CommonTokenStream(lexer)
    parser = SlangParser(tokenStream)
    progContext = parser.prog()
    #dump(progContext, ruleNames=parser.ruleNames)
    print(progContext.toStringTree(recog=parser).replace('\\n', '\n'))
    

    # create abstract tree with own classes
    print("\n------ Abstract Tree ------")
    mainBlock = getProg(progContext)
    print(mainBlock)

    print("\n------ Flatten ------")
    mainBlock = flattenBlock(mainBlock)
    print(mainBlock)

    # this does nothing right now
    #print("\n------ Optimize AST ------")
    #mainBlock = optimizeBlock(mainBlock)
    #print(mainBlock)

    print("\n------ Assembly ------")
    asmText = buildMain(mainBlock)
    print("-"*20)
    #print(asmText)

    with open(OUTFILE, "w", encoding="UTF-8") as oFile:
        oFile.write(asmText)
    

# https://stackoverflow.com/a/76281011
def dump(node, depth=0, ruleNames=None):
    depthStr = '| ' * depth
    if isinstance(node, TerminalNodeImpl):
        print(f'{depthStr}{node}') #{node.symbol} for more details
        pass
    else:
        print(f'{depthStr}[{Trees.getNodeText(node, ruleNames)}]')
        for child in node.children:
            dump(child, depth + 1, ruleNames)

if __name__ == '__main__':
    main()