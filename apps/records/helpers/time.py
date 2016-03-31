TIME_MULTIPLIER = {
    'minutes': 60000,
    'hours': 3600000
}


def convert_time_to_milli(channel, date_obj):
    """
    convert_time_to_milli

    :param channel: apps.records.models.Channel
    :param date_obj: datetime.datetime
    """
    diff = float((date_obj - channel.start_date).total_seconds()) * 1000
    return diff if diff >= 0 else 0
