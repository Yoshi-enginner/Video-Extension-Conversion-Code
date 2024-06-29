import numpy as np
import cv2
from moviepy.editor import VideoFileClip, AudioFileClip

# Load - specify MP4
cap = cv2.VideoCapture("C:\\pathad\\~.mp4")
fps    = cap.get(cv2.CAP_PROP_FPS)
height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
width  = cap.get(cv2.CAP_PROP_FRAME_WIDTH)

# Specify output format-MP4
fourcc = cv2.VideoWriter_fourcc('m', 'p', 'g' , '4')
out = cv2.VideoWriter("C:\\pathadd\\making\\.mp4",int(fourcc), fps, (int(width), int(height)))

while(cap.isOpened()):
	try:
		ret, frame = cap.read()
		out.write(frame)
		cv2.imshow('frame',frame)
		if cv2.waitKey(1) & 0xFF == ord('q'):
			break
	except:
		break
out.release()
cap.release()
cv2.destroyAllWindows()
	

# Add audio using moviepy
# Import video files without audio
video_clip = VideoFileClip("C:\\pathadd\\making\\.mp4")
# Load audio file(path)
audio_clip = AudioFileClip("C:\\pathad\\~.mp4") 
# Set audio to video clip
video_clip = video_clip.set_audio(audio_clip)
# Save as video file with audio
video_clip.write_videofile('C:\\pathadd\\making_complete.mp4')



