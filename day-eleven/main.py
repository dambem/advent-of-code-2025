# aaa: you hhh
# you: bbb ccc
# bbb: ddd eee
# ccc: ddd eee fff
# ddd: ggg
# eee: out
# fff: out
# ggg: out
# hhh: ccc fff iii
# iii: out

# make a branching list 
# starts with aaa -> [bbb, ccc]
# aaa -> [bbb -> ddd, eee]
def read_file(file_path:str):
    with open(f'input/{file_path}', 'r') as file:
        return [str.strip(n) for n in file.readlines()]
def delimit(string:str, char=','):
    return string.split(char)    
def process_files(values):
    vals = []
    for n in values:
        input, output = delimit(n, ':')
        outputs = delimit(str.strip(output), ' ')
        vals.append((input, outputs))
    return vals

class MapMaker:
    def __init__(self):
        self.i_val = 0
        self.you = -1
        self.out = -1
        self.identity_map = {}
        self.main_map = {}
    def get_identity_map(self, value):
        map_id = None
        if value not in self.identity_map:
            self.identity_map[value] =  self.i_val
            map_id = self.i_val
            self.i_val += 1
        else:
            map_id = self.identity_map[value]
        return map_id

    def add_node_to_map(self, value):
        map_id = self.get_identity_map(value)
        if self.main_map.get(map_id) is None:
            self.main_map[map_id] = []

    def add_edge_to_map(self, edge, value):
        map_id = self.get_identity_map(value)
        edge_id = self.get_identity_map(edge)

        if self.main_map.get(map_id) is None:
            self.main_map[map_id] = [edge_id]
        else:
            self.main_map[map_id].append(edge_id)

    def main(self):
        file = read_file('input_second.txt')
        processed = process_files(file)
        for input, outputs in processed:
            self.add_node_to_map(input)
            for n in outputs:
                self.add_edge_to_map(n, input)
        self.out = map_maker.identity_map['out']
    
    def solve(self):
        self.you = map_maker.identity_map['you']
        solution = [self.you]
        path = 0
        while solution != []:
            new_sol = []
            for n in solution:
                if n == self.out:
                    path += 1
                else:
                    new_sol = new_sol + map_maker.main_map[n]
            solution = new_sol
    def solve_svr(self):
        svr = self.identity_map['svr']
        solution = [svr]
        path = 0
        while solution != []:
            new_sol = []
            for n in solution:
                if n == self.out:
                    path += 1
                else:
                    new_sol = new_sol + map_maker.main_map[n]
            solution = new_sol
if __name__ == "__main__":
    map_maker = MapMaker()
    map_maker.main()

    # map_maker.solve()
    map_maker.solve_svr()