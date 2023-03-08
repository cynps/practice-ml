import ffmpeg
import configparser
import glob
import cv2
import math

# pre
config = configparser.ConfigParser()
config.read('config.ini', 'UTF-8')
path = config['DEFAULT']['source_file_path']
filename = config['VARIANT']['source_file_name']
filename_len = len(filename)

files = glob.glob(path + "*")
srcfilepath = ""
for file in files:
  if file[len(file)-filename_len:] == filename:
    print(file)
    srcfilepath = path + filename

video = cv2.VideoCapture(srcfilepath)
frame_rate = video.get(cv2.CAP_PROP_FPS)
frame_count = video.get(cv2.CAP_PROP_FRAME_COUNT)
sec = frame_count / frame_rate
stride = int(config['VARIANT']['stride'])
rangeparam = math.ceil(sec / stride)

print("srcfilepath", srcfilepath)
print("partitions:", rangeparam)

# variant
for i in range(rangeparam):
  start = int(i * stride)
  stream = ffmpeg.input(srcfilepath, ss=start, t=stride)
  stream = ffmpeg.output(stream, "dist/output/output_{}.wav".format(i), format="wav")
  ffmpeg.run(stream)


