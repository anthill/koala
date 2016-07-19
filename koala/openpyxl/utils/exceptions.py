#
# source: https://bitbucket.org/openpyxl/openpyxl/src/93604327bce7aac5e8270674579af76d390e09c0/openpyxl/utils/exceptions.py?at=default&fileviewer=file-view-default
#__________________________________________________________________________________________________________________________________________________________________

from __future__ import absolute_import
# Copyright (c) 2010-2016 openpyxl


"""Definitions for openpyxl shared exception classes."""


class CellCoordinatesException(Exception):
    """Error for converting between numeric and A1-style cell references."""

class IllegalCharacterError(Exception):
    """The data submitted which cannot be used directly in Excel files. It
    must be removed or escaped."""

class NamedRangeException(Exception):
    """Error for badly formatted named ranges."""

class SheetTitleException(Exception):
    """Error for bad sheet names."""

class InsufficientCoordinatesException(Exception):
    """Error for partially specified cell coordinates."""

class InvalidFileException(Exception):
    """Error for trying to open a non-ooxml file."""

class ReadOnlyWorkbookException(Exception):
    """Error for trying to modify a read-only workbook"""

class WorkbookAlreadySaved(Exception):
    """Error when attempting to perform operations on a dump workbook
    while it has already been dumped once"""