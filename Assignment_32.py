import os
import sys
import shutil
import hashlib
import time
from pathlib import Path

def GetChecksum(path, blocksize=1024):
    hasher = hashlib.md5()
    with open(path, 'rb') as f:
        buf = f.read(blocksize)
        while len(buf) > 0:
            hasher.update(buf)
            buf = f.read(blocksize)
    return hasher.hexdigest()


def DisplayChecksum(DirectoryName):
    for folder, subfolder, filenames in os.walk(DirectoryName):
        for f in filenames:
            path = os.path.join(folder, f)
            print(f"File: {f} | Checksum: {GetChecksum(path)}")


def HandleDuplicates(DirectoryName, delete=False):
    start_time = time.time()
    duplicates = {}  # {checksum: [filepaths]}
    log_file = "Log.txt"
    
    for folder, subfolder, filenames in os.walk(DirectoryName):
        for f in filenames:
            path = os.path.join(folder, f)
            checksum = GetChecksum(path)
            if checksum in duplicates:
                duplicates[checksum].append(path)
            else:
                duplicates[checksum] = [path]


    with open(log_file, "w") as log:
        log.write(f"Duplicate File Log - {time.ctime()}\n\n")
        for check, paths in duplicates.items():
            if len(paths) > 1:
                for dup_path in paths[1:]:
                    log.write(f"Duplicate Found: {dup_path}\n")
                    if delete:
                        os.remove(dup_path)
                        print(f"Deleted: {dup_path}")

    end_time = time.time()
    print(f"\nLog created: {log_file}")
    print(f"Execution Time: {end_time - start_time:.4f} seconds")


def DirectoryCopy(Source, Destination):
    if not os.path.exists(Destination):
        os.makedirs(Destination)
    
    for f in os.listdir(Source):
        src_path = os.path.join(Source, f)
        if os.path.isfile(src_path):
            shutil.copy(src_path, Destination)
    print(f"All files copied from {Source} to {Destination}")


def DirectoryCopyExt(Source, Destination, Extension):
    if not os.path.exists(Destination):
        os.makedirs(Destination)
        
    count = 0
    for f in os.listdir(Source):
        if f.endswith(Extension):
            shutil.copy(os.path.join(Source, f), Destination)
            count += 1
    print(f"Copied {count} files with extension {Extension} to {Destination}")


def main():
    if len(sys.argv) < 2:
        print("Usage: python script.py <task_number> [args...]")
        return

    task = sys.argv[1]

    if task == "checksum": # Q1
        DisplayChecksum(sys.argv[2])
    elif task == "duplicate_log": # Q2
        HandleDuplicates(sys.argv[2], delete=False)
    elif task == "duplicate_remove": # Q3 & Q4
        HandleDuplicates(sys.argv[2], delete=True)
    
    elif task == "copy": # Q3
        DirectoryCopy(sys.argv[2], sys.argv[3])
    elif task == "copy_ext": # Q4
        DirectoryCopyExt(sys.argv[2], sys.argv[3], sys.argv[4])

if __name__ == "__main__":
    main()