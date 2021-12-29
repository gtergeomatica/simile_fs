cd static/tte/simile

npm i && npm run build

cd .. && unbun

cd ../../

sed -i 's/'${PWD##*/}'\/static\/tte\/img/img/g' static/tte/js/chunk-vendors.*.js

sed -i 's/("'${PWD##*/}'\/static\/tte\/img/("img/g' static/tte/js/app.*.js

sed -i 's/,\ "\/'${PWD##*/}'\/static\/tte\/service-worker.js"/,\ "'${PWD##*/}'\/static\/tte\/service-worker.js"/' static/tte/js/app.*.js

git apply controllers.patch