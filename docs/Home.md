---
slug: /
---

Welcome
=======

![](https://raw.github.com/wiki/PureDarwin/PureDarwin/images/PD-Opennow.jpg)

[Darwin](http://en.wikipedia.org/wiki/Darwin_%28operating_system%29) is the Open Source operating system from Apple that forms the basis for Mac OS X, and PureDarwin is a community project to make Darwin more usable (some people think of it as the informal successor to OpenDarwin).

One current goal of this project is to provide a useful bootable ISO of Darwin 10.x and Darwin 9.x.
Another goal of this project is to provide additional documentation. [More](1.-About)...

Documentation and quick hints
-----------------------------
Please see the right-hand side navigation bar (under "**Pages**") for wiki documentation. Note that due to the migration of this content from Google Pages to this GitHub Wiki some links might be broken. In this case you should be able to find the correct page in the right-hand side navigation. It would be very kind if you could fix the wiki in this case.

See the [Changelog](_history) for recent updates of this Wiki.

*NEW!* Getting the code
-------------------------
We have just finished migrating the project repository from [Google Code](https://code.google.com/p/puredarwin), to [GitHub](https://github.com/PureDarwin/PureDarwin), and encourage visitors to use the GitHub repository for both contribution, and checking out the latest build source. 

Additionally, as an interim measure, a [version of PureDarwin Xmas](https://github.com/PureDarwin/LegacyDownloads/releases/download/PDXMASNBE01/NewBootEnvironment-XMas-1.7z) with a fixed boot sector, which is compatible with QEMU is also available. 

Status
------

MacPorts is running on PureDarwin 9, potentially giving us thousands of open source software titles.

![](https://raw.github.com/wiki/PureDarwin/PureDarwin/images/macports_on_pd.jpg)

The screenshot above shows a PureDarwin 9 system created from the scripts in our repository, running on real hardware, using TightVNC and [XFCE](Xfce) from MacPorts.

This page shows where we currently are (see the [current blockers](2.-Current-Blockers)).

As of now, you can either build a PureDarwin system yourself based on the information on this site and our and Apple's Open Source and DarwinBuild source code repositories, or download "[PureDarwin Xmas](Xmas)", a developer preview of the operating system based on Apple's Darwin 9 sources and other Open Source projects.

At the same time, the PureDarwin project would like to invite the community to discuss, participate and contribute.

The developer preview is available for download as a pre-configured virtual machine for [VMware](VMware) Fusion 2.0 on Macintosh, and the code used to generate it is available in a Subversion/Mercurial repository form.

A minimal PureDarwin system known as "[PureDarwin Nano](PureDarwin-Nano)" is also available, where only one process is running (a shell).

Credits
-------

We would like to thank
-   [Apple](https://github.com/apple), Inc. for releasing Darwin as Open Source 
-   kvv and _wms for their continuing help
-   Adam Baxter for finding a Gold Sponsor to provide a hosted Mac mini from [MacStadium](http://www.macstadium.com)
-   David Elliott for his work on boot-132
-   The Chameleon team for their work on boot-132
-   The xnu-dev team for their work on the XNU kernel
-   Stuart Crook for his work on PureFoundation
-   Guillaume Verdeau for his work on X.Org
-   Rafirafi for his work on Generic Platform kexts
-   Mac OS Forge 
-   The DarwinBuild project 
-   The MacPorts project
-   The folks at #macosforge, #macports, #macdev, #opendarwin, #puredarwin, 
-   Everyone else contributing to Darwin 

The Wiki pages were recently moved from [Google Sites](https://sites.google.com/a/puredarwin.org/puredarwin/) and in the conversion process some formatting was lost. Please help fixing the markdown of this page by editing it. But please delete nothing, especially not (broken) images; fix them instead (see the main page of the Wiki for an example). 