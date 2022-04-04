import cv2


def transfer(video, save):
    cap = cv2.VideoCapture(video)
    num = 0
    while True:
        if cap.grab():
            num += 1
            if num % 4 == 1:  # 每4帧截取一个图片
                flag, frame = cap.retrieve()  #解码并返回一个帧
                if not flag:
                    continue
                else:
                    cv2.imshow('video', frame)
                    new = save + "\\" + str(int(num / 4)) + ".jpg"
                    print('Processing：' + str(int(num / 4)) + ".jpg(press ESC to exit)")
                    cv2.imencode('.jpg', frame)[1].tofile(new)
        if cv2.waitKey(10) == 27:
            break


video = input('Please enter your video path(./video.mp4):')  # 在此处设置你的视频文件路径以及图片输出路径
save = input('Please enter your image dir(./part1)):')
transfer(video, save)
print('Enjoy!')