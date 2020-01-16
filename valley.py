"""Program to count number of valleys in a string(e.g.:UDDUDUDUUU). where,up is denoted by 'U' and down is denoted by 'D'"""
n = int(input())
s =input()
level = 0
valleys = 0
for direction in s:
    if direction == "U":
        level += 1
        if level == 0:
            valleys += 1
    else:
        level -= 1
         
print valleys
