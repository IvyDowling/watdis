import sys
import wikipedia
import logging
from itertools import islice


def lucky(dis):
    query = ' '.join(dis)
    try:
        luck = wikipedia.page(title=query)
        print (luck.summary)
    except wikipedia.exceptions.DisambiguationError:
        # disambiguation
        e = sys.exc_info()
        for ln in islice(e, 1, len(e) - 1):
            print(ln, "\n")


if __name__ == "__main__":
    logging.captureWarnings(capture=True)
    if len(sys.argv) >= 2:
        if sys.argv[1] == "--help" or sys.argv[1] == "-h":
            print ("Ask me anything")
        else:
            lucky(sys.argv[1:])
    else:
        q = input("What are you looking for?\n").split()
        if q != "":
            lucky(q)
        else:
            print("okay?")
