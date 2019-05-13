#!/usr/bin/env python3

"""
Basic AM Demodulator using I/Q data. 
Turns I/Q data into a useful buffer, demodulates, 
goes to audio.

"""
import numpy as np
import math
import struct
import sys

# Max rate of deviation, in Hertz.
MAX_DEV = 200000 
# Input rate, also in Hertz.
INPUT_RATE = 256000

"""
Run basic demodulation framework. Do some error checking with data from 
previous runs and export each segment as playable audio.

    leftover_data : Byte buffer of previous data to use as needed.
    deviation : Max deviation ratio, scaled by input rate.
"""
def run_demod(leftover_data, deviation, carrier_table):
    # Pull data from standard input.
    data = sys.stdin.buffer.read(INPUT_RATE)

    # Error correction and odd/even checking.
    if not data:
        print ("No data received.")
        return 0
    # Add the sample from the last batch to even out the data.
    data = leftover_data + data
    # Account for short samples and odd bytes.
    if len(data) < 4:
	    leftover_data = data
    if len(data) % 2 == 1:
        remaining_data = data[-3:]
        data = data[:-1]
    else:
        remaining_data = data[-2:]

    # Work with the actual data!    
    
    num_samples = len(data) // 2
    # Get regularized phase angle.
    raw_iq = numpy.frombuffer(data, dtype=numpy.uint8)
    print(raw_iq)
    iq_offset = raw_iq - 127.5
    iq_shifted = iq_offset / 128.0
    iq_complex = iq_shifted.view(complex)
    phase_angle = numpy.angle(iq_complex)
    
    # TODO scale samples to amplitude
    # Turn into something we can play in sox.
    output_data = numpy.multiply(scaled_amplitude, 32767)
    output_stream = output_data.astype(int)


    # Output as raw 16-bit, 1 channel audio
    output_bits = struct.pack(('<%dh' % len(output_stream)), *output_stream)
    sys.stdout.buffer.write(output_bits)

"""
Kick off demodulation, keep a buffer for extra data as needed throughout.
"""
def main():
    # A byte-sized buffer for continuity signal-to-signal.
    leftover_data = b''
    deviation = 0.99 / (2 * numpy.pi * MAX_DEV / INPUT_RATE)
    # Run demodulation indefinitely. Ctrl+C should work to quit.
    while True:
        run_demod(leftover_data, deviation)

if __name__ == "__main__":
    main()
