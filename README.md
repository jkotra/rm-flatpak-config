# rm-flatpak-config

`rm-flatpak-config` is a small python application to delete leftover config files after uninstalling flatpak application(s).

---

## Usage

```
usage: rm-flatpak-config.py [-h] [--debug] [--version]

rm-flatpak-config - Remove config files of flatpak applications!

optional arguments:
  -h, --help     show this help message and exit
  --debug, -D
  --version, -v
```

run the program either with python as a prefix or directly:

`python rm-flatpak-config`

a list will appear to choose from:

```
0 io.github.Hexchat user
1 org.gimp.GIMP user
2 net.mediaarea.MediaInfo user

Choose [0-3]:
```

## Dependencies

`Python 3+`