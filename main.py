import os
import sys
import shutil

# CONSTANT
IMAGE = ['jpeg', 'png', 'jpg', 'svg']
VIDEO = ['avt', 'mp4', 'mov', 'mkv']
DOCS = ['doc', 'docx', 'txt', 'pdf', 'xlsx', 'pptx','rtf']
MUSIC = ['mp3', 'ogg', 'wav', 'amr']
ARCHIVE = ['zip', 'gz', 'tar','7z']
NOT_OTHER = []
NOT_OTHER.extend(VIDEO)
NOT_OTHER.extend(IMAGE)
NOT_OTHER.extend(DOCS)
NOT_OTHER.extend(MUSIC)
NOT_OTHER.extend(ARCHIVE)
IGNORE = ['.DS_Store']


translate_dict = {'а':'a','б':'b','в':'v','г':'g','д':'d','е':'e','ё':'yo',
      'ж':'zh','з':'z','и':'i','й':'i','к':'k','л':'l','м':'m','н':'n',
      'о':'o','п':'p','р':'r','с':'s','т':'t','у':'u','ф':'f','х':'h',
      'ц':'c','ч':'ch','ш':'sh','щ':'sch','ъ':'','ы':'y','ь':'','э':'e',
      'ю':'u','я':'ya', 'А':'A','Б':'B','В':'V','Г':'G','Д':'D','Е':'E','Ё':'YO',
      'Ж':'ZH','З':'Z','И':'I','Й':'I','К':'K','Л':'L','М':'M','Н':'N',
      'О':'O','П':'P','Р':'R','С':'S','Т':'T','У':'U','Ф':'F','Х':'H',
      'Ц':'C','Ч':'CH','Ш':'SH','Щ':'SCH','Ъ':'','Ы':'y','Ь':'','Э':'E',
      'Ю':'U','Я':'YA','ґ':'','ї':'', 'є':'','Ґ':'g','Ї':'i',
      'Є':'e','1':'1','2':'2','3':'3'}

# Parent Directory path

sorted_path = sys.argv[1]

# Print list of file by category
def file_list_by_folder():
    for folder in os.listdir(sorted_path):
        way = os.listdir(os.path.join(sorted_path, folder))
        print('{:>50} - {:<50} '.format('Folder', folder))
        print('{:^100}'.format('-'*99))
        for file in way:
            print('{:^5} {:<95} '.format('',file))
        print('\n')    
        print('{:^100}'.format('-'*99))


# transliterate word function
def translite(word):
    for key in translate_dict:
        word = word.replace(key, translate_dict[key])
    return word


# Rename file to transliterated name
def normalize():
    for el in os.listdir(sorted_path):
        tel =  translite(el)
        os.rename(os.path.join(sorted_path,el), os.path.join(sorted_path,tel))


# Create set of founded extension
def create_ext_set():
    ext_set = set()
    for el in os.listdir(sorted_path):
        ext = el.split('.')[-1]
        if os.path.isfile(os.path.join(sorted_path,el)) and ext in NOT_OTHER:
            ext_set.add(ext)
    return ext_set


# Create set of founded unknown extension
def create_un_ext_set():
    ext_set = set()
    for el in os.listdir(sorted_path):
        ext = el.split('.')[-1]
        if os.path.isfile(os.path.join(sorted_path,el)) and ext not in NOT_OTHER:
            ext_set.add(ext)
    return ext_set


# Delete empty folders
def del_empty_dirs(adress):
    for dirs in os.listdir(adress):
        dir = os.path.join(adress, dirs)
        if os.path.isdir(dir):
            del_empty_dirs(dir)
            if not os.listdir(dir):
                shutil.rmtree(dir)


# Recursed folders extract
def deep_folders(root_folder):
    for subdir, dirs, files in os.walk(root_folder):
        for file in files:
            src = os.path.join(subdir, file)
            dst = os.path.join(root_folder, file)
            shutil.move(src, dst)
        del_empty_dirs(root_folder)



#Sorting image by extension
def sort_Image():
    image_folder_dir = os.path.join(sorted_path,'IMAGE')
    os.mkdir(image_folder_dir)
    for el in os.listdir(sorted_path):
        if os.path.isfile(os.path.join(sorted_path, el)):
            ext = el.split('.')[-1]
            if ext in IMAGE and not ext in IGNORE:
                shutil.move(os.path.join(sorted_path,el),image_folder_dir)


#Sorting video by extension
def sort_Video():
    video_folder_dir = os.path.join(sorted_path,'VIDEO')
    os.mkdir(video_folder_dir)

    for el in os.listdir(sorted_path):
        if os.path.isfile(os.path.join(sorted_path, el)):
            ext = el.split('.')[-1]
            if ext in VIDEO and not ext in IGNORE:
                shutil.move(os.path.join(sorted_path,el),video_folder_dir)


#Sorting doc's by extension
def sort_Docs():
    docs_folder_dir = os.path.join(sorted_path,'DOCS')
    os.mkdir(docs_folder_dir)

    for el in os.listdir(sorted_path):
        if os.path.isfile(os.path.join(sorted_path, el)):
            ext = el.split('.')[-1]
            if ext in DOCS and not ext in IGNORE:
                shutil.move(os.path.join(sorted_path,el),docs_folder_dir)


#Sorting music by extension
def sort_Music():
    music_folder_dir = os.path.join(sorted_path,'MUSIC')
    os.mkdir(music_folder_dir)

    for el in os.listdir(sorted_path):
        if os.path.isfile(os.path.join(sorted_path, el)):
            ext = el.split('.')[-1]
            if ext in MUSIC and not ext in IGNORE:
                shutil.move(os.path.join(sorted_path,el),music_folder_dir)


#Unpack and sorting archive
def sort_Archive():
    archive_folder_dir = os.path.join(sorted_path,'ARCHIVE')
    os.mkdir(archive_folder_dir)

    for el in os.listdir(sorted_path):
        if os.path.isfile(os.path.join(sorted_path, el)):
            ext = el.split('.')[-1]
            if ext in ARCHIVE and not ext in IGNORE:
                shutil.unpack_archive( os.path.join(sorted_path, el), archive_folder_dir)
                os.remove(os.path.join(sorted_path,el))


#Sorting other by extension
def sort_Other():
    other_folder_dir = os.path.join(sorted_path,'OTHER')
    os.mkdir(other_folder_dir)

    for el in os.listdir(sorted_path):
        if os.path.isfile(os.path.join(sorted_path, el)):
            ext = el.split('.')[-1]
            if not ext in IGNORE and not ext in NOT_OTHER:
                shutil.move(os.path.join(sorted_path,el),other_folder_dir)


#Main function
def main():
    deep_folders(sorted_path)
    with_ext = create_ext_set()
    without_ext = create_un_ext_set()
    normalize()
    sort_Image()
    sort_Video()
    sort_Docs()
    sort_Music()
    sort_Archive()
    sort_Other()
    file_list_by_folder()
    print('{:^100}'.format('*'*100))
    print(f"Founded file's with know extension: {with_ext}")
    print(f"Founded file's with unknown extension: {without_ext}")
    print('{:^100}'.format('*'*100))

main()