#!/usr/local/bin/python
# Based on HalosGost post http://unix.stackexchange.com/a/165597/72860
# Note that the magic library here is "python-magic"
# There is some python module naming collision that can occur

# v0.1 FIXME: Problems with loading very large images

import sys
import magic
from gi.repository import Gtk, Gdk, GdkPixbuf


def copy_image(f):
    global clipboard
    image = Gtk.Image.new_from_file(f)
    if image.get_storage_type() == Gtk.ImageType.PIXBUF:
        clipboard.set_image(image.get_pixbuf())
        clipboard.store()
    else:
        print("No image has been pasted yet.")

def copy_text(f):
    global clipboard
    #filter_text = Gtk.FileFilter()
    #filter_text.set_name("RTF file")
    #filter_text.add_mime_type("text/rtf")
    with open(f, 'r') as d:
      buf = d.read()
      clipboard.set_text(buf, -1)
      clipboard.store()


clipboard = Gtk.Clipboard.get(Gdk.SELECTION_CLIPBOARD)
m = magic.open(magic.MAGIC_MIME_TYPE)
m.load()
if (m is None):
  print("Unable to load Magic library")
  exit(-1)

if sys.stdin.isatty():
    if len(sys.argv) != 2:
        print("Usage: copypasta file")
    else:
        f = sys.argv[1]
        mimetype = m.file(f)
        print mimetype
        if mimetype is None or "image" not in mimetype:
          copy_text(f)
        else:
          copy_image(f)
else:
    data = sys.stdin.read(1024) # Enough for mime taste
    mimetype = m.buffer(data)
    # Continue reading
    data += sys.stdin.read()
    print mimetype
    if mimetype is None or "image" not in mimetype:
      clipboard.set_text(data, -1)
    else:
      loader = GdkPixbuf.PixbufLoader()
      status = loader.write(data)
      clipboard.set_image(loader.get_pixbuf())
      loader.close()
    clipboard.store()
