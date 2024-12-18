.. index:: single: appendix
.. _appendix:

.. |-| unicode:: U+2011   .. en dash, trimming surrounding whitespace (substitution definition)
    :trim:

Appendix
========

.. index:: single: appendix; Unicode

.. _entering-unicode:

Unicode
-------

To enter Unicode characters in your metadata manually (rather than with the :ref:`Unicode keyboard<unicode-keyboard>`), you need to use a special sequence of keystrokes. There are two options. Choose the one that is more comfortable for you.

**Method 1**:

Type (and release) ctrl-shift-u, code, {enter,space}

{enter,space} means that you can type either enter or space. You do not need to type leading zeros in the code. If the code is 00e9, you can type just e9. The characters that you type for the code turn into the desired Unicode character when you type enter or space.

**Method 2**:

Press (and hold) ctrl-shift, u, code, release ctrl-shift

Again, you do not need to type leading zeros. The characters that you type for the code turn into the desired Unicode character when you release ctrl-shift.

To find the code for the Unicode character that you want, use a table such as this one: Unicode-table_. The code that you need is the numeric portion of the Unicode code point (the portion after "U+").

Here are some characters that you might need:

==== ========= ==== ========= ==== =========
code character code character code character
==== ========= ==== ========= ==== =========
00e0 à         00e1 á         00e2 â
00e4 ä         00e8 è         00e9 é
00ea ê         00eb ë         00f1 ñ
00f2 ò         00f3 ó         00f4 ô
00f5 õ         00f6 ö         00f9 ù
00fa ú         00fb û         00fc ü
==== ========= ==== ========= ==== =========

.. _unicode-table: http://www.utf8-chartable.de/unicode-utf8-table.pl?number=1024

.. _completers-files:

Completers files
----------------

Wax provides :ref:`automatic completion<autocompletion>` of values you type into metadata fields. Predefined completion values are stored in files in the directory ~/.config/completers. The name of a file corresponds to the key to which the values should be applied. Initially, Wax provides several completers files, including composer, conductor, and orchestra. To create your own completers, use WaxConfig. You can also use a text editor to specify values (one on each line). Wax ignores blank lines and lines that start with # (to signify a comment). When you create or modify a completers file, you must restart Wax before it will know about the new file.

Database organization
---------------------
.. _sound-folder:

Directories are structured as follows::

    recordings
              \_sound
                     \_uuid1
                            \_0
                            \_1
                            \_...
                     \_uuid2
                            \_0
                     \_...

              \_metadata
                        \_short
                               \_Genre1
                               \_Genre2
                               \_...
                        \_long
                        \_config
                        \_completers

              \_images
                      \_uuid1
                      \_uuid2
                      \_...

              \_documents
                         \_uuid1
                         \_uuid2
                         \_...

On selection of a genre, Wax loads the contents of the short file with the genre as its name. Each line of the short file provides short metadata, a uuid, and a work number (work_num). When the user selects a recording, Wax uses the uuid and work_num to access the corresponding entry in the file "long" which contains long metadata for all recordings in the archive. All siblings have the same uuid, so the uuid is sufficient to access corresponding images, documents, and sound files in their respective directories. The sound directory is further divided by disc number.

Disk mounts
-----------

The simplest configuration for disk mounts is for the entire recordings hierarchy to reside on your system disk. However, that disk must have capacity sufficient for the database. 2TB is sufficient for a large collection. It is possible to find a 2TB SSD for $100, so this simple solution will be adequate for most users.

If you already have your system installed on a smaller disk, you could add an SSD to your system and mount it on the :code:`recordings` directory.

You can save a few dollars by choosing a HDD instead of an SSD, but a HDD adds complications. Allowing the HDD to spin all the time will shorten its lifespan. You can configure it to spin down after a period of inactivity using :code:`/etc/hdparm`, but you then have to wait for it to spin up when you need to access it. One option to minimize this annoyance is to use the HDD only for sound files and mount it on the :code:`sound` directory. The data in the other subdirectories of :code:`recordings` (:code:`metadata`, :code:`images`, and :code:`documents`) is typically much smaller, so there is probably sufficient space on your system drive (which presumably is an SSD). You can browse your collection in Select and Play modes without accessing sound files, so you will have to wait for the HDD to spin up (2-5 seconds typically, depending on the size of the HDD) only when you activate play.

Also remember that you should back up your database to another drive. I use :code:`rsync` for this purpose -- something like::

       rsync -a ~/wax/recordings/ /mnt/nas/wax/recordings/

assuming that you have a NAS mounted at :code:`/mnt/nas`. Put this command in :code:`crontab` so that it runs automatically every day.

Config files (.config directory)
--------------------------------

.. _transfer-folder:

- **transfer**: The transfer folder is used to transfer files to (:ref:`Import<file-mode>`) Wax. This folder may contain subfolders if you choose to create them. Note that when the :ref:`file chooser<file-chooser>` tells you that you are in the root folder, this is the folder you are actually in. Use this folder to import sound files, or to import :ref:`images<coverart-button>` or :ref:`documents<documents>`.

- **queuefiles**: Pickles of pixbufs of the primary image and play queue entries.

- **log**: Log files with tracebacks of uncaught errors.

Installation
------------

Installation instruction appear in the README for wax-install at github. They are reproduced here:

Clone wax, wax-config, and wax-install (from the home directory)::

    git clone https://github.com/jeffbarish/wax.git
    git clone https://github.com/jeffbarish/wax-config.git
    git clone https://github.com/jeffbarish/wax-install.git

cd into wax-install and run the program "installer.root" as root::

    sudo ./installer.root

Run installer as youself::

    ./installer

These scripts perform the following functions:

:code:`installer.root`:

- runs apt to install several packages.

- puts starter scripts for wax and waxconfig in /usr/local/bin.

:code:`installer`:

- puts the theme in ~/.themes.

- creates a virtual environment in ~/.venv and installs several packages.

- creates wax subdirectories in ~/wax/.config

When the installer finishes, type "wax" to run wax or "waxconfig" to run waxconfig.

I tested the code on Ubuntu 24.04 running on an Intel processor and on Debian GNU/Linux 12 (Raspberry Pi OS) running on Raspberry Pi 4B. Note that you will need GTK and GStreamer on whatever OS you choose.

You can also install wax on Windows 11 using WSL 2. However, there are limitations. It is not possible to access a CD-drive as a device from WSL, so ripping in Wax on WSL is not possible. Instead, rip using Media Player, put the sound files in the transfer folder of Wax, and import them. Media Player does not embed cover art, so you will need to find cover art (at Amazon, for example) and copy-and-paste it into Wax.

Quick Start
-----------

To create your first recording after installing Wax, insert a CD in your CD drive and go to Edit mode. Select the appropriate genre for your CD using the button in the top left. Click the Create button in the right panel. While the CD is ripping, fill in the boxes on the left panel at least for the primary metadata. Some of the boxes might have been filled in automatically after you initiated the rip using metadata from MusicBrainz. Click the "Save new" button at the bottom when you are ready to save the recording. When the ripping finishes, change the Mode to Select. Your new recording will already be selected. Drag it to the play queue (the right panel). The play button will appear in the top right. Click it to start play. Congratulations. You have just created the first recording in your Wax database.
