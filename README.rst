# msglite

Extracts emails and attachments saved in Microsoft Outlook's .msg files

The python package extract_msg automates the extraction of key email
data (from, to, cc, date, subject, body) and the email's attachments.

### Usage



### Notes on encoding 

Field types:

* 001E - PtypString8 - Non-unicode string
* 001F - PtypString - UTF-18 LE string
* 0102 - PtypBinary - Blob

### Credits

This package is a lightweight and functionally extended fork of:

https://github.com/mattgwwalker/msg-extractor