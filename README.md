Various helper classes to help you develop plugins, modules, etc in ansible

#Install
Install via pip:
    pip install --process-dependency-links git+ssh://git@github.com/venasolutions/ansible_helpers.git@master

..or in your setup.py add this to your project's dependency_links list:
    'git+ssh://git@github.com/venasolutions/ansible_helpers.git@master'

    And then simply add ansible_helpers to your install_requires

#Usage

##plugins 
    To implement a lookup plugin, create a class that extends VenaLookup.
    Implement a method do_lookup() that accepts positional arguments and returns what you looked up.
    See the VenaLookup docstring for more details.

    To implement an iterator lookup plugin, create a class that extends VenaIterator.
    Implement a method do_iterator that given keyword arguments will return a list of values.
    See the VeanIterator docstring for more details.
