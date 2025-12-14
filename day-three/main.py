def main():
    print("Hello from day-three!")

def read_file(file_path) -> list[str]:
    with open(f'input/{file_path}', 'r') as file:
        return [str.strip(x) for x in file.readlines()]

def int_to_list(string):
    val = []
    for n in string:
        val.append(int(n))
    return val

        

def find_largest_point(list_d: list, dig:int = 3):
    digits: list[int] = [int(list_d[0])]
    for d in range(1, len(list_d)):
        pointers = len(digits)   
        val = int(list_d[d]) 
        remaining = len(list_d) - d
        print(remaining)
        for i in range(pointers):
            com = int(digits[i])
            if com > val and len(digits) < dig:
                digits.append(val)
                break
            else:
                digits[i] = com
            if val > com:
                digits[i] = val
                break

    return digits

        

if __name__ == "__main__":
    file = read_file('easy_input.txt')

    for n in range(0, len(file)):
        val = file[n]
        digits = find_largest_point(val, 3)
        print(digits)