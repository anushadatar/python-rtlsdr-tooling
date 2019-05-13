#!/bin/sh -x

# Run the RTL-SDR Framework with the python script, and then play audio.
# Input intended center frequency of the given signal.
rtl_sdr -f $1 -s 256k - | ./am_demod.py -o | sox -t raw -r 256000 -b 16 -c 1 -L -e signed-integer - -d rate 32000
