# =============================================================================
# Created By  : Mohsen Malmir
# Created Date: Fri Nov 09 8:10 PM EST 2018
# Purpose     : this file implements the gui handling to interact with emulators
# =============================================================================

from AppKit import NSWorkspace,NSApplicationActivateIgnoringOtherApps
from Quartz import CGWindowListCopyWindowInfo,kCGWindowListOptionOnScreenOnly
from Quartz import kCGWindowListExcludeDesktopElements,kCGNullWindowID

# this is a list of pairs of (emulator, game) that is supported to interact with
supported_emus = ["OpenEmu"]
supported_games = ["Mortal Kombat 3"]


def activate_emu():
    """
    This function scans all the open windows and returns a handle to the first known
    and supported emulator-game pair.
    Args:
        None
    Returns:
        
    """
    # get a list of all open windows
    windows = CGWindowListCopyWindowInfo(kCGWindowListOptionOnScreenOnly&kCGWindowListExcludeDesktopElements,kCGNullWindowID)
    winname_list = [w.get("kCGWindowName", u"Unknown") for w in windows]
    winrect_list = [w["kCGWindowBounds"] for w in windows]
    # first find the Emulator
    ws = NSWorkspace.sharedWorkspace()
    runningApps = ws.runningApplications()
    # the running processes are checked by their localized name, e.g. "OpenEmu"
    ra_names = [ra.localizedName() for ra in runningApps] 
    for ii, emu in enumerate(supported_emus):
        if emu in ra_names: # if a supported emu is found, check for corresponding games
            if supported_games[ii] in winname_list: # we foudn a supported game of the target emu
                # activate the emu window
                emu_idx = ra_names.index(emu)
                runningApps[emu_idx].activateWithOptions_(NSApplicationActivateIgnoringOtherApps)
                # get the window coordinates
                idx = winname_list.index(supported_games[ii])
                rect = winrect_list[idx]
                rect = [rect.get("X"),rect.get("Y"),rect.get("Width"),rect.get("Height")]
                rect = list(map(int,rect))
                return rect, emu, supported_games[ii]
    return None

if __name__ == "__main__":
    print(activate_emu())
