#!/bin/bash

VERSION=$(cat VERSION.txt)
OUTFILE=out/canvas_api-${VERSION}.zip

if [[ -f "$OUTFILE" ]]; then
  rm -f "$OUTFILE"
fi

mkdir -p ${OUTFILE%/*}
zip -r "$OUTFILE" canvas_api/ -x "*__pycache__*"

echo "Built ${OUTFILE}."
