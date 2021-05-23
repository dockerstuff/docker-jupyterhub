ARG BASE_IMAGE=chbrandt/gispy:gdal
FROM $BASE_IMAGE

MAINTAINER "Carlos H Brandt <carloshenriquebrandt.gmail>"

RUN apt-get update \
    && apt-get install -y npm nodejs \
    && apt-get clean

RUN npm install -g configurable-http-proxy

RUN python3 -m pip --no-cache-dir install jupyterlab jupyterhub

ARG UID=1000
ARG GID=100
ARG PASSWORD=123456
RUN useradd -m -d /home/user -u $UID -g $GID -s /bin/bash user \
    && su - user -c 'ln -s /mnt/data /home/user/data' \
    && echo "user:$PASSWORD" | chpasswd

RUN python3 -m pip install oauthenticator

RUN [ which pip ] || update-alternatives --install /usr/bin/pip pip /usr/bin/pip3 1

COPY ./jupyterhub.conf.d /jupyterhub.conf.d

VOLUME /mnt/data

EXPOSE 8000

CMD ["jupyterhub", "--config=/jupyterhub.conf.d/github_jupyter_config.py", "--port=8000"]
