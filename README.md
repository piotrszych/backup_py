# Backup - Python script and exe

Simple program that creates backup of directories to target path.
Both can be configured in the `config.json` file.

Written with Windows 10 OS in mind.

All messages are in Polish, as this is the target user's language.

## Preparing a distribution build

The script was written using `python3`, version `3.7.3`. If later versions
of the language added some breaking changes, it might need few adjustments.

Ensure you have `pyinstaller` installed. Installation instructions
and documentation https://pyinstaller.org/.

After that, just `cd` into the project's directory and run command:

```
pyinstaller --add-data "config.json;." .\backup.py
```

Please note that `--add-data` option has `;` character as delimeter;
it's probably Windows-specific syntax.