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
        current = _priorityQueue.pop(0)
        if current == end:
            return reconstruct_path
        for neighbor in neighborMap[current]:
            tentativeGscore = gScore[current] + d(current, neighbor)
            if !(gScore[neighbor]) or (tentativeGscore< gScore[neighbor]):
                map[current]= neighbor
                gScore[neighbor]= tentativeGscore
                fScore[neighbor]= tentativeGscore + h(neighbor)
                if neighbor not in _priorityQueue:
                    _priorityQueue.((fscore[neighbor],neighbor))

    return 'Not finding path'
        
