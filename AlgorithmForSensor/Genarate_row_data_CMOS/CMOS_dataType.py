import numpy as np
class CMOS_datatype(object):
    def __init__(self):
        self.rawData = None 
        self.roiData = None
        self.sumRowVal = None
        self.sumColVal = None

        self.peakPoint = None

        self.Xc = None
        self.Yc = None

        self.Px = None
        self.Py = None

        self.coordinateX = None
        self.coordinateY = None
        self.h = None

        self.alpha = None
        self.beta = None

    def dataClear(self):
        self.rawData = None 
        self.roiData = None
        self.sumRowVal = None
        self.sumColVal = None

        self.peakPoint = None

        self.Xc = None
        self.Yc = None