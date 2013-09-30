import os
import sys
import glob
import re


2to3_mapping = {
    "container-fluid": "container",
    "row-fluid": "row",
    "brand": "navbar-brand",
    "hero-unit": "jumbotron",
    "btn-mini": "btn-xs",
    "btn-small": "btn-sm",
    "btn-large": "btn-lg",
    "visible-phone": "visible-sm",
    "visible-tablet": "visible-md",
    "visible-desktop": "visible-lg",
    "hidden-phone": "hidden-sm",
    "hidden-tablet": "hidden-md",
    "hidden-desktop": "hidden-lg",
    "input-prepend": "input-group",
    "input-append": "input-group",
    "add-on": "input-group-addon",
    "btn-navbar": "navbar-btn",
    "thumbnail": "img-thumbnail"
}


class TemplateFinder(object):

    def __init__(self, root_dir):
        pass

    def __iter__(self):
        pass

    def next(self):
        pass


class TwoToThree(object):

    def __init__(self, html):
        self.html = html

    def convert(self):
        self.replace_simple_classes()
        self.replace_span_classes()
        self.replace_btn_classes()
        return self.html

    def replace_simple_classes(self):
        for key, val in 2to3_mapping:
            html = html.replace(key, val)
        return html

    def replace_span_classes(self):        
        pass

    def replace_btn_classes(self):
        pass


if __name__ == "__main__":
    try:
        root_folder = argv[1]
    except IndexError:
        root_folder = os.getcwd()    
    #FIXME: copy to a new directory before manipulating files

    for each in TemplateFinder(root_folder):
        with open(each, 'r') as fr:
            output = TwoToThree(fr.read()).convert()
            with open(each, 'w') as fw:
                fw.write(output)
