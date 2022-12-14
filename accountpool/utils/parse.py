import re

def parse_redis_connection_string(connection_string):
    """
    parse a redis connection string, for example:
    redis://[password]@host:port
    rediss://[password]@host:port
    :param connection_string:
    :return:
    """
    result = re.match('rediss?:\/\/(.*?)@(.*?):(\d+)\/(\d+)', connection_string)
    return (
        result[2],
        int(result[3]),
        result[1] or None,
        result[4] or 0 if result else ('localhost', 6379, None),
    )
