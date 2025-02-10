def greet():
    """
    Simple function printing hello
    :return: 0
    """
    print("Hello!")
    return 0

def greet_improved(name):
    """
    Improved function printing hello
    :param name: str
    :return: None
    """
    print(f"Hello, {name}!")

greet_improved("John")
greet_improved('Jane')

def custom_op(x = 0, y = 0):
    """
    Executes a function
    :param a:
    :param b:
    :return:
    """
    return 10*x + y

print(custom_op(5,8))
x = custom_op(5,4) # arguments by position
print(f'The result of custom_op is {x}')
x = custom_op(x = 5, y = 4) # arguments by name
print(f'The result of custom_op is {x}')

print(custom_op(5)) # using default values for y
print(custom_op(0)) # using default values for both
print(custom_op(y = 9)) # using default values for x

def bond_intro(name):
    print('the name is: ', name)

def bond_name(first = 'James', last = 'Bond'):
    return f'{last}, {first} {last}'

print(bond_name('Niolas', 'Tello'))
bond_intro(bond_name('Nicolas', 'Tello'))