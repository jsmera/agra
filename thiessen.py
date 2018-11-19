from heapq import heappush, heappop
INF = float('inf')

def get_seconds(date_1, date_2):
  delta = abs(date_2 - date_1)
  return 86400*delta.days + delta.seconds

def build_graph(tree, G):
  if tree.getAuthor() not in G:
    G[tree.getAuthor()] = {}
  ocurrencias = []
  for subcomment in tree.getComments():
    assert tree.getDate() <= subcomment.getDate()
    delta = get_seconds(tree.getDate(), subcomment.getDate())
    aux = build_graph(subcomment, G)
    aux.append([subcomment.getAuthor(), 0])

    for k in range(len(aux)):
      aux[k][1] += delta
      if not aux[k][0] in G:
        G[aux[k][0]] = {}

      if aux[k][0] != tree.getAuthor():
        if aux[k][0] in G[tree.getAuthor()]:
          G[tree.getAuthor()][aux[k][0]][0] += aux[k][1]
          G[tree.getAuthor()][aux[k][0]][1] += 1
        else:
          G[tree.getAuthor()][aux[k][0]] = [aux[k][1], 1]

        if tree.getAuthor() in G[aux[k][0]]:
          G[aux[k][0]][tree.getAuthor()][0] += aux[k][1]
          G[aux[k][0]][tree.getAuthor()][1] += 1
        else:
          G[aux[k][0]][tree.getAuthor()] = [aux[k][1], 1]

    ocurrencias += aux

  return ocurrencias

def thiessen(tree):
  G = {}
  build_graph(tree, G)
  distribucion = {}
  for node in G:
    if len(G[node]) in distribucion: distribucion[len(G[node])] += 1
    else: distribucion[len(G[node])] = 1
  
  k = INF
  maxima_frecuencia = -INF
  for grado in distribucion:
    if distribucion[grado] > maxima_frecuencia:
      k = min(grado, k)
      maxima_frecuencia = distribucion[grado]
  participacion = tree.getUserByCommentsList()
  centros = {}
  distance = {}
  usuario = {}
  k = k if k > 2 else 2
  for i in range(len(participacion)):
    if i < k:
      centros[participacion[i][0]] = set()
    distance[participacion[i][0]] = INF
    usuario[participacion[i][0]] = ""
  
  for source in centros:
    heap = [(source, 0)]
    while len(heap):
      u, wi = heappop(heap)
      for v in G[u]:
        acumulado, n = G[u][v]
        promedio = acumulado//n
        last = usuario[v]
        for w in centros:
          if v in centros[w]: last = w
        if wi + promedio < distance[v]:
          distance[v] = wi + promedio
          heappush(heap, (v, wi + promedio))
          if v not in centros:
            if last != "": centros[last].remove(v)
            centros[source].add(v)
        elif wi + promedio == distance[v]:
          heappush(heap, (v, wi + promedio))
          if v not in centros:
            if last != "":
              if v in centros[last] and last > source:
                centros[last].remove(v)
                centros[source].add(v)

  for centro in centros:
    print(centro, end=" ")
    print(*centros[centro], end=" ")
    stop = len(centros[centro])
    for vertice in centros[centro]:
      print(distance[vertice], end=" ")
    print()