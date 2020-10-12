import csv

def loadCards(fileName):
    with open(fileName) as f:
        reader = csv.reader(f, delimiter=",")
        cols = next(reader)
        cards = []
        for line in reader:
            cards.append(dict(zip(cols, line)))
    return cards
