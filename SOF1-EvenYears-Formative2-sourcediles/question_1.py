"""
Answer to question 1 for Formative 2
The equation would occasionally spit out a complex number, so to prevent an error from being thrown I had to check if it was complex first.
"""
import math

PARAMETERS200 = (4.99087, 42.5, 1.81)

def track_points(time, eventParameters):
    """Returns the point score for an event, given the time to complete said
    event and the tuple of event parameters (a,b,c) used to calculate the score

    Args:
        time (float): the athlete's time
        eventParameters (3-tuple): the tuple of three parameters (a,b,c) for
        the event
    
    Returns: the point score rounded down to the nearest whole integer
    """
    if len(eventParameters) != 3:
        raise ValueError("eventParameters requires 3 values")
    a, b, c = eventParameters
    points = a * (b - time) ** c
    if isinstance(points, complex) or points < 0:
        points = 0
    return math.floor(points)

def main():
    print(track_points(22.83, PARAMETERS200))

if __name__ == "__main__":
    main()