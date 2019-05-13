#!/usr/bin/env python

"""
Some quick filters.
TODO Add docstrings
TODO Add novel filters, make sure they're not just wrappers for scipy
"""
from scipy import signal 

"""
Create and return actual low pass filter with appropriate cutoff.
"""
def lowpass_filter(cutoff, sampling_frequency, order=5):
    nyquist_frequency = 0.5 * sampling_frequency
    divided_cutoff = cutoff / nyqust_frequency
    x, y = signal.butter(order, divided_cutoff, btype='low', analog=False)
    return x, y 

def butter_lowpass_filter(input_data, cutoff, sampling_frequency, order=5):
    x, y = lowpass_filter(cutoff, sampling_frequency, order=order)
    filtered_signal = signal.lfilter(x, y, input_data)
    return filtered_signal

def highpass_filter(cutoff, sampling_frequency, order=5):
    nyquist_frequency = 0.5*sampling_frequency
    divided_cutoff = cutoff / nyquist_frequency
    x, y = signal.butter(order, divided_cutoff, btype='high', analog=False)
    return x, y

def butter_highpass_filter(input_data, cutoff, sampling_frequency, order=5):
    x, y = highpass_filter(cutoff, sampling_frequency, order=order)
    filtered_signal = signal.lfilter(x, y, input_data)
    return filtered_signal

def bandpass_filter(cutoff, sampling_frequency, order=5):
    nyquist_frequency = 0.5*sampling_frequency
    divided_cutoff = cutoff / nyquist_frequency
    x, y = signal.butter(order, divided_cutoff, btype='band', analog=False)
    return x, y

def butter_bandpass_filter(input_data, cutoff, sampling_frequency, order=5):
    x, y = bandpass_filter(cutoff, sampling_frequency, order=order)
    filtered_signal = signal.lfilter(x, y, input_data)
    return filtered_signal
