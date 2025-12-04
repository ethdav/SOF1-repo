import math

PARAMETERS200 = (4.99087, 42.5, 1.81)

def track_points(time, eventParameters):
    """Returns the point score for an event, given the time to complete said
    event and the tuple of event parameters (a,b,c) used to calculate the score

    Args:
        time (float): the athlete's time
        eventParameters (3-tuple): the tuple of three parameters (a,b,c) for
        the event
    
    Returns: the rounded down point score
    """
    if len(eventParameters) != 3:
        raise ValueError("eventParameters requires 3 values")
    
    points = eventParameters[0]*(eventParameters[1] - time)**eventParameters[2]
    return math.floor(points)

def main():
    print(track_points(22.83, PARAMETERS200))

if __name__ == "__main__":
    main()