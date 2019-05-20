# FM Demodulation
This directory contains code to decode FM (frequency modulation) signals using an RTL-SDR module.
To run it, call the [bash script](https://github.com/anushadatar/python-rtlsdr-tooling/blob/master/fm/play_fm.sh) that will collect IQ data from the receiver using the [rtl-sdr](https://osmocom.org/projects/rtl-sdr/wiki/Rtl-sdr) command line tool, use the [python script](https://github.com/anushadatar/python-rtlsdr-tooling/blob/master/fm/fm_demod.py) to run the code, and  [sox](http://sox.sourceforge.net/) to play back decoded sounds.
