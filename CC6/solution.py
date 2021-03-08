"""
Name:
Coding Challenge 6
CSE 331 Spring 2021
Professor Sebnem Onsay
"""

import queue

def gates_needed(departures, arrivals):
    """
    :param departures: A python list of floats containing departure times of flights at the airport
    :param arrivals: A python list of floats containing arrival times of flights at the airport
    :return: An integer that represents the max number of gates needed at any point during the day
    """
    maxgates = 0
    aindex = dindex = 0
    nextarrival = 0
    times = queue.SimpleQueue()

    while (dindex < (len(departures)) or aindex < (len(arrivals))):
        if (dindex < len(departures) and departures[dindex] < nextarrival):
            # Plane departed
            if (times.qsize() > maxgates and departures[dindex] != arrivals[aindex-1]):
                # New max (not touch and go)
                maxgates = times.qsize()
            times.get()
            dindex += 1
        else:
            # Plane arrived
            times.put(arrivals[aindex])
            aindex += 1
            if aindex < len(arrivals):
                nextarrival = arrivals[aindex]
            else:
                # Set to 1 second after the next day (1 past the max arrival time)
                nextarrival = 3600 * 24 + 1

    # Check if max was at the end of the day
    if times.qsize() > maxgates:
        maxgates = times.qsize()

    return maxgates
