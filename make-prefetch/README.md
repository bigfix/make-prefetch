make-prefetch
=============

This is a tool to generate `prefetch` statements for downloads in IBM Endpoint
Manager.

## Common Usage

The most common way to use this tool is to run it against a file with
no arguments.

For example, suppose you want to create an action to download
[this picture of Hodor](http://i.imgur.com/YAUeUOG.jpg).

To do this, first download the picture as `hodor.jpg`:

    $ curl http://i.imgur.com/YAUeUOG.jpg > hodor.jpg

Then run `make-prefetch.py` on the file to generate a prefetch statement:

    $ make-prefetch.py hodor.jpg

This will output a prefetch statement with `http://REPLACEME` as the URL:

    prefetch hodor.jpg sha1:ce842e0af799f2ba476511c8fbfdc3bf89612dd0 size:57656 http://REPLACEME sha256:74f69205a016a3896290eae03627e15e8dfeba812a631b5e0afca140722a322b

You can then edit `http://REPLACEME` to instead be the actual URL for the image,
and paste the result directly into your actionscript to download the
picture as `hodor.jpg`:

    prefetch hodor.jpg sha1:ce842e0af799f2ba476511c8fbfdc3bf89612dd0 size:57656 http://i.imgur.com/YAUeUOG.jpg sha256:74f69205a016a3896290eae03627e15e8dfeba812a631b5e0afca140722a322b
