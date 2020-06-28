from localbinarypatterns import LocalBinaryPatterns
import pickle

desc = LocalBinaryPatterns(24, 8)
model = pickle.load(open("..\\models\\detection_model_hybriddata_24_8", 'rb'))


class Spoof:
    def __init__(self, n):
        self.n = n

    def spoof(self, roi_gray):
        hist = desc.describe(roi_gray)
        prediction = model.predict([hist])[0]

        return prediction
