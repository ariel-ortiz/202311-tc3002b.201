import re


def main():
    with open('entrada.txt') as archivo:
        entrada = archivo.read()
    c = re.compile(r"(?:\w+)(?:\'\w*)?")
    result = c.findall(entrada)
    print(result)


if __name__ == '__main__':
    main()
