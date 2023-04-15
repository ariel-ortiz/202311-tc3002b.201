from delta import Compiler, Phase

source = '''
    /* commentario 1 */
    1
    +
    // comentario 2
    1
    /* comentario
       3
    */
'''

c = Compiler('expression_start')
c.realize(source, Phase.EVALUATION)
print(c.parse_tree_str)
print()
print(c.wat_code)
print()
print(c.result)
