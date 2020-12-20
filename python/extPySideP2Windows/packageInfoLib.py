#
# Copyright 2020 Safak Oner.
#
# This library is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.
#
# ----------------------------------------------------------------------------------------------------
# DESCRIPTION
# ----------------------------------------------------------------------------------------------------
## @package extPySideP2Windows                           @brief [ PACKAGE   ] - PySide (Python 2) for Windows OS.
## @dir     extPySideP2Windows/python                    @brief [ DIRECTORY ] - Python path.
## @dir     extPySideP2Windows/python/extPySideP2Windows @brief [ DIRECTORY ] - Python package.
## @file    extPySideP2Windows/packageInfoLib.py         @brief [ FILE      ] - Package info module.
## @package extPySideP2Windows.packageInfoLib            @brief [ MODULE    ] - Package info module.


#
# ----------------------------------------------------------------------------------------------------
# IMPORTS
# ----------------------------------------------------------------------------------------------------


#
#-----------------------------------------------------------------------------------------------------
# CODE
#-----------------------------------------------------------------------------------------------------
## [ str ] - Name of the package.
NAME                = 'extPySideP2Windows'

## [ str ] - Version of the package.
VERSION             = '1.2.2'

## [ str ] - Description about the package.
DESCRIPTION         = 'PySide (Python 2) for Windows OS.'

## [ list of str ] - Keywords to find this package.
KEYWORDS            = ['pyside', 'qt', 'binding', 'gui', 'ui', 'widget']

## [ list of str ] - Platforms which this package meant to be used on.
PLATFORMS           = ['Windows']

## [ list of dict ] - Documentations about the package, keys of dict instances are: title, url.
DOCUMENTS           = []

## [ list of str ] - Applications which this package meant to be initialized for.
APPLICATIONS        = ['standalone']

## [ list of str ] - Python versions supported by this package.
PYTHON_VERSIONS     = ['2']

## [ bool ] - Whether this package is active (in use).
IS_ACTIVE           = True

## [ bool ] - Whether this package is external (third party).
IS_EXTERNAL         = True

## [ list of str ] - E-mail addresses of the developers.
DEVELOPERS          = ['safak@safakoner.com']

## [ list of str ] - Dependent packages.
DEPENDENT_PACKAGES  = []

## [ list of str ] - Python packages contained by this package.
PYTHON_PACKAGES     = ['extPySideP2Windows']