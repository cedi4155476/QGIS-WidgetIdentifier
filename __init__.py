# -*- coding: utf-8 -*-
"""
/***************************************************************************
 WidgetIdentifier
                                 A QGIS plugin
 This Plugin identifies widgets
                             -------------------
        begin                : 2015-07-10
        copyright            : (C) 2015 by Cédric Christen
        email                : cch@sourcepole.ch
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load WidgetIdentifier class from file WidgetIdentifier.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .widget_identifier import WidgetIdentifier
    return WidgetIdentifier(iface)
