# AM Demodulation
This directory contains code to decode AM (amplitude modulation) signals using an RTL-SDR module.
To run it, call the [bash script](https://github.com/anushadatar/python-rtlsdr-tooling/blob/master/am/play_am.sh) that will collect IQ data from the receiver using the [rtl-sdr](https://osmocom.org/projects/rtl-sdr/wiki/Rtl-sdr) command line tool, use the [python script](https://github.com/anushadatar/python-rtlsdr-tooling/blob/master/am/am_demod.py) to run the code, and  [sox](http://sox.sourceforge.net/) to play back decoded sounds.
