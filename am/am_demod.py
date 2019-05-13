#!/usr/bin/env python3
"""
TODO add documentation!
TODO Sometimes this works and sometimes the disk just beeps loudly. Track down the 
TODO Add significantly more filtering + input control so that this can be used in not hypercontrolled environments. 
"""


import cmath
import math
import numpy as np
import struct
import sys
import time

# Center frequency. TODO Make this auto-update.
CENTER_FREQUENCY = 1030000
INPUT_RATE = 256000
STEP_SIZE =  2500

def run_demod(carrier_frequencies):
    input_data = sys.stdin.buffer.read(INPUT_RATE // 5)
    if not input_data:
        print("No data received.")
        return 0;
    input_data = remaining_data + data
    time_base = time.time()
    # Check on odd bytes and then convert to complex.
    if len(data) % 2 == 1:
        remaining_data = data[-1:]
        data = data[:-1]
    iq = numpy.frombuffer(data, dtype=numpy.uint8)
    iq -= 127.5
    iq /= 128.0
    iq = iq.view(complex)    
    carrier = carrier_frequencies[0:len(iq)]
    ifsamples = iqsamples * carrier
    output_raw = numpy.absolute(ifsamples)[1:]
    output_raw /= strength * 4
    output = numpy.clip(output, -0.999, +0.999)

    output = numpy.multiply(output, 32767) # 16-bit WAV
    output_stream = output.astype(int)	
    output_bits = struct.pack('<%dh' % len(output_stream), *output_stream)
    sys.stdout.buffer.write(output_bits)

def main():
    leftover_data = b''
    while True:
        # From sdr library methodology. Note that the frequency and input
        # rate need to be a multiple of the step size for this to work.
        freq = CENTER_FREQUENCY // INPUT_RATE
        carrier_frequencies = []
        for i in range(0, INPUT_RATE//5):
            carrier_frequencies = [cmath.exp(0-1j) * 2 * math.pi * freq * i]
        carrier_frequencies = np.array(carrier_frequencies)
        run_demod(carrier_frequencies)

if __name__ == "__main__":
    main()
