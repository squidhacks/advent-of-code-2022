

#score = {"A X\n":4,"A Y\n":8,"A Z\n":3,"B X\n":1,"B Y\n":5,"B Z\n":9,"C X\n":7,"C Y\n":2,"C Z\n":6}



score = {"A X\n":3,"A Y\n":4,"A Z\n":8,"B X\n":1,"B Y\n":5,"B Z\n":9,"C X\n":2,"C Y\n":6,"C Z\n":7}




count = 0

with open("02.INPUT") as f:

    
    Lines = f.readlines()
    for line in Lines:
        count += score[line]

print(count)
