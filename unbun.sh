#!/bin/bash

BUILD=true;

for i in "$@"; do
  case $i in
    # -e=*|--extension=*)
    #   EXTENSION="${i#*=}"
    #   shift # past argument=value
    #   ;;
    -i|--install)
      INSTALL=true
      shift # past argument=value
      ;;
    --no-build)
      BUILD=false
      shift # past argument with no value
      ;;
    -*|--*)
      echo "Unknown option $i"
      exit 1
      ;;
    *)
      ;;
  esac
done

if [[ $INSTALL = true ]]; then
    cd static/tte/simile
    npm i
    cd ../../../
fi;

if [[ $BUILD = true ]]; then
    cd static/tte/simile
    npm run build
    cd ../../../
fi;

cd static/tte && unbun

cd ../../

sed -i 's/'${PWD##*/}'\/static\/tte\/img/img/g' static/tte/js/chunk-vendors.*.js

sed -i 's/("'${PWD##*/}'\/static\/tte\/img/("img/g' static/tte/js/app.*.js

sed -i 's/,\ "\/'${PWD##*/}'\/static\/tte\/service-worker.js"/,\ "'${PWD##*/}'\/static\/tte\/service-worker.js"/' static/tte/js/app.*.js

git apply controllers.patch
