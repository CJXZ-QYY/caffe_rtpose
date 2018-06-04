chmod u+x install_caffe_and_cpm.sh
./install_caffe_and_cpm.sh
./build/examples/rtpose/rtpose.bin --video [path_to_video]/input.mp4 --write_frames path/ --no_display --no_frame_drops
python ../python/video_generator_cv34_py36.py
