import statistics
awdhj = []
def list_printer():
    how_many_numbers = int(input('enter the amount of numbers for the list: '))
    for x in range(how_many_numbers):
        enter_number_in_list = int(input('enter a number: '))
        awdhj.append(enter_number_in_list)

try:
    list_printer()
except:
    quit(print("only numbers please. restart the code because I dont know how to make it restart itself. ")
)


print('the list: ', awdhj)

count = 0
print('''---------------------------
 count | number ''')

for number in awdhj:
    count = 1 + count
    print(f'{count}          {number}')


print('''---------------------------
the calculations:
''')

sum = sum(awdhj)
average = sum / count
biggest = max(awdhj)
smallest = min(awdhj)
median = statistics.median(awdhj)

print(f'sum: {sum}')
print(f'average: {int(average)}')
print(f'biggest: {biggest}')
print(f'smallest: {smallest}')
print(f'median: {median}')