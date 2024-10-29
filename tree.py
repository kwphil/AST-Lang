from lark import Transformer, Tree
from grammar import grammar
from lark import Lark

class CalculateTree(Transformer):
    def tokens(self, args):
        enum_declaration = "enum T{"
        for item in args:
            if isinstance(item, Tree) and item.data == 'line':
                for identifier_item in item.children:
                    if isinstance(identifier_item, Tree) and identifier_item.data == 'identifier_line':
                        for identifier in identifier_item.children:
                            enum_declaration += f"{identifier[1:]}(String),"

        enum_declaration += "}"
        return enum_declaration

    def type(self, args):
        identifier = args[0]
        print(f"Handling !TYPE directive with identifier: {identifier}")
        self.handle_nested(args[1:])
        return f"Type directive executed with identifier {identifier}"

    def method(self, args):
        identifier = args[0]
        print(f"Handling !METHOD directive with identifier: {identifier}")
        self.handle_nested(args[1:])
        return f"Method directive executed with identifier {identifier}"

    def function(self, args):
        identifier = args[0]
        print(f"Handling !FUNCTION directive with identifier: {identifier}")
        self.handle_nested(args[1:])
        return f"Function directive executed with identifier {identifier}"

    def handle_nested(self, args):
        nested = [arg for arg in args if isinstance(arg, list)]
        if nested:
            for line in nested[0]:
                print(f"Nested code: {line}")

    def line(self, args):
        return args[0] if args else ""

parser = Lark(grammar, parser="lalr", transformer=CalculateTree())
