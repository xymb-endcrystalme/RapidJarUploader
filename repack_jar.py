#!/usr/bin/env python3

import io
import os
import os.path
import sys
import zipfile
import zipp

def recursive_pack_jar(folder):
    bytesio = io.BytesIO()
    archive = zipfile.ZipFile(bytesio, "w")
    for absolute_path, dirs, files in os.walk(folder):
        relative_path = os.path.relpath(absolute_path, folder)
        if '.jar' in relative_path: continue
        for directory in dirs:
            if directory.endswith('.jar'):
                archive.open(os.path.join(relative_path, directory), "w").write(recursive_pack_jar(os.path.join(absolute_path, directory)))

        for file in files:
            data = open(os.path.join(absolute_path, file), "rb").read()
            archive.open(os.path.join(relative_path, file), "w").write(data)

    archive.close()
    return bytesio.getvalue()

if __name__ == "__main__":
    destination_dir = sys.argv[1]
    jar_file = sys.argv[2]
    print("Repacking", destination_dir, "to", jar_file)
    final_jar = recursive_pack_jar(destination_dir)
    open(jar_file, "wb").write(final_jar)
    print("Done", len(final_jar))
