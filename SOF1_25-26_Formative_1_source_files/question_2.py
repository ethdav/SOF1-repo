def time_to_seconds(time):
    """Converts a string in the format "hh:mm:ss" into a time in seconds

    Args:
        time (str): a string in the formtat "hh:mm:ss" or "mm:ss"

    Returns:
        An integer representing time in seconds
    """
    time_list = time.split(":")
    time_list.reverse()
    if len(time_list) < 2 or len(time_list) > 3:
        return None
    for index in range(len(time_list)):
        if len(time_list[index]) != 2:
            return None
        time_list[index] = int(time_list[index])
        if time_list[index] < 0:
            return None
        elif index < 2 and time_list[index] >= 60:
            return None
        elif index == 2 and time_list[index] >= 100:
            return None
    int_time = time_list[0] + time_list[1]*60
    if len(time_list) == 3:
        int_time+=time_list[2]*3600
    return int_time
