from Prim import prim
from Merge import merge
from Kruskal import kruskal

import numpy as np
import matplotlib.pyplot as plt
from random import shuffle

from itertools import combinations
from itertools import chain

def calcDistance(point1, point2):
    dist = 0
    for i in range(0, len(point1)):
        dist += (point1[i] - point2[i])**2
    return dist**(0.5)

if __name__ == '__main__':

    # задаём игрушечный датасет
    # n = 12
    s = 3
    points = [[2.5, 2, 1], [3.5, 2.5, 2], [4, 2, 3], [3, 4, 4], [4, 4, 5], [10, 5, 6], [9, 5.8, 7], [8, 7, 8], [9, 5, 9], [4, 10, 10], [5.2, 9, 11], [6, 10, 12]]
    shuffle(points)

    coords_x = []
    coords_y = []
    for point in points:
        coords_x.append(point[0])
        coords_y.append(point[1])
    plt.scatter(coords_x, coords_y)

    # делим датасет на s частей и строим сочетания
    splits = np.array_split(points, s)
    for array in splits:
        array.tolist()
        # print(list(array))
        
    merge_splits = []
    for D in list(combinations(splits, 2)):
        merge_splits.append(list(chain(D[0], D[1])))   
    # print("D_ij: ")
    # for D in merge_splits:
    #     print(D, sep='\n')

    # Первый этап - алгоритм Прима
    mst = []
    for D in merge_splits:
        n = len(D)
        W = np.zeros((n, n)).tolist()
        for i in range(0, n-1):
            for j in range(i+1, n):
                W[i][j] = calcDistance(D[i], D[j])
                W[j][i] = W[i][j]
    #     print(np.array(W))
        mst.append(prim(W, D))

    # for t in mst:
    #     print(t, sep="\n")

    # сортируем
    for t in mst:
        t.sort(key=lambda i: i[2])
        # print(t, sep="\n")

    # объединяем списки
    new_splits = merge(mst, 2)
    # for i in new_splits:
    #     print(i, sep="\n")

    # строим mst по алгоритму Крускала
    mst = []
    for R in new_splits:
        mst.append(kruskal(R))
    # for t in mst:
    #     print(t, sep='\n')

    # ещё одна итерация: объединяем списки -> строим mst
    new_splits = merge(mst, 2)
    for i in new_splits:
        print(i, sep="\n")

    mst = []
    for R in new_splits:
        mst.append(kruskal(R))
    for t in mst:
        print(t, sep='\n')
