"""A script for building an exe."""

from pathlib import Path
from datetime import datetime
from subprocess import call

if __name__ == "__main__":
    call(['rm', '-rf', 'build', 'dist', '*.spec'])
    now: datetime = datetime.now()
    name: str = 'synthizer-reverb-%s.exe' % now.strftime('%Y-%m-%d')
    call(
        [
            'pyinstaller', '--onefile', '-w', '--clean', '-y', '-n', name,
            'synthizer-reverb.py'
        ]
    )
    p: Path = Path(name + '.spec')
    p.unlink()
