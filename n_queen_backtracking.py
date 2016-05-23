import math
import pprint
pp = pprint.PrettyPrinter(indent=4)

maps = []
N = 8


def init_maps():
    for i in range(N):
        tmp = []
        for j in range(N):
            tmp.append("o")
        maps.append(tmp)

def check(row, column, positions):
    for position in positions:
        delta1 = math.fabs(position["column"]-column)
        delta2 = math.fabs(position["row"]-row)
        if delta1 == delta2 or position["column"] == column:
            return False
    return True

def xepHau(row, positions):
    if row == N:
        """
            if row == N that means every queens have been sorted
        """
        for tmp in positions:
            maps[tmp["row"]][tmp["column"]] = "x"
        return True

    for column in range(N):
        if check(row, column, positions):
            tmp = {}
            tmp["row"] = row
            tmp["column"] = column
            positions.append(tmp)
            if(xepHau(row+1, positions) is True):
                return True
            else:
                positions.pop()
                continue
        

    return False

if __name__ == '__main__':
    init_maps()
    # we start with row 0 and list position queens empty
    xepHau(0, [])
    pp.pprint(maps)


        
