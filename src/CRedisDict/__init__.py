"""
Created on June 16 2020

@author: Joan Hérisson
"""

from sys import stdout as sys_stdout
from time import time, sleep

def print_OK(time=-1):
    sys_stdout.write("\033[0;32m") # Green
    print(" OK", end = '', flush=True)
    sys_stdout.write("\033[0;0m") # Reset
    if time!=-1: print(" (%.2fs)" % time, end = '', flush=True)
    print()

def print_FAILED():
    sys_stdout.write("\033[1;31m") # Red
    print(" Failed")
    sys_stdout.write("\033[0;0m") # Reset
    print()

from redis import ConnectionError as redis_conn_error
def wait_for_redis(redis_conn, time_limit):
    redis_on = False
    start = time()
    end = time()
    print("Waiting for redis connection...", end = '', flush=True)
    while (not redis_on) and (end-start<time_limit) :
        try:
            redis_conn.ping()
            redis_on = True
        except redis_conn_error:
            print(".", end = '', flush=True)
            sleep(5)
            end = time()
    if redis_on: print_OK()
    else: print_FAILED()
    return redis_on

from .CRedisDict import CRedisDict


__all__ = ('CRedisDict', 'wait_for_redis')
