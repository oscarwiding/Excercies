def main():

    sekvens = ["hepp", "hopp", "hue"]

    for i in ["abc", "def", "ghy"]:
        print(i)

    for i in range(2, 10, 2):
        if i == 6:
            continue
        print(i)
    else:
        print("Hej då")

    for _ in range(2):
        print("tihi")

    for variable in sekvens:
        for c in variable:
            print(c)
        print("-----")

if __name__ == "__main__":
    main()
