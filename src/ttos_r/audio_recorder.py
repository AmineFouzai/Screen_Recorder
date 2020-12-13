import pyaudio
import wave

class AudioRecorder(object):

    def __init__(self,output="audio.wav"):
        self.chunk = 1024  # Record in chunks of 1024 samples
        self.sample_format = pyaudio.paInt16  # 16 bits per sample
        self.channels = 2
        self.fs = 44100  # Record at 44100 samples per second
        self.seconds = 3
        self.output = output
        self.audio_input = pyaudio.PyAudio()
        self.stream = self.audio_input.open(format=self.sample_format,
                        channels=self.channels,
                        rate=self.fs,
                        frames_per_buffer=self.chunk,
                        input=True)
        self.frames= []


    def start(self):
        while True:
            self.data = self.stream.read(self.chunk)
            self.frames.append(self.data)

    def stop(self):
        self.stream.stop_stream()
        self.stream.close()
        self.audio_input.terminate()

    def save(self):
        self.wf = wave.open(self.output, 'wb')
        self.wf.setnchannels(self.channels)
        self.wf.setsampwidth(self.audio_input.get_sample_size(self.sample_format))
        self.wf.setframerate(self.fs)
        self.wf.writeframes(b''.join(self.frames))
        self.wf.close()


audioRecorder=AudioRecorder()
try:
    audioRecorder.start()
except KeyboardInterrupt as e:
    audioRecorder.stop()
    audioRecorder.save()
