from delta import Compiler, Phase

source = '123'

c = Compiler('expression_start')
c.realize(source, Phase.EVALUATION)
print(c.parse_tree_str)
print()
print(c.wat_code)
print()
print(c.result)
