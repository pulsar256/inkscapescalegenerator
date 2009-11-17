#!/usr/bin/env python
'''
Copyright (C) 2009 Sascha Poczihoski, sascha@junktech.de

This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 2 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA

TODO
	- fix bug: special chars in suffix
'''

import sys, math
sys.path.append('/usr/share/inkscape/extensions') # or another path, as necessary
import inkex
from simplestyle import *


class ScaleGen(inkex.Effect):
    """
    Example Inkscape effect extension.
    Creates a new layer with a "Hello World!" text centered in the middle of the document.
    """
    def __init__(self):
        """
        Constructor.
        Defines the "--what" option of a script.
        """
        # Call the base class constructor.
        inkex.Effect.__init__(self)

        # Define string option "--what" with "-w" shortcut and default value "World".
        self.OptionParser.add_option('-f', '--scalefrom', action = 'store',
          type = 'int', dest = 'scalefrom', default = '0',
          help = 'Measure from...')
        self.OptionParser.add_option('-t', '--scaleto', action = 'store',
          type = 'int', dest = 'scaleto', default = '20',
          help = 'Measure to...')
        self.OptionParser.add_option('-c', '--reverse', action = 'store',
          type = 'string', dest = 'reverse', default = 'false',
          help = 'Reverse order:')             
        self.OptionParser.add_option('', '--rotate', action = 'store',
          type = 'string', dest = 'rotate', default = '0',
          help = 'Rotate:')                   
        self.OptionParser.add_option('-b', '--scaleres', action = 'store',
          type = 'int', dest = 'scaleres', default = '100',
          help = 'Measure resolution:')                   
        self.OptionParser.add_option('-g', '--scaleheight', action = 'store',
          type = 'int', dest = 'scaleheight', default = '100',
          help = 'Height of scale:')
        self.OptionParser.add_option('-s', '--fontsize', action = 'store',
          type = 'int', dest = 'fontsize', default = '16',
          help = 'Font Size:')
        self.OptionParser.add_option('-i', '--suffix', action = 'store',
          type = 'string', dest = 'suffix', default = '',
          help = 'Suffix:')

	# label offset
        self.OptionParser.add_option('-x', '--labeloffseth', action = 'store',
          type = 'int', dest = 'labeloffseth', default = '45',
          help = 'Label offset h:')   
        self.OptionParser.add_option('-y', '--labeloffsetv', action = 'store',
          type = 'int', dest = 'labeloffsetv', default = '45',
          help = 'Label offset v:') 
          
        # marker div
        self.OptionParser.add_option('-m', '--mark0', action = 'store',
          type = 'int', dest = 'mark0', default = '10',
          help = 'Div of labeled marker:')
        self.OptionParser.add_option('-n', '--mark1', action = 'store',
          type = 'int', dest = 'mark1', default = '5',
          help = 'Div of bold marker:')
        self.OptionParser.add_option('-o', '--mark2', action = 'store',
          type = 'int', dest = 'mark2', default = '1',
          help = 'Div of standard marker:')
          
        # marker strength        
        self.OptionParser.add_option('-p', '--mark0str', action = 'store',
          type = 'float', dest = 'mark0str', default = '10.0',
          help = 'Strength of labeled marker:')
        self.OptionParser.add_option('-q', '--mark1str', action = 'store',
          type = 'float', dest = 'mark1str', default = '5.0',
          help = 'Strength of bold marker:')
        self.OptionParser.add_option('-r', '--mark2str', action = 'store',
          type = 'float', dest = 'mark2str', default = '1.0',
          help = 'Strength of standard marker:')
          
        # marker width
        self.OptionParser.add_option('-w', '--mark1wid', action = 'store',
          type = 'int', dest = 'mark1wid', default = '75',
          help = 'Width of bold marker (\%):')
        self.OptionParser.add_option('-v', '--mark2wid', action = 'store',
          type = 'int', dest = 'mark2wid', default = '50',
          help = 'Width of standard marker (\%):')       
                             
        self.OptionParser.add_option('-u', '--unit', action = 'store',
          type = 'string', dest = 'unit', default = 'mm',
          help = 'Unit:')                                

    def addLabel(self, i, x, y, grp, fontsize):
    	res = self.options.scaleres
    	pos = i*res + fontsize/2
    	text = inkex.etree.SubElement(grp, inkex.addNS('text','svg'))
    	text.text = str(i)+self.options.suffix.encode("utf8")
    	#rotate = self.options.rotate
    	fs = str(fontsize)
        style = {'text-align' : 'center', 'text-anchor': 'middle', 'font-size': fs}
        text.set('style', formatStyle(style))
#        text.set('x', str(inkex.unittouu(str(x)+self.options.unit)+self.options.labeloffseth))
#        text.set('y', str(inkex.unittouu(str(y)+self.options.unit)+self.options.labeloffsetv))
        text.set('x', str(float(x)+int(self.options.labeloffseth)))
        text.set('y', str(float(y)+int(self.options.labeloffsetv)))        
        grp.append(text)
        
    def addLine(self, i, scalefrom, scaleto, grp, grpLabel, type=2):
    	reverse = self.options.reverse
    	rotate = self.options.rotate
    	unit = self.options.unit    	
    	fontsize = self.options.fontsize
    	res = self.options.scaleres
    	label = False
    	if reverse=='true':
    		# Count absolut i for labeling
    		counter = 0
 		for n in range(scalefrom, i):
 			counter += 1
 		n = scaleto-counter-1
 	else:
 		n = i
		
    	if type==0:
	    	line_style   = { 'stroke': 'red',
        	             'stroke-width': str(self.options.mark0str) }
        	x1 = 0
        	y1 = i*res
        	x2 = self.options.scaleheight
        	y2 = i*res
        	
        	label = True
        	
    	if type==1:
	    	line_style   = { 'stroke': 'black',
        	             'stroke-width': str(self.options.mark1str) }
        	x1 = 0
        	y1 = i*res
        	x2 = self.options.scaleheight*0.01*self.options.mark1wid
        	y2 = i*res
        	
    	if type==2:
	    	line_style   = { 'stroke': 'black',
        	             'stroke-width': str(self.options.mark2str) }
        	x1 = 0
        	y1 = i*res
        	x2 = self.options.scaleheight*0.01*self.options.mark2wid
        	y2 = i*res    	      

       	x1 = str(inkex.unittouu(str(x1)+unit) )
       	y1 = str(inkex.unittouu(str(y1)+unit) )
       	x2 = str(inkex.unittouu(str(x2)+unit) )
       	y2 = str(inkex.unittouu(str(y2)+unit) )
       	if rotate=='90':
       		tx = x1
	       	x1 = y1
       		y1 = tx
       			
       		tx = x2
       		x2 = y2
       		y2 = tx
       	
    	if label==True:
		self.addLabel(n , x2, y2, grpLabel, fontsize)
    	line_attribs = {'style' : formatStyle(line_style),
                    inkex.addNS('label','inkscape') : 'name',
                    'd' : 'M '+x1+','+y1+' L '+x2+','+y2}

    	line = inkex.etree.SubElement(grp, inkex.addNS('path','svg'), line_attribs )
   	

    def effect(self):
    	
        scalefrom = self.options.scalefrom
        scaleto = self.options.scaleto
        scaleheight = self.options.scaleheight
        mark0 = self.options.mark0
        mark1 = self.options.mark1
        mark2 = self.options.mark2

        # Get access to main SVG document element and get its dimensions.
        svg = self.document.getroot()

        # Again, there are two ways to get the attributes:
        width  = inkex.unittouu(svg.get('width'))
        height = inkex.unittouu(svg.get('height'))
        
        # Create new group
        centre = self.view_center   #Put in in the centre of the current view
	grp_transform = 'translate' + str( centre )

        grp_name = 'Scale Labels'
        grp_attribs = {inkex.addNS('label','inkscape'):grp_name,
                           'transform':grp_transform }
	grpLabel = inkex.etree.SubElement(self.current_layer, 'g', grp_attribs)
		
	grp_name = 'Scale Mark labeled'
        grp_attribs = {inkex.addNS('label','inkscape'):grp_name,
                           'transform':grp_transform }
	grpMark0 = inkex.etree.SubElement(self.current_layer, 'g', grp_attribs)
	grp_name = 'Scale Mark medium'
        grp_attribs = {inkex.addNS('label','inkscape'):grp_name,
                           'transform':grp_transform }
	grpMark1 = inkex.etree.SubElement(self.current_layer, 'g', grp_attribs)	
	grp_name = 'Scale Mark default'
        grp_attribs = {inkex.addNS('label','inkscape'):grp_name,
                           'transform':grp_transform }
	grpMark2 = inkex.etree.SubElement(self.current_layer, 'g', grp_attribs)	

	# to allow positive to negative counts
        if scalefrom < scaleto:
        	scaleto += 1
        else:
        	temp = scaleto
        	scaleto = scalefrom+1
        	scalefrom = temp
 	
	skip = 0
        for i in range(scalefrom, scaleto):
        	if (i % mark0)==0:
        		div = 0		# This a the labeled marker
        		grpMark = grpMark0
        	elif (i % mark1)==0:
        		div = 1 	# the medium marker
        		grpMark = grpMark1
        	elif (i % mark2)==0:
        		div = 2 	# the default marker
        		grpMark = grpMark2
        	else:
        		skip=1	# Don't print a marker this time	        		
        	if skip==0:
        		self.addLine(i, scalefrom, scaleto, grpMark, grpLabel, div) # addLabel is called from inside
        	skip = 0


# Create effect instance and apply it.
effect = ScaleGen()
effect.affect()

