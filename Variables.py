def main():
    #En int kan vara oändligtstor och oändligt liten
    #En int lagrar hela tal
    number = 1313144444444444444444444443*2323223123131
    print(len(str(number)))

    #Float är ett tal med decimaler
    number_float = 1313.313
    print(number_float)

    #Str är en variabel med text
    name = "Oscar"
    print(name.lower())
    while True:
        number_as_string = input("Enter a number: ")
        if number_as_string.isdigit():
            number_as_string = int(number_as_string)
            break
        else:
            print("Oii, laddie that's not a number!")
    print(int(number_as_string) + 2)


if __name__ == "__main__":
    main()
