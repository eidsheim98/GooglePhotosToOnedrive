import onedrive_handler, photos_api, json

gp = photos_api.Photos_API()

with open('config.json', 'r+') as file:
    j = file.read()
    j = json.loads(j)
    ONEDRIVE_IMAGES_PATH = j["ONEDRIVE_IMAGES_PATH"]
    if ONEDRIVE_IMAGES_PATH == '':
        ONEDRIVE_IMAGES_PATH = input('Please insert path to where images are stored: ')
    ONEDRIVE_ALBUM_PATH = j["ONEDRIVE_ALBUM_PATH"]
    if ONEDRIVE_ALBUM_PATH == '':
        ONEDRIVE_ALBUM_PATH = input('Please insert path to where you want the albums stored: ')
    #TODO create json and finish parameters here

images, count = gp.get_albums()
onedrive_handler.copy_images(images)