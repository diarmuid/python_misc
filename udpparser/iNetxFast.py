__author__ = 'diarmuid'

import struct


class iNetxFast():
    def __init__(self,buf):
        self.streamid = None
        self.sequence = None
        self.valid = False
        self.unpack(buf)

    def unpack(self,buf):
        (controlword,self.streamid,self.sequence) = struct.unpack('III',buf[:11])
        if controlword == 0x11000000:
            self.valid = True
