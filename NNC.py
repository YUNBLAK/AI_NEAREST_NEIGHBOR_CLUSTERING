import math
import matplotlib.pyplot as plt

def euclidean(x1, x2):
    length = 0
    for i in range(len(x1)):
        length += (x1[i] - x2[i]) ** 2
    return length ** 0.5

def clustering(iterable, temparr, distance):
    prev = None
    group = []
    for item in iterable:
        if not prev or euclidean(item, prev) <= distance:
            temparr.append(group)
            group.append(item)
        else:
            yield group
            group = [item]
            temparr.append(group)
        prev = item
    if group:
        yield group
        
def main():
    arr = [[465, 675], [477, 668], [78, 658], [586, 638], [607, 627], [588, 625], 
            [609, 620], [604, 619], [775, 609], [480, 606], [485, 594], [459, 590], 
            [387, 434], [831, 432], [399, 430], [797, 428], [353, 427], [398, 425], 
            [406, 437], [335, 399], [344, 411], [875, 396]]
    
    #arr.append([530, 650])
    arr.sort()
    clustered_arr = []
    temparr = []
    distance = 88
    
    dict(enumerate(clustering(arr, temparr, distance)))
    for i in range(0, len(temparr)):
        if temparr[i] not in clustered_arr:
            clustered_arr.append(temparr[i])
    for i in range(0, len(clustered_arr)):
        print(i+1, clustered_arr[i])

if __name__ == "__main__":
    main()