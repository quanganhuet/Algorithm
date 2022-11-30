from queue import PriorityQueue


map={}

def reconstruct_path(start, end):
    paths = [end]
    while(true):
        previous = map["end"]
        if previous == start:
            break
        path.insert(0, previous) 
    return path

def a_star(start, end, neighborMap, h):
    _priorityQueue= PriorityQueue()
    gScore={start:0}
    fScore={start:h(start)}
    map[start]=''

    _priorityQueue.put((fscore[start],start))
    while not _priorityQueue.empty():
        get_current = _priorityQueue.get()
        current = get_current[1]
        if current == end:
            return reconstruct_path
        for neighbor in neighborMap[current]:
            tentativeGscore = gScore[current] + d(current, neighbor)
            if !(gScore[neighbor]) or (tentativeGscore< gScore[neighbor]):
                map[current]= neighbor
                gScore[neighbor]= tentativeGscore
                fScore[neighbor]= tentativeGscore + h(neighbor)
                if neighbor not in _priorityQueue:
                    _priorityQueue.put((fscore[neighbor],neighbor))

    return 'Not finding path'

def dijkstra(start, end, listNodes, neighborMap)
    _priorityQueue= PriorityQueue()
    _priorityQueue.put((0,start))
    gScore={start: 0}
    for node in listNodes:
        _priorityQueue.put((10e14,node))
    
    while not _priorityQueue.empty():
        get_current = _priorityQueue.get()
        current = get_current[1]
        priority = get_current[0]
        if current == end:
            if priority ==10e14:
                return "Not found"
            return reconstruct_path
        for neighbor in neighborMap[current]:
            tentativeGscore = gScore[current] + d(current, neighbor)
            if (tentativeGscore< gScore[neighbor]):
                map[current]= neighbor
                gScore[neighbor]= tentativeGscore
            

        
