#!/bin/sh -x

# Run the RTL-SDR Framework with the python script, and then play audio.
rtl_sdr -f 1030K -s 256k - | ./am_demod.py -o | sox -t raw -r 256000 -b 16 -c 1 -L -e signed-integer - -d rate 32000
