def main():
    number = 10
    letter = "X"

    while number > 0 and letter == "X":
        if number == 5:
            letter = "Y"
        print(number)
        number -= 1


if __name__ == "__main__":
    main()
