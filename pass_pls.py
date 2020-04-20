#!/usr/bin/env python3

import sys
import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, GLib

def ask_pass(primary_message, secondary_message=None):
    dialog = Gtk.MessageDialog(
        title="ssh-askpass",
        message_type=Gtk.MessageType.WARNING,
        text=primary_message,
        buttons=Gtk.ButtonsType.OK_CANCEL,
    )

    if secondary_message is not None:
        dialog.format_secondary_text(secondary_message)

    password_entry = Gtk.Entry()
    password_entry.set_visibility(False)
    password_entry.set_margin_start(20)
    password_entry.set_margin_end(20)
    password_entry.connect("activate", lambda w: dialog.response(Gtk.ResponseType.OK))

    dialog.get_content_area().add(password_entry)
    dialog.show_all()

    response = dialog.run()
    password = password_entry.get_text()
    dialog.destroy()

    if response != Gtk.ResponseType.OK:
        return None

    return password

def confirm(primary_message, secondary_message=None):
    dialog = Gtk.MessageDialog(
        title="ssh-askpass",
        message_type=Gtk.MessageType.WARNING,
        text=primary_message,
        buttons=Gtk.ButtonsType.YES_NO,
    )

    if secondary_message is not None:
        dialog.format_secondary_text(secondary_message)

    dialog.set_default_response(Gtk.ResponseType.YES)
    dialog.set_response_sensitive(Gtk.ResponseType.YES, False)
    dialog.set_response_sensitive(Gtk.ResponseType.NO, False)

    def enable_buttons():
        dialog.set_response_sensitive(Gtk.ResponseType.YES, True)
        dialog.set_response_sensitive(Gtk.ResponseType.NO, True)
        return False

    # Delay enabling of buttons to prevent accidental confirmation
    GLib.timeout_add(500, enable_buttons)

    response = dialog.run()
    dialog.destroy()

    if response != Gtk.ResponseType.YES:
        return False

    return True

def main(args=None):
    if args is None:
        args = sys.argv[1:]

    message = " ".join(args)
    lines = message.split("\n")
    
    primary_message = lines[0].strip()
    if primary_message == "":
        primary_message = "ssh-askpass"

    secondary_message = "\n".join(lines[1:]).strip()
    if secondary_message == "":
        secondary_message = None

    if primary_message.endswith("?"):
        ok = confirm(primary_message, secondary_message)
        if not ok:
            exit(1)
    else:
        result = ask_pass(primary_message, secondary_message)
        if result is None:
            exit(1)
        else:
            print(result)

    exit(0)

if __name__ == "__main__":
    main()
