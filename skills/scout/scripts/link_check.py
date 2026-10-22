#!/usr/bin/env python3
"""Check that every URL cited in a dossier folder resolves.

Usage: python3 link_check.py <dossier-folder>

Scans every Markdown file under the folder, requests each unique URL (HEAD,
then GET), and prints a summary plus the URLs that are broken or that refuse
automated requests. A resolving link is not proof that the page says what the
entry claims; it only catches dead and invented links.

Standard library only. Needs network access, so it runs in Claude Code or a
terminal, not in a sandbox without network.
"""
import collections
import concurrent.futures as cf
import pathlib
import re
import sys
import urllib.error
import urllib.request

UA = {"User-Agent": "Mozilla/5.0 (Macintosh) dossier-link-check/0.1"}
# Stops at whitespace, closing brackets, quotes and backticks. A ">" inside a
# query (for example numericFilters=created_at_i>123) is kept; a trailing one
# from an <autolink> is stripped below.
URL = re.compile(r"https?://[^\s)\]\"'`]+")


def check(url):
    for method in ("HEAD", "GET"):
        try:
            req = urllib.request.Request(url, headers=UA, method=method)
            with urllib.request.urlopen(req, timeout=15) as resp:
                return url, resp.status
        except urllib.error.HTTPError as err:
            if method == "HEAD" and err.code in (400, 403, 404, 405, 429, 501):
                continue
            return url, err.code
        except Exception as err:  # noqa: BLE001 - report any failure kind
            if method == "HEAD":
                continue
            return url, type(err).__name__
    return url, "unknown"


def main(folder):
    root = pathlib.Path(folder)
    urls = set()
    for md in root.rglob("*.md"):
        if "transcript" in md.name:
            continue
        for match in URL.findall(md.read_text(encoding="utf-8")):
            urls.add(match.rstrip(".,;:>"))
    with cf.ThreadPoolExecutor(16) as pool:
        results = list(pool.map(check, sorted(urls)))
    counts = collections.Counter()
    problems = []
    for url, status in results:
        if isinstance(status, int) and status < 400:
            counts["resolve"] += 1
        elif status in (401, 403, 429):
            counts["refuse automated requests"] += 1
            problems.append(("refused", status, url))
        else:
            counts["broken"] += 1
            problems.append(("broken", status, url))
    print(f"{len(urls)} URLs: " + ", ".join(f"{n} {k}" for k, n in counts.items()))
    for kind, status, url in sorted(problems):
        print(f"{kind}\t{status}\t{url}")
    return 1 if counts["broken"] else 0


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    sys.exit(main(sys.argv[1]))
