import cv2

fps = 24   
frame_size=(1280,720)
total_frame_num=1000
video_out_dir='/home/[username]/video_maker/posepic/result.mp4'
#fourcc = cv2.VideoWriter_fourcc('M','J','P','G')  #for .mp4 output
fourcc = cv2.VideoWriter_fourcc('D','I','V','X')  #for .mp4 output
#fourcc = cv2.VideoWriter_fourcc('I','4','2','0')  #for .avi output
videoWriter = cv2.VideoWriter(video_out_dir, fourcc, fps, frame_size)  
for i in range(0,total_frame_num):
    frame = cv2.imread('/home/[dir_to_images]/'+str(i).zfill(6)+'.jpg')
    #print (str(i).zfill(6))
#    cv2.imshow('img', img12)
#    cv2.waitKey(1000/int(fps))
    videoWriter.write(frame)
videoWriter.release()
