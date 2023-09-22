import cv2
import numpy as np
import time

# Ik denk dat niet gaat werken.


x_shift = 0
y_shift = 0
zoom = 0

resolution_width = 1920
resolution_height = 1080

wait_for_key_per_frame = False;


def stitch_images(img_left, img_right):
    # image_right = self.shift_image_vertically(img_left, right_y_shift)
    return np.concatenate((img_left, img_right), axis=1)


def apply_video_controls(img):
    # VID CONTROLS HERE
    return img


def resize_img(img):
    # resize based on res width and height
    dim = (resolution_width, resolution_height)
    # resize image
    resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
    return resized


def show_frame_in_webpage(img):
    pass


def show_frame_opencv(img):
    cv2.imshow('final frame', img)


def read_next_file():
    return None


def stop_video_stream():
    # When everything done, release the video capture object
    vid_right.release()
    vid_left.release()

    # Closes all the frames
    cv2.destroyAllWindows()


# open video's // Download from:
# https://h2909571.stratoserver.net/Recordings/2020-03-07-14-29-01/
vid_left = cv2.VideoCapture('assets/videos/left.mp4')
vid_right = cv2.VideoCapture('assets/videos/right.mp4')

fps = int(vid_left.get(cv2.CAP_PROP_FPS))
print('fps: ', fps)

# Read until video is completed
while vid_left.isOpened() and vid_right.isOpened():
    # Capture frame-by-frame
    ret_left, frame_left = vid_left.read()
    ret_right, frame_right = vid_right.read()

    if ret_left == True and ret_left == True:
        stitched_frame = stitch_images(img_left=frame_left, img_right=frame_right)

        # set values shift and zoom using keyboard and mouse
        applied_vid_controls_frame = apply_video_controls(stitched_frame)

        resized_frame = resize_img(applied_vid_controls_frame)
        # show frame in webpage? keen ideetjes hoe dat moet
        # show_frame_in_webpage(frame)

        # show frame in opencv
        show_frame_opencv(resized_frame)

        # delay for fps only needed when showing in opencv window
        if wait_for_key_per_frame:
            # any key
            cv2.waitKey(0)
        else:
            time.sleep(1 / fps)

        # Press Q on keyboard to  exit
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

    # Break the loop
    else:
        next_file = read_next_file()

        if next_file is not None:
            pass
        else:
            stop_video_stream()
            break
