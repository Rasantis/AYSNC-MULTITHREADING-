# Multithreaded video capture with OpenCV and Python

Capturing a video stream from a camera in python can be done with openCV. However, when doing this operation on the main
thread, performance won’t be great, especially when capturing in HD quality. By using the VideoCaptureThreading class, the 
video capture operation runs in a separate (green) thread. The performance increases dramatically as shown below (on 
a MacBook Pro) :

For 640×480:
```
[i] Frames per second: 28.71, with_threading=False
[i] Frames per second: 81.67, with_threading=True
```
For 1280×720
```
[i] Frames per second: 15.02, with_threading=False
[i] Frames per second: 52.04, with_threading=True
```

The `VideoCaptureThreading` class contains:

* an `__init__` function that opens the video capture stream, sets the frame dimensions and creates a lock object for 
thread save assigning and copying of the frames.
* a `start` function to create and start the thread
* an `update` function that will be called in a separate thread.
* a `read` function that we will call from our code to retrieve a new frame.
* a `stop` function to stop (join) the thread
* an `__exit__` function to clean up some resources.

The beautiful part of this class is that it enables you to update existing code with minimal change. You only have to 
add  
```from gfd.py.video.capture import VideoCaptureThreading```
and change the line containing
```
cap = cv2.VideoCapture()
```
to
```
cap = VideoCaptureThreading()
```
and add
```
cap.start()
```
and
```
cap.stop()
```
at the beginning and end of the capture read() loop. That’s it, very easy. An example can be found in the `test` folder of
this project.

## Running the test

In the root folder of this repository, run the following commands:

```
$ export PYTHONPATH=`pwd`/main
$ python test/videocapturethreading.py
```
