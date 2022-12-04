blocks = open("inputday1.txt").read().split("\n\n")

Maxruntotal = 0
 

for block in blocks:
    print("")
    print("I AM RESETTING THE COUNTER")  
    total = 0

    for line in block.split("\n"):
        print (f'line: {line}')
        calories=int(line) 
        total = total + calories    
    print(f'total: {total}')
    
    #if total > Maxruntotal: 
     #   Maxruntotal = total
    Maxruntotal=max([Maxruntotal, total])
print(f'MaxRunTotal: {Maxruntotal}') 
    
#part 2
#highest = [0]*3

#current = 0

#for line in inputday1:
#	if (line == "\n"):
#		highest.sort()
#		if (current > highest[0]):
#			highest[0] = current
#		current = 0
#	else:
#		current += int(line)

#print(sum(highest))