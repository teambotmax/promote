# -*- coding: utf-8 -*-
class Callback(object):

    def __init__(self, callback):
        self.callback = callback

    def PinVerified(self, pin):
        self.callback("Input this PIN code '" + pin + "' 🌸โปรดล็อกอินเข้าสู่ระบบ RollChan ภายใน 2 นาที🌸")

    def QrUrl(self, url, showQr=True):
        if showQr:
            notice='or scan this QR '
        else:
            notice=''
        self.callback('🌸ยินดีต้อนรับสู่บริการเซลฟ์บอทของ RollChan🌸\nกรุณาล็อกอินภายใน 2 นาที🌙\n' + url + '\n🎲By แมวขาว🎲')
        if showQr:
            try:
                import pyqrcode
                url = pyqrcode.create(url)
                self.callback(url.terminal('green', 'white', 1))
            except:
                pass

    def default(self, str):
        self.callback(str)
