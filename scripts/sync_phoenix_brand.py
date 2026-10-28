from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[1]
PHOENIX = "/assets/brand/phoenix-mark.png"
FAVICON = "/assets/brand/favicon.png"
APPLE_ICON = "/assets/brand/apple-touch-icon.png"
THEME_VERSION = "20261028-10"
OG_IMAGE = "https://reincarnationpk.com/assets/generated/homepage-digital-intelligence.webp"
OG_LOGO = "https://reincarnationpk.com/assets/brand/logo.png"


hero_pattern = re.compile(
    r'(?P<open><div[^>]*class="[^"]*\bhero_bg-logo\b[^"]*"[^>]*>)'
    r'\s*(?:<svg\b.*?</svg>|<img\b[^>]*>)\s*</div>',
    re.DOTALL,
)


def phoenix_hero(match: re.Match[str]) -> str:
    opening = match.group("open")
    if "brand-phoenix-watermark" not in opening:
        opening = opening.replace(
            "hero_bg-logo", "hero_bg-logo brand-phoenix-watermark", 1
        )
    return (
        f'{opening}<img src="{PHOENIX}" alt="" aria-hidden="true" '
        'class="brand-phoenix-watermark__image"></div>'
    )


def replace_meta_content(
    html: str, property_name: str, replacement: str, attribute_name: str = "property"
) -> str:
    pattern = re.compile(
        rf'<meta\b(?=[^>]*\b{re.escape(attribute_name)}="{re.escape(property_name)}")[^>]*>',
        re.IGNORECASE,
    )

    def update(match: re.Match[str]) -> str:
        tag = match.group(0)
        content = re.search(r'(?:^|\s)content="([^"]*)"', tag, re.IGNORECASE)
        if not content or content.group(1) == replacement:
            return tag
        legacy = content.group(1)
        tag = tag.replace(
            f'content="{legacy}"', f'content="{replacement}"', 1
        )
        if "data-legacy-content=" not in tag:
            tag = tag[:-1] + f' data-legacy-content="{legacy}">'
        return tag

    return pattern.sub(update, html)


updated = 0
hero_count = 0
for path in ROOT.rglob("*.html"):
    html = path.read_text(encoding="utf-8")
    original = html

    html, count = hero_pattern.subn(phoenix_hero, html)
    hero_count += count
    html = html.replace(
        "/672a218a745565a8de00b5ec/phoenix-hero-watermark.png?v=20261028-3",
        PHOENIX,
    )
    html = replace_meta_content(html, "og:image", OG_IMAGE)
    html = replace_meta_content(html, "og:logo", OG_LOGO)
    html = replace_meta_content(html, "twitter:image", OG_IMAGE, "name")

    html = re.sub(
        r'<link\b[^>]*\brel="(?:shortcut )?icon"[^>]*>',
        f'<link href="{FAVICON}" rel="icon" type="image/png" sizes="512x512">',
        html,
        count=1,
    )
    html = re.sub(
        r'<link\b[^>]*\brel="apple-touch-icon"[^>]*>',
        f'<link href="{APPLE_ICON}" rel="apple-touch-icon" sizes="180x180">',
        html,
        count=1,
    )
    html = re.sub(
        r'/assets/brand/theme\.css(?:\?v=[^"\s]+)?',
        f'/assets/brand/theme.css?v={THEME_VERSION}',
        html,
    )

    if html != original:
        path.write_text(html, encoding="utf-8")
        updated += 1

print(f"Updated phoenix branding in {updated} HTML files; replaced {hero_count} hero SVGs.")
