
# ASCII ART v1.0 - image to text, Python version
# based on Delphi component by Matthias Matting
# which was based on PHP source code from Boosty's Ascii Artist,
# (c)2018 MoNsTeR/GDC, Noniewicz.com, Jakub Noniewicz
# cre: 20180504

import cv2

def asciiart(params, fn):
    RC = ['W', '@', '#', '*', '+', ':', '.', ',', ' ']
    ima = cv2.imread(fn, 0) # note: as gray
    rows, cols = ima.shape
    text = ''
    y = 0
    while y < rows:
        line = ''
        i = 0
        while i < (cols - params['Resolution']):
            if params['CalcMedian'] == True:
                Bright = 0
                for k in range(params['Resolution']):
                    Bright = Bright + ima[y, i+k]
                Bright = Bright / params['Resolution']
                line = line + RC[int(Bright/255*8)]
            else:
                Bright = ima[y, i]
                line = line + RC[int(Bright/255*8)]
            i += params['Resolution']
        text = text + '\r\n' + line
        y += params['Resolution']
        if params['FixDistortion'] == True:
            y = int (y + (params['Resolution']/3)+1)
    return text


if __name__ == '__main__':
    params = {'CalcMedian': True, 'FixDistortion': False, 'Resolution': 1}
    text = asciiart(params, 'test-src1.png')
    print(text)
    params = {'CalcMedian': True, 'FixDistortion': True, 'Resolution': 2}
    text = asciiart(params, 'test-src2.jpg')
    print(text)
