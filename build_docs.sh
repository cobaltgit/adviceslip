#!/bin/bash

cd "$(dirname "$0")"
DOCS_DIR="./docsrc"
PROJECT_DIR="./src/adviceslip"

sphinx-apidoc -o "$DOCS_DIR" -f "$PROJECT_DIR"
cd "$DOCS_DIR"
if ! find -- "./_build" -prune -type d -empty | grep -q '^'; then
        make clean
fi
make github