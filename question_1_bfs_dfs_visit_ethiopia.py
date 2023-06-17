# Data Structure Reprentation Using Dictonary Data Structure 
graph = {
        'Addis Ababa': ['Adama', 'Ambo', 'Debre Berhan'],
        'Adama': ['Matahara', 'Asella', 'Batu', 'Addis Ababa'], 
        'Ambo': ['Wolkite', 'Addis Ababa', 'Nekemte'], 
        'Debre Berhan': ['Addis Ababa', 'Debre Sina'], 
        'Matahara': ['Adama', 'Awash'], 
        'Asella': ['Adama', 'Assasa'], 
        'Batu': ['Adama', 'Buta Jirra', 'Shashamene'], 
        'Wolkite': ['Ambo', 'Worabe', 'Jimma'], 
        'Nekemte': ['Ambo', 'Bedelle', 'Gimbi'], 
        'Debre Sina': ['Debre Berhan', 'Kemise', 'Debre Markos'], 
        'Awash': ['Chiro', 'Gobi Rasu', 'Matahara'], 
        'Assasa': ['Asella', 'Dodolla'], 
        'Buta Jirra': ['Batu', 'Worabe'], 
        'Shashamene': ['Batu', 'Hawassa', 'Dodolla', 'Hossana'], 
        'Worabe': ['Wolkite', 'Hossana', 'Buta Jirra'], 
        'Jimma': ['Wolkite', 'Bonga', 'Bedelle'], 
        'Bedelle': ['Nekemte', 'Gore', 'Jimma'], 
        'Gimbi': ['Nekemte', 'Dambidollo'], 
        'Kemise': ['Debre Sina', 'Dessie'], 
        'Debre Markos': ['Debre Sina', 'Finote Selam'],
        'Chiro': ['Awash', 'Dire Dawa'], 
        'Gobi Rasu': ['Awash', 'Samara'], 
        'Dodolla': ['Assasa', 'Shashamene', 'Bale'], 
        'Hawassa': ['Shashamene', 'Dilla'], 
        'Hossana': ['Shashamene', 'Worabe', 'Wolaita Sodo'], 
        'Bonga': ['Jimma', 'Dawro', 'Tepi', 'Mizan Teferi'], 
        'Gore': ['Tepi', 'Gambella', 'Bedelle'], 
        'Dambidollo': ['Gimbi', 'Assosa', 'Gambella'], 
        'Dessie': ['Kemise', 'Woldia'], 
        'Finote Selam': ['Debre Markos', 'Bahirdar', 'Injibara'], 
        'Dire Dawa': [ 'Chiro', 'Harar'], 
        'Samara': [ 'Gobi Rasu', 'Fanti Rasu', 'Alamata', 'Woldia'],
        'Bale': ['Liben', 'Dodolla', 'Goba', 'Sof Oumer'], 
        'Dilla': ['Hawassa', 'Bulehora'], 
        'Wolaita Sodo': ['Arba Minchi', 'Dawro', 'Hossana'], 
        'Dawro': [ 'Bonga', 'Basketo', 'Wolaita Sodo'], 
        'Tepi': ['Gore', 'Bonga', 'Mizan Teferi'], 
        'Mizan Teferi': ['Tepi', 'Bonga', 'Basketo'], 
        'Gambella': ['Gore', 'Dambidollo'], 
        'Assosa': ['Dambidollo', 'Metekel'], 
        'Woldia': ['Dessie', 'Lalibella', 'Samara', 'Alamata'],
        'Bahirdar': ['Finote Selam', 'Injibara', 'Metekel', 'Azezo', 'Debre Tabor'], 
        'Injibara': ['Bahirdar', 'Finote Selam'], 
        'Harar': [ 'Dire Dawa', 'Babile'], 
        'Fanti Rasu': ['Samara', 'Kilbet Rasu'], 
        'Alamata': ['Samara', 'Woldia', 'Mekelle', 'Sekota'], 
        'Liben': ['Bale'], 
        'Goba': ['Bale', 'Sof Oumer', 'Dega Habur'], 
        'Sof Oumer': ['Goba', 'Bale', 'Kebri Dehar'], 
        'Bulehora': [ 'Dilla', 'Yabello'], 
        'Arba Minchi': ['Wolaita Sodo', 'Konso', 'Basketo'], 
        'Basketo': [ 'Arba Minchi', 'Dawro', 'Mizan Teferi', 'Benchi Maji'], 
        'Metekel': [ 'Assosa', 'Bahirdar'],
        'Lalibella': ['Woldia', 'Debre Tabor', 'Sekota'],
        'Debre Tabor': ['Lalibella', 'Bahirdar'], 
        'Azezo': ['Gondar', 'Bahirdar', 'Metema'], 
        'Babile': [ 'Harar', 'Jigjiga'], 
        'Kilbet Rasu': ['Fanti Rasu' ], 
        'Mekelle': ['Alamata', 'Adwa', 'Adigrat', 'Sekota'], 
        'Sekota': ['Alamata', 'Mekelle', 'Lalibella'], 
        'Dega Habur': ['Goba', 'Jigjiga', 'Kebri Dehar'], 
        'Kebri Dehar': ['Gode', 'Sof Oumer', 'Dega Habur', 'Werdez'], 
        'Yabello': [ 'Bulehora', 'Konso', 'Moyale'], 
        'Konso': ['Arba Minchi', 'Yabello'], 
        'Benchi Maji': [ 'Basketo'], 
        'Gondar': [ 'Azezo', 'Metema', 'Debarke'],
        'Metema': [ 'Azezo', 'Gondar'],  
        'Jigjiga': [ 'Babile', 'Dega Habur'], 
        'Adwa': [ 'Mekelle', 'Axum', 'Adigrat'],
        'Adigrat': [ 'Mekelle', 'Adwa'], 
        'Gode': [ 'Dollo', 'Kebri Dehar' ], 
        'Werdez': [ 'Kebri Dehar'], 
        'Moyale': [ 'Yabello'], 
        'Debarke': [ 'Gondar', 'Shire'], 
        'Axum': ['Shire', 'Adwa'], 
        'Dollo': [ 'Gode'], 
        'Shire': [ 'Axum', 'Humera', 'Debarke'],
        'Humera': [ 'Shire', 'Gondar']
}

# DFS

def dfs(graph, start_node, target_node, visited=None, path=None):
    if visited is None:
        visited = set()
    if path is None:
        path = []

    path.append(start_node)
    visited.add(start_node)

    # Check if start node is target node
    if start_node == target_node:
        return path

    # Navigate Through the graph
    for neighbor in graph[start_node]:
        if neighbor not in visited:
            result = dfs(graph, neighbor, target_node, visited, path)
            if result is not None:
                return result

    path.pop()

    return None

# BFS
from collections import deque

def bfs(graph, start_node, target_node):
    # Create a double ended Queue 
    queue = deque()
    visited = set()
    visited.add(start_node)
    # initialize queue with start node and path to start node
    queue.append((start_node, [start_node]))
    

    while queue:
        
        # Pop node from the queue
        current_node, path = queue.popleft()

        # check if current node is target node 
        if current_node == target_node:
            return path
        
        # Navigate through the neigbors of the current node
        for neighbor in graph[current_node]:
            if neighbor not in visited:
                visited.add(neighbor)
                # Add the neighbor and path to neighbor to the queue if not visited
                queue.append((neighbor, path + [neighbor]))

    return None







start_node = 'Addis Ababa'
target_node = 'Gondar'

print('\n Question Number 1: Depth First Search')
print(' ===================================== \n')
path_dfs = dfs(graph, start_node, target_node)

if path_dfs is not None:
    print("Path :", ' -> '.join(path_dfs))
else:
    print("Path not found.")

print('\n Question Number 1: Breadth First Search')
print(' ===================================== \n')

path_bfs = bfs(graph, start_node, target_node)

if path_bfs is not None:
    print("Path :", ' -> '.join(path_bfs))
else:
    print("Path not found.")