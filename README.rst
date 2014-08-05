###################
ftrack sphinx vimeo
###################

This plugin is derived from
`sphinxcontrib.youtube <https://github.com/thewtex/sphinx-contrib/tree/master/youtube>`_

*************
Documentation
*************

This module defines a directive, `vimeo`.  It takes a single, required
argument, a Vimeo video ID::

    ..  vimeo:: 12345678

The referenced video will be embedded into HTML output.  By default, the
embedded video will be sized for 720p content.  To control this, the
parameters "aspect", "width", and "height" may optionally be provided::

    ..  vimeo:: 12345678
        :width: 640
        :height: 480

    ..  vimeo:: 12345678
        :aspect: 4:3

    ..  vimeo:: 12345678
        :width: 100%

    ..  vimeo:: 12345678
        :height: 200px
