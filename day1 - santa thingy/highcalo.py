import time
with open('day1 - santa thingy\input.txt') as f:
    lines =f.readlines()


elf1 = 0
elf2 = 0
for line in lines:    
    if line == "\n":
        if elf1 > elf2:
            elf2= elf1
        elf1=0        
    else:
        elf1 += int(line)  
        
print(time.process_time())
print(elf2)