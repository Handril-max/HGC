import platform

def system_dpi():
    host_os = platform.system()
    if host_os == 'Windows':
        #import ctypes
        #ScaleFactor=ctypes.windll.shcore.GetScaleFactorForDevice(0)
        ScaleFactor = 100
        return ScaleFactor
    if host_os == 'Linux':
        ScaleFactor = 200
        return ScaleFactor
    if host_os == 'Darwin':
        ScaleFactor = 200
        return ScaleFactor
    if host_os == 'Haniux':
        ScaleFactor = 200
        return ScaleFactor

def to_dpi():
    for_dpi = int((int(system_dpi()))/100)
    return for_dpi
