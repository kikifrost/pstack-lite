#!/usr/bin/env python3
"""Install selected skills without overwriting existing directories."""
from pathlib import Path
import argparse
import os
import shutil
import sys

REPO = Path(__file__).resolve().parents[1]


def install(source: Path, destination: Path, names: list[str]) -> None:
    conflicts = [name for name in names if (destination / name).exists() or (destination / name).is_symlink()]
    if conflicts:
        raise FileExistsError('Existing skills; nothing installed: ' + ', '.join(conflicts))
    destination.mkdir(parents=True, exist_ok=True)
    created = []
    try:
        for name in names:
            target = destination / name
            target.mkdir()
            created.append(target)
            shutil.copytree(source / name, target, dirs_exist_ok=True)
    except Exception:
        for target in reversed(created):
            shutil.rmtree(target)
        raise


def main() -> int:
    source = REPO / 'skills'
    available = sorted(path.name for path in source.iterdir() if (path / 'SKILL.md').is_file())
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--dest', type=Path, default=Path(os.environ.get('CODEX_HOME', str(Path.home() / '.codex'))) / 'skills')
    parser.add_argument('skills', nargs='*', help='Skill names; defaults to all 12')
    args = parser.parse_args()
    names = list(dict.fromkeys(args.skills or available))
    unknown = set(names) - set(available)
    if unknown:
        parser.error('Unknown skills: ' + ', '.join(sorted(unknown)))
    try:
        destination = args.dest.expanduser().resolve()
        install(source, destination, names)
    except OSError as error:
        print(str(error), file=sys.stderr)
        return 1
    print(f'Installed {len(names)} skills into {destination}')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
