#! /usr/bin/env python

from scipy.io import wavfile
from scipy.interpolate import BarycentricInterpolator
import damage, recognize, utils

sample_rate, samples = wavfile.read('songs/hakuna_matata.wav')
samples = samples[5000000:5000050]

newsamples = samples.copy()
damage.zerofill(newsamples, 0.3)

matches = recognize.cheat(samples, newsamples)
x, y = utils.tovalidxy(newsamples, matches)
f = BarycentricInterpolator(x, y)
utils.repair(newsamples, matches, f)

import matplotlib.pyplot as plt

plt.title('Lagrange interpolation')
plt.xlabel('Frame')
plt.ylabel('Amplitude')
plt.plot(samples, label='real')
plt.plot(newsamples, label='interpolated')
plt.legend(loc='best')
plt.show()
