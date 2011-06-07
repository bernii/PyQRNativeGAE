PyQRNativeGAE
==============

How to use (example in Django):
-------------------------------

Simply just import it and generate QR Code.

    from PyQRNative import QRErrorCorrectLevel
    from PyQRNativeGAE import QRCode
    qr = QRCode(QRCode.get_type_for_string(url), QRErrorCorrectLevel.L)
    qr.addData("https://github.com/bernii/PyQRNativeGAE")
    qr.make()
    return HttpResponse(qr.make_svg(), mimetype="image/svg+xml")

or

    return HttpResponse(qr.make_image(), mimetype="image/png")

Work for various domestic clients. Meetings with clients. Preparing application architecture. jkImplementation of UI. Backend and frontend development works on intranet and internet applications and websites. Working as individual and as a part of bigger team. Project management. Face to face and remote communication.

Prereqs:
----------
Included in repo so you don't have to manually download it. Just for informational purposes.

- http://code.google.com/p/pyqrnative/ - Lib for generating QRCodes using PIL which is not available on GAE
- http://the.taoofmac.com/space/projects/PNGCanvas - pure python PNG canvas, very nice one