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

d1 = CRedisDict('d1', redis)
d1['A'] = '1'
d1['B'] = 'b'
d1['C'] = {'a': 1, 'b': 2}
```
## Tests
Test can be run with the following commands:
```bash
cd tests
pytest -v
```

## CI
The `ci/` folder is dedicated to continuous integration. From there, `check` and `test` steps can be processed into Docker containers. In addition, the full `conda` cycle (`build`, `test`, `convert` and `publish`) can be processed. Different commands are described below and have to be run from  `ci/` folder.
### Check in docker
`check-indocker.sh`: run `flake` and `bandit` across sources and `tests/` scripts.
### Test in docker
`pytest-indocker.sh`: run `pytest` into `tests` folder. Has to be used to debug since is much faster than `conda` process.
### Conda
#### Full cycle (build-test-convert-publish)
`conda-doAll-indocker.sh`: process into all ci steps from building to publishing. Publishing secrets ANACONDA_USER and ANACONDA_TOKEN have to be set in `ci/.secrets`.
#### Clean
`docker/scripts/conda-clean_env-indocker.sh`: clean the conda environment
#### Build
`docker/scripts/conda-build-indocker.sh`: build the conda environment (based on `recipe/meta.yml`) needed to run tests
#### Test
`docker/scripts/conda-test-indocker.sh`: run tests from conda package archive(s) built in the `build` step
#### Convert
`docker/scripts/conda-convert-indocker.sh`: run tests from conda package archive(s) built in the `build` step
#### Publish
`docker/scripts/conda-publish-indocker.sh`: publish package files from conda package archive(s) built and converted in the previous steps. Publishing secrets ANACONDA_USER and ANACONDA_TOKEN have to be set in `ci/.secrets`.


## Authors

* **Joan Hérisson**


## Licence
CRedisDict is released under the MIT licence. See the LICENCE file for details.
