# Nearest Neighbor Clustering Algorithm (NNC)
## by YUNBLAK
### Nearest Neighbors Clustering without any Library

[IMAGES ARE FROM NASA]

I thought of NNC algorithm while analyzing Sunspots. I got the coordinate value(X,Y)s of small sunspots through Image Processing and came up with a way to form close coordinates into a single cluster. We differ from the KNN algorithm in that we need to automatically form clusters without a specified K value because we don't know how many Sunspot clusters can be formed in the sun. An NNC algorithm is an algorithm that automatically clusters coordinates based on distance.
  
    # SUNSPOTS COORNATES VALUES
    arr = [[465, 675], [477, 668], [78, 658], [586, 638], [607, 627], [588, 625], 
            [609, 620], [604, 619], [775, 609], [480, 606], [485, 594], [459, 590], 
            [387, 434], [831, 432], [399, 430], [797, 428], [353, 427], [398, 425], 
            [406, 437], [335, 399], [344, 411], [875, 396]]

![Z004](https://user-images.githubusercontent.com/87653966/127765464-b0ae0a5e-9f79-4857-9784-0e7470e23236.png)


#### EUCLIDEAN DISTANCE
We calculated the distance of each coordinate using the Euclidean distance technique. Because NNC techniques work based on the distance of each coordinates, it is important to calculate the distance. In other words, if the distance from this cluster to other cluster is farther than a certain value, it is judged as a different cluster, and if it is close, it is judged as the same cluster.

    def euclidean(x1, x2):
        length = 0
        for i in range(len(x1)):
            length += (x1[i] - x2[i]) ** 2
        return length ** 0.5

![Z001](https://user-images.githubusercontent.com/87653966/127765248-8700730c-0c8f-4b0f-b08d-31ff8d7c72c0.PNG)

#### NNC CLUSTERING METHOD
    # distance = 88
    
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
            
    # OUTPUT
    # 1 [[78, 658]]
    # 2 [[335, 399], [344, 411], [353, 427], [387, 434], [398, 425], [399, 430], [406, 437]]
    # 3 [[459, 590], [465, 675], [477, 668], [480, 606], [485, 594]]
    # 4 [[586, 638], [588, 625], [604, 619], [607, 627], [609, 620]]
    # 5 [[775, 609]]
    # 6 [[797, 428], [831, 432], [875, 396]]
    
I checked if it was recognized as the same cluster if I added a dot between the two clusters.

    arr.append([530, 650])

![Z002](https://user-images.githubusercontent.com/87653966/127765249-d5c0feb1-52fc-4fdc-89fd-dc2655fda909.PNG)

As a result, the two groups, which were recognized as different clusters, were recognized as the same clusters by one new point. I came to think of these NNC algorithms to cluster black spots to detect changes and outliers in black spots. I also want to cluster them and learn images to see how they affect the future.
