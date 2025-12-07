"""
Answer to question 4 of formative 2
"""

def check_level(level):
    if level[-1] == 0 or level[0] == 0:
        return False
    elif len(level) == 1:
        return True
    
    jumps = level[0]
    if jumps >= len(level):
        jumps = len(level) - 1
    while jumps > 0:
        if level[jumps] == 0:
            jumps -= 1
        else:
            return check_level(level[jumps:])
    return False

def main():
    level = [1,2,0,3,0,0,1]
    print(check_level(level))

if __name__ == "__main__":
    main()