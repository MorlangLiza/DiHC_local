import heapq

def merge(mst, k):
    merge_mst = []
    iter1 = len(mst)//k
    if len(mst)%k != 0:
        iter1 += 1
    
    for i in range(0, iter1):
        merge_mst.append(mst[i*k])
        for j in range(1, k):
            if i*k+j > len(mst)-1:
                break
            temp = heapq.merge(merge_mst[i], mst[i*k+j], key=lambda z: z[2])
            merge_mst[i] = [a for a in temp]
            
    return merge_mst