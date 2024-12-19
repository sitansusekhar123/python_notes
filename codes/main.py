import random


def random_number_generator():
    random_number = random.randint(1, 1000)
    return random_number

if __name__ == "__main__":
    print("I am in the main function")
    my_random_number = random_number_generator()
    print(my_random_number)
    