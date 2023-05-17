import os
import shutil
from zipfile import ZipFile #import modules

Download_Path = os.path.expanduser("~/Downloads")  # creates the path adress by adding user path
Desktop_Path= os.path.expanduser("~/Desktop")
X_Dictionary={}
for x in os.listdir(Download_Path):   # loop through all the files in that directory
    File_Path=os.path.join(Download_Path,x)
    if os.path.isfile(File_Path):
        x_size=os.stat(File_Path).st_size
        X_Dictionary.setdefault(x_size,[]).append(File_Path)   # dictonary of file size ase key
print(X_Dictionary)
for size , files in X_Dictionary.items():
    if len(files)>1:    # check if there is more than one file with same size
        for i in range(len(files)):
            for j in range(i+1, len(files)):
                file1=files[i]
                file2=files[j]
                with open(file1, 'rb') as f1, open(file2,'rb') as f2:
                    if f1.read() == f2.read():    # check bytes of the files
                        os.remove(file2)   # removes the duplicate


extensions = {
    ".pdf":"PDFs",
    ".docx": "Word Document",
    ".xlsx": "Excels",
    ".jpg": "Images",
    ".png": "Images",
    ".mp3": "Musics",
    ".mp4": "Videos",
    ".py": "python file",
    ".mkv": "Videos",
    ".dmg": "Installation Folder",
    ".mov": "Iphone Videos",
    ".HEIC":"Iphone Photos",
    ".txt": "Text File",
    ".html": "html file",
    ".jpeg": "Images",
    ".zip": "Zip File",
     ".flac": "Musics"

}   # you can add extensions with your need

for x in os.listdir(Download_Path):
    File_Extension=os.path.splitext(x)[1]
    if File_Extension in extensions:
        Folder_Name=extensions[File_Extension]
        Folder_Path=os.path.join(Download_Path,Folder_Name)
        if not os.path.exists(Folder_Path):
            os.mkdir(Folder_Path)
        File_path=os.path.join(Download_Path,x)
        shutil.move(File_path,Folder_Path)   # moves file to the dedicated directory
    else:
        if File_Extension.strip():
            print("You need to add " + File_Extension + " in the extension dictionary.")

for z in os.listdir("/Users/user/Downloads/Zip File"):
    with ZipFile(os.path.join("/Users/user/Downloads/Zip File", z), "r") as zip_ref:
        zip_ref.extractall("/Users/user/Downloads/Zip File")   # extract zip file to dedicated directory


