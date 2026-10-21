#!/usr/bin/env python3
"""Look up name candidates on npm, PyPI, crates.io and GitHub.

Usage: python3 name_check.py <name> [<name> ...]

Prints one Markdown table row per name. GitHub lookups use the `gh` CLI when
it is installed and signed in; otherwise that column reads "not checked".
This is a collision check, not trademark or legal clearance. Same-space
products still need a web search.

Standard library only. Needs network access.
"""
import json
import shutil
import subprocess
import sys
import urllib.error
import urllib.request

UA = {"User-Agent": "name-check/0.1"}


def get(url):
    try:
        req = urllib.request.Request(url, headers=UA)
        with urllib.request.urlopen(req, timeout=15) as resp:
            return resp.status, json.loads(resp.read().decode())
    except urllib.error.HTTPError as err:
        return err.code, None
    except Exception as err:  # noqa: BLE001
        return type(err).__name__, None


def registry(url, describe):
    status, data = get(url)
    if status == 404:
        return "free"
    if status == 200 and data:
        return "taken: " + (describe(data) or "")[:50]
    return f"unknown ({status})"


def github(name):
    if not shutil.which("gh"):
        return "not checked"
    proc = subprocess.run(
        ["gh", "api", f"search/repositories?q={name}+in:name&sort=stars&per_page=50"],
        capture_output=True, text=True,
    )
    if proc.returncode != 0:
        return "not checked"
    items = json.loads(proc.stdout).get("items", [])
    exact = [i for i in items if i["name"].lower() == name.lower()]
    if not exact:
        return "no exact-name repos"
    top = exact[0]
    return f"{len(exact)} exact-name repos; top {top['full_name']} ({top['stargazers_count']} stars)"


def main(names):
    print("| Name | npm | PyPI | crates.io | GitHub |")
    print("|---|---|---|---|---|")
    for name in names:
        npm = registry(f"https://registry.npmjs.org/{name}", lambda d: d.get("description"))
        pypi = registry(f"https://pypi.org/pypi/{name}/json", lambda d: d["info"].get("summary"))
        crates = registry(f"https://crates.io/api/v1/crates/{name}", lambda d: d["crate"].get("description"))
        print(f"| {name} | {npm} | {pypi} | {crates} | {github(name)} |")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    main(sys.argv[1:])
