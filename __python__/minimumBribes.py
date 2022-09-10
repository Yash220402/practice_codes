def minimumBribes(q):
    count = 0
    for i in range(len(q)):
        if q[i] > i+3:
            print("Too Chaotic!")
            return

        for j in range(max(0, q[i]-2), i):
            if q[j] > q[i]:
                count += 1
    print(count)


if __name__ == "__main__":
    q = [5, 1, 2, 3, 7, 8, 6, 4]
    minimumBribes(q)

    q = [1, 2, 5, 3, 7, 8, 6, 4]+
    minimumBribes(q)