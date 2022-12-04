#so i want to attribute values to the items and change it from list to array. e.g. a-z are 1-26 and A-Z 27-52. then i want to find the middle point and bisect each value in the array
#i then want to see if a same value is found in the left and the right, and where this is the case to log it
# the logged duplicates need to be summed using the values, and this total is the answer

#Python: Part 1:

with open("inputday03.txt") as file:
    list = []
    for i in file:
        i = i.strip()
        first = i[0:int((len(i)/2))]
        second = i[int((len(i)/2)):]
        letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        for x in range(len(letters)):
            if letters[x] in first:
                if letters[x] in second:
                    list.append(letters[x])
sum = 0
for i in list:
    value = letters.index(i)+1
    sum += value
print(sum)
#Part 2:

with open("inputday03.txt") as file:
    mod = 0
    list = []
    letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    content = file.readlines()
    while True:
        text = content[0+mod:3+mod]
        for i in letters:
            if (i in text[0]) and (i in text[1]) and (i in text[2]):
                list.append(i)
        mod += 3
        if mod == 300:
            break
sum = 0
for i in list:
    value = letters.index(i)+1
    sum += value
print(sum)


#Alternative
#Part 1:

#import string    
#with open('input', 'r') as file:
#  sum = 0
#  for line in file:
#    midpoint = len(line) // 2
#    first_half, second_half = line[:midpoint], line[midpoint:].strip()
#    sum += int(string.ascii_letters.index(''.join(set(first_half).intersection(second_half)))) + 1
#  print(sum)

#part 2
#import string  
#with open('input', 'r') as file:
#  sum = 0
#  lines = file.readlines()
#  for i in range(0, len(lines), 3):
#    sum += int(string.ascii_letters.index(''.join(set(lines[i].strip()).intersection(lines[i+1].strip())intersection(lines[i+2].strip())))) + 1
#  print(f'Part 2: {sum}')