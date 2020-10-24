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
 SNO	 Application ID 
0 	 com.github.johnfactotum.Foliate (system)
1 	 io.github.Hexchat (user)
2 	 org.gimp.GIMP (user)
3 	 org.gnome.Glade (user)
4 	 org.gnome.Boxes (user)
5 	 com.bitstower.Markets (user)
6 	 net.mediaarea.MediaInfo (user)
7 	 com.github.johnfactotum.Foliate (user)
8 	 org.pitivi.Pitivi (user)

Choose [0-9]:

```

## Dependencies

`Python 3+`