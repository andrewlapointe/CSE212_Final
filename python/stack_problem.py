list = []
list.append(3)
list.append(4)
list.pop()
list.append(2)


answer1 = input('What is the value of the stack? (sum all intergers)\n> ')
if answer1 == '5':
    print('Correct')
else:
    print('False',list)
    print('the sum is 5')