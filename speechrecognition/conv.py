import ffmpeg

stream = ffmpeg.input("sample2201191510.ogg")
stream = ffmpeg.output(stream, "sample.wav")

ffmpeg.run(stream)
