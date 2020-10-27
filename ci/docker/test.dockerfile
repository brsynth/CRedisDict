ARG IMAGE
FROM ${IMAGE}

RUN conda update -n base -c defaults conda \
 && conda install -y -c conda-forge pyyaml

ARG HOME
WORKDIR ${HOME}/tests

ADD ci ci
ADD recipe recipe

RUN python ci/pytest/parse_recipe.py > ci/pytest/build_configs.txt
RUN for pkg in `cat ci/pytest/build_configs.txt` ; do \
      conda create -n test_$pkg $pkg ; \
      conda env update -n test_$pkg --file ci/pytest/environment.yml ; \
    done

ADD tests tests

ARG PKG
ADD ${PKG} tests/${PKG}

# run command into all environments created above
ENTRYPOINT ["conda", "env", "list", "|cut", "-d\" \"", "-f1|tail", "-n+4 |grep", "test_|xargs", "-L", "1", "-I", "env"]
