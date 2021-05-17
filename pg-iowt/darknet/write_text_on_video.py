import cv2
import numpy as np
import os

input_vid = 'mock_or1_out.MP4'
output_vid = 'mock_or1_frames.MP4'
dataspace = 'data/mock_or/'


video_capture = cv2.VideoCapture(dataspace + input_vid)
frame_num = 0
fps = int(video_capture.get(cv2.CAP_PROP_FPS))
size = (int(video_capture.get(3)), int(video_capture.get(4)))

result = cv2.VideoWriter(dataspace + output_vid, cv2.VideoWriter_fourcc(*'MJPG'), fps, size)
while (video_capture.isOpened()):
	ret, frame = video_capture.read()
	frame_num += 1
	if ret == True:
		font = cv2.FONT_HERSHEY_SIMPLEX
		cv2.putText(frame, str(frame_num), (50,50), font, 1, (0, 255, 255), 2, cv2.LINE_4)
		result.write(frame)
		cv2.imshow('Frame', frame)
		if cv2.waitKey(1) & 0xFF == ord('q'): # Press q to quit video
			break
			
	else:
		break


video_capture.release()
result.release()
cv2.destroyAllWindows()

print('video saved')
