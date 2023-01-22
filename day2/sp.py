my_score = 0
string = { "A": 1,
            "X" : 1,
            "B" :2,
            "Y" :2,
            "C" :3,
            "Z" :3
}

with open('D:\Code\AOC22\day2\input.txt') as f:
    lines =f.readlines()
    
    
for line in lines:
    line = line.split()     
    
    print(line)
    if line[1] == "X":
        if line[0] == "A":
            my_score += string["Z"]
        elif line[0] == "B":
            my_score += string["X"]
        elif line[0] == "C":
            my_score += string["Y"] 
                  

    elif line[1] == 'Y':
        if line[0] == "A":
            my_score += string["X"]
            
            my_score += 3
            
        elif line[0] == "B":
            my_score += string["Y"]
            my_score += 3
        elif line[0] == "C":
            my_score += string["Z"]
            my_score += 3
            
       
    elif line[1] == "Z":        
        if line[0] == "A":
            my_score += string["Y"]
            my_score += 6
        elif line[0] == "B":
             my_score += string["Z"]
             my_score += 6
        elif line[0] == "C":
            my_score += string['X']
            my_score += 6
           
        
    
  
print(my_score)

 