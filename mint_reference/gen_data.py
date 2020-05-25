import os
import glob
import random

from PIL import Image

IMG_WIDTH = 416
IMG_HEIGHT = 416

SRC_ROOT_DIR = '..'
TARGET_ROOT_DIR = '/media/natu/data/data/mint'

random.seed(1234)

def random_choice_back(dir):
    glob_str = os.path.join(SRC_ROOT_DIR, dir, '*.*' )
    all_files = glob.glob(glob_str)

    selected = random.randint(0, len(all_files)-1)
    fname = all_files[selected]

    im = Image.open(fname)
    im_h, im_w = im.size

    rand_x_range = im_w - IMG_WIDTH
    rand_y_range = im_h - IMG_HEIGHT

    crop_x = random.randint(0, rand_x_range-1)
    crop_y = random.randint(0, rand_y_range-1)

    crop_box = (crop_x, crop_y, crop_x + IMG_WIDTH, crop_y + IMG_HEIGHT)

    im_back = im.crop(crop_box)
    return im_back

def get_logo():
    # 一旦決め打ちで
    logo = Image.open(os.path.join(SRC_ROOT_DIR, 'logo', '20-2_SynchRoid2.png'))
    return logo

def paste_logo(im_back, im_logo):
    im_back = im_back.convert('RGBA')
    canvas = Image.new('RGBA', im_back.size, (255, 255, 255, 0))

    # logoの変形
    ori_h, ori_w = im_back.size

    bb_h = int(ori_h * random.uniform(0.1, 0.5))
    bb_w = int(ori_w * random.uniform(0.1, 0.5))

    small_logo = im_logo.resize((bb_w, bb_h), resample=Image.BILINEAR)

    rand_x_range = IMG_WIDTH - bb_w
    rand_y_range = IMG_HEIGHT - bb_h

    bb_x = random.randint(0, rand_x_range)
    bb_y = random.randint(0, rand_y_range)

    pos = (bb_x, bb_y)

    canvas.paste(small_logo, pos, small_logo)

    result = Image.alpha_composite(im_back, canvas).convert('RGB')
    return result, (bb_x, bb_y, bb_w, bb_h)

def make_data(n, dir, bd_dir='back'):
    logo = get_logo()

    for i in range(n):
        back = random_choice_back(bd_dir)
        im, bb = paste_logo(back, logo)

        # 画像を保存
        fname = '%08d.png' % i
        im.save(os.path.join(TARGET_ROOT_DIR, dir, fname))

        # アノテーションデータを保存
        bb_x, bb_y, bb_w, bb_h = bb
        bb_center_x_norm = (bb_x + (bb_w / 2.0)) / IMG_WIDTH
        bb_center_y_norm = (bb_h + (bb_h / 2.0)) / IMG_HEIGHT
        bb_w_norm = bb_w / IMG_WIDTH
        bb_h_norm = bb_h / IMG_HEIGHT

        txt_fname = '%08d.txt' % i
        txt_file_path = os.path.join(TARGET_ROOT_DIR, dir, txt_fname)
        with open(txt_file_path, 'w') as fp:
            # [クラス] [矩形の中心座標x] [矩形の中心座標y] [矩形のwidth] [矩形のheight]
            s = "0 %f %f %f %f\n" % (bb_center_x_norm, bb_center_y_norm, bb_w_norm, bb_h_norm)
            fp.write(s)

        if i % 1000 == 0:
            print('.')

def main():
    # test data
    print('generate test data')
    make_data(100, 'test', bd_dir='back_test')

    # validation data
    print('generate val data')
    make_data(1000, 'val')

    # train data
    print('generate train data')
    make_data(100000, 'train')

    print('finished.')





if __name__ == '__main__':
    main()



