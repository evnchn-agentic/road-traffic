"""Fetch every source cited in FACTCHECK.md and check its quoted text still appears there.

Usage: python3 check_quotes.py FACTCHECK.md
Rows are table lines whose last two cells are `[...](url)` and `"quote"`.
Needs `pdftotext` (poppler) for PDF sources. Exit 1 if any quote is missing.
"""
import html, re, subprocess, sys, unicodedata

ROW = re.compile(r'^\|\s*(\w+)\s*\|.*\[[^\]]*\]\((https?://\S+?)\)\s*\|\s*"(.+)"\s*\|\s*$')


def norm(s):
    s = unicodedata.normalize('NFKC', html.unescape(s)).lower()
    s = s.translate(str.maketrans('‘’“”–— ', "''\"\"-- "))
    return re.sub(r'\s+', ' ', re.sub(r'[*_`]', '', s)).strip()


def page_text(url):
    # curl, not urllib: some gov.hk hosts send a chain Python's bundled CAs reject
    r = subprocess.run(['curl', '-sSLf', '--max-time', '60', '-A', 'Mozilla/5.0 (Macintosh) factcheck', url],
                       capture_output=True, check=True)
    body = r.stdout
    if body[:4] == b'%PDF':
        return subprocess.run(['pdftotext', '-layout', '-', '-'], input=body, capture_output=True).stdout.decode('utf-8', 'replace')
    text = body.decode('utf-8', 'replace')
    text = re.sub(r'(?is)<(script|style)\b.*?</\1>', ' ', text)
    return re.sub(r'<[^>]+>', ' ', text)


def main(path):
    rows = [m.groups() for line in open(path, encoding='utf-8') if (m := ROW.match(line.strip()))]
    bad = 0
    for cid, url, quote in rows:
        try:
            ok = norm(quote.replace('\\|', '|')) in norm(page_text(url))
            status = 'OK  ' if ok else 'MISS'
        except Exception as e:
            ok, status = False, f'ERR {type(e).__name__}'
        bad += not ok
        print(f'{status} {cid:4} {url}')
    print(f'{len(rows) - bad}/{len(rows)} quotes found')
    return 1 if bad or not rows else 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1]))
