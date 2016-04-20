This extension renders three types of markers to ensemble a usual scale for measurement. The output is grouped by marker type and label to enable you to set custom line width and colors.

# Features #

**Scale types:**
  * Line
  * Circular

**Units:** (the text chosen for labels is independent of this)
  * mm
  * cm
  * inch
  * pixel
  * point

**Vector based**

# Requirements #

**Inkscape**

# Downloads #

[Download latest zip archive (17.02.2015)](http://www.junktech.de/media/inkscapescaleplugin/InkscapeExtension_ScaleRender_0.91-20150217.zip)


[All downloads](http://www.junktech.de/media/inkscapescaleplugin/)

# Screenshots #

New Feature label outside without and with dangling:

![https://inkscapescalegenerator.googlecode.com/svn/wiki/screenshots/label_outside_white.png](https://inkscapescalegenerator.googlecode.com/svn/wiki/screenshots/label_outside_white.png)
![https://inkscapescalegenerator.googlecode.com/svn/wiki/screenshots/dangling_feature_white.png](https://inkscapescalegenerator.googlecode.com/svn/wiki/screenshots/dangling_feature_white.png)

click for svg:

![![](http://inkscapescalegenerator.googlecode.com/svn/wiki/screenshots/exampleScaleThumb.png)](http://inkscapescalegenerator.googlecode.com/svn/wiki/screenshots/exampleScale.svg)

click for full bitmap:

![![](http://inkscapescalegenerator.googlecode.com/svn/wiki/screenshots/linuxThumb.png)](http://inkscapescalegenerator.googlecode.com/svn/wiki/screenshots/linux.png)
Linux with new ui

![![](http://inkscapescalegenerator.googlecode.com/svn/wiki/screenshots/windowsThumb.png)](http://inkscapescalegenerator.googlecode.com/svn/wiki/screenshots/windows.png)
Windows with old ui

![![](http://inkscapescalegenerator.googlecode.com/svn/wiki/screenshots/linux2Thumb.png)](http://inkscapescalegenerator.googlecode.com/svn/wiki/screenshots/linux2.png)
Linux with old ui and separated groups

# README #

- **INSTALL**

Put "render\_scale.inx" and "render\_scale.py" in your Inkscape extension directory.

On Linux:   "~/.config/inkscape/extensions/"

On Windows: "Inkscape\share\extensions\" (inside your programs folder)

- **Known bugs**

> ui float precision is limited to 1

> suffix doesn't support several special chars

- **Changelog**

17.02.2015
> include changes made by Paul Rogalinski-Pinter
> indentation cleanup - it's all tabs now
> fixed line scale bug
10.07.2014
> updated the install packages with the changes made by Roger Jeurissen
27.06.2010
> fixed ° (degree char) in suffix
12.06.2010
> changed default circular label offset to -4.8 from 8
> > - so the label will spawn above the scale

> changed INSTALL-section in README
> > - added extension path for inkscape-0.47
01.12.2009

> added tabs for ui
> added circular scales

18.11.2009
> default values updated, so there is something visible after first install

17.11.2009
> initial release


---


# Author #

2009 Sascha Poczihoski, sascha@junktech.de
> original author

2013 Roger Jeurissen, roger@acfd-consultancy.nl
> dangling labels and inside/outside scale features

2015 Paul Rogalinski, pulsar@codewut.de
> adapted Inkscape 0.91 API changes