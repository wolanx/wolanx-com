---
title: paddle 百度飞桨
date: 2024-05-05T17:15:51+08:00
tags: [python]
---


```shell
# download zip
# https://github.com/PaddlePaddle/PaddleOCR?tab=readme-ov-file#%EF%B8%8F-pp-ocr%E7%B3%BB%E5%88%97%E6%A8%A1%E5%9E%8B%E5%88%97%E8%A1%A8%E6%9B%B4%E6%96%B0%E4%B8%AD
# 中英文超轻量PP-OCRv4模型（15.8M）

docker pull paddlepaddle/paddle:2.6.1
docker run --name paddle_docker -it -v $PWD:/paddle registry.baidubce.com/paddlepaddle/paddle:2.6.1 /bin/bash

pip install paddle2onnx


paddle2onnx --model_dir ch_ppocr_mobile_v2.0_cls_infer \
             --model_filename inference.pdmodel \
             --params_filename inference.pdiparams\
             --save_file cls.onnx
paddle2onnx --model_dir ch_PP-OCRv4_det_infer \
             --model_filename inference.pdmodel \
             --params_filename inference.pdiparams\
             --save_file det.onnx
paddle2onnx --model_dir ch_PP-OCRv4_rec_infer \
             --model_filename inference.pdmodel \
             --params_filename inference.pdiparams\
             --save_file rec.onnx
```


