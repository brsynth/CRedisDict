# CRedisDict

[![Anaconda-Server Badge](https://anaconda.org/brsynth/credisdict/badges/latest_release_date.svg)](https://anaconda.org/brsynth/credisdict)
[![Anaconda-Server Badge](https://anaconda.org/brsynth/credisdict/badges/version.svg)](https://anaconda.org/brsynth/credisdict)
![Test suite)](https://github.com/brsynth/credisdict/workflows/Test%20suite/badge.svg)

Data structure to implement a dictionary whose keys and values can complex data (dict, list...) and are stored in a Redis database. The dictionary is initiated by copying each single (key,value) rather than using `hmset`. It takes more time at initialisation but it is faster each time a key is accessed.

## Prerequisites

* Python 3 with the following modules:
    * redis

## Install
### From Conda
```sh
[sudo] conda install -c brsynth credisdict
```

## Use
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
### In Docker
```bash
cd tests
./test-in-docker.sh
```

## CI
The folder `ci` is dedicated to continuous integration. From there, multiple steps can be processed.
### Full publishing cycle
`conda-doAll-indocker.sh`: process into all ci steps for publishing (build-test-convert).
### Clean
`conda-clean_env-indocker.sh`: clean the conda environment
### Build
`conda-build-indocker.sh`: build the conda environment (based on `recipe/meta.yml`) needed to run tests
### Test
`conda-test-indocker.sh`: run tests from conda package archive(s) built in the `build` step
### Convert
`conda-convert-indocker.sh`: run tests from conda package archive(s) built in the `build` step
### Publish
`conda-publish-indocker.sh`: publish package files from conda package archive(s) built and converted in the previous steps


## Authors

* **Joan Hérisson**


## Licence
CRedisDict is released under the MIT licence. See the LICENCE file for details.
