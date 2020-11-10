# CRedisDict

[![Anaconda-Server Badge](https://anaconda.org/brsynth/credisdict/badges/version.svg)](https://anaconda.org/brsynth/credisdict)
[![Anaconda-Server Badge](https://anaconda.org/brsynth/credisdict/badges/latest_release_date.svg)](https://anaconda.org/brsynth/credisdict)
![Test suite)](https://github.com/brsynth/credisdict/workflows/Test%20suite/badge.svg)

[![Anaconda-Server Badge](https://anaconda.org/brsynth/credisdict/badges/installer/conda.svg)](https://conda.anaconda.org/brsynth)
[![Anaconda-Server Badge](https://anaconda.org/brsynth/credisdict/badges/platforms.svg)](https://anaconda.org/brsynth/credisdict)

[![Anaconda-Server Badge](https://anaconda.org/brsynth/credisdict/badges/license.svg)](https://anaconda.org/brsynth/credisdict)

Data structure to implement a dictionary whose keys and values can be complex data (dict, list...) and are stored in a Redis database. The dictionary is initiated by copying each single (key,value) rather than using `hmset`. It takes more time at initialisation but it is faster each time a key is accessed.

## Prerequisites
* Python 3 with the following modules:
    * redis

## Install
### From Conda
```sh
[sudo] conda install -c brsynth credisdict
```

## Use
First, redis has to be installed and started:
```sh
[sudo] conda install -c conda-forge redis
[sudo] redis-server --daemonize yes
```

Then, the following Python code can be executed:
```python
from redis      import StrictRedis
from credisdict import CRedisDict, wait_for_redis

# Init the redis connection
redis = StrictRedis(host='localhost', port=6379, db=0, decode_responses=True)

# Wait for redis server
if not wait_for_redis(redis, 5):
    exit()

=======
```python
from credisdict import CRedisDict, wait_for_redis

redis = StrictRedis(host='localhost', port=6379, db=0, decode_responses=True)
if not wait_for_redis(redis, 10):
    exit()

d1 = CRedisDict('d1', redis)
d1['A'] = '1'
d1['B'] = 'b'
d1['C'] = {'a': 1, 'b': 2}
```
## Tests
Test can be run with the following commands:

### Natively
```bash
cd tests
pytest -v
```

# CI/CD
For further tests and development tools, a CI toolkit is provided in `ci` folder (see [ci/README.md](ci/README.md)).


## Authors

* **Joan Hérisson**


## Licence
CRedisDict is released under the MIT licence. See the LICENCE file for details.
