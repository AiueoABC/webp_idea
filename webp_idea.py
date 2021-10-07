import cv2
import numpy as np
import urllib.request
from io import BytesIO


def imread_url(url):
    ret = urllib.request.urlopen(url, timeout=15)
    while True:
        res = ret.read(65535)
        # if b'--frame\r\nContent-Type: image/jpeg' in res:
        if b'RIFF' in res:
            webp_s = res.find(b'RIFF')
            filesize = int(res[webp_s+4:webp_s+8][::-1].hex(), 16)
            webp_obj = res[webp_s:webp_s+12+filesize]
            print(f'===\nFilesize: {filesize}\nActualsize: {len(webp_obj)}')
            print(webp_obj)
            print('===')
            img_stream = BytesIO(webp_obj)
            frame = cv2.imdecode(np.frombuffer(img_stream.read(), np.uint8), 1)
            cv2.imshow('test', frame)
            if cv2.waitKey(1) == ord('q'):
                break
    cv2.destroyAllWindows()
    return webp_obj


if __name__ == '__main__':
    url = "http://url_put_here"
    res = imread_url(url)
    print(res)
