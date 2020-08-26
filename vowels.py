def main():
    vowels = "aeoiyu"
    letter = input("input a letter: ")

    if letter.lower() in vowels:
        print("it was a vowel")
    else:
        print("it wasn't a vowel")


if __name__ == "__main__":
    main()
