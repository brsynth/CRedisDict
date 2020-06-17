
from sys import path as sys_path
sys_path.insert(0, '/home/src')
from CRedisDict import CRedisDict, wait_for_redis
from redis import StrictRedis
from logging import getLogger

def _print_preINSTR(instr):
    print()
    print(instr)
    print('_' * len(instr))
    print("   * instruction ", end='')

def _print_postINSTR(var, value):
    print("OK")
    print("   * result:")
    print("      + type  of", var, "= ", type(value))
    print("      + value of", var, "= ", value)
    print()

def test(instr):
    _print_preINSTR(instr)
    var,value = instr.replace(" ", "").split("=")
    exec(instr, globals())
    _print_postINSTR(var, value)

if __name__ == "__main__":

    logger = getLogger(__name__)
    logger.info('Started instance of CRedisDict')

    r = StrictRedis(host='db', port=6379, db=0, decode_responses=True)

    if not wait_for_redis(r, 30):
        logger.critical("Database is not reachable")
        exit()

    test("d1 = CRedisDict('d1', r)")
    test("d1['A'] = 1")
    test("d1['B'] = 'b'")
    test("d1['C'] = {'a': 1, 'b': 2}")
    test("d2 = CRedisDict('d2', r, d1)")
    test("d3 = d2")
    test("d4 = CRedisDict('d1', r, d3.dict())")
