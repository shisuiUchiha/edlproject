import pyaudio
import audioop

CHUNK = 1024
FORMAT = pyaudio.paFloat32 #paInt8
CHANNELS = 1
RATE = 44100 #sample rate
RECORD_SECONDS = 5
#WAVE_OUTPUT_FILENAME = "output.wav"

p = pyaudio.PyAudio()

stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK) #buffer

print("* recording")

#frames = []
#data=[]
output=0
j=0
for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    mx=audioop.rms(data,2)
    output=output+mx
    print mx
    #frames.append(data) # 2 bytes(16 bits) per channel
    j=j+1


print j
ans=output/j
print ans

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



print x

stream.stop_stream()
stream.close()
p.terminate()

