import ffmpeg
import configparser
import glob
import cv2
import math

# pre
config = configparser.ConfigParser()
config.read('config.ini', 'UTF-8')
path = config['DEFAULT']['source_file_path']
except_filename = config['DEFAULT']['except_file_name']
except_filename_len = len(except_filename)

files = glob.glob(path + "*")
srcfilepath = ""
for file in files:
  target_filename = file[len(file)-except_filename_len:]
  if file[len(file)-except_filename_len:] != except_filename:
    print(file)
    srcfilepath = file

    video = cv2.VideoCapture(srcfilepath)
    frame_rate = video.get(cv2.CAP_PROP_FPS)
    frame_count = video.get(cv2.CAP_PROP_FRAME_COUNT)
    sec = frame_count / frame_rate
    stride = int(config['VARIANT']['stride'])
    rangeparam = math.ceil(sec / stride)

    # variant
    for i in range(rangeparam):
      start = int(i * stride)
      stream = ffmpeg.input(srcfilepath, ss=start, t=stride)
      stream = ffmpeg.output(stream, "dist/output/{}_output_{}.wav".format(target_filename, i), format="wav")
      ffmpeg.run(stream)
