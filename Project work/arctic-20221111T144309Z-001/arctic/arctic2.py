#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 10 15:18:39 2022

@author: paddy
"""

import librosa as lb
import matplotlib.pyplot as plt
import numpy as np
import scipy.signal as sg
import scipy as sp
from scipy import fft

# load file from arctic dataset
path = 'F:\\Python@IITMandi\\Programming practicum project work\\arctic-20221111T144309Z-001\\arctic\\'
wavfile = 'arctic_a0431.wav'
# channel 0 is speech, channel 1 is EGG
y,fs = lb.load(path + wavfile,sr=8000,mono=False)
s = y[0] # speech
e = y[1] # EGG

# visualising the speech signal
plt.figure()
plt.plot(s)
plt.title('Entire speech')

#framing
winsize=240
sframes = lb.util.frame(s,frame_length=960,hop_length=450)
eframes = lb.util.frame(e,frame_length=960,hop_length=450)

# select a frame
sel = 10
sig = sframes[:,sel]
egg = eframes[:,sel]

# plot them
plt.figure()
plt.plot(sframes[:,sel])
plt.title('Speech')
plt.figure()
plt.plot(eframes[:,sel])
plt.title('EGG')
# plt.show()

# spectra of speech and EGG
NFFT = fft.next_fast_len(winsize,True)
freqAxis = fft.fftfreq(NFFT,d=1/fs)
Sig = np.abs(sp.fft.fft(sig,n=NFFT))
Sig = Sig[0:NFFT//2]
freqAxis = freqAxis[0:NFFT//2]

plt.figure()
plt.plot(freqAxis,Sig)
plt.grid(True)
plt.xlabel('Freq in Hz')
plt.ylabel('Mag spectrum')
plt.title('speech sprectrum')
# plt.show()

NFFT = fft.next_fast_len(winsize,True)
freqAxis = fft.fftfreq(NFFT,d=1/fs)
Egg = np.abs(sp.fft.fft(egg,n=NFFT))
Egg = Egg[0:NFFT//2]
freqAxis = freqAxis[0:NFFT//2]

plt.figure()
plt.plot(freqAxis,Egg)
plt.grid(True)
plt.xlabel('Freq in Hz')
plt.ylabel('Mag spectrum')
plt.title('EGG spectrum')
# plt.show()

# get first diff of EGG
eggDiff = np.diff(egg)
plt.figure()
plt.plot(-eggDiff)
plt.show()











