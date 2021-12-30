FROM ubuntu:20.04

ARG user=py4web
ARG password=none
ARG DEBIAN_FRONTEND=noninteractive

RUN apt update && apt install -y git python3 python3-pip memcached

RUN service memcached restart

RUN groupadd -r $user && useradd -m -r -g $user $user

RUN python3 -m pip install -U py4web==1.20210906.1

USER $user

RUN cd /home/$user/ && py4web setup --yes apps

RUN cd /home/$user/ && \
    if [ "$password" = "none" ]; then echo "no admin"; else py4web set_password < "$password"; fi

USER root

RUN apt-get update && apt-get upgrade -y && \
    apt-get install -y nodejs \
    npm git

RUN cd /home/$user/apps/ && mkdir simile_fs

COPY . /home/$user/apps/simile_fs

RUN git clone https://github.com/Franc-Brs/unbundler.git && cd /unbundler && cp unbun /bin && chmod +x /bin/unbun

RUN pip install bs4 jsbeautifier cssbeautifier lxml

RUN cd /home/$user/apps/simile_fs && bash unbun.sh

USER $user

EXPOSE 8000

WORKDIR /home/$user/

CMD py4web run --password_file password.txt --host 0.0.0.0 --port 8000 apps
