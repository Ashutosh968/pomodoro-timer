import ctypes
import winsound


def set_process_dpi_awareness():
    ctypes.windll.shcore.SetProcessDpiAwareness(True)


def beep1():
    winsound.Beep(323, 250)
    winsound.Beep(583, 250)


def beep2():
    winsound.Beep(523, 250)
    winsound.Beep(783, 250)
