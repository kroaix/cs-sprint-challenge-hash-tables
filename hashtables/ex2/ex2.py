#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # Your code here
    cache = {}
    route = []

    for ticket in tickets:
        cache[ticket.source] = ticket.destination
        
    route.append(cache["NONE"])
    start = cache["NONE"]

    while start != "NONE":
        next_destination = cache[start]
        route.append(next_destination)
        start = next_destination

    return route
