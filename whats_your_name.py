def print_full_name(first, last):
    message = "Hello " + first + " " + last + "! You just delved into python."
    return message
    
    

if __name__ == '__main__':
    first_name = "Ash"
    last_name = "ketchum"
    response = print_full_name(first_name, last_name)
    print(response)