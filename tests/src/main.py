
from sys import path as sys_path
sys_path.insert(0, '/home/src')
from CRedisDict import CRedisDict, wait_for_redis
from redis import StrictRedis
from logging import getLogger

if __name__ == "__main__":

    logger = getLogger(__name__)
    logger.info('Started instance of CRedisDict')

    r = StrictRedis(host='db', port=6379, db=0, decode_responses=True)

    if not wait_for_redis(r, 30):
        logger.critical("Database is not reachable")
        exit()

    d = CRedisDict('test', r)
    d['A'] = 1
    d['B'] = 'b'
    d['C'] = {'a': 1, 'b': 2}

    print(d.dict())
