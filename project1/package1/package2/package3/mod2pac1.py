from .mod1pac1 import hello


def good_word(name):
    hello(name)
    print(f'Ты лучший {name}!')


if __name__ == '__main__':
    good_word('Урбан')
