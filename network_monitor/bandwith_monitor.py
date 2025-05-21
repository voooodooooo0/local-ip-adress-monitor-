# bandwidth_monitor.py
import psutil
import time

def get_bandwidth():
    net1 = psutil.net_io_counters()
    time.sleep(1)  # measure over 1 second
    net2 = psutil.net_io_counters()

    sent = (net2.bytes_sent - net1.bytes_sent) * 8 / 1e9  # in Gigabits
    recv = (net2.bytes_recv - net1.bytes_recv) * 8 / 1e9
    return sent, recv
