#!/usr/bin/env python3

import sys
import zipfile
import zipp
import os.path
import io
import time
from pathlib import Path

def recursive_unpack_jar(jar, folder, jars_to_unpack):
    with zipfile.ZipFile(jar, "r") as archive:
        for zip_path in archive.namelist():
            path = zipp.Path(archive, zip_path)
            if path.is_dir():
                Path(os.path.join(folder, zip_path)).mkdir(parents=True, exist_ok=True)
            if path.is_file():
                Path(os.path.dirname(os.path.join(folder, zip_path))).mkdir(parents=True, exist_ok=True)
                destination_jar = False
                for unpack in jars_to_unpack:
                    if unpack in zip_path: destination_jar = True
#                if zip_path.endswith(".jar"): destination_jar = True
                if destination_jar == True:
                    Path(os.path.join(folder, zip_path)).mkdir(parents=True, exist_ok=True)
                    recursive_unpack_jar(io.BytesIO(path.read_bytes()), os.path.join(folder, zip_path), jars_to_unpack)
                else:
                    data = path.read_bytes()
                    write_file = False
                    if not Path(os.path.join(folder, zip_path)).exists(): write_file = True
                    else:
                        old_data = open(os.path.join(folder, zip_path), "rb").read()
                        if old_data != data:
                            write_file = True
                    if write_file:
                        print("Writing file", zip_path)
                        open(os.path.join(folder, zip_path), "wb").write(data)

if __name__ == "__main__":
    jar_file = sys.argv[1]
    destination_dir = sys.argv[2]
    jars_to_unpack = sys.argv[3].split("|")
    print("Unpacking", jar_file, "to", destination_dir)
    recursive_unpack_jar(jar_file, destination_dir, jars_to_unpack)
    print("Done")
