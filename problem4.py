
user_input = int(input("N = "))
numbers = []

def make_a_list_():
    for i in range(1, user_input + 1):
        numbers.append(str(i))

def convert_list():
    for i in range(len(numbers)):
        if int(numbers[i]) % 3 == 0 and int(numbers[i]) % 5 == 0:
            numbers[i] = "FizzBuzz"
        elif int(numbers[i]) %  3 == 0:
            numbers[i] = "Fizz"
        elif int(numbers[i]) %  5 == 0:
            numbers[i] = "Buzz" 
        else: 
            continue

make_a_list_()
convert_list()
print(numbers)

# make_a_list_()