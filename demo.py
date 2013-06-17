#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
File: demo.py
Author: huxuan
Email: i(at)huxuan.org
Description: Demo show about dialog of GTG
"""

from gi.repository import GObject, Gtk

import info

PATH_ABOUT_UI = 'about.ui'

class About(Gtk.Window):
    """docstring for About"""
    def __init__(self):
        self.builder = Gtk.Builder()
        self.builder.add_from_file(PATH_ABOUT_UI)

        SIGNAL_CONNECTIONS_DIC = {
            "on_about_delete":
                self.on_about_close,
            "on_about_close":
                self.on_about_close,
        }
        self.builder.connect_signals(SIGNAL_CONNECTIONS_DIC)

        self.about = self.builder.get_object("about_dialog")
        self.about.set_website(info.URL)
        self.about.set_website_label(info.URL)
        self.about.set_version(info.VERSION)
        self.about.set_authors(info.AUTHORS)
        self.about.set_artists(info.ARTISTS)
        self.about.set_documenters(info.DOCUMENTERS)
        self.about.set_translator_credits(info.TRANSLATORS)

    def on_about_close(self, widget, response):
        """
        close the about dialog
        """
        Gtk.main_quit()
        return True

    def show(self):
        self.about.show()

def main():
    """docstring for main"""
    about = About()
    about.show()
    Gtk.main()

if __name__ == '__main__':
    main()
