from shutil import copy2
import os
from paths import *

def copy_images(filesdict):
    #filesdict = {'StarPhone': ['poephone1.png', 'r2phone1.png', 'reyphone1.png', 'BB8phone.png', 'kylophone.png', 'lukephone.png', 'finnhone2.png', '3pophone.png', 'lukephone2.png', 'cassphone.png', 'jynphone.png', 'jynphone2.png', 'k2phone.png'], 'RR': ['DSC_0119.JPG', 'IMG_20180811_024915.jpg', 'Snapchat-759381755.jpg', 'received_247065412632480.jpeg', 'Snapchat-1805495101.jpg', 'Snapchat-778404164.mp4'], 'Tasha har basja': ['IMG_20170419_205737.jpg', 'IMG_20170419_205742.jpg', 'IMG_20170419_205746.jpg', 'IMG_20170419_205750.jpg', 'IMG_20170419_205753.jpg', 'IMG_20170419_205756.jpg', 'IMG_20170419_205801.jpg', 'VID_20170419_205829.mp4']}
    not_copied_images = {}
    full_i = 0
    for key in filesdict.keys():
        not_copied_images_list = []
        filenames = filesdict.get(key)
        for filename in filenames:
            #print('Processing file {}'.format(filename))
            src = ONEDRIVE_IMAGES_PATH + filename
            dst = ONEDRIVE_ALBUM_PATH + key + '\\' + filename
            try:
                copy2(src, dst)
                print('Copying file {} to album {}'.format(filename, key))
            except FileNotFoundError:
                # print('Initiating new album directory: {}'.format(key))
                create_album_folder(key)
                print('Copying file {} to album {}'.format(filename, key))
                try:
                    copy2(src, dst)
                except:
                    not_copied_images_list.append(filename)
            not_copied_images[key] = not_copied_images_list


    if not_copied_images is not {}:
        for key in not_copied_images.keys():
            with open(ONEDRIVE_ALBUM_PATH + key + '\\' + 'not_copied.txt', 'w+') as file:
                for image in not_copied_images_list:
                    file.write(image + '\n')
                print('{} files not copied, see file "not_copied.txt" in folder {}'.format(
                    len(not_copied_images_list), key
                ))
                #print('Not copied from album {}, filename {}'.format(key, not_copied_images[key]))



def create_album_folder(title):
    path = ONEDRIVE_ALBUM_PATH + title
    try:
        os.mkdir(path)
    except OSError as e:
        #print("Creation of the directory %s failed" % path)
        pass
    else:
        #print("Successfully created the directory %s " % path)
        pass

def write_not_copied(key, not_copied_images):
    path = ONEDRIVE_ALBUM_PATH + key + '\\not_copied.txt'
    with open(path, 'wr+') as file:
        pass

if __name__ == '__main__':
    copy_images('None')

