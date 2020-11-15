"""
Network class

Code written by Bryn Abyan Ghiffar
"""

from typing import TypeVar, Generic, List

T = TypeVar('T')

class NetworkNode(Generic[T]):

    def __init__(self, key : T, item : T) -> None:
        self.key = key
        self.item = item
        self.connections = []
        self.connections_count = 0
    
    def connect(self, other_node) -> None:
        """connects self to other node"""
        assert type(other_node) is NetworkNode, "target must be of type NetworkNode"
        assert not (other_node in self.connections), "node already connected"
    
        other_node.connections.append(self)
        self.connections.append(other_node)
        self.connections_count += 1
        other_node.connections_count += 1  

    def disconnect(self, other_node):
        """disconnects self from other node"""
        if len(self.connections) == 0:
            raise Exception("Node does not have connections")
    
        assert type(other_node) is NetworkNode, "target must be of type NetworkNode"
        found = False
        i1 = -1 # This is the index of the
                # to be deleted node in the self 
        try:
            # finding target_node in self.connections
            while not found:
                i1 += 1
                if self.connections[i1] is other_node:
                    found = True
        except IndexError:
            raise Exception("Node not found")

        # if other_node is found in self.connections,
        # then self should also be found in
        # other_node.connections
        found = False
        i2 = -1 # This is the index of self
                # in the to be deleted node
        # finding self in target_node.connections
        while not found:
            i2 += 1
            if other_node.connections[i2] is self:
                found = True
        del(self.connections[i1]) # removing connection
                                    # from self
        del(other_node.connections[i2]) # removing connection
                                            # from target node
        other_node.connections_count -= 1
        self.connections_count -= 1


class Network(Generic[T]):

    def __init__(self) -> None:
        self.nodes = []
    
    def dfs_aux(self, current : NetworkNode, key : T, visited : List[NetworkNode]) -> NetworkNode:
        if current.key == key:
            return current
        else:
            visited.append(current)
            to_visit = [node for node in current.connections if node not in visited]
            for node in to_visit:
                findings = self.dfs_aux(node, key, visited)
                if findings is not None:
                    return findings
    
    def dfs(self, key : T) -> NetworkNode:
        assert len(self.nodes) > 0, "Network must have nodes"
        findings = self.dfs_aux(self.nodes[0], key, [])
        if findings is None:
            raise Exception("key not found")
        return findings
    
    def __setitem__(self, key : T, item : T) -> None:
        node = self.dfs(key)
        node.item = item

    def __getitem__(self, key : T) -> None:
        return self.dfs(key).item
    
    def load_from_matrix(self, matrix) -> None:
        """
        creates a Network based on the input
        adjacency matrix.

        Note : This Network implementation
        is non-directional as well as non-weighted.
        Therefore, when taking in the adjacency matrix
        the graph only looks at the top right triangle
        of the adjacency matrix.
        """
        dim = len(matrix)
        self.nodes = [NetworkNode(i, None) for i in range(dim)]
        for i in range(dim):
            for j in range(i + 1, dim):
                if matrix[i][j] == 1:
                    self.nodes[i].connect(self.nodes[j])



if __name__ == '__main__':
    mat = [ [0, 1, 1, 0, 0],
            [1, 0, 0, 1, 1],
            [1, 0, 0, 0, 0],
            [0, 1, 0, 0, 0],
            [0, 1, 0, 0, 0]]
    my_graph = Network()
    my_graph.load_from_matrix(mat)
    my_graph[0] = 4
    print(my_graph[4])