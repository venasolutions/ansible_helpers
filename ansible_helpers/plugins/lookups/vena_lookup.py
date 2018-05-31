#!/usr/bin/env python

from ansible.errors import AnsibleError

from ansible_helpers.plugins.lookups.base_lookup import VenaLookupBase

class VenaLookup(VenaLookupBase):
    """
    Abstract class for implementing an ansible lookup. The goal of this class
    is to do most of the ansible boilerplate necessary to make implementing
    a lookup as easy as possible. Ideally you should be able to implement
    a method that looks very much like just python and be good to go. IE something
    like `def do_lookup(self, vpc_name, region)` might lookup a vpc and return
    a vpc id
    """
    def __init__(self, flatten=False, no_args=False, **kwargs):
        super(VenaLookup, self).__init__(**kwargs)
        self.flatten = flatten
        self.no_args = no_args #set true if your lookup is expected not to accept args

    def run(self, *arg_list, **kwargs):
        """
        Main entrypoint for a value lookup.
        args_list contains the arguments passed to the lookup. To use this abstract class
        you must implement do_lookup() and we will pass the args passed to the lookup in order
        """

        arg_list, extra_args = self.get_args(arg_list, kwargs)

        if not arg_list and not extra_args:
            if self.no_args:
                #special case for lookups that don't accept any args, call once
                return [ self.do_lookup() ]
            else:
                raise AnsibleError("expected at least one arg but none found!")

        results = []
        for args in arg_list:
            r = self.do_lookup(*args, **extra_args)
            if self.flatten:
                results.extend(r)
            else:
                results.append(r)

        return results

    def get_args(self, args, kwargs):
        #based on lookup_kwargs(), extract them from the kwargs injected by ansible
        #(we get a whole bunch of noise that we don't necessarily want in the lookup)
        extra_args = { arg : kwargs[arg] for arg in self.lookup_kwargs() if arg in kwargs }

        return args, extra_args

    def lookup_kwargs(self):
        """
        Return a list of keyword args your lookup supports. We'll extract them from
        the args injected by ansible
        """
        return []

    def do_lookup(self, *args):
        raise NotImplementedError()
