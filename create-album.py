import os
import sys
import shutil
import argparse
import zipfile
from random import shuffle

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("root_dir", help="Directory containing manga folders to process.")
    parser.add_argument("-s", "--shuffle", help="Whether the album images should be shuffled.", action= "store_true")
    parser.add_argument("-r", "--reverse", help="Whether the album should have its images reversed", action="store_true")
    parser.add_argument("-o", "--output", help="Directory to store albums", action="store_true")
    parser.add_argument("-n", "--nested", help= "Whether the source images are nested within a second level folder", action="store_true")
    parser.add_argument("-e", "--extension", help="Which extension to save the album as. Supported: 7z, cbz, zip")

    args = parser.parse_args()

    if args.output == False:
        args.output = args.root_dir
    
    if args.extension is None or args.extension not in [".zip", ".cbz", ".7z"]:
        args.extension = ".cbz"
        
    for dir in os.listdir(args.root_dir):
        full_paths = os.path.join(args.root_dir, dir)

        if args.nested:
            full_paths = os.path.join(args.root_dir, dir, dir)
        process_folder(full_paths, args)

def process_folder(dir, args):
    if os.path.isdir(dir) == False:
        return
    dir_files = os.listdir(dir)
    fullpaths_map = map(lambda name: os.path.join(dir, name), dir_files)

    fullpaths= []
    for path in fullpaths_map:
        fullpaths.append(path)

    dir_name = dir.split("\\")[-1]
    counter = 1
    if args.reverse:
        counter = len(dir_files)

    if args.shuffle:
        shuffle(fullpaths)

    with zipfile.ZipFile(os.path.join(args.output, dir_name + args.extension), 'w') as zip:
        for file in fullpaths:
            if os.path.isfile(file) == False or len(file.split(".")) != 2 or file.split(".")[1] == "zip":
                continue
            #print(os.path.join(args.output, str(counter) + "."+ file.split(".")[1]))
            #shutil.move(file, os.path.join(args.output, str(counter) + "."+ file.split(".")[1]))
            zip.write(file, str(counter) + "."+ file.split(".")[1])
            if args.reverse:
                counter -= 1
            else:
                counter += 1
            #print(os.path.join(dir, file))
        

if __name__ == "__main__":
    main()