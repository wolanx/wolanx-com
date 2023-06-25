from antlr4 import *

from libraries.antlr.dist_Calculantlr.CalculantlrLexer import CalculantlrLexer
from libraries.antlr.dist_Calculantlr.CalculantlrParser import CalculantlrParser
from libraries.antlr.dist_Calculantlr.CalculantlrVisitor import CalculantlrVisitor
from libraries.antlr.dist_Hello.HelloLexer import HelloLexer
from libraries.antlr.dist_Hello.HelloParser import HelloParser
from libraries.antlr.dist_Hello.HelloVisitor import HelloVisitor


class MyHelloVisitor(HelloVisitor):
    def visitS(self, ctx: HelloParser.SContext):
        return ctx.ID()


class MyCalculantlrVisitor(CalculantlrVisitor):
    def visitAtomExpr(self, ctx: CalculantlrParser.AtomExprContext):
        return int(ctx.getText())

    def visitParenExpr(self, ctx: CalculantlrParser.ParenExprContext):
        return self.visit(ctx.expr())

    def visitOpExpr(self, ctx: CalculantlrParser.OpExprContext):
        a = self.visit(ctx.left)
        b = self.visit(ctx.right)

        op = ctx.op.text
        if op == "+":
            return a + b
        elif op == "-":
            return a - b
        elif op == "*":
            return a * b
        elif op == "/":
            if b == 0:
                print("divide by zero!")
                return 0
            return a / b


def doHello(line: str):
    input_stream = InputStream(line)

    # lexing
    lexer = HelloLexer(input_stream)
    stream = CommonTokenStream(lexer)

    # parsing
    parser = HelloParser(stream)
    tree = parser.s()

    # use customized visitor to traverse AST
    visitor = MyHelloVisitor()
    ret = visitor.visit(tree)
    print(line, "=", ret)


def doCalculantlr(line: str):
    input_stream = InputStream(line)

    # lexing
    lexer = CalculantlrLexer(input_stream)
    stream = CommonTokenStream(lexer)

    # parsing
    parser = CalculantlrParser(stream)
    tree = parser.expr()

    # use customized visitor to traverse AST
    visitor = MyCalculantlrVisitor()
    ret = visitor.visit(tree)
    print(line, "=", ret)


if __name__ == "__main__":
    doCalculantlr("33 * 2")
    doCalculantlr("32 / 8")
    doCalculantlr("1 + 2 * 2")
    doCalculantlr("3 / (3 + 3)")

    doHello("hello asd123")
