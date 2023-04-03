import os
import sys
import shutil

# CONSTANT
IMAGE = ['jpeg', 'png', 'jpg', 'svg']
VIDEO = ['avt', 'mp4', 'mov', 'mkv']
DOCS = ['doc', 'docx', 'txt', 'pdf', 'xlsx', 'pptx']
MUSIC = ['mp3', 'ogg', 'wav', 'amr']
ARCHIVE = ['zip', 'gz', 'tar','7z']
NOT_OTHER = []
NOT_OTHER.extend(VIDEO)
NOT_OTHER.extend(IMAGE)
NOT_OTHER.extend(DOCS)
NOT_OTHER.extend(MUSIC)
NOT_OTHER.extend(ARCHIVE)

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
                os.remove(way)
    del_empty_dirs(adress)


def sort_Image():
    image_folder_dir = os.path.join(sorted_path,'IMAGE')
    os.mkdir(image_folder_dir)

    for el in os.listdir(sorted_path):
        ext = el.split('.')[-1]
        if ext in IMAGE:
            shutil.move(os.path.join(sorted_path,el),image_folder_dir)


def sort_Video():
    video_folder_dir = os.path.join(sorted_path,'VIDEO')
    os.mkdir(video_folder_dir)

    for el in os.listdir(sorted_path):
        ext = el.split('.')[-1]
        if ext in VIDEO:
            shutil.move(os.path.join(sorted_path,el),video_folder_dir)

def sort_Docs():
    docs_folder_dir = os.path.join(sorted_path,'DOCS')
    os.mkdir(docs_folder_dir)

    for el in os.listdir(sorted_path):
        ext = el.split('.')[-1]
        if ext in DOCS:
            shutil.move(os.path.join(sorted_path,el),docs_folder_dir)

def sort_Music():
    music_folder_dir = os.path.join(sorted_path,'MUSIC')
    os.mkdir(music_folder_dir)

    for el in os.listdir(sorted_path):
        ext = el.split('.')[-1]
        if ext in MUSIC:
            shutil.move(os.path.join(sorted_path,el),music_folder_dir)

def sort_Archive():
    archive_folder_dir = os.path.join(sorted_path,'ARCHIVE')
    os.mkdir(archive_folder_dir)

    for el in os.listdir(sorted_path):
        ext = el.split('.')[-1]
        if ext in ARCHIVE:
            shutil.move(os.path.join(sorted_path,el),archive_folder_dir)

def sort_Other():
    other_folder_dir = os.path.join(sorted_path,'OTHER')
    os.mkdir(other_folder_dir)

    for el in os.listdir(sorted_path):
        ext = el.split('.')[-1]
        if ext not in NOT_OTHER :
            shutil.move(os.path.join(sorted_path,el),other_folder_dir)

                
def main():
    deep_folders(sorted_path)
    sort_Image()
    sort_Video()
    sort_Docs()
    sort_Music()
    sort_Archive()
    sort_Other()



main()