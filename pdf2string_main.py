# coding:utf-8
# !/usr/bin/env python

__author__ = 'SAF'

from PIL import Image
from pytesser import *
import pdfminer
from pdfminer.converter import TextConverter

from pdfminer.pdfinterp import PDFResourceManager
import os

Const_Image_Format = [".jpg", ".jpeg", ".bmp", ".png"]

def pdf2pic(tar_fname, source_fname):
    """
    使用A4纸像素的打印效果
    :param tar_fname:
    :param source_fname:
    :return:
    """
    cmd = "mutool.exe draw -o %s -h 3508 -w 2479 %s" % (tar_fname, source_fname)
    print cmd
    # os.popen(cmd)
    pass


class FileFilt:
    fileList = [""]
    counter = 0

    def __init__(self):
        pass

    def FindFile(self, dirr, filtrate=1):
        global Const_Image_Format
        for s in os.listdir(dirr):
            newDir = os.path.join(dirr, s)
            if os.path.isfile(newDir):
                if filtrate:
                    if newDir and (os.path.splitext(newDir)[1] in Const_Image_Format):
                        self.fileList.append(newDir)
                        self.counter += 1
                else:
                    self.fileList.append(newDir)
                    self.counter += 1


def pic2string(fname='d:/test.png'):
    image = Image.open(fname)
    txt = image_to_string(image)
    return txt


def main():
    pass


if __name__ == '__main__':
    b = FileFilt()
    b.FindFile(dirr="C:\Users\SAF\Desktop\pdf2string")
    # print(b.counter)
    txt = ""
    cnt = 1
    for k in b.fileList[1:]:
        print "k is", k
        content = pic2string(k)
        txt = txt + content + "\n"
        f = open("res%d.txt" % cnt, "w")
        f.write(content)
        f.close()
        cnt += 1
    f = open("res.txt", "w")
    f.write(txt)
    f.close()

    # pdf2pic("fdfad%d.png", "fda.pdf")
