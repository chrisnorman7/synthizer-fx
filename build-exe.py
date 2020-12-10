"""A script for building an exe."""

from datetime import datetime
from subprocess import call

if __name__ == "__main__":
    call(['rm', '-rf', 'build', 'dist', '*.spec'])
    now: datetime = datetime.now()
    call(
        [
            'pyinstaller', '--onefile', '-w', '--clean', '-y', '-n',
            'synthizer-reverb-%s.exe' % now.strftime('%Y-%m-%d'),
            'synthizer-reverb.py'
        ]
    )
