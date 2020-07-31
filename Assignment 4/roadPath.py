import sys


class Heap():
    def __init__(self):
        """
        Constructor for the class
        Time complexity: O(1)
        Space complexity: O(1)
        Error handle: N/A
        Return: N/A
        Parameter: N/A
        Precondition: N/A
        """
        self.array = []
        self.size = 0
        self.pos = []

    def heapify(self, idx):
        """
            Given a valid array, will turn into a min-heap
            Time complexity: O(log n)
            Space complexity: O(1)
            Error handle: N/A
            Return: N/A
            Parameter: idx: an index in which to heapify from
            Precondition: An array full of numbers
        """
        small = idx
        l = 2*idx + 1
        r = 2*idx + 2

        if l < self.size and self.array[l][1] < self.array[small][1]:
            small = l
        if r < self.size and self.array[r][1] < self.array[small][1]:
            small = r
        if small != idx:
            self.pos[self.array[small][0]] = idx
            self.pos[self.array[idx][0]] = small
            self.swapNode(small, idx)
            self.heapify(small)

    def isIn(self, ver):
        """
            Checks to see if given vertex is in min-heap
            Time complexity: O(1)
            Space complexity: O(1)
            Error handle: N/A
            Return: True or False depending if vertex is in heap
            Parameter: vertex in which to check
            Precondition: A vertex in or not in heap
        """
        if self.pos[ver] < self.size:
            return True
        return False

    def decrease(self, ver, dist):
        """
            Decreases the vertex
            Time complexity: O(log n)
            Space complexity: O(1)
            Error handle: N/A
            Return: N/A
            Parameter: vertex: the position of the vertex in the graph, the new distance to update in heap
            Precondition: A valid heap
        """
        x = self.pos[ver]
        self.array[x][1] = dist

        while x > 0 and self.array[x][1] < self.array[(x-1) // 2][1]:
            self.pos[self.array[x][0]] = (x-1)//2
            self.pos[self.array[(x - 1) // 2][0]] = x
            self.swapNode(x, (x-1)//2)
            x = (x-1) //2

    def extract(self):
        """
            Extracts the minimum value in the heap
            Time complexity: O(log n)
            Space complexity: O(1)
            Error handle: If empty returns nothing
            Return: The minimum item in the heap
            Parameter: N/A
            Precondition: A valid min-heap
        """
        if self.isEmpty():
            return

        r = self.array[0]

        last = self.array[self.size - 1]
        self.array[0] = last

        self.pos[last[0]] = 0
        self.pos[r[0]] = self.size - 1

        self.size -= 1
        self.heapify(0)

        return r

    def isEmpty(self):
        """
            Check to see if the heap is empty
            Time complexity: O(1)
            Space complexity: O(1)
            Error handle: N/A
            Return: True or false depending if its in heap
            Parameter: N/A
            Precondition: A heap with a size
        """
        if self.size == 0:
            return True
        return False


    def swapNode(self, node1, node2):
        """
            Given two nodes and swaps them
            Time complexity: O(1)
            Space complexity: O(1)
            Error handle: N/A
            Return: N/A
            Parameter: node1: A given node in graph node2: another given node in the graph
            Precondition: Valid nodes in the graph
        """
        temp = self.array[node1]
        self.array[node1] = self.array[node2]
        self.array[node2] = temp

    def MinHeapNode(self, vec, dist):
        """
            Creates a node to put in the graph
            Time complexity: O(1)
            Space complexity: O(1)
            Error handle: N/A
            Return: The node to be added to the graph
            Parameter: The vertex to be added and distance of the edge
            Precondition: A valid distance and vertex
        """
        minNode = [vec, dist]
        return minNode

def printArr(dist, n, path):
    """
        Given a path, distance and target, returns the valid form to be returned
        Time complexity: O(1)
        Space complexity: O(path + distance)
        Error handle: N/A
        Return: The given path distance depending on if its valid or not
        Parameter: dist: the distance of the path, n: the end point of the path, path: The actual path
        Precondition: Values to be converted to the right format
    """
    if dist[n] == sys.maxsize:
        return [[], -1]
    else:
        integs = [int(x) for x in path[n].split(',')]
        return (integs, dist[n])


class Graph:
    def __init__(self):
        """
        Constructor for the class
        Time complexity: O(1)
        Space complexity: O(1)
        Error handle: N/A
        Return: N/A
        Parameter: N/A
        Precondition: N/A
        """
        self.graph = []
        self.max = 0
        self.graph2 = []

    def changeGraph(self):
        """
            Changes the size of the graph depending on how many values are in the filename_roads
            Time complexity: O(max)
            Space complexity: O(max)
            Error handle: N/A
            Return: N/A
            Parameter: N/A
            Precondition: A value for the size of the graph
        """
        self.graph = [None] * self.max

    def add(self, source, dest, weight):
        """
            Adds a edge to the graph, edge being destination and length
            Time complexity: O(1)
            Space complexity: O(1)
            Error handle: Given an apporiate value, will add to graph
            Return: N/A
            Parameter: source: The source/start of path, target: The end of the path, weight: length of the edge
            Precondition: A graph has been initiated
        """
        edge = [dest, weight]
        if self.graph[source] is not None:
            self.graph[source].append(edge)
        else:
            self.graph[source] = [edge]

    def buildGraph(self, filename_roads):
        """
            From a given file, will build the graph from a list of vertex to vertex and length
            Time complexity: O(E)
            Space complexity: O(E + W + spaces)
            Error handle: If the wrong file name will return error
            Return: N/A
            Parameter: filename_roads: the file to be read and implemented into a graph
            Precondition: A valid file
        """
        data_file = []
        try:
            data = open(filename_roads, 'r')
        except FileNotFoundError as fnf_error:
            print(fnf_error)
            return None
        else:
            for line in data:
                line = line.split(" ")
                data_file.append(line)
                if int(line[0]) > self.max and int(line[0]) > int(line[1]):
                    self.max = int(line[0])
                elif int(line[1]) > self.max and int(line[1]) > int(line[0]):
                    self.max = int(line[1])
        self.max += 1
        self.changeGraph()
        for item in data_file:
            self.add(int(item[0]), int(item[1]), float(item[2]))


    def quickestPath(self, source, target):
        """
            This function returns the quickest path possible given a source and target
            Time complexity: O(E log V)
            Space complexity: O(E + V)
            Error handle: Handle inappropriate values and graphs
            Return: Either [[], -1] or the path from source to target and distance
            Parameter: source: The source/start of path, target: The end of the path
            Precondition: Path parameters on the graph
        """
        num = self.max
        distance = []
        heap = Heap()
        for n in range(num):
            distance.append(sys.maxsize)
            heap.array.append(heap.MinHeapNode(n, distance[n]))
            heap.pos.append(n)

        heap.pos[source] = source
        distance[source] = 0
        heap.decrease(source, distance[source])

        heap.size = num
        path = [str(source)] * len(distance)
        while not heap.isEmpty():
            node = heap.extract()
            x = node[0]
            if x == target:
                return printArr(distance, target, path)
            if self.graph[x] is None:
                continue
            else:
                for c in self.graph[x]:
                    vec = c[0]
                    if heap.isIn(vec) and distance[x] != sys.maxsize:
                        if c[1] + distance[x] < distance[vec]:
                            distance[vec] = c[1] + distance[x]
                            path[vec] = str(path[x]) + "," + str(c[0])
                            heap.decrease(vec, distance[vec])
        return printArr(distance, target, path)


    def augmentGraph(self, filename_camera, filename_toll):
        """
            From a given file, will augment the graph such that the quickestSafePath can run
            Time complexity: O(V + E)
            Space complexity: O(E + V)
            Error handle: If the wrong file name will return error
            Return: N/A
            Parameter: filename_toll and filename_camera: the file to be read and implemented into a graph
            Precondition: A valid filenames
        """
        datas = []
        try:
            data = open(filename_toll, 'r')
        except FileNotFoundError as fnf_error:
            print(fnf_error)
            return None
        else:
            for line in data:
                datas.append(line.split(" "))
        for item in datas:
            for edge in self.graph[int(item[0])]:
                item[1] = item[1].replace("\n", "")
                if edge[0] == int(item[1]):
                    edge.append(True)
                    break
        self.cameras = []
        try:
            data = open(filename_camera, 'r')
        except FileNotFoundError as fnf_error:
            print(fnf_error)
            return None
        else:
            for line in data:
                item = line.split(" ")
                item = item[0]
                item.replace("\n", "")
                self.cameras.append(int(item))

    def quickestSafePath(self, source, target):
        """
            This function returns the quickest path possible given a list of toll rodes and cameras to avoid
            and a source and target
            Time complexity: O(E log V)
            Space complexity: O(E + V )
            Error handle: Handle inappropriate values and graphs
            Return: Either [[], -1] or the path from source to target and distance
            Parameter: source: The source vertex and target vertex
            Precondition: Path parameters on the graph
        """
        num = self.max
        distance = []
        heap = Heap()
        for n in range(num):
            if n not in self.cameras:
                distance.append(sys.maxsize)
                heap.array.append(heap.MinHeapNode(n, distance[n]))
                heap.pos.append(n)
            else:
                distance.append(-1)
                heap.array.append(heap.MinHeapNode(n, distance[n]))
                heap.pos.append(n)

        heap.pos[source] = source
        distance[source] = 0
        heap.decrease(source, distance[source])

        heap.size = num
        path = [str(source)] * len(distance)
        while not heap.isEmpty():
            node = heap.extract()
            x = node[0]
            if node[1] is -1:
                continue
            if x == target:
                return printArr(distance, target, path)
            if self.graph[x] is None:
                continue
            else:
                for c in self.graph[x]:
                    vec = c[0]
                    if len(c) >= 3:
                        continue
                    if heap.isIn(vec) and distance[x] != sys.maxsize:
                        if c[1] + distance[x] < distance[vec]:
                            distance[vec] = c[1] + distance[x]
                            path[vec] = str(path[x]) + "," + str(c[0])
                            heap.decrease(vec, distance[vec])
        return printArr(distance, target, path)

    def addService(self, filename_service):
        """
            From a given file, will create a new graph such that the quickestDetourPath can run
            Time complexity: O(nElogV) n being the size of the file
            Space complexity: O(E + V)
            Error handle: If the wrong file name will return error
            Return: N/A
            Parameter: filename_service: the file to be read and to create a new graph
            Precondition: A valid filename
        """
        self.graph2 = [None] * self.max
        try:
            data = open(filename_service, 'r')
        except FileNotFoundError as fnf_error:
            print(fnf_error)
            return None
        else:
            for line in data:
                item = line.replace("\n", "")
                item = int(item)
                for n in range(self.max):
                    if n == item:
                        continue
                    temp = self.quickestPath(n, item)
                    temp = list(temp)
                    if temp[1] == -1:
                        continue
                    if self.graph2[n] is None:
                        self.graph2[n] = [[temp[0][-1], temp[1]]]
                    else:
                        self.graph2[n].append([temp[0][-1], temp[1]])
        try:
            data = open(filename_service, 'r')
        except FileNotFoundError as fnf_error:
            print(fnf_error)
            return None
        else:
            for line in data:
                item = line.replace("\n", "")
                item = int(item)
                for n in range(self.max):
                    if n == item:
                        continue
                    temp = self.quickestPath(item, n)
                    temp = list(temp)
                    if temp[1] == -1:
                        continue
                    if self.graph2[item] is None:
                        self.graph2[item] = [[temp[0][-1], temp[1]]]
                    else:
                        self.graph2[item].append([temp[0][-1], temp[1]])

    def quickestDetourPath(self, source, target):
        """
            This function returns the quickest path possible given a list of detour vertices and a source and target
            Time complexity: O(E log V)
            Space complexity: O(E + V)
            Error handle: Handle inappropriate values and graphs
            Return: Either [[], -1] or the path from source to target and distance
            Parameter: source: The source vertex and target vertex
            Precondition: Path parameters on the graph
        """
        num = self.max
        distance = []
        heap = Heap()
        for n in range(num):
            distance.append(sys.maxsize)
            heap.array.append(heap.MinHeapNode(n, distance[n]))
            heap.pos.append(n)

        heap.pos[source] = source
        distance[source] = 0
        heap.decrease(source, distance[source])

        heap.size = num
        path = [str(source)] * len(distance)
        while not heap.isEmpty():
            node = heap.extract()
            x = node[0]
            if x == target:
                break
            if self.graph2[x] is None:
                continue
            else:
                for c in self.graph2[x]:
                    vec = c[0]
                    if c[1] == 0:
                        path[vec] = str(path[x])
                    if heap.isIn(vec) and distance[x] != sys.maxsize:
                        if c[1] + distance[x] < distance[vec]:
                            distance[vec] = c[1] + distance[x]
                            path[vec] = str(path[x]) + "," + str(c[0])
                            heap.decrease(vec, distance[vec])

        path = path[target].split(",")
        if len(path) == 1:
            return [[], -1]
        temp = self.quickestPath(source, int(path[1]))
        temp2 = self.quickestPath(int(path[1]), target)
        final = (temp[0] + temp2[0][1:], temp[1] + temp2[1])
        return final


def main(lines):
    print(lines)
    graph = Graph()
    graph_file = input("Enter the file name for the graph : ")
    camera_file = input("Enter the file name for the camera nodes : ")
    toll_file = input("Enter the file name for the toll nodes : ")
    service_file = input("Enter the file name for the service nodes : ")
    print(lines)
    source_node = input("Source Node: ")
    sink_node = input("Sink Node: ")
    print(lines)
    print("Quickest Path:")
    graph.buildGraph(graph_file)
    print(graph.quickestPath(source_node, sink_node))
    print(lines)
    print("Safe quickest path:")
    graph.augmentGraph(camera_file, toll_file)
    print(graph.quickestSafePath(source_node, sink_node))
    print(lines)
    print("Quickest detour path:")
    graph.addService(service_file)
    print(graph.quickestDetourPath(source_node, sink_node))
    print(lines)

if __name__ == '__main__':
    lines = "---------------------------------------------------------------------"
    main(lines)