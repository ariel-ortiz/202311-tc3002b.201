import re
from enum import Enum


class TokenType(Enum):
    IDENTIFIER = 1
    INTEGER = 2
    FLOAT = 3
    SYMBOL = 4


compiled_re = re.compile(
    r'''
      (?P<identifier> [a-zA-Z]\w* )
    | (?P<float>      \d+[.]\d+   )
    | (?P<integer>    \d+         )
    | (?P<symbol>     [.,;()!?]   )
    | (?P<space>      \s          )
    | (?P<other>      .           ) # hace match con lo que sea,
                                    # debe ir al final
    ''', re.ASCII | re.VERBOSE)


def main():
    texto = '''
        uno;
        dos;
        tres;
        1234?
        12.34;
        (67);
    '''
    result = []
    for m in compiled_re.finditer(texto):
        if m['identifier']:
            result.append((TokenType.IDENTIFIER, m.group(), m.span()))
        elif m['float']:
            result.append((TokenType.FLOAT, m.group(), m.span()))
        elif m['integer']:
            result.append((TokenType.INTEGER, m.group(), m.span()))
        elif m['symbol']:
            result.append((TokenType.SYMBOL, m.group(), m.span()))
    print(result)


if __name__ == '__main__':
    main()
