import datetime
from django.utils import timezone


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


def convert_hour_to_milli(channel, interval_start, interval_end, offset=0):
    """
    convert_hour_to_milli

    This function converts given initial and end hour to milliseconds
    elapsed from channel initial time.

    :param channel: apps.records.models.Channel
    :param interval_start: str
    :param interval_end: str
    :returns (int, int)
    """
    hour, minute = interval_start.split(':')
    hour, minute = int(hour), int(minute)
    initial_time = (channel.start_date + datetime.timedelta(minutes=offset)).replace(hour=hour, minute=minute, tzinfo=timezone.get_fixed_timezone(offset))

    #if initial_time < channel.start_date:
    #    initial_time = initial_time + datetime.timedelta(days=1)

    hour, minute = interval_end.split(':')
    hour, minute = int(hour), int(minute)
    end_time = initial_time.replace(hour=hour, minute=minute)

    if initial_time > end_time:
        end_time = end_time + datetime.timedelta(days=1)

    return convert_time_to_milli(channel, initial_time), \
           convert_time_to_milli(channel, end_time)

