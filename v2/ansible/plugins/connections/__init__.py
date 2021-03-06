# (c) 2012-2014, Michael DeHaan <michael.dehaan@gmail.com>
#
# This file is part of Ansible
#
# Ansible is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Ansible is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Ansible.  If not, see <http://www.gnu.org/licenses/>.

# Make coding more python3-ish
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from ansible import constants as C
from ansible.errors import AnsibleError

# FIXME: this object should be created upfront and passed through
#        the entire chain of calls to here, as there are other things
#        which may want to output display/logs too
from ansible.utils.display import Display

__all__ = ['ConnectionBase']


class ConnectionBase:
    '''
    A base class for connections to contain common code.
    '''

    has_pipelining = False
    become_methods = C.BECOME_METHODS

    def __init__(self, connection_info, *args, **kwargs):
        self._connection_info = connection_info
        self._display = Display(verbosity=connection_info.verbosity)


    def _become_method_supported(self, become_method):
        ''' Checks if the current class supports this privilege escalation method '''

        if become_method in self.__class__.become_methods:
            return True

        raise AnsibleError("Internal Error: this connection module does not support running commands via %s" % become_method)
