from networkx import Graph

def read_graph(path):
    # Error object to be used if parsing fails
    error = IOError("Format of file %s is illegal" % path)

    with open(path) as graph_file:
        g = Graph()

        # Read the first line for number of nodes and number of edges
        nv, ne = read_line(graph_file.readline())

        # Traverse all lines
        for line in graph_file.readlines():
            n1, n2 = read_line(line)

            # Check whether the nodes are in a legal range
            if (n1 > nv or n1 < 1 or n2 > nv or n2 < 1):
                raise error
            g.add_edge(n1, n2)

        # Check the number of edges is correct
        if len(g.edges()) != ne:
            raise error

        return g


def read_line(line):
    strs =  line[:-1].split(' ')
    return (int(strs[0]), int(strs[1]))
