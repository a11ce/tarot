import random
import sys

import tarot

def main():
    cards = tarot.loadCards("cards/cards.csv")
    if len(sys.argv) > 1:
        for _ in range(int(sys.argv[1])):
            print(asLine(random.choice(cards)))
    else:
        print(asLine(random.choice(cards)))
        
def asLine(card):
    formCard = [val + (" " * (colLen-len(val))) for val, colLen in zip(card.values(), [21, 21, 10, 18, 10, 10, 0])]
    return "".join(list(formCard))
    
if __name__ == "__main__":
    main()