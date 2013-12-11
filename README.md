Bootstrap 2 to 3
================

Helps to convert your templates from bootstap2 to 3.


* Replaces all bootstarp 2 classes to corresponding 3 classes

* Converts span* classes intelligently to col-mod-*


How to use as a script
----------------------

python bootstrap_2to3.py <root-project-directory>

This finds all .html files under the root folder and replaces bootstrap2 classes.


As a library
------------

pip install bootstrap_2to3

    from bootstrap_2to3 import convert
    
    convert()  # To convert all .html files under current directory
    convert('/user/works/project')  # To convert all .html files under given directory



