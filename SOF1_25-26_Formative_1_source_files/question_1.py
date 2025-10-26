def seconds_to_time(time):
    """Returns a string in the format "hh:mm:ss" from a time in seconds

    Args:
        time (int): time in seconds
    
    Returns:
        A string in the format "hh:mm:ss"
    """
    hh = time//3600
    mm = (time%3600)//60
    ss = (time%3600)%60
    if time > 359999 or time < 0:
        return None
    elif time >= 3600:
        return f"{hh:0>2}:{mm:0>2}:{ss:0>2}"
    else:
        return f"{mm:0>2}:{ss:0>2}"
