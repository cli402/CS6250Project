from mininet.net import Mininet
from mininet.node import CPULimitedHost, RemoteController
from mininet.link import TCLink
from mininet.cli import CLI
from mininet.util import custom, dumpNetConnections

from lib.topo.topo import KLTopo


# A temporary script to start the topology and CLI
def main():
    topo = KLTopo()
    host = custom(CPULimitedHost, cpu=.15)
    link = custom(TCLink, bw=10, delay='1ms', max_queue_size=200)
    net = Mininet(topo=topo, host=host, link=link, controller=RemoteController)
    net.start()
    dumpNetConnections(net)
    CLI(net)

if __name__ == "__main__":
    main()
