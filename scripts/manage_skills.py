"""Local packaging/install utility; does not access network or overwrite by default."""
import argparse
from pathlib import Path
import shutil
import zipfile
import re

ROOT = Path(__file__).resolve().parents[1]
MAIN = 'financial-modelling'


def validate(folder):
    content = (folder / 'SKILL.md').read_text(encoding='utf-8')
    match = re.match(r'\A---\nname: ([a-z0-9-]+)\ndescription: ([^\n]+)\n---\n', content)
    if not match or match[1] != folder.name or not 1 <= len(match[1]) <= 64 or len(match[2]) > 1024:
        raise ValueError(f'Invalid front matter: {folder}')
    for link in re.findall(r'\]\(([^)]+)\)', content):
        if '://' not in link and not (folder / link).is_file():
            raise FileNotFoundError(f'{folder}: {link}')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('action', choices=['validate', 'package', 'install'])
    parser.add_argument('--agent', choices=['claude', 'codex'])
    parser.add_argument('--all', action='store_true')
    parser.add_argument('--replace', action='store_true')
    args = parser.parse_args()
    folders = sorted(p for p in (ROOT / 'skills').iterdir() if p.is_dir())
    for folder in folders:
        validate(folder)
    if args.action == 'validate':
        print(f'Validated {len(folders)} skill folders (structure and direct links only).')
        return
    if args.action == 'package':
        dest = ROOT / 'dist'
        dest.mkdir(exist_ok=True)
        for folder in folders:
            archive = dest / f'{folder.name}.zip'
            with zipfile.ZipFile(archive, 'w', zipfile.ZIP_DEFLATED) as z:
                for file in sorted(folder.rglob('*')):
                    if file.is_file():
                        z.write(file, file.relative_to(folder.parent))
            print(archive)
        return
    if not args.agent:
        parser.error('install requires --agent')
    dest = ROOT / ('.claude' if args.agent == 'claude' else '.agents') / 'skills'
    selected = folders if args.all else [ROOT / 'skills' / MAIN]
    for folder in selected:
        target = dest / folder.name
        if target.exists() and not args.replace:
            raise FileExistsError(f'{target}: already exists; review then use --replace if appropriate')
        if target.is_symlink():
            raise ValueError(f'Refusing symlink: {target}')
    dest.mkdir(parents=True, exist_ok=True)
    for folder in selected:
        target = dest / folder.name
        if target.exists():
            shutil.rmtree(target)
        shutil.copytree(folder, target)
        print(f'Installed {target}')


if __name__ == '__main__':
    main()
