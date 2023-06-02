def kruskal(R):
    connected = set()   # соединенные с кем-либо вершины
    D = {}              # изолированные группы вершин
    mst = []            # рёбра искомого дерева
    # print(len(R))

    for r in R:  
        if r[0] not in connected or r[1] not in connected:
            if r[0] not in connected and r[1] not in connected:
                D[r[0]] = [r[0], r[1]]          # формируем ключ с номерами вершин
                D[r[1]] = D[r[0]]               # и связываем их с одним и тем же списком вершин
            else:
                if not D.get(r[0]):             # если в словаре нет первой вершины, то
                    D[r[1]].append(r[0])        # добавляем в список первую вершину
                    D[r[0]] = D[r[1]]           # и добавляем ключ с номером первой вершины
                else:
                    D[r[0]].append(r[1])
                    D[r[1]] = D[r[0]]

            mst.append(r)                   # добавляем ребро в остов
            connected.add(r[0])
            connected.add(r[1])

    for r in R:    # объединяем изолированные группы вершин
        if r[1] not in D[r[0]]:         # если вершины принадлежат разным группам
            # print("test1: ", r[1], D[r[0]])
            # print("test2: ", r[0], D[r[1]])
            mst.append(r)
            gr1 = D[r[0]]                # объединем списки двух групп вершин
            D[r[0]] += D[r[1]]
            D[r[1]] += gr1

    return mst