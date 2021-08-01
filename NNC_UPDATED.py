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
            if group not in temparr:
                temparr.append(group)
            group.append(item)
        else:
            yield group
            group = [item]
            if group not in temparr:
                temparr.append(group)
        prev = item
    if group:
        yield group

def get_clusters(arr, distance):
    temparr = []
    arr.sort()
    dict(enumerate(clustering(arr, temparr, distance)))
    return temparr
        
def main():
    arr = [[465, 675], [477, 668], [78, 658], [586, 638], [607, 627], [588, 625], 
            [609, 620], [604, 619], [775, 609], [480, 606], [485, 594], [459, 590], 
            [387, 434], [831, 432], [399, 430], [797, 428], [353, 427], [398, 425], 
            [406, 437], [335, 399], [344, 411], [875, 396]]
    
    #arr.append([530, 650])
    temparr_new = get_clusters(arr, 88)
    
    for i in range(0, len(temparr_new)):
        print(i+1, temparr_new[i])

if __name__ == "__main__":
    main()