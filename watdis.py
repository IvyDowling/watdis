import sys
import wikipedia
import logging
from itertools import islice


def run(dis):
    query = ' '.join(dis)
    try:
        luck = wikipedia.page(title=query)
        return luck.summary
    except wikipedia.exceptions.DisambiguationError:
        # many possible wiki pages
        e = sys.exc_info()
        r = ""
        for ln in islice(e, 0, len(e)):
            r += str(ln) + "\n"
        return r
    except wikipedia.exceptions.PageError:
        return "-No page found for that value"


if __name__ == "__main__":
    logging.captureWarnings(capture=True)
    if len(sys.argv) >= 2:
        if sys.argv[1] == "--help" or sys.argv[1] == "-h":
            print ("Ask me anything")
    while True:
        q = input("What are you looking for? ('quit' to exit)\n").split()
        if(len(q) > 0):
            if (len(q) == 1 and q[0] == "quit"):
                #end
                print("so long!")
                break
            else:
                print(run(q))


        else:
            print(run(sys.argv[1:]))
    else:
        q = input("What are you looking for?\n").split()
        if q != "":
            run(q)
        else:
            print("so long!")
