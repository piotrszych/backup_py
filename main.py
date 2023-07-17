import json
import os
import shutil
from termcolor import colored
from datetime import datetime

def _errorAndExit(message):
    print(colored(message, 'red'))
    os.system('pause')
    exit(1)

def _testConfig(config):
    if all(k in config for k in ("sources", "destination")):
        return True
    raise ValueError(f"Brak wymaganych pól w pliku konfiguracyjnym. (sources -> array, destination -> string)")

def _currentDateTimeString():
    now = datetime.now()
    return now.strftime("%Y-%m-%d_%H-%M")

def _createPathsIfNotExist(path):
    doExists = os.path.exists(path)
    if not doExists:
        os.makedirs(path)
        print(colored(f"Stworzono brakujące foldery w ścieżce: {path}"))
    return True


config = None
try:
    f = open("config.json", encoding='utf-8')
    config = json.load(f)
    _testConfig(config)
except FileNotFoundError:
    _errorAndExit("Brak pliku konfiguracyjnego (config.json).")
except json.JSONDecodeError as e:
    _errorAndExit(f"Nieprawidłowy format pliku: {e}")
except ValueError as e:
    _errorAndExit(e)

destnationBase = config['destination']
sources = config['sources']

allPaths = [destnationBase] + sources
print(allPaths)
for p in allPaths:
    _createPathsIfNotExist(p)

destination = os.path.join(os.sep, destnationBase, _currentDateTimeString())
_createPathsIfNotExist(destination)

for s in sources:
    print(f"Kopiowanie '{s}'...")
    targetDirName = os.path.basename(os.path.normpath(s))
    shutil.copytree(s, os.path.join(os.sep, destination, targetDirName))
    print(colored("[✓]", "green"), f"Zrobione.")

print(colored(f"Sukces!", "green"))
print(colored(f"Zakończono tworzenie kopii zapasowej {len(sources)} folderu/ów.", "green"))
os.system('pause')
exit(0)