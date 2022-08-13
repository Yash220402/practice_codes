def substrings(word):
    a = [word[:i] for i in range(1, len(word) + 1)]
    return a


def pheonixWord(n, words):
    wordPairs = [set(words[:i]) for i in range(1, n+1)]
    print(wordPairs)


def main():
    n = 3
    words = ["cross", "stop", "arm"]
    print(pheonixWord(n, words=words))


if __name__ == '__main__':
    main()
