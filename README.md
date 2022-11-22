# RapidJarUploader
Upload .jars over slow connections way faster with rsync.

## Usage
### Prerequisites
```
sudo apt -y install python3-pip
sudo pip3 install zipp
```
### Your development machine
```
./unpack_jar.py ~/MultiPaper/build/libs/MultiPaper-bundler-1.19.2-R0.1-SNAPSHOT-reobf.jar /tmp/multipaper/ "MultiPaper-MasterMessagingProtocol-1.19.2-R0.1-SNAPSHOT.jar|MultiPaper-API-1.19.2-R0.1-SNAPSHOT.jar|multipaper-1.19.2.jar"
rsync -va multipaper root@youserver.org:/tmp/multipaper
```
### Remote server
```
./repack_jar.py /tmp/multipaper multipaper.jar
```

## Caveat
RapidJarUploader doesn't support file removal. If you need to remove files just rm the directory on source and rsync with --delete.
I personally don't need that feature. Patches are welcome.