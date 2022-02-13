from datetime import datetime


def isotoepoch(ts):

    return int(datetime.strptime(ts, "%Y-%m-%dT%H:%M:%S.%f").timestamp())


def epochtoiso(t):

    return datetime.utcfromtimestamp(t).isoformat()
