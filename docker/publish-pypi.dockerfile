ARG IMAGE
FROM ${IMAGE}

# RUN apt-get update
 # \
 # && apt-get install -y \
 #      gcc \
 #      musl-dev libffi-dev libressl-dev

ARG FILE
COPY ${FILE}.req .
# install requirements
RUN python3 -m pip install --upgrade pip \
 && python3 -m pip install --no-cache-dir --user --upgrade setuptools wheel --no-warn-script-location \
 && python3 -m pip install --no-cache-dir --user --upgrade -r ${FILE}.req

ARG HOME
WORKDIR ${HOME}
