#!/usr/bin/env bash


SCRIPTPATH="$( cd "$(dirname "$0")" ; pwd -P )"
cd $SCRIPTPATH

cd ..

python -m unittest discover
