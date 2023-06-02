import random
   
def prim(W, arr):

    points_count = len(W)
 
    # выбор начального города
    free_vertexes = list(range(0, points_count))
 
    starting_vertex = random.choice(free_vertexes)
    connected = [starting_vertex]
    free_vertexes.remove(starting_vertex)
 
    road_length = 0
    mst = []
 
    # пока есть свободные вершины
    while free_vertexes:
        min_link = None  # соединение, образующее минимальный путь
        overall_min_path = float('inf')   # минимальный путь среди всех возможных
 
        # проход по всем уже связанным вершинам
        for current_vertex in connected:
            weights = W[current_vertex]   # связи текущей вершины с другими
 
            min_path = float('inf')
            free_vertex_min = current_vertex
 
            # проход по связанным вершинам
            for vertex in range(points_count):
                vertex_path = weights[vertex]
                if vertex_path == 0:
                    continue
 
                if vertex in free_vertexes and vertex_path < min_path:
                    free_vertex_min = vertex
                    min_path = vertex_path
 
            if free_vertex_min != current_vertex:
                if overall_min_path > min_path:
                    min_link = (current_vertex, free_vertex_min)
                    overall_min_path = min_path

            path_length = W[min_link[0]][min_link[1]]
         
        k1 = min_link[0]
        k2 = min_link[1]
        # print('Connecting %s to %s [%s]' % (int(arr[k1][2]), int(arr[k2][2]), path_length))
        mst.append([int(arr[k1][2]), int(arr[k2][2]), path_length])
        
        road_length += path_length
        free_vertexes.remove(min_link[1])
        connected.append(min_link[1])
        
    # print("\n")
    return list(mst)