"""MkDocs hooks for Nazir's eMahad Notes site.

Single hook: strip the MarkText-specific <style> blocks that live at the top
of every notes/section/README .md file. Those style blocks set body fonts +
heading colors for MarkText viewing; in MkDocs Material they would override
the theme's CSS and break the site's typography.

The blocks are leading-position only (top of file, before any markdown
content). We do a non-greedy match anchored at the start and strip the first
<style>...</style> block plus any trailing whitespace before the next
markdown content.
"""
import re

_STYLE_BLOCK = re.compile(
    r'^\s*<style\b[^>]*>.*?</style>\s*',
    flags=re.DOTALL | re.IGNORECASE,
)


def on_page_markdown(markdown, *, page, config, files):
    return _STYLE_BLOCK.sub('', markdown, count=1)
