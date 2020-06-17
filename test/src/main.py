
from sys import path as sys_path
sys_path.insert(0, '/home/src')
from CRedisDict import CRedisDict, wait_for_redis
from redis import StrictRedis
from logging import getLogger

def print_preINSTR(instr):
    print()
    print(instr)
    print('_' * len(instr))
    print("   * instruction ", end='')

def print_postINSTR(var, value):
    print("OK")
    print("   * result:")
    print("      + type  of", var, "= ", type(value))
    print("      + value of", var, "= ", value)
    print()

if __name__ == "__main__":

    logger = getLogger(__name__)
    logger.info('Started instance of CRedisDict')

    r = StrictRedis(host='db', port=6379, db=0, decode_responses=True)

    if not wait_for_redis(r, 30):
        logger.critical("Database is not reachable")
        exit()

    print_preINSTR("d1 = CRedisDict('d1', r)")
    d1 = CRedisDict('d1', r)
    print_postINSTR("d1", d1.dict())

    print_preINSTR("d1['A'] = 1")
    d1['A'] = 1
    print_postINSTR("d1['A']", d1['A'])

    print_preINSTR("d1['B'] = 'b'")
    d1['B'] = 'b'
    print_postINSTR("d1['B']", d1['B'])

    print_preINSTR("d1['C'] = {'a': 1, 'b': 2}")
    d1['C'] = {'a': 1, 'b': 2}
    print_postINSTR("d1['C']", d1['C'])

    print_preINSTR("d2 = CRedisDict('d2', r, d1)")
    d2 = CRedisDict('d2', r, d1)
    print_postINSTR("d2", d2.dict())

    print_preINSTR("d3 = d2")
    d3 = d2
    print_postINSTR("d3", d3.dict())
