from pathlib import Path
import toml
from . import config, commands, utils, conversations, oandr


cfg = toml.loads(Path(".env").read_text())

__version__ = ".".join(map(str,cfg["version"]))
__all__ = ['config', 'commands', 'utils', 'conversations', 'oandr', 'filestuff']

