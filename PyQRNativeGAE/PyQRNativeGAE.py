'''
Created on 03-06-2011

@author: berni
'''
from PyQRNative import QRCode as QRCodeNormal
from pngcanvas import PNGCanvas
from qrcode.PyQRNative import QR8bitByte, QRBitBuffer, QRUtil, \
    QRErrorCorrectLevel, QRRSBlock


class QRCode(QRCodeNormal):
    '''
    Class for generation QRCodes on Google App Engine in native Python 
    '''

    def make_image(self):
        '''
        Creates PNG image with QR Code
        '''
        boxsize = 10 # pixels per box
        offset = 4 # boxes as border
        pixelsize = (self.getModuleCount() + offset + offset) * boxsize

        canvas = PNGCanvas(pixelsize, pixelsize)
        for row in range(self.getModuleCount()):
            for column in range(self.getModuleCount()):
                if (self.isDark(row, column) ):
                    pos_x = (column + offset) * boxsize
                    pos_y = (row + offset) * boxsize
                    canvas.filledRectangle(pos_x, pos_y, pos_x + boxsize, pos_y + boxsize)
        return canvas.dump()


    @staticmethod
    def get_type_for_string(string):
        '''
        Get QRCode type (complexity) for a string
        @param string:
        '''
        type_number = 0
        total_data_count = 0
        buff_len = 1000
        string_bit = QR8bitByte(string)
        while buff_len > total_data_count * 8:
            type_number += 1
            buff = QRBitBuffer()
            buff.put(string_bit.mode, 4)
            buff.put(string_bit.getLength(), QRUtil.getLengthInBits(string_bit.mode, type_number) )
            string_bit.write(buff)
            buff_len = buff.getLengthInBits()
            rs_blocks = QRRSBlock.getRSBlocks(type_number, QRErrorCorrectLevel.L)
            total_data_count = 0
            for i in range(len(rs_blocks)):
                total_data_count += rs_blocks[i].dataCount
        return type_number

    def make_svg(self, color_on='black', color_off='white'):
        '''
        Creates SVG xml image with QR Code
        @param color_on: color_on color
        @param color_off: color_off color
        '''
        boxsize = 10 # pixels per box
        offset = 4 # boxes as border
        self.size = (self.getModuleCount() + offset + offset) * boxsize
        width = height = self.size
        scale = self.size / self.getModuleCount()
        ver = 1
        ecl = 'L'

        svg_begin = '''<?xml version="1.0" standalone="no"?>
<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN"
  "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">
<svg width="%d" height="%d" version="1.1"
  xmlns="http://www.w3.org/2000/svg"
  xmlns:xlink="http://www.w3.org/1999/xlink">
 <desc>QR Code (version=%d, ecl=%s)</desc>
 <defs>
  <rect id="m" width="1" height="1" fill="%s"/>
 </defs>
 <rect x="0" y="0" fill="%s" width="%d" height="%d"/>
 <g transform="translate(%s, %s) scale(%s)">
        ''' % (width, height, ver, ecl, color_on, color_off, width, height, 0, 0, scale)

        svg_end = '''
 </g>
</svg>
        '''
        svg_strs = []
        for row in range(self.getModuleCount()):
            for column in range(self.getModuleCount()):
                if (self.isDark(row, column) ):
                    svg_strs.append('<use xlink:href="#m" x="%d" y="%d"/>' % (column, row))

        return "".join([svg_begin, "".join(svg_strs), svg_end])
