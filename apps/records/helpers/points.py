import math


def get_pow2(points):
    '''
    Returns max pox below number of points
    param: points can be an int (lenght) or a list (points)
    '''
    length = len(points) if not isinstance(points, int) else points
    return int(math.log(length, 2))


def get_max_pow2(points_sets):
    max_pow = None
    for pset in points_sets:
        pow2 = get_pow2(pset)
        if max_pow is None or max_pow > pow2:
            max_pow = pow2

    return max_pow
