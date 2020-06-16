# CRedisDict

Data structure to implement a dictionary whose keys and values can complex data (dict, list...) and are stored in a Redis database. The dictionary is initiated by copying each single (key,value) rather than using `hmset`. It takes more time at initialisation but it is faster each time a key is accessed.

## Prerequisites

* Python 3 with the following modules:
    * redis
    * json


## Authors

* **Joan Hérisson**


## Licence
CRedisDict is released under the MIT licence. See the LICENCE file for details.
