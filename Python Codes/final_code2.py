import math
import numpy
import pyaudio
import audioop
from final_code import final_vr1
from final_code import final_vs1
from final_code import final_vz1
from final_code import flag1
from final_code import ref_res


def sine(frequency, length, rate):
    length = int(length * rate)
    factor = float(frequency) * (math.pi * 2) / rate
    return numpy.sin(numpy.arange(length) * factor)

def play_tone1(stream, frequency=2000, length=2, rate=44100): #this is for switching to read v_s
    chunks = []
    signal=sine(frequency, length, rate)
    stereo_signal=numpy.zeros([len(signal),2])
    stereo_signal[:, 0]=signal[:] #0 for left and 1 for right
    chunks.append(stereo_signal)

    chunk = numpy.concatenate(chunks) * 0.9

    stream.write(chunk.astype(numpy.float32).tostring())

def play_tone2(stream, frequency=2500, length=2, rate=44100): #this is for switching to read v_r
    chunks = []
    signal=sine(frequency, length, rate)
    stereo_signal=numpy.zeros([len(signal),2])
    stereo_signal[:, 0]=signal[:] #0 for left and 1 for right
    chunks.append(stereo_signal)

    chunk = numpy.concatenate(chunks) * 0.9

    stream.write(chunk.astype(numpy.float32).tostring())


def play_tone3(stream, frequency=3000, length=2, rate=44100): #this is for switching to read v_z
    chunks = []
    signal=sine(frequency, length, rate)
    stereo_signal=numpy.zeros([len(signal),2])
    stereo_signal[:, 0]=signal[:] #0 for left and 1 for right #0.9 for 3.2 #0.25 for 1.8
    chunks.append(stereo_signal)

    chunk = numpy.concatenate(chunks) * 0.9

    stream.write(chunk.astype(numpy.float32).tostring())


def play_tone6(stream, frequency=4000, length=2, rate=44100): #this is for switching to default 10kohm
    chunks = []
    signal=sine(frequency, length, rate)
    stereo_signal=numpy.zeros([len(signal),2])
    stereo_signal[:, 0]=signal[:] #0 for left and 1 for right
    chunks.append(stereo_signal)

    chunk = numpy.concatenate(chunks) * 0.9

    stream.write(chunk.astype(numpy.float32).tostring())



def reading_mic(stream,RATE,CHUNK,RECORD_SECONDS):
    output=0
    j=0
    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        mx=audioop.rms(data,2)
        output=output+mx
        #print mx
    #frames.append(data) # 2 bytes(16 bits) per channel
        j=j+1


    #print j
    ans=output/j
    #print ans

    x=0

    if ans>=17550 and ans<17800:
        x=0.1
    elif ans<17550 and ans>=16000:
        x=0.2
    elif ans<16000 and ans>=14400:
        x=0.3
    elif ans<14400 and ans>=13750:
        x=0.4
    elif ans<13750 and ans>=13230:
        x=0.5
    elif ans<13230 and ans>=12960:
        x=0.6
    elif ans<12960 and ans>=12800:
        x=0.7
    elif ans<12800 and ans>=12650:
        x=0.8
    elif ans<12650 and ans>=12550:
        x=0.9
    elif ans<12550 and ans>=12450:
        x=1.0
    elif ans<12450 and ans>=12360:
        x=1.1
    elif ans<12360 and ans>=12300:
        x=1.2
    elif ans<12300 and ans>=12250:
        x=1.3
    elif ans<12250 and ans>=12210:
        x=1.4
    elif ans<12210 and ans>=12170:
        x=1.5
    elif ans<12170 and ans>=12130:
        x=1.6
    elif ans<12130 and ans>=12090:
        x=1.7
    elif ans<12090 and ans>=10000:
        x=1.8

    return x




if flag1==1:
    p = pyaudio.PyAudio()
    CHUNK = 1024
    FORMAT = pyaudio.paFloat32 #paInt8
    CHANNELS = 1
    RATE = 44100 #sample rate
    RECORD_SECONDS = 5
    switch=ref_res
    stream = p.open(format=pyaudio.paFloat32,
                    channels=2, rate=44100, output=1)

    #sending a signal to switch to read v_s

    play_tone1(stream)


    stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)

    v_s=reading_mic(stream,RATE,CHUNK,RECORD_SECONDS)



    #sending a signal to switch and read v_z

    stream = p.open(format=pyaudio.paFloat32,
                    channels=2, rate=44100, output=1)

    play_tone2(stream)


    stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)

    v_r=reading_mic(stream,RATE,CHUNK,RECORD_SECONDS)


     #sending a signal to switch and read v_r

    stream = p.open(format=pyaudio.paFloat32,
                    channels=2, rate=44100, output=1)


    play_tone3(stream)


    stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)

    v_z=reading_mic(stream,RATE,CHUNK,RECORD_SECONDS)




    final_vr2=v_r
    final_vs2=v_s
    final_vz2=v_z
    ref_res2=switch
    stream = p.open(format=pyaudio.paFloat32,
                    channels=2, rate=44100, output=1)
    play_tone6(stream)
    stream.close()
    p.terminate()



