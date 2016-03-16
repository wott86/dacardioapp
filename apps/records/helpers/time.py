def convert_time_to_milli(channel, date_obj):
    diff = float((date_obj - channel.start_date).total_seconds()) * 1000
    return diff if diff >= 0 else 0
