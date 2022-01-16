# Simile Full Stack

## Install

`cd <path>/<to>/apps`

`git clone  --recursive git@github.com:gtergeomatica/simile_fs.git`

## Setup

`cd simile_fs/static/tte/simile`

`npm i && npm run build`

n.b per unbun è necessario aver installato: `bs4 jsbeautifier cssbeautifier lxml`

`cd .. && unbun`

`cd ../../`

`sed -i 's/'${PWD##*/}'\/static\/tte\/img/img/g' static/tte/js/chunk-vendors.*.js`

`sed -i 's/("'${PWD##*/}'\/static\/tte\/img/("img/g' static/tte/js/app.*.js`

`sed -i 's/,\ "\/'${PWD##*/}'\/static\/tte\/service-worker.js"/,\ "'${PWD##*/}'\/static\/tte\/service-worker.js"/' static/tte/js/app.*.js`

## Run

`cd ../../`

`py4web run apps`

## Regen

`rm simile_fs/static/tte/js/app.*.js`

e quindi ripetere i passi del parafrafo **Setup**.

## Main Doc

[unbundler](https://github.com/ali96343/unbundler): dove tutto è cominciato.

## Utilizzo Docker 

Clonare il repository:
`git clone  --recursive git@github.com:gtergeomatica/simile_fs.git`

Costruire l'immagine e tirare su il container con l'orchestratore:
`docker-compose up -d`

Attualmente per dato che non c'è condivisione di volumi, se si vuole cambiare qualcosa è necessario o entrare nel container o cambiare qualcosa nel repository e ripetere il processo per costruire l'immagine.
