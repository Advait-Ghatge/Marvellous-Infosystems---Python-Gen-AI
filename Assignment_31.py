import sys
import os
import shutil
from pathlib import Path

def DirectoryScanner(DirectoryName):

    if (os.path.exists(DirectoryName) == False):

        print()
        print("The given directory is not found in current folder")
        return
    
    if (os.path.isdir(DirectoryName) == False):

        print()
        print("The given input does not map to a directory")
        return
    
    else:

        print()
        print("Directory found :", DirectoryName)


def FileExtension(DirectoryName, Extension = ".py"):
    
    for FolderName, SubFolderName, FileName in os.walk(DirectoryName) :


        for FName in FileName :

            FileStr = str(FName)

            if FileStr.endswith(Extension):
                print()
                print("Filename is -", FName)


def main():
    
    # Answer 1
    
    if (len(sys.argv) != 3):

        print()
        print("Insufficient number of command line arguments for Q1")
        print()
        return

    Dir1 = sys.argv[1]
    Ext1 = sys.argv[2]

    DirectoryScanner(Dir1)

    if Ext1.startswith("."):
        
        print()
        print("File extension is valid!")
        print("File extension is :", Ext1)

        FileExtension(Dir1, Ext1)

    else:

        print()
        print("Given extension is not valid")
        return
    

# Answer 2

def RenameExt(DirectoryName, Extension1, Extension2):
    
    ext1 = Extension1 if Extension1.startswith('.') else f'.{Extension1}'
    ext2 = Extension2 if Extension2.startswith('.') else f'.{Extension2}'
    
    for folder_name, sub_folders, file_names in os.walk(DirectoryName):
        for f_name in file_names:
            
            if f_name.endswith(ext1):
                
                old_path = Path(folder_name) / f_name
                
                new_path = old_path.with_suffix(ext2)
                
                old_path.rename(new_path)
                
                print(f"Renamed: {old_path.name} -> {new_path.name}")

# Answer 3

def DirectoryCopy(SourceDir, DestDir):
    try:
        
        if not os.path.exists(DestDir):
            os.makedirs(DestDir)
            print(f"Created destination directory: {DestDir}")
        
        for folder_name, sub_folders, file_names in os.walk(SourceDir):
            for f_name in file_names:
                source_path = os.path.join(folder_name, f_name)
                shutil.copy(source_path, DestDir)
        
        print(f"Successfully copied all files to {DestDir}")
    except Exception as e:
        print(f"An error occurred: {e}")


# Answer 4

def DirectoryCopyExt(SourceDir, DestDir, Extension):
    try:
        if not os.path.exists(DestDir):
            os.makedirs(DestDir)
            print(f"Created destination directory: {DestDir}")

        count = 0
        for folder_name, sub_folders, file_names in os.walk(SourceDir):
            for f_name in file_names:
                if f_name.endswith(Extension):
                    source_path = os.path.join(folder_name, f_name)
                    shutil.copy(source_path, DestDir)
                    count += 1
        
        print(f"Successfully copied {count} files with extension '{Extension}' to {DestDir}")
    except Exception as e:
        print(f"An error occurred: {e}")


def main3():

    if len(sys.argv) == 3:
        src = sys.argv[1]
        dest = sys.argv[2]
        if DirectoryScanner(src):
            DirectoryCopy(src, dest)


    elif len(sys.argv) == 4:
        src = sys.argv[1]
        dest = sys.argv[2]
        ext = sys.argv[3]
        if DirectoryScanner(src):
            DirectoryCopyExt(src, dest, ext)
    
    else:
        print("\nInvalid Usage.")
        print("Usage for Q3: script.py <SourceDir> <DestDir>")
        print("Usage for Q4: script.py <SourceDir> <DestDir> <Extension>")


def main2():
    
    if (len(sys.argv) != 4):

        print()
        print("Insufficient number of command line arguments for Renaming Extension")
        print()
        return

    Dir1 = sys.argv[1]
    Ext1 = sys.argv[2]
    Ext2 = sys.argv[3]


    if Ext1.startswith("."):
        
        print()
        print("File extension is valid!")
        print("File extension is :", Ext1)


    else:

        print()
        print("Given extension is not valid")
        return


    RenameExt(Dir1, Ext1, Ext2)


if __name__ == "__main__":
    main()
    main2()
    main3()