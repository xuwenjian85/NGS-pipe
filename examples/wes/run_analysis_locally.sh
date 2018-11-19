#!/bin/bash

unset DISPLAY
snakemake -j 32 -s SRP051153.snake --configfile config.json -p
