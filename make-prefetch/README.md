make-prefetch
=============

This is a tool to generate `prefetch` statements for downloads in IBM Endpoint
Manager.

## Using a URL argument

Suppose you want to create a prefetch statement to download
[this picture of Hodor](http://i.imgur.com/YAUeUOG.jpg).

The easiest way to do this is to run `make-prefetch.py` on the URL:

    $ make-prefetch.py http://i.imgur.com/YAUeUOG.jpg

That will output a prefetch statement to download the picture:

    prefetch YAUeUOG.jpg sha1:ce842e0af799f2ba476511c8fbfdc3bf89612dd0 size:57656 http://i.imgur.com/YAUeUOG.jpg sha256:74f69205a016a3896290eae03627e15e8dfeba812a631b5e0afca140722a322b

However, the file will be downloaded as `YAUeUOG.jpg` on the client. To instead
download it as `hodor.jpg`, you can use the `--name` argument:

    $ make-prefetch.py --name hodor.jpg http://i.imgur.com/YAUeUOG.jpg

This will output the same prefetch statement as before, but it will be
downloaded as `hodor.jpg` on the client.

    prefetch hodor.jpg sha1:ce842e0af799f2ba476511c8fbfdc3bf89612dd0 size:57656 http://i.imgur.com/YAUeUOG.jpg sha256:74f69205a016a3896290eae03627e15e8dfeba812a631b5e0afca140722a322b

## Using a file argument

Suppose you have already downloaded 
[this picture of Hodor](http://i.imgur.com/YAUeUOG.jpg) and you want to create a
prefetch statement for it.

To do this, run `make-prefetch.py` on the file to generate a prefetch statement:

    $ make-prefetch.py hodor.jpg

This will output a prefetch statement with `http://REPLACEME` as the URL:

    prefetch hodor.jpg sha1:ce842e0af799f2ba476511c8fbfdc3bf89612dd0 size:57656 http://REPLACEME sha256:74f69205a016a3896290eae03627e15e8dfeba812a631b5e0afca140722a322b

You can then edit `http://REPLACEME` to instead be the actual URL for the image,
and paste the result directly into your actionscript to download the
picture as `hodor.jpg`:

    prefetch hodor.jpg sha1:ce842e0af799f2ba476511c8fbfdc3bf89612dd0 size:57656 http://i.imgur.com/YAUeUOG.jpg sha256:74f69205a016a3896290eae03627e15e8dfeba812a631b5e0afca140722a322b
