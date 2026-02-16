# Personal Introduction Program

def main():
    print("--- Welcome to the Personal Introduction Portal ---")
    print("Please answer the following questions so we can know you better.\n")

    #Using input() and storing in variables
    name = input("What is your name? ")
    age = input("How old are you? ")
    hobby = input("What is your favorite hobby? ")

    #Making the output friendly and welcoming
    print("*"*50)
    print(f"Hello {name}! It's wonderful to meet you.")
    print(f"It's cool that you are {age} years old and enjoy {hobby}.")
    print("We are thrilled to have you here at The Developers Arena!")
    print("*"*50)

if __name__ == "__main__":
    main()