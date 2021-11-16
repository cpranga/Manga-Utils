import os
import sys
import shutil
import argparse
import zipfile


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("root_dir", help="Directory containing manga folders to process.")
    parser.add_argument("-s", "--shuffle", help="Whether the album images should be shuffled.", action= "store_true")
    parser.add_argument("-r", "--reverse", help="Whether the album should have its images reversed", action="store_true")
    parser.add_argument("-o", "--output", help="Directory to store albums", action="store_true")
    parser.add_argument("-n", "--nested", help= "Whether the source images are nested within a second level folder", action="store_true")

    args = parser.parse_args()

    if args.output == False:
        args.output = args.root_dir
    
    for dir in os.listdir(args.root_dir):
        full_paths = os.path.join(args.root_dir, dir)

        if args.nested:
            full_paths = os.path.join(args.root_dir, dir, dir)
        process_folder(full_paths, args)

def process_folder(dir, args):
    dir_files = os.listdir(dir)
    fullpaths = map(lambda name: os.path.join(dir, name), dir_files)
    
    counter = 1
    if args.reverse:
        counter = len(dir_files)

    with zipfile.ZipFile(os.path.join(args.output, "t.zip"), 'w') as zip:
        for file in fullpaths:
            if os.path.isfile(file) == False or file.split(".")[1] == "zip":
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