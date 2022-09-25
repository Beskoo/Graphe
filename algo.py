def generate_random_graph(vertices, edges):
    import random
    graph = {}
    for i in range(vertices):   # iterer sur les sommets
        graph[i] = []
    for i in range(edges):    # iterer sur les aretes
        a = random.randint(0, vertices-1)   # choisir un sommet au hasard
        b = random.randint(0, vertices-1)   # choisir un sommet au hasard
        if a != b:  
            graph[a].append(b)  # ajouter l'arete (a,b)
            graph[b].append(a)  # ajouter l'arete (b,a)
    return graph

graph = generate_random_graph(1000, 15000)

def is_dominant_set(graph, set):
    for node in graph:      # pour chaque noeud
        if node not in set:
            flag = False 
            for neighbor in graph[node]:    # pour chaque voisin 
                if neighbor in set:     # si un voisin est dans le set
                    flag = True
                    break
            if not flag:
                return False
    return True


def dominant_set(graph):

    dominant_set = []
    flag=set() 
    for node in graph: # pour chaque noeud

        if node not in flag: 
            dominant_set.append(node) 

            for neighbor in graph[node]: 
                flag.add(neighbor)

    return dominant_set


print(generate_random_graph(1000, 15000))
print(is_dominant_set(graph, [2,3,1,5,7]))
print(dominant_set(graph))