import csv


def main():
    pass


def loadCards(fileName):
    with open(fileName) as f:
        reader = csv.reader(f, delimiter=",")
        cols = next(reader)
        cards = []
        for line in reader:
            cards.append(dict(zip(cols, line)))
    return cards


def asMonoLine(card):
    formCard = [
        val + (" " * (colLen - len(val)))
        for val, colLen in zip(card.values(), [21, 21, 10, 18, 10, 10, 0])
    ]
    return "".join(list(formCard))


def as60WidthLines(card):
    data = list(card.values())
    s = "```\n{}\t({})\n".format(data[0], data[1])
    s += "\t{}\n".format(",".join(
        [aspect for aspect in data[2:6] if aspect != ""]))
    s += "\t{}\n```".format(data[6])
    return s


if __name__ == "__main__":
    main()
