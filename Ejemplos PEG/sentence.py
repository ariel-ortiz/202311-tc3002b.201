from arpeggio import NoMatch
from arpeggio.cleanpeg import ParserPEG

peg = '''
    sentence  = adjective noun verb adjective noun EOF
    adjective = 'red' / 'peculiar' /  'jumping' / 'fat' / 'fuzzy'
    noun      = 'birds' / 'dogs' / 'worms' / 'donkeys' / 'geese' / 'cats'
    verb      = 'hate' / 'trip' / 'love' / 'bite'
'''

parser = ParserPEG(peg, 'sentence')
try:
    tree = parser.parse('fat cats love red worms')
    print(tree.tree_str())
except NoMatch as e:
    print(e)
