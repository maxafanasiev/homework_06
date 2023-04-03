import os
import sys
import shutil

# CONSTANT
IMAGE = ['JPEG', 'PNG', 'JPG', 'SVG']
VIDEO = ['AVI', 'MP4', 'MOV', 'MKV']
DOCS = ['DOC', 'DOCX', 'TXT', 'PDF', 'XLSX', 'PPTX']
MUSIC = ['MP3', 'OGG', 'WAV', 'AMR']
ARCHIVE = ['ZIP', 'GZ', 'TAR']


# Parent Directory path
sorted_path = sys.argv[1]


# Delete empty folders
def del_empty_dirs(adress):
    for dirs in os.listdir(adress):
        dir = os.path.join(adress, dirs)
        if os.path.isdir(dir):
            del_empty_dirs(dir)
            if not os.listdir(dir):
                shutil.rmtree(dir)


# Recursed folders extract
def deep_folders(adress):
    for el in os.listdir(adress):
        way = os.path.join(adress, el)
        if os.path.isdir(way): 
            deep_folders(way)
        else:     
            try: 
                shutil.move(way,sorted_path)
            except: 
                print(f"file {way} already exist")
                os.remove(way)
    del_empty_dirs(adress)


def sort_Image():
    pass

def sort_Video():
    pass

def sort_Docs():
    pass

def sort_Music():
    pass

def sort_Archive():
    pass

def sort_Other():
    pass

                

deep_folders(sorted_path)
