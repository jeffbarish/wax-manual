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

Automatic tagging
-----------------

When you rip a CD, Wax automatically tags the sound files. If you ever copy your sound files to another platform (e.g., your smartphone), the player that you use on that platform will display the tags. Obviously, tags cannot contain all of the rich metadata available in Wax, but they can provide information sufficient to identify recordings. Unfortunately, standards for tags (ID3 notwithstanding) and for reassembling individual tracks into complete recordings are poor to nonexistent, so do not expect results as coherent as those provided by Wax.

To tag sound files, Wax must convert its rich metadata to tags. The algorithms for performing this conversion reside in the module widgets.edit.left.tagextractors. In Wax, every genre generally has its own set of metadata keys. Accordingly, there must be a tag extractor for each genre. I provide a set of extractors for the genres that I provide with Wax. If you define your own genres and you want Wax to tag sound files corresponding to recordings in those genres, you must create your own extractors. Use the ones that I provided as models. You might also want to fiddle with the extractors that I provided. Your player might recognize more tags than mine. If so, you can add code to convert other Wax metadata to those tags. If you do not specify an extractor for a new genre, Wax politely declines to tag sound files in that genre.

The dictionary self.metadata_long has metadata for both primary and secondary in their long form. self.metadata_short has metadata for primary in their short form. self.tags is the dictionary that contains all the tags for specifying the work. The call special method returns values for the track titles. The generic extractors are simple mappings from one Wax metadata key to one tag. Other extractors allow you to specify more complicated mappings involving multiple Wax keys going to one tag.

Split liner notes
-----------------

Websites that sell recordings usually offer a PDF of the liner notes with your purchase. Sometimes, the PDF has two pages side by side. You will also encounter side-by-side pages in liner notes when you scan physical liner notes using a flatbed scanner. Wax will happily display side-by-side pages in the document viewers, but liner notes are easier to read when the PDF has individual pages on each PDF page. One of the tools available in the :code:`wax-tools` repository, :code:`splitlinernotes.py`, will split a PDF with side-by-side pages into a new PDF with individual pages. Run the program with the :code:`-h` option to get a help message. In most cases, you will simply specify the name of the input file on the command line::

       python splitlinernotes.py linernotes.pdf

The program creates a new PDF called :code:`new.pdf` with tandem pages split into singles. If the original PDF has pages that do not need to be split, specify those pages in the :code:`-p` (preserve) option. Sometimes the liner notes will include pages that you do not need to include. They might contain text in other languages or advertisements. Use the :code:`-x` (exclude) option to exclude them from :code:`new.pdf`. The argument to these two options can be a single integer :code:`n1`, a range of pages :code:`n1-n2`, or a list of pages :code:`n1,n2,n3`. Do not use spaces in the argument. To rearrange pages, use :code:`-m n1,n2` to move page :code:`n1` to page :code:`n2`. For multiple moves, specify additional :code:`-m` options. Note that page numbering for :code:`-p` is pre-split, but for :code:`-m` and :code:`-x` it is post-split. It is easy to get confused if you use both :code:`-x` and :code:`-m`. Be aware that move happens before exclude. Use :code:`-o` to automatically run the program :code:`okular` on :code:`new.pdf` so that you can quickly confirm that :code:`new.pdf` reflects your intentions.
