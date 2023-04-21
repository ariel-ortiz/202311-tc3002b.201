from delta import Compiler, Phase

source = '''
    var x, y;
    x = false;
    y = 5;
    if !x {
        y = y * 2;
    } else {
        y = y + 1;
    }
    y
'''

c = Compiler('program_start')
c.realize(source, Phase.EVALUATION)
# print(c.parse_tree_str)
# print()
# print(c.symbol_table)
# print()
print(c.wat_code)
print()
print(c.result)
