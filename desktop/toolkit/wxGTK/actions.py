# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    pisitools.flags.add("-fno-strict-aliasing")

    autotools.configure("--enable-shared \
                         --disable-optimise \
                         --disable-debug \
                         --disable-rpath \
                         --enable-intl \
                         --enable-timer \
                         --enable-unicode \
                         --enable-sound \
                         --enable-mediactrl \
                         --enable-xrc \
                         --enable-graphics_ctx \
                         --enable-display \
                         --enable-joystick \
                         --disable-gtktest \
                         --disable-sdltest \
                         --disable-precomp-headers \
                         --with-gtk=3 \
                         --with-libpng=sys \
                         --with-libjpeg=sys \
                         --with-libtiff=sys \
                         --with-libxpm=sys \
                         --with-sdl \
                         --without-gnomevfs \
                         --with-opengl \
                         --with-regex=builtin \
                         --with-zlib=sys \
                         --with-expat=sys")

def build():
    autotools.make()
    autotools.make("-C locale allmo")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    #autotools.install()

    pisitools.dodoc("docs/*.txt", "docs/*.htm")
