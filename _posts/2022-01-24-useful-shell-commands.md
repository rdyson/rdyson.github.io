---
layout: post
title: "Useful Shell Commands"
date: "2022-01-24 14:30:00"
categories: development
---

My own sort of [commandlinefu](https://www.commandlinefu.com).

* [File operations](#file-operations)
* [List and find files](#list-and-find-files)
* [Folders](#folders)
* [Text files](#text-files)
* [CSVs](#csvs)
* [Networking](#networking)
* [Images](#images)
* [Video](#video)
* [Miscellaneous](#miscellaneous)

## File operations

Run a command for multiple files
```sh
for i in *; do tinypng $i; done;
```

Batch prepend filename
```sh
for f in *.jpg; do mv "$f" "Image Foo - $f"; done
```

Batch rename files
```sh
for i in * ; do j=`echo $i | sed 's#searchstring#replacestring#g' - ` ; mv "$i" "$j" ; done
```

Batch rename part of a filename (have to install rename from brew)
```sh
rename 's/.txt/.md/i' *
```

Remove spaces from filenames
```sh
find . -depth -name '* *' | while IFS= read -r f ; do mv -i "$f" "$(dirname "$f")/$(basename "$f"|tr ' ' _)" ; done
```

Copy files by extension to new directory
```sh
ls *.jpg | xargs -n1 -i cp {} /directory
```

Wildcards and tokens
```sh
for file in *.src; do mv ${file} ${file%.src}.c; done
```


## List and find files

ls by size
```sh
ls -S
```

ls order by last modified
```sh
ls -ltr
```

ls files in subdirectories
```sh
ls *
```

Find all files with extension
```sh
find -name "*.xcf"
```

Find and copy all files by extension
```sh
cp `find / -name "*.jpg"` .
```

Find files modified in last x mins
```sh
find / -mmin -120
```

Find files larger than a certain size
```sh
find /etc -size 100k
```

Find large directories
```sh
du -h /|grep M|sort -nr|head -15
```

Find total size of directory (including subdirectories)
```sh
du -ch directory
```

Find files owned by specific group
```sh
find -group {group_name}
```

Find and delete files with a specific name
```sh
find /home/userA/folderA/* -type f \( -name "delete1.txt" -or -name "delete2.txt" \) -delete
```

Sort directory by file size
```sh
du -h | sort -n
```

Print the file count per subdirectory
```sh
du -a | cut -d/ -f2 | sort | uniq -c | sort -nr
```

## Folders

Create nested dirs
```sh
mkdir -p dir1/dir2/dir3/dir4/
```

Create folders based on list of filenames
```sh
for file in *.mov; do mkdir -- "${file%.mov}"; mv -- "$file" "${file%.mov}"; done
```

Move files out of nested folders
```sh
find ~/foo/ -type f -print0 | xargs -0 mv -t ~/bar
```

Differences between folder contents
```sh
diff -rq folder1 folder2
```

Recursive difference between folder contents
```sh
diff <(cd dir1 && find | sort) <(cd dir2 && find | sort)
```

Delete all subdirectories with a specific name
```sh
find /home/userA/folderA/* -depth -name "match" -type d -exec rm -rfv "{}" \;
```


## Text files

Insert header row into file
```sh
sed '1i FRUITS' file1
```

Remove first line of file
```sh
sed '1d' INPUT_FILE_NAME
```

Substitute "foo" with "bar" only for lines which contain "baz"
```sh
sed '/baz/s/foo/bar/g'
```

Find human readable strings in a file
```sh
strings data.txt
```

Find lines that occur only once
```sh
sort data.txt | uniq -u
```

Find similarities between two files
```sh
grep -Fx -f file1 file2
```

Remove duplicate lines
```sh
sort -u myfile.csv
```

Grep recursively, return only filenames
```sh
grep -rl foo .
```

Grep for multiple terms
```sh
grep 'word1' filename | grep 'word2'
```


## CSVs

Keep certain columns from a csv
```sh
cut -d ',' -f 1,2,3 old.csv > new.csv
```

Remove non-adjacent duplicates
```sh
cat test.csv | perl -ne '$H{$_} or print' > test_nodupes.csv
```


## Networking

Check open ports
```sh
nmap -sS 127.0.0.1
```

Get IP address
```sh
curl ifconfig.me
```

Ping  every 10 seconds, audible bell if no response
```sh
ping -i 10 -A 127.0.0.1
```

Download all URLs in file
```sh
cat url-list.txt | xargs wget –c
```


## Images

Find dimensions of image with ImageMagick
```sh
identify -format '%w %h\n' flat/bg-flat-hero.jpg
```

Convert image format
```sh
mogrify -format png *.jpg
```

Replace color in batch of images; first color is to, second is from
```sh
mogrify -path batch -format png -fuzz 10% -fill "#003A70" -opaque "#15ACCF" *.png
```


## Video

Bulk convert using ffmpeg
```sh
find . -name '*.avi' -exec ffmpeg -i {} {}.mpg \;
```

Combine video files using ffmpeg given a list of files
```sh
# mylist.txt
file '/path/to/file1'
file '/path/to/file2'
file '/path/to/file3'
```

```sh
ffmpeg -f concat -safe 0 -i mylist.txt -c copy output.mp4
```

Convert mov to mp4
```sh
find . -name '*.mov' -exec ffmpeg -i {} {}.mp4 \;
```

Resize video
```sh
for x in *.mp4; do ffmpeg -i $x -vf scale=iw/2:ih/2 shrunk-$x; done
```
or

```sh
for x in *.mp4; do ffmpeg -i $x -vf scale=320:-1 shrunk-$x; done
```


## Miscellaneous

Sudo run last command
```sh
sudo !!
```

Run a command every 30 seconds
```sh
while true; do diskutil cs list | grep 'Conversion Progress' ; sleep 30; done
```

Another way to run a command every 30 seconds
```sh
watch -n 30 ls -l
```

Create a tar.gz
```sh
tar -pczf name_of_your_archive.tar.gz /path/to/directory
```

Extract first 10 seconds from wav file
```sh
sox input.wav output.wav trim 0 10
```

Alert when a process finishes
```
ls && tput bel
```

Open multiple URLs in Chrome
```sh
open -a "Google Chrome.app" https://cnn.com https://google.com https://duckduckgo.com
```
