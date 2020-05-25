import os
import glob


TAFGET_DIR = '/home/natu/gitproj/darknet/cfg/mint'
IMAGE_ROOT_DIR = '/media/natu/data/data/mint'


def make_text(fname):
    text_fname = os.path.join(TAFGET_DIR, '%s.txt' % fname)

    print('open %s' % text_fname)
    with open(text_fname, 'w') as fp:
        glob_str = os.path.join(IMAGE_ROOT_DIR, fname, '*.png')
        img_list = glob.glob(glob_str)
        for l in img_list:
            fp.write(l + '\n')

def main():
    make_text('test')
    make_text('val  ')
    make_text('train')

    print('finished.')


if __name__ == '__main__':
    main()


