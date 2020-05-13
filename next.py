with open('output.txt', 'r') as file:
    data = file.read().replace('\n', '')
splitted = data.split()

print splitted[3]
print splitted[4]
print splitted[5]
print splitted[6] 
print splitted[7]
