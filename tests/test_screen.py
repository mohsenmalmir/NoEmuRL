# =============================================================================
# Created By  : Mohsen Malmir
# Created Date: Thu Nov 08 8:27 PM EST 2018
# Purpose     : this file implements the test of screen functionality
# =============================================================================

from NoEmuRL import screen
import numpy as np

def test_grab():
    # grab the next frame from the default monitor
    shot = screen.grab()
    # check the numpy image with 3 channels
    assert(type(shot) == np.ndarray)
    assert(len(shot.shape) == 3)
