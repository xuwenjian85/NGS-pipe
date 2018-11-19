#!/bin/bash

unset DISPLAY
snakemake -j 32 -s SRP051153-gatk.snake --configfile config.json -p
