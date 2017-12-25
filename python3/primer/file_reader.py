fileName = 'pi_digits.txt'
pi_string = ''

with open(fileName) as file_object:
    lines = file_object.readlines()

    for line in lines:
        pi_string+=line.strip()

    """打印10位"""
    print(pi_string[:10])
    print(len(pi_string))

birthday = input("please Enter your birthday: ")

if birthday in pi_string:
    print("your birthday appear in digits")
else:
    print("your birthday not in appear in digits")
