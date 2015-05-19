#!/usr/local/bin/python
# Based on HalosGost post http://unix.stackexchange.com/a/165597/72860
# Note that the magic library here is "python-magic"
# There is some python module naming collision that can occur

# v0.1 FIXME: Problems with loading very large images

import sys
import magic
from gi.repository import Gtk, Gdk, GdkPixbuf

clipboard = Gtk.Clipboard.get(Gdk.SELECTION_CLIPBOARD)
m = magic.open(magic.MAGIC_MIME_TYPE)
m.load()
if (m is None):
  print("Unable to load Magic library")
  exit(-1)

source = None
data = None

if sys.stdin.isatty():
  if len(sys.argv) != 2:
    print("Usage: copypasta file, or pipe stdout into copypasta")
  else:
    source = open (sys.argv[1], 'r')
else:
  source = sys.stdin

# Taste the source
data = source.read(1024) # Enough for mime taste
mimetype = m.buffer(data)
      
# Continue reading
data += source.read()
print mimetype
if mimetype is None or "image" not in mimetype:
  clipboard.set_text(data, -1)
else:
  loader = GdkPixbuf.PixbufLoader()
  status = loader.write(data)
  clipboard.set_image(loader.get_pixbuf())
  loader.close()

clipboard.store()
