import os
import shutil
from datetime import date

src = r'C:\Users\Moritz\Downloads'

today = date.today().strftime("%d-%m-%Y")

for root, subdirs, files in os.walk(src) :
    for file in files:
        path = os.path.join(root, file)
        #Dokumente
        if file.endswith('txt') or file.endswith('odt') or file.endswith('pdf') or file.endswith('rtf') or file.endswith('doc') or file.endswith('docx'):
            dest = os.path.join(r'E:\Downloads\Dokumente', file)
            shutil.move(path, dest)
        #Bilder
        elif file.endswith('jpg') or file.endswith('jpeg'):
            dest = os.path.join(r'E:\Downloads\Bilder', file)
            shutil.move(path, dest)
        #Videos
        elif file.endswith('mp4') or file.endswith('gif') or file.endswith('mpg') or file.endswith('mpeg'):
            dest = os.path.join(r'E:\Downloads\Videos', file)
            shutil.move(path, dest)
        #Präsentationen
        elif file.endswith('ppt') or file.endswith('pptx'):
            dest = os.path.join(r'E:\Downloads\Praesentationen', file)
            shutil.move(path, dest)
        #Musik
        elif file.endswith('mp3') or file.endswith('wav'):
            dest = os.path.join(r'E:\Downloads\Musik', file)
            shutil.move(path, dest)
        #EXE
        elif file.endswith('exe'):
            dest = os.path.join(r'E:\Downloads\EXE', file)
            shutil.move(path, dest)
        #Java
        elif file.endswith('java'):
            dest = os.path.join(r'E:\Downloads\Java', file)
            shutil.move(path, dest)
        #Python
        elif file.endswith('py'):
            dest = os.path.join(r'E:\Downloads\Python', file)
            shutil.move(path, dest)
        #Komprimierte
        elif file.endswith('zip') or file.endswith('tgz') or file.endswith('rar'):
            dest = os.path.join(r'E:\Downloads\Komprimierte Dateien', file)
            shutil.move(path, dest)
        #Sonstiges
        else:
            dest = os.path.join(r'E:\Downloads\Sonstige', file)
            shutil.move(path, dest)