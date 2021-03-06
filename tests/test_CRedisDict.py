"""
Created on June 17 2020

@author: Joan Hérisson
"""

from unittest   import TestCase
from credisdict import CRedisDict, wait_for_redis
from redis      import StrictRedis


# Cette classe est un groupe de tests. Son nom DOIT commencer
# par 'Test' et la classe DOIT hériter de unittest.TestCase.
class Test_CRedisDict(TestCase):

    def setUp(self):
        self.redis = StrictRedis(host='localhost', port=6379, db=0, decode_responses=True)
        if not wait_for_redis(self.redis, 10):
            exit()
        self.redis.flushall()

    # init(redis) + dict()
    def test_initEmpty(self):
        self.redis.flushall()
        d = CRedisDict('d', self.redis)
        self.assertEqual(d.dict(), {})

    def test_initFromCRedisDict(self):
        self.redis.flushall()
        d1 = CRedisDict('d1', self.redis)
        d1['A'] = '1'
        d1['B'] = 'b'
        d1['C'] = {'a': 1, 'b': 2}
        d2 = CRedisDict('d2', self.redis, d1)
        self.assertEqual(d1.dict(), d2.dict())

    def test_initFromDict(self):
        self.redis.flushall()
        d1 = {}
        d1['A'] = '1'
        d1['B'] = 'b'
        d1['C'] = {'a': 1, 'b': 2}
        d2 = CRedisDict('d2', self.redis, d1)
        self.assertEqual(d2.dict(), d1)

    # keys()
    def test_keys(self):
        self.redis.flushall()
        d1 = CRedisDict('d1', self.redis)
        d1['A'] = '1'
        d1['B'] = 'b'
        d1['C'] = {'a': 1, 'b': 2}
        self.assertEqual(d1.keys(), ['A', 'B', 'C'])

    # exists()
    def test_exists(self):
        self.redis.flushall()
        d1 = CRedisDict('d1', self.redis)
        d1['A'] = '1'
        d1['B'] = 'b'
        d1['C'] = {'a': 1, 'b': 2}
        self.assertEqual(CRedisDict.exists(self.redis, 'd1'), True)
        self.assertEqual(CRedisDict.exists(self.redis, 'd2'), False)

    # len()
    def test_len(self):
        self.redis.flushall()
        d1 = CRedisDict('d1', self.redis)
        d1['A'] = '1'
        d1['B'] = 'b'
        d1['C'] = {'a': 1, 'b': 2}
        self.assertEqual(len(d1), 3)
        d2 = CRedisDict('d2', self.redis)
        self.assertEqual(len(d2), 0)

    # is_empty
    def test_empty(self):
        self.redis.flushall()
        d1 = CRedisDict('d1', self.redis)
        d1['A'] = '1'
        d1['B'] = 'b'
        d1['C'] = {'a': 1, 'b': 2}
        self.assertEqual(d1.is_empty(), False)
        d2 = CRedisDict('d2', self.redis)
        self.assertEqual(d2.is_empty(), True)

    # update()
    def test_update(self):
        self.redis.flushall()
        d1 = {}
        d1['A'] = '1'
        d1['B'] = 'b'
        d1['C'] = {'a': 1, 'b': 2}
        d1_r = CRedisDict('d1', self.redis, d1)
        d2 = {}
        d2['D'] = '4'
        d2['E'] = 'e'
        d2['F'] = {'d': 4, 'e': 5}
        d2_r = CRedisDict('d2', self.redis, d2)
        d2_r.update(d1_r)
        d2.update(d1)
        self.assertEqual(d2_r.dict(), d2)

    def test_addInt(self):
        self.redis.flushall()
        d = CRedisDict('d', self.redis)
        d['A'] = 1
        self.assertEqual(d['A'], 1)

    def test_addStr(self):
        self.redis.flushall()
        d = CRedisDict('d', self.redis)
        d['B'] = 'b'
        self.assertEqual(d['B'], 'b')

    def test_addDict(self):
        self.redis.flushall()
        d = CRedisDict('d', self.redis)
        d['C'] = {'a': 1, 'b': 2}
        self.assertEqual(d['C'], {'a': 1, 'b': 2})

    def test_copyCRedisDict(self):
        self.redis.flushall()
        d1 = CRedisDict('d1', self.redis)
        d1['A'] = '1'
        d1['B'] = 'b'
        d1['C'] = {'a': 1, 'b': 2}
        d2 = d1
        self.assertEqual(d1.dict(), d2.dict())

    def test_copyDict(self):
        self.redis.flushall()
        d1 = {}
        d1['A'] = '1'
        d1['B'] = 'b'
        d1['C'] = {'a': 1, 'b': 2}
        d2 = CRedisDict('d2', self.redis)
        d2.copy(d1)
        self.assertEqual(d2.dict(), d1)

    def test_equal(self):
        self.redis.flushall()
        d1 = {}
        d1['A'] = '1'
        d1['B'] = 'b'
        d1['C'] = {'a': 1, 'b': 2}
        d2 = CRedisDict('d2', self.redis, d1)
        self.assertEqual(d2.dict(), d1)
