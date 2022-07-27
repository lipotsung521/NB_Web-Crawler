# https://blog.csdn.net/weixin_41010198/article/details/106544789

# 匯入opencv模組
import cv2

class Compress_img:
    def __init__(self, img_path):
        self.img_path = img_path
        self.img_name = img_path.split('/')[-1]

    def compress_img_CV(self, compress_rate=0.5, show=False):
        img = cv2.imread(self.img_path)
        heigh, width = img.shape[:2]
        # 双三次插值
        img_resize = cv2.resize(img, (int(heigh*compress_rate), int(width*compress_rate)),
                                interpolation=cv2.INTER_AREA)
        cv2.imwrite('result_cv_' + self.img_name, img_resize)
        print("%s 已压缩，" % (self.img_name), "压缩率：", compress_rate)
        if show:
            cv2.imshow(self.img_name, img_resize)
            cv2.waitKey(0)

if __name__ == '__main__':
    img_path = './ym.jpg'
    compress = Compress_img(img_path)

    # 使用opencv压缩图片
    compress.compress_img_CV()