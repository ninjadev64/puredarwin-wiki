The Z shell
===========
<div style="margin:5px 10px;display:inline;float:right">
[![](../_/rsrc/1223242963057/users/zsh/wizard.gif)](zsh/wizard.gif%3Fattredirects=0)
This page is about using zsh on PureDarwin system.
Normally, PureDarwin comes with the bash shell which most users will be familiar with.
Some users might prefer to use zsh however. This page is a work in progress, please feel free to contribute.


<div class="sites-embed-border-off sites-embed" style="width:250px;">


Contents
1.  [**1** Availability](zsh.html#TOC-Availability)
    1.  [**1.1** In PureDarwin](zsh.html#TOC-In-PureDarwin)
    2.  [**1.2** In the DarwinBuild project](zsh.html#TOC-In-the-DarwinBuild-project)
    3.  [**1.3** In the MacPorts project](zsh.html#TOC-In-the-MacPorts-project)
2.  [**2** Changing an user's default shell](zsh.html#TOC-Changing-an-user-s-default-shell)
3.  [**3** zshrc](zsh.html#TOC-zshrc)
4.  [**4** Resources](zsh.html#TOC-Resources)

### Availability
#### In PureDarwin
Available.
#### In the DarwinBuild project
Available.
See the [DarwinBuild](../developers/darwinbuild.html) page on how to compile a project if needed.
#### In the MacPorts project
Available.
Take a look at [Using the MacPorts project](../developers/macports.1.html) page for more information about MacPorts if you don't know how to build it.


__Note:__ You should also take a look in the available variants (you can use `port info zsh` or `port variants zsh` if you want to know the description associated to the respective variant).
The zsh port appears to be "[pure](../developers/macports/purity.html)" as shown below.

[![](../_/rsrc/1224017323026/users/zsh/pd_portviz%20zsh_directed.png%3Fheight=200&width=143)](zsh/pd_portviz%20zsh_directed.png%3Fattredirects=0)

### Changing an user's default shell
To use zsh as the default shell of the currently logged-in user, do

chsh -s /bin/zsh

To revert back to bash, do 

chsh -s /bin/bash
### zshrc
Populate your ~/.zshrc (or /etc/zshrc) with:


`export PATH=/bin:/sbin:/usr/bin:/usr/sbin:/usr/local/bin:/usr/local/sbin:/usr/libexec:/System/Library/CoreServices`
`export PATH=/opt/local/bin:/opt/local/sbin:$PATH`
`export PATH=/usr/X11R6/bin:$PATH`
`export EDITOR=/usr/bin/vi`
`alias ll='ls -lh'`
`PS1='%n@%m:%~%# '`
`TERM='vt100'`
`bindkey -e`
<div style="font-family:arial,sans-serif">
-   Some PATH could be optional, depending the flavor.
-   PS1 sets the prompt like user@PureDarwin:~% in your home dir and 
-   TERM variable could be 'ansi' or per example 'xterm-color'.
-   the bindkey -e command allows you to use emac style for ^A, ^E, and ^D shortcut (how paradoxal since the EDITOR is vi? ;)).
<div style="font-family:arial,sans-serif">
__Note__: zsh is the only shell we know that it is able to run in interactive mode without (or with a broken) standard input.
### Resources {style="font-family:arial,sans-serif"}
<div style="font-family:arial,sans-serif">
<http://www.zsh.org/>
<div style="font-family:arial,sans-serif">
<http://zsh.dotsrc.org/> (mirror: <http://zsh.sourceforge.net/> )
<div style="font-family:arial,sans-serif">

<div style="font-family:arial,sans-serif">
<http://en.wikipedia.org/wiki/Zsh> 
