#!/usr/bin/env python
import os


KernelVersion = "4.13.2"

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    gcf = "/boot/grub2/grub.cfg"
    if not os.path.isfile(gcf): return


    os.environ["PATH"] = "/usr/sbin:/usr/bin:/sbin:/bin"
    os.system("grub2-mkconfig -o %s" % gcf)
    os.system("mkinitcpio -p linux")

    # Must run depmod to keep the modules up to date
    os.system("/sbin/depmod %s" % KernelVersion)
