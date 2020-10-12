import random
import sys

import tarot

def main():
    cards = tarot.loadCards("cards/cards.csv")
    if len(sys.argv) > 1:
        for _ in range(int(sys.argv[1])):
            print(tarot.asMonoLine(random.choice(cards)))
    else:
        print(tarot.asMonoLine(random.choice(cards)))
        
if __name__ == "__main__":
    main()