import socket
import struct
import numpy as np
import sys
sys.path.append("/home/root/opencv_build/lib")
import cv2 as cv

PORT = 64265

s = socket.socket()
s.bind(('', PORT))
s.listen(1)

conn, addr = s.accept()

def sendImg(img):
    rows = img.shape[0]
    cols = img.shape[1]
    channels = img.shape[2] if len(img.shape) > 2 else 1

    conn.send(struct.pack('iii', rows, cols, channels) + img.tostring())

def read(size):
    batchSize = 4096
    data = ''
    while len(data) < size:
        data += conn.recv(batchSize)
    return data

def receiveImg():
    rows, cols, channels = struct.unpack('iii', conn.recv(4*3))
    data = read(rows * cols * channels)
    return np.fromstring(data, dtype=np.uint8).reshape([rows, cols, channels])


while True:
    try:
        img = receiveImg()
        img = cv.Canny(img, 100, 200)
        sendImg(img)
    except Exception as e:
        conn.close()
        conn, addr = s.accept()
