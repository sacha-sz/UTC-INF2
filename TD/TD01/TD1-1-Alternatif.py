if __name__ == "__main__":
    for i in range(1, 10):
        print(" " * (9 - i), end='')
        for j in range(1, i + 1):
            print(j, end='')
        for j in range(i - 1, 0, -1):
            print(j, end='')
        print()
