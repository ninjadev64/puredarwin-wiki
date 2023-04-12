Visualize mach-o dependencies
=============================
In the spirit of [Vizualize dependencies in MacPorts](../macports/macports-dependencies-overview.html) and [Vizualize KEXTs dependencies](../kexts/kexts-dependencies-overview.html), this page describes a way to track mach-o file dependencies and related satellite information (e.g: blockers).


<div class="sites-embed-border-off sites-embed" style="width:444px;">


Contents
1.  [**1** Prerequisites](mach-o-dependencies-overview.html#TOC-Prerequisites)
2.  [**2** Using pd_machviz to generate a graph](mach-o-dependencies-overview.html#TOC-Using-pd_machviz-to-generate-a-graph)
    1.  [**2.1** A simple example across otool dependencies](mach-o-dependencies-overview.html#TOC-A-simple-example-across-otool-dependencies)
    2.  [**2.2** A circular view of xterm dependencies](mach-o-dependencies-overview.html#TOC-A-circular-view-of-xterm-dependencies)
    3.  [**2.3** Checking for purity in passwd](mach-o-dependencies-overview.html#TOC-Checking-for-purity-in-passwd)
3.  [**3** Resources](mach-o-dependencies-overview.html#TOC-Resources)

### Prerequisites

[Graphviz](http://www.graphviz.org/) is an opensource graph visualization software from AT&T Laboratories and Bell Laboratories (Lucent Technologies).

<div style="font-family:courier new,monospace">
port install graphviz +the_variants_you_need

or grab and compile the source from [graphviz.org](http://graphviz.org/).
__Note:__ On Mac OS X, [Pixelglow](http://www.pixelglow.com/graphviz/) is a nice a front-end, you can even see the graph being built in real-time.
### Using pd_machviz to generate a graph
The *[pd_machviz](http://code.google.com/p/puredarwin/source/browse/trunk/scripts/pd_machviz)* tool is available in the [svn/hg trunk](http://code.google.com/p/puredarwin/source/browse/trunk/scripts/).
#### A simple example across otool dependencies
A hierarchical view:

![](/img/developers/otool/mach-o-dependencies-overview/otool.dot_directed.png)

The corresponding script output:

<div style="font-family:courier new,monospace">
./pd_machviz /usr/bin/otool
<div style="font-family:courier new,monospace">

<div style="font-family:courier new,monospace">
Generate dependencies graphs of /usr/bin/otool
<div style="font-family:courier new,monospace">


<div style="font-family:courier new,monospace">
 Legend:
<div style="font-family:courier new,monospace">
 1  + foo
<div style="font-family:courier new,monospace">
 2  |`- bar                                             No more dependency
<div style="font-family:courier new,monospace">
 2  |`+ baz impure! /Blocker_1 -> file_involved_1       Impurity detected
<div style="font-family:courier new,monospace">
 2  |`+ baz impure! /Blocker_. -> file_involved_.       Impurity detected
<div style="font-family:courier new,monospace">
 2  |`+ baz impure! /Blocker_n -> file_involved_n       Impurity detected
<div style="font-family:courier new,monospace">
 2  |`+ baz                                             Dependency found
<div style="font-family:courier new,monospace">
 3  | |`. qux                                           Cached file (Already processed)
<div style="font-family:courier new,monospace">


<div style="font-family:courier new,monospace">
Now generating dependencies tree, please wait...
<div style="font-family:courier new,monospace">


<div style="font-family:courier new,monospace">
 1  + /usr/bin/otool
<div style="font-family:courier new,monospace">
 2  |`+ /usr/lib/libgcc_s.1.dylib
<div style="font-family:courier new,monospace">
 3  | |`+ /usr/lib/libSystem.B.dylib
<div style="font-family:courier new,monospace">
 4  | | |`- /usr/lib/system/libmathCommon.A.dylib
<div style="font-family:courier new,monospace">
 2  |`. /usr/lib/libSystem.B.dylib
<div style="font-family:courier new,monospace">
Generation of otool.dot complete.
<div style="font-family:courier new,monospace">


<div style="font-family:courier new,monospace">
Now drawing graphs from otool.dot, please wait...
<div style="font-family:courier new,monospace">
Generation of otool.dot_directed.png complete.
<div style="font-family:courier new,monospace">
Generation of otool.dot_circular.png complete.
<div style="font-family:courier new,monospace">
Generation of otool.dot_radial.png complete.
<div style="font-family:courier new,monospace">
Generation of otool.dot_undirected.png complete.
<div style="font-family:courier new,monospace">
Generation of otool.dot_undirectedBIS.png complete.
#### A circular view of xterm dependencies

![](/img/developers/otool/mach-o-dependencies-overview/xterm.dot_circular.png)
#### Checking for purity in passwd

![](/img/developers/otool/mach-o-dependencies-overview/passwd.dot_undirectedBIS.png)

### Resources {style="margin:10px 10px 10px 0px;background-color:transparent;color:rgb(0,0,0);font-family:Arial,Verdana,sans-serif;font-size:18px"}
[http://www.graphviz.org](http://www.graphviz.org/)
the [otool](../otool.html) page

