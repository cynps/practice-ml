import ffmpeg
stride = 180 # sec, strict param

# variant
srcfilepath = "dist/src/02_.mov" # movie file name
rangeparam = 13 # file size(sec) / stride

for i in range(rangeparam):
  start = int(i * stride)
  stream = ffmpeg.input(srcfilepath, ss=start, t=stride)
  stream = ffmpeg.output(stream, "dist/output/output_{}.wav".format(i), format="wav")
  ffmpeg.run(stream)
