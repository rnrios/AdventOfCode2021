import numpy as np
from queue import PriorityQueue
INF = np.inf
 
# Djikstra implementation taken from: https://www.geeksforgeeks.org/
# shortest-paths-from-all-vertices-to-a-destination/
class Graph:
    def __init__(self, V: int) -> None:
 
        self.V = V

        self.adj = [[] for _ in range(V)]
    def add_edge_rev(self, u: int, v: int, w: int) -> None:
        self.adj[v].append((u, w))
 
    def shortest_path(self, dest: int) -> None:
        pq = PriorityQueue()
        
        dist = [INF for _ in range(self.V)]
 
        pq.put((0, dest))
        dist[dest] = 0
 
        while not pq.empty():
            u = pq.get()[1]
            for i in self.adj[u]: 
                v = i[0]
                weight = i[1]
                if (dist[v] > dist[u] + weight):      
                    dist[v] = dist[u] + weight
                    pq.put((dist[v], v))

        print("Destination Vertex Distance from all vertex")
        for i in range(self.V):
            if i==0 or i==self.V-1:
                print("{} \t\t {}".format(i, dist[i]))

def preproc(filename):
    f = open(filename, 'r').read().splitlines()
    array = np.array([[int(x) for x in line] for line in f])
    return array


def create_list(arr):
    flattened_arr = arr.ravel()
    N = flattened_arr.shape[0]
    num_rows, num_cols = arr.shape[0], arr.shape[1]
    adj_list = []
   
    for i in range(5*num_rows):
        for j in range(5*num_cols):
            if i-1 >= 0:
                new_val = (arr[(i-1)%num_rows][j%(num_cols)] + int((i-1)/num_rows) + int(j/num_cols))
                if new_val >= 10:
                    new_val -= 9
                adj_list.append((i*5*num_cols+j, (i-1)*5*num_cols+j, max(new_val, 1)))
            
            if j-1 >= 0:
                new_val = (arr[i%num_rows][(j-1)%(num_cols)] + int(i/num_rows) + int((j-1)/num_cols))
                if new_val >= 10:
                    new_val -= 9
                adj_list.append((i*5*num_cols+j, i*5*num_cols+j-1, max(new_val, 1)))
                
            if i==12 and j==2:
                print(arr[i%num_rows][(j+1)%num_cols], arr[2][3])

            if j+1 < 5*num_cols:
                new_val = (arr[i%num_rows][(j+1)%num_cols] + int(i/num_rows) + int((j+1)/num_cols))
                if new_val >= 10:
                    new_val -= 9
                adj_list.append((i*5*num_cols+j, i*5*num_cols+j+1, max(new_val, 1)))

            if i+1 < 5*num_cols:
                new_val = (arr[(i+1)%num_rows][j%num_cols] + int((i+1)/num_rows) + int(j/num_cols))
                if new_val >= 10:
                    new_val -= 9
                adj_list.append((i*5*num_cols+j, (i+1)*5*num_cols+j, max(new_val, 1)))
            
    return adj_list, 25*N


def main():
    arr = preproc('input.txt')
    adj_list, N = create_list(arr)
    graph = Graph(N)
    for i, x in enumerate(adj_list):
        graph.add_edge_rev(x[0], x[1], x[2])
    graph.shortest_path(N-1)
    
    
if __name__ == '__main__':
    main()