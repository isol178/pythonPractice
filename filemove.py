import os
import shutil

#このソースファイルがあるディレクトリのひとつ下のディレクトリにあるpdfファイルを抜き出すコード
tempdir = os.getcwd()
sub = os.listdir(tempdir)
subdir = [f for f in sub if os.path.isdir(os.path.join(tempdir, f))] #ディレクトリのみ抜き出す

for d in subdir:
    contents = os.listdir(d)
    files = [f for f in contents if os.path.isfile(os.path.join(tempdir + "/" + d, f))]
    for f in files:
         if f.endswith(".pdf"): #拡張子の指定
              shutil.move(tempdir + "/" + d + "/" + f, tempdir)

print("finished")
