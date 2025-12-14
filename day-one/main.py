
def main():
    print("Hello from day-one!")


def read_lines_from_file(file_path):
    with open(file_path, 'r') as file:
        return file.readlines()
    

def analyse_line(line) -> tuple[float, str]: 
    num = int(line[1:])
    rot = line[0]
    
    return num, rot


def rotate_r(dial, val):
    temp = dial + val
    if temp < 100:
        return 0, temp
    if temp == 100:
        return 1, 0
    if temp > 100:
        zeros = (temp//100)
        temp = (temp%100)

        return zeros, temp

def rotate_l(dial, val):
    temp = dial - val
    mod = 0
    if temp > 0:
        return 0, temp
    if temp == 0:
        return 1, temp
    if dial == 0 and val < 100:
        return 0, temp+100
    if dial == 0:
        mod -=1 
    if temp <= 0:
        zeros = abs(temp//100)
        temp = (temp%100)
        zeros += mod 
        if temp == 0:
            zeros += 1
        return zeros, temp
            

if __name__ == "__main__":
    dial = 50
    zero_point = 0
    print(f'DIAL: {dial}')
    lines = read_lines_from_file("input.txt")
    for n in lines:
        val, loc = analyse_line(n)
        if loc == 'R':
            zero, dial = rotate_r(dial, val)
            zero_point += zero
        if loc == 'L':
            zero, dial = rotate_l(dial, val)
            zero_point += zero
        print(f'Clicks: {zero}, D:{dial} {loc}:{val}')
        
    print(zero_point)