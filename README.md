# Google Photos To Onedrive

This project reads filenames from albums created in Google Photos and creates an album containing files with the same filename in Onedrive. Its primary function is to locate the full-resolution images in the Onedrive camerafolder, and copy them to a new album. I got the idea because to get more space on Google Photos, the images get compressed, but I enjoy the user interface of Photos more than that of Onedrive

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

This project requires a key from Google to work. This means that you'll have to create a project in the Google Cloud Console, enable the Google Photos api, download the credentials.json file, and place it in the file directory

### Installing

To get this project up and running, first clone the repository into desired folder using

```
git clone https://github.com/eidsheim98/GooglePhotosToOnedrive.git
```

Then install the required packages using

```
pip install -r requirements.txt
```

After this, you are good to go! Just run this

```
python main.py
```

Or this if you have python2 installed as well

```
python3 main.py
```



