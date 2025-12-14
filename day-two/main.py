import sys 
try:
    file_path = sys.argv[1]
except IndexError:
    file_path = 'input.txt'
def main():
    print(f"Hello from day-two! {file_path}")

def read_file(file_path) -> str:
    with open(f'input/{file_path}', 'r') as file:
        return str.strip(file.read())
def delimit(string:str, char=','):
    return string.split(char)
if __name__ == "__main__":
    file = read_file(file_path)
    
    str_list = delimit(file)
    invalid_ids = []
    for id_ in str_list:
        a, b = delimit(id_, '-')
        element_range = range(int(a), int(b)+1, 1)
        for n in element_range:
            leng = str(n)
            chars = len(leng)//2
            valid_final = False
            if False:
                valid_final = False
                next
            else:
                elem_pos = range(1, len(leng))
                valid_final = False
                for j in elem_pos:
                    if len(leng)%j == 0:
                        pos = j
                        chars = leng[0:pos]
                        valid = True
                        for x in range(1, (len(leng)//j)):
                            if chars != leng[pos:pos+j]:
                                valid = False
                                break
                            chars = leng[pos:pos+j]
                            pos = pos+j
                        if valid:
                            valid_final = True
            if valid_final:
                invalid_ids.append(n)       
    print(invalid_ids)                 
    print(sum(invalid_ids))