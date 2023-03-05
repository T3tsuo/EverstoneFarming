

def sum_seconds(date_format):
    time_map = {}
    time_string = ["hours", "minutes"]
    time_list = date_format.split(".")

    for i in range(len(time_list)):
        if time_list[i] != '':
            time_map[time_string[i]] = int(time_list[i])

    temp = 0
    if "hours" in time_map:
        temp += time_map["hours"] * 3600
    if "minutes" in time_map:
        temp += time_map["minutes"] * 60
    return temp
