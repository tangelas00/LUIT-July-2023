
import random  #The random module of the stand library generates random numbers and provide additional functions for applying random operations

print("------------------------------")
print("Welcome to random generator! ")
print("------------------------------")


def generate_random_name(department, length=6):  # this function generates a random name by combining the department name with random characters and numbers.
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    random_chars = ''.join(random.choice(characters) for _ in range(length))
    return f"{department}-{random_chars}"

def main():# this proccess users imput
    valid_departments = ["Marketing", "Accounting", "FinOps"]

    try:
        department_name = input("Enter the name of your department: ")
        department_name = department_name.strip().capitalize()
        if department_name not in valid_departments:
            print("Please use the Name Generator for Marketing, Accounting, or FinOps departments only.")
            return

        num_instances = int(input("Enter the number of EC2 instances you want names for: "))

        if num_instances <= 0:
            print("Number of instances must be a positive integer.")
            return

        unique_names = [generate_random_name(department_name) for _ in range(num_instances)]

        print("\nGenerated Unique Names:")
        for name in unique_names:
            print(name)

    except ValueError:
        print("Invalid input. Please enter a valid number of instances.")

if __name__ == "__main__":   #sed to execute some code only if the file was run directly, and not imported
    main()

