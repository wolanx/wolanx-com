---
title: ffmpeg
date: 2016-10-17
tags: [linux]
---

- download https://ffmpeg.org/download.html

> ffmpeg -i test.mov -vcodec libx264 -s 960x540 -preset fast -crf 22 -y -acodec copy test.mp4

- 通过调节"22"，可以调节清晰度，（这个取值0~50，一般取18到30左右合适。0是无损，50就看不清了）


## old

```shell
./ffmpeg.exe -list_devices true -f dshow -i dummy

./ffmpeg.exe -f dshow -i video="screen-capture-recorder":audio="virtual-audio-capturer" ab.mp4
./ffmpeg.exe -f dshow -i video="screen-capture-recorder" yo.mp4
./ffmpeg.exe -f dshow -i audio="virtual-audio-capturer" yo.mp3


./ffmpeg.exe -f dshow -i video="screen-capture-recorder" -f dshow -i audio="virtual-audio-capturer" 222.avi



./ffmpeg.exe -list_devices true -f dshow -i test.mp4
./ffmpeg.exe -f x11grab -s 842x676 -r 50 -i :0.0+228,213 test.mp4
./ffmpeg.exe -vcodec mpeg4 -b 1000 -r 10 -g 300 test.avi
```
