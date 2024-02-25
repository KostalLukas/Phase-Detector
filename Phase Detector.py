# -*- coding: utf-8 -*-
"""
Phase Detector Simulation v1.0

Lukas Kostal, 23.2.2024, ICL
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as ss


# function to produce sinusoid waveform
def sin(t, f, phi=0):
    return np.sin(2 * np.pi * f * t + phi)

# function to produce sqaure waveform
def sqr(t, f, phi=0):
    return ss.square(2 * np.pi * f * t + phi, 0.5)


# initial and final time in s
ti = 0
tf = 2

# frequency and frequency difference in Hz
f = 2
f_delta = 0.16

# phase difference in radians
phi = 0

# sampling frequency and cutoff frequency in Hz
fs = 1000
fc = 2

# order of low pass filter
n = 1

# array of time
t = np.linspace(ti, tf, int(fs * (tf - ti)))

# input signal and reference signal
V1 = sin(t, f + f_delta, phi)
V2 = sqr(t, f)

# intermediate signal output from mixer
V3 = V1 * V2

# normalise cutoff frequency and generate low pass filter
fc = fc / (2 * fs)
a, b = ss.butter(n, fc, 'low')

# calculate output voltage and ideal average
Vout = ss.filtfilt(a, b, V3)
Vavg = np.mean(V3)

# plot subplots
fig, axs = plt.subplots(3, sharex=True)
fig.suptitle('Simulated Phase Detector')

axs[0].plot(t, V1, c='b')
axs[1].plot(t, V2, c='b')
axs[2].plot(t, V3, c='b')
axs[2].plot(t, Vout, c='r')
axs[2].axhline(Vavg, c='r', ls='--')

axs[1].set_ylabel('voltage (V)')
axs[2].set_xlabel('time (s)')

plt.savefig('plot.png', dpi=300, bbox_inches='tight')
plt.show()