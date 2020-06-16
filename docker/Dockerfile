ARG IMAGE
FROM ${IMAGE}

COPY requirements.txt .
# install requirements
RUN python3 -m pip install --upgrade pip \
 && python3 -m pip install -r requirements.txt

 RUN python3 -m pip install --user --upgrade setuptools wheel \
  && python3 -m pip install --user --upgrade twine

WORKDIR /home
RUN mkdir CRedisDict
COPY src/CRedisDict.py CRedisDict/__init__.py
COPY src/setup.py LICENSE README.md ./
RUN ls -lah CRedisDict
#COPY src src
#COPY docker/.pypirc .
