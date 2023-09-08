from sys import argv

from moviepy.editor import *

video = argv[1]

video_clip = VideoFileClip(video).fx(vfx.speedx, 2)

video_clip.write_gif("C:\\Users\\User\\Downloads\\video.gif")

