# Bochs, the Open Source IA-32 emulation project

![The Bochs logo](https://sites.google.com/a/puredarwin.org/puredarwin/developers/bochs/Bochs%20logo.gif?attredirects=0)

**Contents:**
1. [Boot sequence](https://github.com/PureDarwin/PureDarwin/wiki/Bochs#boot-sequence)
    1. [The Plex86/Bochs VGABios](https://github.com/PureDarwin/PureDarwin/wiki/Bochs#The-plex86-bochs-vgabios)
    2. [DFE bootloader](https://github.com/PureDarwin/PureDarwin/wiki/Bochs#dfe-bootloader)
        1. [Decompressing extensions](https://github.com/PureDarwin/PureDarwin/wiki/Bochs#decompressing-extensions)
        2. [CPU:FSB multiplier detection fails](https://github.com/PureDarwin/PureDarwin/wiki/Bochs#cpu-fsb-multiplier-detection-fails)
    3. [Chameleon bootloader](https://github.com/PureDarwin/PureDarwin/wiki/Bochs#chameleon-bootloader)
        1. [Kernel Panic](https://github.com/PureDarwin/PureDarwin/wiki/Bochs#kernel-panic)
2. [Resources](https://github.com/PureDarwin/PureDarwin/wiki/Bochs#resources)

## Boot sequence

### The Plex86/Bochs VGABios
![Bochx plex86 vga bios](https://sites.google.com/a/puredarwin.org/puredarwin/developers/bochs/Bochx%20plex86%20vga%20bios.png?attredirects=0)

### DFE bootloader
![Bochs DFE bootloader](https://sites.google.com/a/puredarwin.org/puredarwin/developers/bochs/Bochs%20dfe%20bootloader.png?attredirects=0)

#### Decompressing extensions
![XNU decompression in Bochs](https://sites.google.com/a/puredarwin.org/puredarwin/developers/bochs/xnu%20decompression%20in%20Bochs.png?attredirects=0)

#### CPU:FSB multiplier detection fails
*Please, let us know if you have a solution.*

![Bochs fails on CPU FSB detection](https://sites.google.com/a/puredarwin.org/puredarwin/developers/bochs/Bochs%20fails%20on%20CPUFSB%20detection.png?attredirects=0)

### Chameleon bootloader
![Bochs Chameleon bootloader](https://sites.google.com/a/puredarwin.org/puredarwin/developers/bochs/Bochs%20chameleon%20bootloader.png?attredirects=0)

#### Kernel Panic
![Bochs Panic voodoo](https://sites.google.com/a/puredarwin.org/puredarwin/developers/bochs/Bochs%20panic%20Voodoo.png?attredirects=0)

far..

![Bochs trying to boot PureDarwin on machbochs with debug_on](https://sites.google.com/a/puredarwin.org/puredarwin/developers/bochs/Bochs%20trying%20to%20boot%20PD%20on%20machbochs%20debug_on.png?attredirects=0)

Then it stalls.

## Resources
* http://bochs.sourceforge.net/
* http://code.google.com/p/xnu-dev (Voodoo, A fork of the XNU kernel)