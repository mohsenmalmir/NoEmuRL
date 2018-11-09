# =============================================================================
# Created By  : Mohsen Malmir
# Created Date: Thu Nov 08 8:27 PM EST 2018
# Purpose     : this file implements the test of screen functionality
# =============================================================================

from noemurl import screen
import numpy as np
import time
import cv2

def test_grab():
    # grab the next frame from the default monitor
    shot = screen.grab()
    # check the numpy image with 3 channels
    assert(type(shot) == np.ndarray)
    assert(len(shot.shape) == 3)


def test_grab_bbox():
    # test the bounding box argument of grab
    shot = screen.grab(bbox=[0,0,100,100])
    # check the image size
    assert(shot.shape[0] == 100)
    assert(shot.shape[1] == 100)


def test_grab_speed():
    # capture frames for a second, and print the results
    start = time.time()
    cntr = 0
    while time.time() - start < 1:
        next_shot = screen.grab()
        cntr += 1
    print("\n%d frames captured in %d seconds\n" %(cntr, time.time()-start))
