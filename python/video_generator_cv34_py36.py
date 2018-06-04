import cv2

fps = 24   
#fourcc = cv2.VideoWriter_fourcc('M','J','P','G')  
fourcc = cv2.VideoWriter_fourcc('M','P','4','2')  
#fourcc = cv2.VideoWriter_fourcc('D','I','V','X')  
#fourcc = cv2.VideoWriter_fourcc('I','4','2','0')  
videoWriter = cv2.VideoWriter('/home/king/video_maker/posepic/fh_result1.mp4', fourcc, fps, (1280,720))  
for i in range(0,4102):

    frame = cv2.imread('/home/king/video_maker/posepic/fh_output_full/frame'+str(i).zfill(6)+'.jpg')
    #print (frame)
#    cv2.imshow('img', img12)
#    cv2.waitKey(1000/int(fps))
    videoWriter.write(frame)
videoWriter.release()
