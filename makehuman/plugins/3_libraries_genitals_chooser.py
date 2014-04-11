#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

"""
**Project Name:**      MakeHuman

**Product Home Page:** http://www.makehuman.org/

**Code Home Page:**    https://bitbucket.org/MakeHuman/makehuman/

**Authors:**           Thomas Larsson, Marc Flerackers

**Copyright(c):**      MakeHuman Team 2001-2014

**Licensing:**         AGPL3 (http://www.makehuman.org/doc/node/the_makehuman_application.html)

    This file is part of MakeHuman (www.makehuman.org).

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU Affero General Public License as
    published by the Free Software Foundation, either version 3 of the
    License, or (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU Affero General Public License for more details.

    You should have received a copy of the GNU Affero General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.

**Coding Standards:**  See http://www.makehuman.org/node/165

Abstract
--------

Genital proxy library.
"""

import gui3d
import mh
import proxychooser

class GenitalsTaskView(proxychooser.ProxyChooserTaskView):

    def __init__(self, category):
        super(GenitalsTaskView, self).__init__(category, 'genitals')

    def getObjectLayer(self):
        #return 3
        return 5

    def proxySelected(self, proxy):
        self.human.genitalsProxy = proxy

    def proxyDeselected(self, proxy, suppressSignal = False):
        self.human.genitalsProxy = None

    def onShow(self, event):
        super(GenitalsTaskView, self).onShow(event)
        if gui3d.app.settings.get('cameraAutoZoom', True):
            gui3d.app.setGlobalCamera()


# This method is called when the plugin is loaded into makehuman
# The app reference is passed so that a plugin can attach a new category, task, or other GUI elements


taskview = None

def load(app):
    global taskview

    category = app.getCategory('Geometries')
    taskview = GenitalsTaskView(category)
    taskview.sortOrder = 2
    category.addTask(taskview)

    taskview.registerLoadSaveHandlers()


# This method is called when the plugin is unloaded from makehuman
# At the moment this is not used, but in the future it will remove the added GUI elements


def unload(app):
    taskview.onUnload()

