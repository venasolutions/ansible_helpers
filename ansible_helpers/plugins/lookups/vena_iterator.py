#!/usr/bin/env python

from ansible.errors import AnsibleError

from ansible_helpers.plugins.lookups.base_lookup import VenaLookupBase

class VenaIterator(VenaLookupBase):
    """
    Abstract class for implementing an ansible iterator. Lookups that extend
    this class are expected to implement a method do_iterator() that accepts
    keyword arguments only. In run() we'll take the dictionary passed to the
    lookup and pass them like do_iterator(**kwargs)
    """

    def run(self, terms=None, **kwargs):
        return self.do_iterator(**terms)

    def do_iterator(self, **kwargs):
        raise NotImplementedError()
