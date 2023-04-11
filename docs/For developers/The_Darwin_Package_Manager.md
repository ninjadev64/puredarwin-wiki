The Darwin Package Manager
==========================
<div style="direction:ltr">
This is Stuart and Aladin's proposal for "dm", a Darwin Package Manager. It is based on the discussion on the [Package management](../package-management.html) page.
<div style="direction:ltr">
Feel free to rip it apart.
<div style="direction:ltr">

<div style="direction:ltr">

<div class="sites-embed-border-off sites-embed" style="width:378px;">


Contents
1.  [**1** Scope](the-darwin-package-manager.html#TOC-Scope)
    1.  [**1.1** Supersets](the-darwin-package-manager.html#TOC-Supersets)
    2.  [**1.2** Subsets](the-darwin-package-manager.html#TOC-Subsets)
    3.  [**1.3** Mandatory files involved at run-time](the-darwin-package-manager.html#TOC-Mandatory-files-involved-at-run-time)
2.  [**2** darwinup](the-darwin-package-manager.html#TOC-darwinup)
3.  [**3** The PureDarwin Package Database](the-darwin-package-manager.html#TOC-The-PureDarwin-Package-Database)
4.  [**4** Groups and Systems](the-darwin-package-manager.html#TOC-Groups-and-Systems)
5.  [**5** The "core" group](the-darwin-package-manager.html#TOC-The-core-group)
6.  [**6** Updates](the-darwin-package-manager.html#TOC-Updates)
7.  [**7** Security](the-darwin-package-manager.html#TOC-Security)
8.  [**8** Language](the-darwin-package-manager.html#TOC-Language)
9.  [**9** Usage](the-darwin-package-manager.html#TOC-Usage)
10. [**10** At Installation Time](the-darwin-package-manager.html#TOC-At-Installation-Time)
11. [**11** Package Database Admin Toold](the-darwin-package-manager.html#TOC-Package-Database-Admin-Toold)
    1.  [**11.1** dbaudit](the-darwin-package-manager.html#TOC-dbaudit)
    2.  [**11.2** dbstats](the-darwin-package-manager.html#TOC-dbstats)
    3.  [**11.3** pdpdmake](the-darwin-package-manager.html#TOC-pdpdmake)
    4.  [**11.4** dtbi](the-darwin-package-manager.html#TOC-dtbi)

### Scope
<div style="direction:ltr">
"dm" will be a command line tool used to manage the darwinbuild components of a Darwin system, namely:
<div style="direction:ltr">
-   Binary roots available from src.macosforge.org/Roots
-   Patched binaries from code.google.com/p/puredarwin (inc. PureDarwin pd_* scripts and PureFoundation)
<div style="direction:ltr">
These locations would be checked in turn for binaries, in the same way that darwinbuild currently checks for patch files and tarballs.
#### Supersets
<div style="direction:ltr">
darwinup
<div style="direction:ltr">
darwinxref
<div style="direction:ltr">
<div style="direction:ltr">
(patched MacPorts?)
#### Subsets
<div style="direction:ltr">
"dm" would also be used to install other package managers (e.g., MacPorts), which would then be used to install other packages.
<div style="direction:ltr">
 (is a tweaked DarwinBuild where the pseudo-chroot is in fact the root (/) plausible?)
<div style="direction:ltr">

<div style="direction:ltr">
#### Mandatory files involved at run-time
<div style="direction:ltr">
The Darwin Package Manager should take a filename (if possible) which does not exist in any UNIX distribution and/or GNU/Linux distro.
<div style="direction:ltr">
Some propositions for the filename crossed with other involved filenames (if possible too) described later:
<div style="direction:ltr">
-   dm (*Darwin package Database*)
    pdpd or pd2 (
-   
-   dtpm (Darwin's Trivial Package Manager)
-   dtbi (Darwin's Trivial Binary Installer)

<div style="direction:ltr">


<div style="direction:ltr">
<div style="direction:ltr">
Where the "dm" tool should be installed has to be discussed, it could be in:

<div style="direction:ltr">
-   `/usr/local/sbin`
    According to *hier* it could also be in /usr/local/sbin and by default "dm" is not included in the basic operating system (Darwin)..
         /usr/         contains the majority of user utilities and applications
                       local/    executables, libraries, etc. not included by the basic operating system
-   <span style="font-family:courier new,monospace"><span style="font-size:small">/usr/sbin/
    <span style="font-family:Arial;font-size:13px">According to *hier..*
    <span style="font-family:courier new;font-size:12px">     /usr/         contains the majority of user utilities and applications
                       sbin/     system daemons & system utilities (executed by users)</span></span></span></span>
<div style="direction:ltr">
-   `/usr/libexec/`
    <span style="font-family:courier new;font-size:12px">     /usr/         contains the majority of user utilities and applications
                       libexec/  system daemons & system utilities (executed by other programs)</span>
-   <span style="font-family:courier new;font-size:12px">/opt/local/bin/port
    <span style="font-family:arial,sans-serif">__Note:__ If we pach `port' from the MacPorts project, then the default location is obvious.</span></span>

<div style="direction:ltr">
  ----------------------------------------------------- --------------------------------------------------------------------------------
  **Filename**        *To be determined*...
  **Permissions**     Admin privileges, executable, read..
                                                        (-r-xr-xr-x root  admin ?)
                                                        Admin users can then use it to add and remove packages as needed.
  **Path**            *To be determined...*
  **Miscellaneous**   The Darwin Package Manager
  ----------------------------------------------------- --------------------------------------------------------------------------------
------------------------------------------------------------------------
The PureDarwin Package Database ("pdpd" or "pd2") is still abstract at this time.
For the potential filename:
-   "pdpd" or "pd2" for PureDarwin Package Database
-   "dpd(b)" for Darwin Package Data(b)ase
__Note:__ If we choose to patch `port' from the MacPorts project, this repository will be useless except if we want to log and/or record in parallel the events.

  ----------------------------------------------------- -------------------------------------------------------------------------
  **Filename**        *To be determined...*
  **Permissions**     <span>*To be determined...*</span>
  **Path**            *To be determined...*
  **Miscellaneous**   The (Pure)Darwin Package Database
                                                        
                                                        
  ----------------------------------------------------- -------------------------------------------------------------------------
------------------------------------------------------------------------
A launchd plist file (`org.puredarwin.xyzt.plist`?) in `/System/Library/LaunchDaemons/`

  ----------------------------------------------------- --------------------------------------------------------------------------------
  **Filename**        org.puredarwin.[*tobedetermined*].plist
  **Permissions**     (-rw-r--r--  root  wheel)
                                                        
  **Path**            /System/Library/LaunchDaemons/
  **Miscellaneous**   Launchd plist (scheduling, update..)
  ----------------------------------------------------- --------------------------------------------------------------------------------

### darwinup
<div style="direction:ltr">
"dm" will use darwinup for the lowest-level installation and un-installation. darwinup works much like a version control system, keeping track of which files are altered during an install so that it can then "roll back" the file system at un-install time. It does not, however, have any idea of dependencies or the ability to fetch files from repositories. These are the features which "dm" will provide.
<div style="direction:ltr">

<div style="direction:ltr">
If we use `darwinup', we could need to list *all* features/possibilities provided by `darwinup', list what we clearly need for a plausible start, and make a diff between both lists.
### The PureDarwin Package Database
Central to "dm" will be the PureDarwin Package Database ("pdpd" or "pd2"). This will be based on a complete package list and dependency information extracted from the darwinxref database, augmented with information about packages provided by PureDarwin and others. The tools described below can help compile this information, but the amount of work involved should not be under estimated. Package management systems simplify matters for the user by shifting the task of tracking and resolving package inter-dependencies to those who administer the packaging system.
<div style="direction:ltr">
-   For simplicity I'm not planning on keeping darwinxref's detailed file list information (the contents of each package). Will this be a problem? Will users want to search for individual files? And if they do, could we just use a wrapper around xref.puredarwin.org to retrieve this info? **Answer:** Each package produced and packages by darwinbuild has a receipt (/usr/local/darwinbuild/receipts/&lt;package&gt;) which lists all of the files added. This will solve the problem for installed packages.
<div style="direction:ltr">
To the data from darwinxref we will add:
<div style="direction:ltr">
-   Localised descriptions of each package
-   "groups" and "systems" information (explained below)
<div style="direction:ltr">
One of the first things "dm" should do when it's run is to check for an updated version of the pd2 database and download it.
### Groups and Systems
<div style="direction:ltr">
Groups and Systems provide a way of grouping collections of packages together to make it easier for the user to choose and install the packages they need.
<div style="direction:ltr">
-   Groups are collections of packages, assembled by theme eg. "web_services" or "perl_and_libraries"
-   Systems are collections of packages, forming complete special-purpose Darwin distributions eg. "full_desktop", "rescue_tools", "office_server", "web_server"
<div style="direction:ltr">
Group and Systems names should never be the same as package names.
### The "core" group
<div style="direction:ltr">
There should be a special "core" group which contains all of the components every PureDarwin installation needs (eg. the kernel(s), launchd, general .KEXTs, the main frameworks). This should always be installed, and cannot be un-installed, but can be updated.
<div style="direction:ltr">

<div style="direction:ltr">
The "core" group could include all of the packages needed to create a network connection and run "dm". We could then make the first stage of the installation process preparing the destination disk and installing the "core" group, with the second part being running "dm" from the destination disk. (This would allow us to provide multiple first stages -- eg. install from LiveCD, Linux, Windows -- with a single common second stage).
<div style="direction:ltr">

<div style="direction:ltr">
The "core" group would probably be written directly to the destination disk and not installed via darwinup.
### Updates
<div style="direction:ltr">
"dm" will have an `--update` mode (possibly scheduled via launchd) which will check for updated versions of the installed packages.
<div style="direction:ltr">
Now, here we have a problem, since by default the binary roots we will be using don't include any version information in their files names. That said, it is very rare for the MacOSForge roots to be updated, and if need be we could add version information to the roots held by PureDarwin.
<div style="direction:ltr">

<div style="direction:ltr">
Update information will have to be dated. "dm" will keep track of when it last checked for updates. It will collect a list of all packages updated since that time, check which of those it has installed, and download these updates.
<div style="direction:ltr">

<div style="direction:ltr">
"dm" should also be also be able to update itself, via several ways (itself, macports, darwinbuild, etc.. at least it should be symetric to the installation ways and perhaps more).
### Security
<div style="direction:ltr">
Different "security" mechanisms could/should be provided, feel free to add and/or strike them:
<div style="direction:ltr">
-   Checksuming (md5, sha-1, sha-2 family, etc..) itself and packages for from integrity to security purposes.
-   If something is remotely retrieved, we should have the possibility (by default that would be nice) to establish a "secure" (many possible ways too..) connection.
-   If "dm" is aware of the resident binaries deployed in the system, checksum could also be possible against them (but it could take some resource, and this kind of process could be moved into a "spotlight-like" daemon).
### Language
<div style="direction:ltr">
"dm" will need to be written in a language which allows the invocation of external commands (darwinup, curl), the processing (regex) and storage of text (the output from darwinup) and database access (pd2). If "dm" is going to be included in the "core" group then so will its support libraries/interpretter. A scripting language seems like the best option.
<div style="direction:ltr">

<div style="direction:ltr">
Mini poll:
<div style="direction:ltr">
-   Stuart suggests Perl: "*but I'm fairly flexible on this point. (Unlike Python and indentations.)*"
-   Aladin suggests to not reinvent the wheel and enhance the MacPorts project in patching `port' and creating special portfile for our needs. Stuart will look into this.
-   Alternatively,  `#!/bin/sh` or Lua (this one is not in the "core" group).
### Usage
<div style="direction:ltr">

<div style="direction:ltr">
So, could it be also possible that "dm" is a patch of `port' command (from the MacPorts project) which extends its functionalities to our needs because a lot of things and good features are already inside. We will provide some specific ports too. We could ask exactly the same for a tweaked darwinbuild which points to root. Also in the installation process, a lot of packages are for "user-land" and comes from darwinbuild (and/or macports) at this time.
<div style="direction:ltr">


<div style="direction:ltr">
 ```--info { package | group | system }`
<div style="direction:ltr">
<span style="white-space:pre"><span style="font-family:courier new,monospace">     </span></span>`--list { installed | available }`
<div style="direction:ltr">
`--get [config_setting]`
<div style="direction:ltr">
`--set config_setting value`
<div style="direction:ltr">
`--add [options] package_list`
<div style="direction:ltr">
`--remove [options] package_list`
<div style="direction:ltr">
`--update`
<div style="direction:ltr">
 
<div style="direction:ltr">
`--info` displays information about the given package, group or system -- whether it is currently installed, where it can be found, version, dependencies, and in the case of groups and systems, which packages they contain.
<div style="direction:ltr">


<div style="direction:ltr">
`--list` without an argument lists all installed packages. With "available" option, list all packages in the package database.
<div style="direction:ltr">


<div style="direction:ltr">
`--get` without an argument lists the current values of all all `config_settings` (which will have default built-in values, values stored in /etc/dm.config, and can be over-ridden by the `[options]` flags to `--add` and `--remove`). If `config_setting` is provided, the settings for just that setting are displayed.
<div style="direction:ltr">


<div style="direction:ltr">
`--set` sets the value of a particular `config_setting` (after checking that it's valid) and stores it in /etc/dm.config.
<div style="direction:ltr">


<div style="direction:ltr">
`--add` adds the packages in `package_list` to the current Darwin install.
<div style="direction:ltr">


<div style="direction:ltr">
`--remove` removes the packages in `package_list` from the current Darwin install.
<div style="direction:ltr">

<div style="direction:ltr">
 `package_list` 
> is a list of space-separated package, group and system names. If an entry contains a "." or a "/" it is treated as a path to a file, which is read. It is expected to contain a list of package, group or system names, which are then added to the package_list. This will allow custom configurations to be built and used time and again. eg.
<div style="direction:ltr">

> perl python ruby <span style="font-size:small">will add the curl, perl, python and ruby packages
> </span>
> <span style="font-family:courier new">--add recovery_tools file_servers emacs    </span>will add the emacs package, all packages from the file_servers group, and all packages from the recovery_tools system
> --add Chess packages.txt will add the Chess package, and any packages, groups or systems listed in packages.txt
<div style="direction:ltr">


<div style="direction:ltr">
 `options`
> over-ride the defaults stored in /etc/dm.config for the duration of the single command. (This is not a complete list.)
<div style="direction:ltr">

<div style="direction:ltr">
-   --dependencies { YES | NO } -- The dependencies `config_setting`. By default this is YES, meaning that for every package added its dependencies are found and added at the same time. (I'm not really sure about how we handle removing dependencies. Either we store some form of reference count for packages, or we re-check dependencies at the time. Either way, we should stop the user from removing a package which other packages depend on.)
-   --cache directory_path -- The cache `config_setting`. This is checked for packages before remote repositories. This will allow installation from CD images without needing networking.
-   --temp directory_path -- The temp `config_setting`. This is where packages are downloaded to. It is also checked for packages before remote repositories.
<div style="direction:ltr">

<div style="direction:ltr">
`--update` fetches a list of package changes since the last update and compares it to the list of installed packages. It then downloads those packages which have changed and installs them.
<div style="direction:ltr">

### At Installation Time
<div style="direction:ltr">
An interactive installer will present the user with lists of systems, groups or packages for them to choose from. Their choices will then be passed to "dm", which will resolve dependencies, download the packages, and install them.
<div style="direction:ltr">
### Package Database Admin Toold
dbtool.zip below contains a couple of simple Perl scripts, described below. These are a first attempt at producing some tools for creating and managing the package database. These are intended to be used by the packaging system admins, not by the end user. They mostly work on plain text files, so it should be possible to keep all of the associated resources (package lists, language files, core, group and system lists) under revision control and automate the process of producing the package database.
Please also note that at this point I see the "dm" tool more as a binary installer than a fully-fledged package manager.
#### dbaudit
`dbaudit` does a brute-force audit of a darwinbuild environment, finding which packages have binary roots and attempting to calculate dependencies for those that do.
<div style="display:block;margin-right:auto;margin-left:auto;text-align:center">
[![](../../_/rsrc/1237804812020/developers/package-management/the-darwin-package-manager/dbaudit.png%3Fheight=237&width=420)](the-darwin-package-manager/dbaudit.png%3Fattredirects=0)
The output package list is a simple text file with one line per package found. Each line has the format:
    PackageName Y build version { dependency1 dependency2 ... dependencyN }
Where "Y" could also be "N" and signals that a binary root was found. If no root was found, no version or dependency information will be provided.
Dependencies are listed as package names, if resolved, or the full path of linked library paths otherwise.
#### dbstats
`dbstats` produces a simple summary of the `dbaudit` output file. The information in this file may go towards providing the dependency information needed by a Darwin package manager.
package_list.zip contains the package list which `dbaudit` produced for a 9G55pd1 install of darwinbuild. It shows:
    `423 packages, 79 missing binary roots, 79 unresolved dependencies`
(The two 79s are purely coincidental and unrelated, I think.)

#### pdpdmake
`pdpdmake` takes a number of input files and either creates or updates a SQLite database file according to their contents.
<div style="display:block;margin-right:auto;margin-left:auto;text-align:center">
[![](../../_/rsrc/1237805196013/developers/package-management/the-darwin-package-manager/pdpdmake.png%3Fheight=356&width=420)](the-darwin-package-manager/pdpdmake.png%3Fattredirects=0)
<div style="text-align:left;display:block;margin-right:auto;margin-left:auto">
As a minimum, at least one package list must be provided.
#### dtbi
<div style="text-align:left;display:block;margin-right:auto;margin-left:auto">
`dtbi` (Darwin Trivial Binary Installer) is a Perl prototype of a basic installer for Darwin. It's main purpose is to generate discussion. Currently it will query a pdpd database (there's one produced from the packages_list.txt file below provided as an example) for information about packages. If `darwinup` is installed, `dtbi` will query it for a list of installed packages. It will add a new package, plus any uninstalled packages which that package depends upon, downloading the binary from MacOSForge.
<div style="text-align:left;display:block;margin-right:auto;margin-left:auto">

<div style="text-align:left;display:block;margin-right:auto;margin-left:auto">
To try `dtbi` in PureDarwinXmas:
<div style="text-align:left;display:block;margin-right:auto;margin-left:auto">
1.  Install the CPAN package (Perl modules, needed for database access).
2.  Install `curl` (if you want to try installing packages).
3.  Install `darwinup` (from `darwinbuild`) into /usr/sbin/ (we can argue about where it *should* go later).
4.  Copy `dtbi` and the db database file into the same directory (/Users/Shared/ is nice).
<div style="text-align:left;display:block;margin-right:auto;margin-left:auto">
Currently, only the `--info`,` --list` and `--add` options have been implemented. Again, this is just a quick Perl prototype to get people talking and to see if this solves a problem for us. The fact that this version requires 10+Mb of Perl modules suggests we'll actually be using a different language for the production version.
<div style="text-align:left;display:block;margin-right:auto;margin-left:auto">

<div style="text-align:left;display:block;margin-right:auto;margin-left:auto">
Your comments below or in #puredarwin, please.


