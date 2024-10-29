from tree import parser


print(parser.parse("!TOKENS\n|-identifier\n|-hello"))
print(parser.parse("!FUNCTION .main\n| # code here ...\n| .exit 0")) 
print(parser.parse("!TYPE -identifier\n| !METHOD :new \n|\n| #setup code\n|!rust let x = 0\n|<!rust x = x + 1\nprintln!(\"Hello, World!\")\n>"))
