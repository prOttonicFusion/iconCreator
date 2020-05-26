# iconCreator
Creating icon sets manually can be a real hassle. This script makes it easier by converting a single image file into complete icon sets for use on
- Windows (i.e. a `Icon.ico` file)
- MacOS (complete with the recommended transparent margin)
- Most Linux distros

## Requirements
Python 3 with [Pillow](https://pillow.readthedocs.io/en/stable/) installed

## Usage
```
python iconCreator.py <image-file>
```
The outputed icons are placed in a directory tree as shown below. 
```
icons
├── Icon.ico
├── base
│   ├── 16.png
│   ├── 24.png
│   ├── 32.png
│   ├── 48.png
│   └── 64.png
├── linux
│   ├── 128.png
│   ├── 256.png
│   ├── 512.png
│   └── 1024.png
└── mac
    ├── 128.png
    ├── 256.png
    ├── 512.png
    └── 1024.png
```
