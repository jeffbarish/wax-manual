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

On selection of a genre, Wax loads the contents of the short file with the genre as its name. Each line of the short file provides short metadata, a uuid, and a work number (work_num). When the user selects a recording, Wax uses the uuid and work_num to access the corresponding entry in the file "long" which contains long metadata for all recordings in the archive. All siblings have the same uuid, so the uuid is sufficient to access corresponding images, documents, and sound files in their respective directories. The sound directory is further divided by disc number. Imports have all sound files in the subdirectory for "disc 0".

Config files (.config directory)
--------------------------------

.. _transfer-folder:

- **transfer**: The transfer folder is used to transfer files to (:ref:`Import<file-mode>`) Wax. This folder may contain subfolders if you choose to create them. Note that when the :ref:`file chooser<file-chooser>` tells you that you are in the root folder, this is the folder you are actually in. Use this folder to import sound files, or to import :ref:`images<coverart-button>` or :ref:`documents<documents>`.

- **queuefiles**: Pickles of pixbufs of the primary image and play queue entries.

- **log**: Log files with tracebacks of uncaught errors.

