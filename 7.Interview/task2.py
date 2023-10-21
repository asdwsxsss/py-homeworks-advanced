from task1 import Stack

string1 = '(((([{}]))))'

test = Stack(list(string1))

while test.size == False:
    list_temp = []
    list_temp2 = []
    sumbol = test.pop()
    if sumbol == ')' or '}' or ']':
        list_temp.append(sumbol)
    elif sumbol == '(' or '{' or '[':
        list_temp2.append(sumbol)