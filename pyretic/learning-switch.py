#!/usr/bin/python

from pyretic.lib.corelib import *
from pyretic.lib.std import *
from pyretic.lib.query import packets

# A learning switch based on pyretic


# Helper functions
def get_src_mac(pkt):
    """ Returns the source MAC address of the packet. """
    return pkt['srcmac']


def get_dst_mac(pkt):
    """ Returns the destination MAC address of the packet. """
    return pkt['dstmac']


def get_switch(pkt):
    """ Returns the switch of the packet. """
    return pkt['switch']


def get_port(pkt):
    """ Returns the port the packet came in on. """
    return pkt['port']


# Learning switch
class LearningSwitch(DynamicPolicy):

    def __init__(self):
        DynamicPolicy.__init__(self)

        # Initialize the forwarding table
        self.fwd_table = {}

        # Use flooding at first
        self.flood = flood()

        # Get the first packet from each new MAC address on a switch
        new_pkts = packets(1, ['srcmac', 'switch'])
        new_pkts.register_callback(self.learn_route)
        self.query = new_pkts

        # Initialize the policy
        self.push_rules()

    def learn_route(self, pkt):
        switch = get_switch(pkt)
        src_mac = get_src_mac(pkt)
        port = get_port(pkt)
        if switch not in self.fwd_table:
            self.fwd_table[switch] = {}
        self.fwd_table[switch][src_mac] = port
        self.print_switch_tables()
        self.push_rules()

    def push_rules(self):
        new_policy = None
        not_flood_pkts = None

        for entry in self.fwd_table.keys():
            for fwd_rule in self.fwd_table[entry].keys():
                if new_policy == None:
                    new_policy = (match(switch=int(entry), dstmac=fwd_rule) >>
                                  fwd(self.fwd_table[entry][fwd_rule]))
                else:
                    new_policy += (match(switch=int(entry), dstmac=fwd_rule) >>
                                   fwd(self.fwd_table[entry][fwd_rule]))

                if not_flood_pkts == None:
                    not_flood_pkts = (
                        match(switch=int(entry), dstmac=fwd_rule))
                else:
                    not_flood_pkts |= (
                        match(switch=int(entry), dstmac=fwd_rule))

        if new_policy == None:
            self.policy = self.flood + self.query
        else:
            self.policy = if_(not_flood_pkts, new_policy,
                              self.flood) + self.query

    def print_switch_tables(self):
        for entry in self.fwd_table.keys():
            print "Switch " + str(entry)
            for fwd_rule in self.fwd_table[entry].keys():
                print "   %s : %s" % (str(fwd_rule), str(self.fwd_table[entry][fwd_rule]))
        print "----------------"


def main():
    return LearningSwitch()
