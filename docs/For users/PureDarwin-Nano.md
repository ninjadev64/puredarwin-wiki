# PureDarwin Nano

This page describes the minimal components needed for a minimal PureDarwin system (also known as "PureDarwin Nano"). 

## Contents

1.  [Download](#Download)
2.  [Components](#Components)
    1.  [Bootloader](#C-Bootloader)
    2.  [Installer](#C-Installer)
    3.  [Interactive mode](#C-Interactive-mode)
3.  [Virtual machine](#Virtual-machine)
    1.  [VMware](#VM-VMware)
    2.  [QEMU](#VM-QEMU)  

This system is a **proof-of-concept** of a minimal bootable Darwin 9 system that can be built from the components that Apple provides through the [DarwinBuild](http://darwinbuild.macosforge.org/) project.

[![](https://sites.google.com/a/puredarwin.org/puredarwin/downloads/puredarwin-nano/puredarwin.jpg?attredirects=0)](https://sites.google.com/a/puredarwin.org/puredarwin/downloads/puredarwin-nano/puredarwin.jpg?attredirects=0)

-----

<a name="Download"></a>Download
--------

A ready-made VMware virtual machine containing a minimal Darwin 9 system (PureDarwin nano (based on 9C31)) can be downloaded [here](https://sites.google.com/a/puredarwin.org/puredarwin/downloads).  

    MD5  (puredarwinnano0df46.tbz2) = f6853449e263dd83bba0ac9662f29143
    SHA1 (puredarwinnano0df46.tbz2) = 7a32331fcb443538f0737c172160f3cef6067ec9

The virtual machine contains an ISO that could be used on real hardware as well.

<a name="Components"></a>Components
----------
Here is what such a minimal system needs to consist of:


[![Components Screenshot](https://sites.google.com/a/puredarwin.org/puredarwin/_/rsrc/1234090957898/downloads/puredarwin-nano/Bild%202.png)](https://sites.google.com/a/puredarwin.org/puredarwin/downloads/puredarwin-nano/Bild%202.png?attredirects=0)

Notes: [VoodooPS2*](https://github.com/PureDarwin/PureDarwin/wiki/PS2_Controller) or (exclusively) [ACPIPS2Nub.kext](http://code.google.com/p/puredarwin/source/browse/Roots/pd/ACPIPS2Nub.root.tar.gz) and [ApplePS2Controller.kext](http://code.google.com/p/puredarwin/source/browse/Roots/pd/ApplePS2Controller.root.tar.gz) ([sources](http://tgwbd.org/darwin/extensions.html)) are only required if you want to use a PS/2 keyboard and/or mouse.
The number of files can be further brought down by using a [prelinked mach_kernel](https://github.com/PureDarwin/PureDarwin/wiki/XNU,_the_kernel). This removes the need for the System directory.
Using _kextcache_, the boot process can be faster, the image bigger.

### <a name="C-Bootloader"></a>Bootloader

Of course, the system needs to be made bootable by [boot](https://github.com/PureDarwin/PureDarwin/wiki/boot) and/or [efiboot](https://github.com/PureDarwin/PureDarwin/wiki/efiboot). 
Chameleon is reported to work.

### <a name="C-Installer"></a>Installer

An installer is currently being prepared.

### <a name="C-Interactive-mode"></a>Interactive mode

An interactive shell is run by default. In fact, `/sbin/launchd` is replaced by a shell script that runs `/bin/bash`.

[![Interactive Mode Screenshot](https://sites.google.com/a/puredarwin.org/puredarwin/_/rsrc/1234090957898/downloads/puredarwin-nano/bash%20interactive%20mode%20in%20nano.png)](https://sites.google.com/a/puredarwin.org/puredarwin/downloads/puredarwin-nano/bash%20interactive%20mode%20in%20nano.png?attredirects=0)

The Z shell (zsh) is also usable as an interactive UNIX command interpreter (shell).

[![ZSH Screenshot](https://sites.google.com/a/puredarwin.org/puredarwin/_/rsrc/1234090957898/downloads/puredarwin-nano/VMware%20running%20PureDarwin%20nano%20with%20interactive%20commands.png)](https://sites.google.com/a/puredarwin.org/puredarwin/downloads/puredarwin-nano/VMware%20running%20PureDarwin%20nano%20with%20interactive%20commands.png?attredirects=0)

<a name="Virtual-machine"></a>Virtual machine
---------------
"PureDarwin nano" reported to work with VMware products (Fusion and Player), QEMU and VirtualBox
See [VMware](https://github.com/PureDarwin/PureDarwin/wiki/vmware) page, [QEMU](https://github.com/PureDarwin/PureDarwin/wiki/qemu) page and [VirtualBox](https://github.com/PureDarwin/PureDarwin/wiki/virtualbox) page for more information.

### <a name="VM-VMWarwe"></a>VMware

[![VMWare Screenshot](https://sites.google.com/a/puredarwin.org/puredarwin/_/rsrc/1234090957898/downloads/puredarwin-nano/nanovmwarelittlegray.png)](https://sites.google.com/a/puredarwin.org/puredarwin/downloads/puredarwin-nano/nanovmwarelittlegray.png?attredirects=0)

### <a name="VM-QEMU"></a>QEMU

[![QEMU Screenshot](https://sites.google.com/a/puredarwin.org/puredarwin/_/rsrc/1254082132956/downloads/puredarwin-nano/qemu1.png?height=321&width=420)](https://sites.google.com/a/puredarwin.org/puredarwin/downloads/puredarwin-nano/qemu1.png?attredirects=0)