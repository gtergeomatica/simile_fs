# Simile Full Stack

## Install

`cd <path>/<to>/apps`

`git clone  --recursive git@github.com:gtergeomatica/simile_fs.git`

## Setup

`cd simile_fs/static/tte/simile`

`npm i && npm run build`

`cd .. && unbun`

`cd ../../`

`sed -i 's/'${PWD##*/}'\/static\/tte\/img/img/g' static/tte/js/chunk-vendors.*.js`

`sed -i 's/("'${PWD##*/}'\/static\/tte\/img/("img/g' static/tte/js/app.*.js`

`sed -i 's/,\ "\/'${PWD##*/}'\/static\/tte\/service-worker.js"/,\ "'${PWD##*/}'\/static\/tte\/service-worker.js"' static/tte/js/app.*.js`

## Run

`cd ..`

`py4web run apps`

## Regen

`rm simile_fs/static/tte/js/app.*.js`

e quindi ripetere i passi del parafrafo **Setup**.

## Main Doc

[unbundler](https://github.com/ali96343/unbundler): dove tutto è cominciato.
