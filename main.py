from trunfo import Trunfo
from pprint import pprint

if __name__ == "__main__":
    res = Trunfo.compare_cards()

    """
        Deve printar algo parecido com isso:
        {'draw': 1, 'player_1': 3, 'player_2': 4}
    """
    pprint(res)
