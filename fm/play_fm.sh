#!/bin/sh -x

# Run the RTL-SDR Framework with the python script, and then play audio.
rtl_sdr -f 88.9 -s 256k - | ./fm_demod.py -o | sox -t raw -r 256000 -b 16 -c 1 -L -e signed-integer - -d rate 32000
