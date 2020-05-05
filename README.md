# pass-pls

A GTK-based implementation of ssh-askpass.

**Why?** Because `ssh-askpass-gnome` was asking for a password even for confirmations.
Also, its lack of margins bothered me.

## Screenshots

![Ask](https://raw.githubusercontent.com/undecidabot/pass-pls/master/screenshots/ask.png)

![Confirm](https://raw.githubusercontent.com/undecidabot/pass-pls/master/screenshots/confirm.png)

## Installation

To install:
```
$ sudo pip3 install pass-pls
$ sudo update-alternatives --install /usr/bin/ssh-askpass ssh-askpass /usr/local/bin/pass-pls 100
```

To uninstall:
```
$ sudo update-alternatives --remove ssh-askpass /usr/local/bin/pass-pls
```

If you do not have `update-alternatives`, manually create a symlink instead.
