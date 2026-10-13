#!/usr/bin/env python3
"""Check packaging and observable installer and log behavior offline."""
from pathlib import Path
import csv
import re
import subprocess
import sys
import tempfile
import yaml

REPO = Path(__file__).resolve().parents[1]


def check_package() -> None:
    skills = sorted((REPO / 'skills').iterdir())
    assert len(skills) == 12, f'Expected 12 skills, found {len(skills)}'
    for skill in skills:
        text = (skill / 'SKILL.md').read_text()
        parts = text.split('---', 2)
        assert len(parts) == 3 and not parts[0].strip(), skill
        meta = yaml.safe_load(parts[1])
        assert meta['name'] == skill.name, skill
        assert isinstance(meta['description'], str) and meta['description'].strip(), skill
        assert set(meta) <= {'name', 'description', 'metadata'}, skill
        config = yaml.safe_load((skill / 'agents/openai.yaml').read_text())
        assert config['policy']['allow_implicit_invocation'] is False, skill
    for file in REPO.rglob('*.md'):
        if '.git' in file.parts:
            continue
        for link in re.findall(r'\[[^\]]*\]\(([^)]+)\)', file.read_text()):
            if '://' in link or link.startswith('#'):
                continue
            target = (file.parent / link.split('#', 1)[0]).resolve()
            assert target.is_relative_to(REPO), (file, link)
            assert target.exists(), (file, link)
    print('12 skill packages, invocation policies and Markdown links passed')


def run_install(destination: Path, *names: str) -> subprocess.CompletedProcess:
    return subprocess.run([sys.executable, str(REPO / 'scripts/install.py'), '--dest', str(destination), *names], capture_output=True, text=True)


def check_installer() -> None:
    with tempfile.TemporaryDirectory(prefix='pstack-lite-check-') as tmp:
        destination = Path(tmp) / 'skills'
        result = run_install(destination, 'how')
        assert result.returncode == 0, result.stderr
        assert (destination / 'how/SKILL.md').read_bytes() == (REPO / 'skills/how/SKILL.md').read_bytes()
        sentinel = destination / 'how/user-edit.txt'
        sentinel.write_text('Keep the existing local edit')
        result = run_install(destination, 'why', 'how')
        assert result.returncode != 0, result.stdout
        assert not (destination / 'why').exists()
        assert sentinel.read_text() == 'Keep the existing local edit'
        result = run_install(destination, '../outside')
        assert result.returncode != 0
        assert not (Path(tmp) / 'outside').exists()
        full = Path(tmp) / 'all'
        result = run_install(full)
        assert result.returncode == 0, result.stderr
        assert len(list(full.iterdir())) == 12
        for source in (REPO / 'skills').rglob('*'):
            if source.is_file():
                assert (full / source.relative_to(REPO / 'skills')).read_bytes() == source.read_bytes(), source
    print('Selective and full install, unknown-name rejection, conflict atomicity and local-edit preservation passed')


def check_log() -> None:
    with tempfile.TemporaryDirectory(prefix='pstack-lite-log-') as tmp:
        path = Path(tmp) / 'nested/decisions.tsv'
        script = REPO / 'skills/show-me-your-work/scripts/log.sh'
        subprocess.run(['bash', str(script), str(path), 'start', 'Inspect', '=untrusted\tcell\nnext', 'local fixture', 'open'], check=True)
        subprocess.run(['bash', str(script), str(path), 'check', 'Append', 'Keep history', 'local fixture', 'passed'], check=True)
        with path.open() as file:
            rows = list(csv.reader(file, delimiter='\t'))
        assert len(rows) == 3 and all(len(row) == 6 for row in rows)
        assert rows[0] == ['ts', 'phase', 'decision', 'why', 'evidence', 'result']
        assert rows[1][3] == "'=untrusted cell next"
        assert rows[1][1] == 'start' and rows[2][1] == 'check'
    print('TSV header, append behavior, cell sanitization and formula protection passed')


if __name__ == '__main__':
    check_package()
    check_installer()
    check_log()
