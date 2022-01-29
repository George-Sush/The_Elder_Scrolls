import ctypes
from ctypes import wintypes

user32 = ctypes.WinDLL("user32")

SW_HIDE = 0
SW_SHOW = 5

user32.FindWindowW.restype = wintypes.HWND
user32.FindWindowW.argtypes = (
    wintypes.LPCWSTR,  # lpClassName
    wintypes.LPCWSTR,
)  # lpWindowName

user32.ShowWindow.argtypes = (wintypes.HWND, ctypes.c_int)  # hWnd  # nCmdShow


def hide_taskbar():
    hWnd = user32.FindWindowW("Shell_traywnd", None)
    user32.ShowWindow(hWnd, SW_HIDE)


def unhide_taskbar():
    hWnd = user32.FindWindowW("Shell_traywnd", None)
    user32.ShowWindow(hWnd, SW_SHOW)
