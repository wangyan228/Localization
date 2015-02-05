class config():
    def __init__(self):
        self.LOC_MIC1 = ( 0.137,   0.0,     0.0)
        self.LOC_MIC2 = (-0.06,  0.10392, 0.0)
        self.LOC_MIC3 = (-0.06, -0.11864, 0.0)
        self.LOC_MIC4 = ( 0.0,    0.0,     0.145)

        self.DISTANCE_TEST = 0.4

        self.SAMPLING_RATE = 1.0/(7.0e-6)

        self.SPEED_SOUND = 340.0

    def getPortPublisherPassThrough(self):
      return 5557

    def getPortPublisher(self):
      return 5556

    def getPortAnalysisPublisher(self):
      return 5558

    def getMicLocs(self):
        return (self.LOC_MIC1, self.LOC_MIC2, self.LOC_MIC3, self.LOC_MIC4)

    def getTestDistance(self):
        return self.DISTANCE_TEST

    def getSamplingRate(self):
        return self.SAMPLING_RATE

    def getSpeedSound(self):
        return self.SPEED_SOUND

    def printDebug(self):
        print "mic locations:", self.getMicLocs()
        print "test distance:", self.getTestDistance()
        print "sampling rate:", self.getSamplingRate()
        print "speed of sound:", self.getSpeedSound()

if __name__ == "__main__":
    sut = config()
    sut.printDebug()
