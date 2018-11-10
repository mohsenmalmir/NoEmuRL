# =============================================================================
# Created By  : Mohsen Malmir
# Created Date: Thu Nov 08 8:09 PM EST 2018
# Purpose     : this file implements the screen functionality for NoEmuRL
# =============================================================================

from mss import mss
from PIL import Image
import numpy as np
import cv2

mss_obj = mss()


def grab(monitor=0, bbox=None):
    """
    This function grabs an screenshot from the specific monitor 
    and returns the target bounding box if specified or the entire screen otherwise.
    Args:
        monitor: (int) index of the monitor to use
        bbox: List[int] x1y1x2y2 coordinates to be retrieved from the screenshot.
    Returns:
        numpy array, the captured screenshot is returned
    """
    # check for valid monitor id
    if monitor >= len(mss_obj.monitors):
        print("Invalid monitor index, resorting to default monitor!")
        monitor = 0
    # check for valid boudning box
    if bbox is not None and len(bbox) != 4:
        print("invalid bounding box specified, ignoring the bbox for grab!")
        bbox = None
    if bbox is not None:
        bbox = list(map(int,bbox))
        x1,y1,x2,y2 = bbox
        if x1>x2 or y1>y2:
            print("invalid bounding box coordinates, ignoring bounding box!")
            bbox = None
    # grab the screen shot
    mss_im = mss_obj.grab(mss_obj.monitors[monitor])
    # convert the PIL image
    pil_img = Image.frombytes("RGB",mss_im.size,mss_im.rgb)
    # convert to numpy array
    np_img = np.array(pil_img)
    # image is RGB, convert it to BGR
    np_img = cv2.cvtColor(np_img, cv2.COLOR_RGB2BGR)
    if bbox is not None:
        x1,y1,x2,y2 = bbox
        x1,y1 = max(0,x1), max(0,y1)
        x2,y2 = min(np_img.shape[1],x2), min(np_img.shape[0],y2)
        np_img = np_img[y1:y2,x1:x2]
    return np_img
        


