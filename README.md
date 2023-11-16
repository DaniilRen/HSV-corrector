# HSV-corrector

opencv-python == 4.8.1.78

1. run 'pip install -r src/requirements.txt' and launch video_correction.py
2. Use trackbars to filter colors
3. Press 'q' to close video and stop script

By default, video is broadcast from your webcam.
Change main() parameters if you want: 
type - input type (by default - video, you can choose 'image')
src - video file path (by default 0 - webcam);
format - video format (by default 'bgr', you can choose 'rgb', 'hsv', 'lab')
edit - enable/disable filters (by default True)