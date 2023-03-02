import pymem
from pymem import *

def WriteFoV():
    py_dev = Pymem("DEVOUR.exe")
    thread_handle = py_dev.process_handle
    game = pymem.process.module_from_name(thread_handle, "GameAssembly.dll").process_handle
    py_dev.write_float(game + 0x43E2F0, 200.0)
if __name__ == "__main__":
    WriteFoV()