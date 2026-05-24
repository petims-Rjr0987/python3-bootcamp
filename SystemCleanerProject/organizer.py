import os
import shutil

def files_organizer(directory_path):  
    for filename in os.listdir(directory_path):
        full_path =  os.path.join(directory_path , filename)
        if os.path.isfile(full_path):
            
            if '.' in filename:
                file_extension = filename.split('.')[-1].lower()
            else:
                file_extension= "sans extention"

            folder_name = os.path.join(directory_path , file_extension)

            if not os.path.exists(folder_name):
                os.makedirs(folder_name)
            elif os.path.exists(folder_name) and not os.path.isdir(folder_name):
                print(f"⚠️ Conflit : Un fichier nommé '{file_extension}' empêche le rangement des fichiers .{file_extension}")
            
            shutil.move(full_path , os.path.join(folder_name , filename))

    print("Cleaning complete")
