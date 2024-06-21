#!/bin/bash

set -e
cd "${0%/*}" || exit 1;   # Go to the script location

if test ! -f config-sat-1.sif
then
    echo "Compiling linear-complex."
    cd src
    apptainer build ../config-sat-1.sif config-sat-1.def
else
    echo "linear-complex already compiled."
fi
