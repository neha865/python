#change video .MP4 to Image .GIF format
from moviepy.editor import *
video = VideoFileClip("/Users/sreeneha/Downloads/videotogif/vecteezy_happy-birthday-greeting-in-2d-animation-format_3321328.mp4")
video.write_gif("/Users/sreeneha/Downloads/videotogif/vecteezy_happy-birthday-greeting-in-2d-animation-format_3321328.gif")