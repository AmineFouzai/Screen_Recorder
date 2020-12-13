import moviepy.editor as mpe


class Vsync(object):

    def __init__(self,video_soruce,audio_source,output):
        self.video_soruce=video_soruce
        self.audio_source=audio_source
        self.output=output

    def vsync(self):
        self.video_soruce= mpe.VideoFileClip(self.video_soruce)
        self.audio_source = mpe.AudioFileClip(self.audio_source)
        final=self.video_soruce.set_audio(self.audio_source)
        final.write_videofile(self.output,codec='mpeg4' ,audio_codec='libvorbis')
        
vsync=Vsync(video_soruce="video.avi",audio_source="audio.wav",output="final.mp4")
try:
    vsync.vsync()
except Exception as e:
    raise e


