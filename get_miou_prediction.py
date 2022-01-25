from unet import Unet
from PIL import Image
import numpy as np
import os
import copy
class miou_Unet(Unet):
    # def detect_image(self, image):
    #     orininal_h = np.array(image).shape[0]
    #     orininal_w = np.array(image).shape[1]
    #
    #     img, nw, nh = self.letterbox_image(image,(self.model_image_size[1],self.model_image_size[0]))
    #     img = [np.array(img)/255]
    #     img = np.asarray(img)
    #
    #     pr = self.model.predict(img)[0]
    #     pr = pr.argmax(axis=-1).reshape([self.model_image_size[0],self.model_image_size[1]])
    #     pr = pr[int((self.model_image_size[0]-nh)//2):int((self.model_image_size[0]-nh)//2+nh), int((self.model_image_size[1]-nw)//2):int((self.model_image_size[1]-nw)//2+nw)]
    #
    #     image = Image.fromarray(np.uint8(pr)).resize((orininal_w,orininal_h))
    #
    #     return image

    def detect_image(self, image):
        old_img = copy.deepcopy(image)
        orininal_h = np.array(image).shape[0]
        orininal_w = np.array(image).shape[1]

        img, nw, nh = self.letterbox_image(image, (self.model_image_size[1], self.model_image_size[0]))
        img = [np.array(img) / 255]
        img = np.asarray(img)

        pr = self.model.predict(img)[0]
        pr = pr.argmax(axis=-1).reshape([self.model_image_size[0], self.model_image_size[1]])
        pr = pr[int((self.model_image_size[0] - nh) // 2):int((self.model_image_size[0] - nh) // 2 + nh),
             int((self.model_image_size[1] - nw) // 2):int((self.model_image_size[1] - nw) // 2 + nw)]

        seg_img = np.zeros((np.shape(pr)[0], np.shape(pr)[1], 3))

        for c in range(self.num_classes):
            seg_img[:, :, 0] += ((pr[:, :] == c) * (self.colors[c][0])).astype('uint8')
            seg_img[:, :, 1] += ((pr[:, :] == c) * (self.colors[c][1])).astype('uint8')
            seg_img[:, :, 2] += ((pr[:, :] == c) * (self.colors[c][2])).astype('uint8')

        image = Image.fromarray(np.uint8(seg_img)).resize((orininal_w, orininal_h))

        if self.blend:
            image = Image.blend(old_img, image, 0.7)

        return image

unet = miou_Unet()

image_ids = open(r"newdata/val.txt",'r').read().splitlines()

if not os.path.exists("./miou_pr_dir"):
    os.makedirs("./miou_pr_dir")

for image_id in image_ids:
    image_path = "./newdata/vimages/"+image_id+".jpg"
    image = Image.open(image_path)
    image = unet.detect_image(image)
    image.save("./miou_pr_dir/" + image_id + ".png")
    print(image_id," done!")
