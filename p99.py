import os
import shutil
import time

days=30
tem = time.time()-(days*24*60*60)
srcpath = input("enter the path of source")

deleted_folder = 0 
deleted_file = 0

if os.path.exists(srcpath):

    for (root,dirs,files) in os.walk(srcpath):

        srctime=os.stat(srcpath).st_ctime

        if srctime < tem :
            shutil.rmtree(srcpath)
            deleted_folder +=1
            print("deleted source folder"+str(deleted_folder))
            print("")
            break

        else:
            for i in files:
                pathway = root+"/"+i
                ctime=os.stat(pathway).st_ctime

                if ctime<tem :
                    print(i)                
                    os.remove(pathway)
                    deleted_file +=1
                    print("no of files deleted"+str(deleted_file))
                    print("")


            for d in dirs :     
                pathway = root+"/"+d
                ctime=os.stat(pathway).st_ctime

                if ctime<tem :
                    print(d)
                    shutil.rmtree(pathway)
                    deleted_folder+=1
                    print("deleted no of folders"+str(deleted_folder))
                    print("")
