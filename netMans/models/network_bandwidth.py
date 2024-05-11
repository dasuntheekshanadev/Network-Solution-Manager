# models/network_bandwidth.py

import psutil

def get_network_bandwidth():
    network_stats = psutil.net_io_counters(pernic=True)
    return network_stats
