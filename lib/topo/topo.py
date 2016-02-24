from mininet.topo import Topo

from lib.util.read_graph import read_graph


class GraphTopo(Topo):

    def __init__(self, graph_name, max_queue_size=None, **params):

        # Initialize topo
        Topo.__init__(self, **params)

        # Host and link configuration
        # hconfig = {'cpu': cpu}
        # lconfig = {'bw': bw, 'delay': delay, 'max_queue_size': max_queue_size}

        # Read the graph from file
        path = 'data/' + graph_name + '.gr'
        g = read_graph(path)

        switches = {}

        # Traverse nodes and add hosts and switchs
        for node in g.nodes():
            host = self.addHost('h%d' % node)
            switch = self.addSwitch('s%d' % node)
            self.addLink(switch, host)
            switches[node] = switch

        for edge in g.edges():
            self.addLink(switches[edge[0]], switches[edge[1]])


class KLTopo(GraphTopo):

    def __init__(self, **params):
        GraphTopo.__init__(self, 'kl', **params)


class NSFTopo(GraphTopo):

    def __init__(self, **params):
        GraphTopo.__init__(self, 'nsf', **params)
