# copypasta
A command-line only Unix copy buffer manager in Python, most similar to copyq,
xsel, and xclip, but supporting MIME-type detection to play well with desktop
applications such as LibreOffice and web browsers.

## Author
Jeffrey Baitis, jeff@baitis.net

## Purpose
[copyq](https://github.com/hluk/CopyQ) provides excellent copy and paste
features, including clipboard management.  However, all I really want is
something lightweight to handle shuttling data from the filesystem to and from
the UNIX clipboard, and this is where **copypasta** comes in.

## Features and goals
- UNIX philosophy
- MIME-type detection
- Standard input handling
- Portability and convenience (Python for now!)
