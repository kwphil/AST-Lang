grammar = """
    start: directive

    directive: "!TOKENS" identifier_line?        -> tokens
             | "!TYPE" IDENTIFIER nested_code?   -> type
             | "!METHOD" METHOD nested_code?     -> method
             | "!FUNCTION" FUNCTION nested_code? -> function

    nested_code: ("|" line)+

    identifier_line: ("|" IDENTIFIER)+

    line: COMMENT
        | statement
        | nested_code
        | directive

    statement: FUNCTION
             | METHOD
             | INLINE_CODE

    IDENTIFIER: "-" TEXT
    COMMENT: /#.*/
    FUNCTION: /\\..+/
    METHOD: /:.+/
    TEXT: /[a-zA-Z_][a-zA-Z0-9_]+/
    INLINE_CODE: SINGLELINE_CODE
               | MULTILINE_CODE

    SINGLELINE_CODE: "!rust" /.+/
    MULTILINE_CODE: "<!rust" /[\\s\\S]*?/ ">"

    %import common.WS
    %ignore WS
"""
