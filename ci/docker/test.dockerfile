ARG IMAGE
FROM ${IMAGE}

RUN conda update -n base -c defaults conda \
 && conda install -y -c conda-forge pyyaml jinja2

# --clone build
# RUN conda env update -n test --file conda_env_test.yml

ARG HOME
WORKDIR ${HOME}/tests

ADD ci ci
ADD recipe recipe

RUN  python ci/pytest/parse_recipe.py
RUN  conda env create -n test --file ci/pytest/environment.yml

ADD tests tests

ARG PKG
ADD ${PKG} tests/${PKG}

ENTRYPOINT ["conda", "run", "-n", "test"]
