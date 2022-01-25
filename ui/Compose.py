import PIL.Image as Image
import os
import cv2
# 定义图像拼接函数
def image_compose(imgPath,savePath):
    IMAGES_PATH = imgPath  # 图片集地址
    IMAGES_FORMAT = ['.jpg', '.JPG']  # 图片格式
    IMAGE_SIZE = 256  # 每张小图片的大小
    IMAGE_ROW = 8  # 图片间隔，也就是合并成一张图后，一共有几行
    IMAGE_COLUMN = 10  # 图片间隔，也就是合并成一张图后，一共有几列
    IMAGE_SAVE_PATH = savePath  # 图片转换后的地址

    # 获取图片集地址下的所有图片名称
    image_names = [name for name in os.listdir(IMAGES_PATH) for item in IMAGES_FORMAT if
                   os.path.splitext(name)[1] == item]

    image_names.sort(key=lambda x: int(x[:-4]))

    # 简单的对于参数的设定和实际图片集的大小进行数量判断
    if len(image_names) != IMAGE_ROW * IMAGE_COLUMN:
        raise ValueError("合成图片的参数和要求的数量不能匹配！")
    to_image = Image.new('RGB', (IMAGE_COLUMN * IMAGE_SIZE, IMAGE_ROW * IMAGE_SIZE))  # 创建一个新图
    # 循环遍历，把每张图片按顺序粘贴到对应位置上
    for y in range(1, IMAGE_ROW + 1):
        for x in range(1, IMAGE_COLUMN + 1):
            if(y==8):
                from_image = Image.open(IMAGES_PATH + image_names[IMAGE_COLUMN * (y - 1) + x - 1]).resize(
                 (IMAGE_SIZE, 128), Image.ANTIALIAS)
            else:
                from_image = Image.open(IMAGES_PATH + image_names[IMAGE_COLUMN * (y - 1) + x - 1]).resize(
                (IMAGE_SIZE, IMAGE_SIZE), Image.ANTIALIAS)
            to_image.paste(from_image, ((x - 1) * IMAGE_SIZE, (y - 1) * IMAGE_SIZE))

    print(type(to_image))
    box = (0, 0, 2560, 1920)
    to_image=to_image.crop(box)
    # cv2.imwrite(IMAGE_SAVE_PATH, to_image)
    to_image.save(IMAGE_SAVE_PATH)
    # 保存新图到数据库
    # fp = open(IMAGE_SAVE_PATH, 'rb')
    # img = fp.read()
    # fp.close()
    #
    # sql = "insert into input(path,imgName,image) values(%s,%s,%s)"  # 注意此处与前一种形式的不同
    # parm = (IMAGE_SAVE_PATH, name, img)
    # cur, conn = self.getLink()
    # cur.execute(sql, parm)
    # conn.commit()


# image_compose()  # 调用函数