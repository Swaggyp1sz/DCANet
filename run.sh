#!/usr/bin/env bash

# This script is used to train a model. More specific setttings can
# be found and modified in a train.yml file under the experiment dir


# basic settings
degradation=$1
model=$2
file_name=$3
exp_id=001
gpu_id=0
rate=30

rm -rf out_LR.mp4
rm -rf LOSS_LR.mp4
# ffmpeg -i ${file_name}.mp4 -strict -2 -s 270x480 out_LR.mp4
ffmpeg -i ${file_name}.mp4 -vf scale=iw/4:ih/4 -strict -2 out_LR.mp4  #视频分辨率降低为低分辨率
rm -rf ./data/xxxx/xxx/*
rm -rf ./results/xxxx/G_iter200000LossLR/xxx/*
ffmpeg -i out_LR.mp4 ./data/xxxx/xxx/%5d.png


# run
python ./codes/main.py \
  --exp_dir ${exp_dir} \
  --mode valid \
  --model ${model} \
  --opt test.yml \
  --gpu_id ${gpu_id} 

ffmpeg -r ${rate} -start_number 00001 -i ./results/xxxx/G_iter200000LossLR/xxx/%5d.png -pix_fmt nv12 LOSSLR_out.mp4  #输出高分辨率视频