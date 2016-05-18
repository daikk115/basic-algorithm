import math
import pprint
pp = pprint.PrettyPrinter(indent=4)

maps = []

def init_maps():
    for i in range(8):
        tmp = []
        for j in range(8):
            tmp.append(0)
        maps.append(tmp)

def check(row, column, positions):
    for position in positions:
        delta1 = math.fabs(position["column"]-column)
        delta2 = math.fabs(position["row"]-row)
        if delta1 == delta2 or position["column"] == column:
            return False
    return True

def xepHau(row, positions):
    if row == 8:
        pp.pprint(positions)
        return True
    for column in range(8):
        # print row, column
        # print positions
        if check(row, column, positions):
            tmp = {}
            tmp["row"] = row
            tmp["column"] = column
            positions.append(tmp)
            maps[row][column] = 1
            if(xepHau(row+1, positions) is True):
                return True
            else:
                positions.pop()
                continue
        

    return False

if __name__ == '__main__':
    init_maps()
    positions = xepHau(0, [])


        