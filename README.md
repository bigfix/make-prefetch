[![Build Status](https://travis-ci.org/bigfix/make-prefetch.svg?branch=master)](https://travis-ci.org/bigfix/make-prefetch) [![Coverage Status](https://coveralls.io/repos/bigfix/make-prefetch/badge.svg?branch=travis-build&service=github)](https://coveralls.io/github/bigfix/make-prefetch?branch=travis-build)

make-prefetch
===

This is a tool to generate [prefetch](https://developer.bigfix.com/action-script/reference/download/prefetch.html) statements for downloads in BigFix ActionScript.

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

To specify the URL to download the file from, you can use the `--url` argument:

    $ make-prefetch.py hodor.jpg --url http://example.com/winterfell/hodor.jpg

This will output the same prefetch statement as before, but the URL will be
`http://example.com/winterfell/hodor.jpg`.

    prefetch hodor.jpg sha1:ce842e0af799f2ba476511c8fbfdc3bf89612dd0 size:57656 http://example.com/winterfell/hodor.jpg sha256:74f69205a016a3896290eae03627e15e8dfeba812a631b5e0afca140722a322b

Support
===
Any issues or questions regarding this software should be filed via [GitHub issues](https://github.com/bigfix/make-prefetch/issues).
