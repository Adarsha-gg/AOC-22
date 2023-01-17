import time
with open('day1\part2\input.txt') as f:
    lines =f.readlines()
    
elf1 = 0
elf2 = 0
elf3 =0
temp = 0

for line in lines:    
    if line == "\n":          
        if elf1 > elf2:
            temp = elf3
            elf3 = elf2
            elf2 = elf1
        elif elf1 > elf3:
            temp = elf3
            elf3 = elf1
        elif elf1 > temp:
            temp = elf1                    
        elf1 = 0             
    else:
        elf1 += int(line)  
        
print(time.process_time())
print(temp)
print(elf3)
print(elf2)
print(temp + elf3 +elf2)