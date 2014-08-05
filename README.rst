###################
ftrack sphinx vimeo
###################

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

*********************
Copyright and license
*********************

Copyright (c) 2014 ftrack

Licensed under the Apache License, Version 2.0 (the "License"); you may not use
this work except in compliance with the License. You may obtain a copy of the
License in the LICENSE.txt file, or at:

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software distributed
under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR
CONDITIONS OF ANY KIND, either express or implied. See the License for the
specific language governing permissions and limitations under the License.

