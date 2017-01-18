import math
import numpy
import pyaudio


def sine(frequency, length, rate):
    length = int(length * rate)
    factor = float(frequency) * (math.pi * 2) / rate
    return numpy.sin(numpy.arange(length) * factor)


def play_tone(stream, frequency=10000, length=50, rate=44100):
    chunks = []
    signal=sine(frequency, length, rate)
    stereo_signal=numpy.zeros([len(signal),2])
    stereo_signal[:, 1]=signal[:] #0 for left and 1 for right
    chunks.append(stereo_signal)

    chunk = numpy.concatenate(chunks) * 0.5

    stream.write(chunk.astype(numpy.float32).tostring())



p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paFloat32,
                channels=2, rate=44100, output=1)

play_tone(stream)

var=1
stream.close()
p.terminate()
