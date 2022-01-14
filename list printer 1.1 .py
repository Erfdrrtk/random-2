import statistics # this module is needed to find the median of the list
the_list = [] # this list will be filled by user later
def list_printer():
    how_many_numbers = int(input('enter the amount of numbers for the list: '))  # for the number of things that will be in the list, the user will-
    for x in range(how_many_numbers):                                            # be asked to enter a number. each number the user inputs will be appended to the list
        enter_number_in_list = int(input('enter a number: '))
        the_list.append(enter_number_in_list)
# the function above contains the code that fills the list
print('''--- welcome to list printer ---
you will be allowed to fill the list, and then the program will make calculations for the list. Enjoy :D
''')

# this try and except part will quit the code if the user enters something that causes an error in the code.
# this is too prevent annoying red error text and to make the code more clean :)
try:
    list_printer()
except:
    quit(print("only numbers please. restart the code because I dont know how to make it restart itself. "))


print('the list: ', the_list)

count = 0
print('''---------------------------
 count | number ''')

for number in the_list:
    count = 1 + count
    print(f'{count}          {number}')


print('''---------------------------
the calculations:
''')

sum = sum(the_list)
average = sum / count
biggest = max(the_list)
smallest = min(the_list)
median = statistics.median(the_list)

print(f'sum: {sum}')
print(f'average: {int(average)}')
print(f'biggest: {biggest}')
print(f'smallest: {smallest}')
print(f'median: {median}')