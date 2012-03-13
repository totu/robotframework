#  Copyright 2008-2012 Nokia Siemens Networks Oyj
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

"""This package implements html file writing.

:mod:`robot.reporting`, :mod:`robot.libdoc` and :mod:`robot.testdoc` use
this package.
"""

from .htmlfilewriter import HtmlFileWriter, ModelWriter
from .jsonwriter import JsonWriter

LOG = 'rebot/log.html'
REPORT = 'rebot/report.html'
LIBDOC = 'libdoc/libdoc.html'
TESTDOC = 'testdoc/testdoc.html'
