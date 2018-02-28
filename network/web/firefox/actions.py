#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# LimeLinux 2017
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools, pisitools, shelltools, get




ObjDir = "build"
arch = get.ARCH()

shelltools.export("SHELL", "/bin/sh")

def setup():
    shelltools.export("CFLAGS", "%s -fno-delete-null-pointer-checks -fno-lifetime-dse -fno-schedule-insns2" % get.CFLAGS())
    shelltools.export("CXXFLAGS", "%s -fno-delete-null-pointer-checks -fno-lifetime-dse -fno-schedule-insns2" % get.CFLAGS())
    pisitools.dosed(".mozconfig", "##JOBCOUNT##", get.makeJOBS())
    shelltools.makedirs(ObjDir)
    shelltools.cd(ObjDir)
    shelltools.system("../configure --prefix=/usr --libdir=/usr/lib")

    

def build():
    shelltools.cd(ObjDir)
    autotools.make("./mach build")
    autotools.make("./mach buildsymbols")


def install():
    shelltools.cd(ObjDir)
    shelltools.export("CFLAGS", "%s -fno-delete-null-pointer-checks -fno-lifetime-dse -fno-schedule-insns2" % get.CFLAGS())
    shelltools.export("CXXFLAGS", "%s -fno-delete-null-pointer-checks -fno-lifetime-dse -fno-schedule-insns2" % get.CFLAGS())
    shelltools.system("DESTDIR=%s ./mach install " % get.installDIR())

    # Install language packs
    pisitools.insinto("/usr/lib/firefox/browser/extensions", "./lang_pack/*")

    # Create profile dir, we'll copy bookmarks.html in post-install script
    pisitools.dodir("/usr/lib/firefox/browser/defaults/profile")

    # Install branding icon
    pisitools.insinto("/usr/share/pixmaps", "browser/branding/official/default256.png", "firefox.png")
    
    # Install docs
    pisitools.dodoc("LEGAL", "LICENSE")
