

file1 = input('Enter the name of file: ')
opening = open(file1)
count = 0

for i in opening:
    i = i.rstrip()
    if i.startswith('IS'):
        count = count + 1
    
print('There were', count, '(IS) lines in', file1)
    