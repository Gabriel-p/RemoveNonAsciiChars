# RemoveNonAsciiChars

Simple plugin to replace non-ASCII characters to ASCII by removing accents,
and remaining non-ASCII characters.

Turns:

    á à â ä ñ

into

    a a a a n

and removes characters like:

    ¡ ¿ ß


## Installation

Installation via [Sublime Package Control][wbond].

1. [Install Sublime Package Control][wbond 2]
2. From inside Sublime Text, open Package Control's Command Pallet:
   <kbd>CTRL+SHIFT+P</kbd> (Windows, Linux) or <kbd>CMD+SHIFT+P</kbd> (Mac).
3. Type `install package` and hit Return. A list of available packages will
   be displayed.
4. Type `RemoveNonAsciiChars` and hit Return.


## Using

1. Bring out the command palette with <kbd>CTRL+SHIFT+P</kbd> (Windows,
   Linux) or <kbd>CMD+SHIFT+P</kbd> on Mac.
2. Type `Remove Non Ascii Chars` until you see the commands.
3. Select `Remove non Ascii characters (File)` for removing in the entire file,
   or `Remove non Ascii characters (Select)` for removing only in the selected
   text.

## Author

* Gabriel Perren - [@Gabriel-p](https://github.com/Gabriel-p)

Original [idea and code](http://stackoverflow.com/a/38909594/1391441) by
[Keith Hall](http://stackoverflow.com/users/4473405/keith-hall).


## License

[GPL-v3.0](https://www.gnu.org/licenses/gpl-3.0.en.html).


[wbond]: http://wbond.net/sublime_packages/package_control
[wbond 2]: http://wbond.net/sublime_packages/package_control/installation