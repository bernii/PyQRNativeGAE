PyQRNativeGAE
==============
A small lib for genrating 2D QRCodes on Google App Engine infrastructure. Most libraries don't work as they use PIL which is not fully supported on GAE. I've created this project on top of other QRCode generation library that was using PIL and made some edits + added feature of SVG codes generation. 

How to use (example in Django):
-------------------------------

Simply just import it and generate QR Code.

    from PyQRNative import QRErrorCorrectLevel
    from PyQRNativeGAE import QRCode
	url = "https://github.com/bernii/PyQRNativeGAE"
    qr = QRCode(QRCode.get_type_for_string(url), QRErrorCorrectLevel.L)
    qr.addData(url)
    qr.make()
    return HttpResponse(qr.make_svg(), mimetype="image/svg+xml")

or

    return HttpResponse(qr.make_image(), mimetype="image/png")

That's it. Works great on Google App Engine.

Prereqs:
----------
Included in repo so you don't have to manually download it. Just for informational purposes.

- http://code.google.com/p/pyqrnative/ - Lib for generating QRCodes using PIL which is not available on GAE
- http://the.taoofmac.com/space/projects/PNGCanvas - pure python PNG canvas, very nice one