#!/usr/bin/env bash

cd "$(dirname "$0")"
PIPENV_VENV_IN_PROJECT=1 pipenv install
Rscript <(echo "renv::activate()")
Rscript <(echo "renv::restore()")
pipenv shell