from pathlib import Path
import json
import re
import sys


ROOT = Path(__file__).resolve().parents[1]
LEGACY_PREFIX = "/672a218a745565a8de00b5ec/"
GENERATED_PREFIX = "/assets/generated/"
UNTILED_ASSETS = {"homepage-digital-intelligence.webp"}

ALT_TO_ASSET = {
    "A hand holding a smartphone displaying an app interface. Below the phone, a large, prominent red App Store icon is visible.": "ios-platform-device.webp",
    "A mobile mockup of an Android app developed by Reincarnation's Android app developers, showing the internal interface.": "android-app-mockup.webp",
    "A mobile mockup of an app developed by Reincarnation's app developers, showing the internal interface.": "mobile-app-mockup.webp",
    "A mobile mockup of an iOS app developed by Reincarnation's iOS app developers, showing the internal interface.": "ios-app-mockup.webp",
    "An Android smartphone displaying an app interface. Next to the phone, a large, prominent green Android logo is visible.": "android-platform-device.webp",
    "Bearded man in gray hoodie writing on a whiteboard filled with handwritten notes and diagrams.": "whiteboard-systems-lead.webp",
    "Businesswoman presenting a Q4 growth bar and line chart to two seated colleagues at a modern desk.": "business-growth-presentation.webp",
    "Diagram of app planning on a whiteboard by the Reincarnation team, discussing business challenges and solutions for mobile and web applications to improve, scale, or streamline processes.": "app-planning-whiteboard.webp",
    "Eight men in a meeting room, one writing on large sheets on the table while others watch.": "operations-workshop.webp",
    "Glowing red digital profile of a human head made of particles with a bright spot in the brain area on a dark background.": "homepage-digital-intelligence.webp",
    "Group of five professionals in a meeting room with a laptop and sticky notes on the table.": "planning-team.webp",
    "Man in glasses writing on a whiteboard with numbers 3, 4, and 5 and a simple diagram.": "planning-steps-whiteboard.webp",
    "Man in white shirt discussing with two others in a bright office with a motivational poster on the wall.": "homepage-collaboration.webp",
    "Man in yellow shirt writing on a whiteboard with notes about CMS, SMP, and API consumers.": "systems-architecture-whiteboard.webp",
    "Man sketching designs by hand at a desk with two laptops, sketches, coffee, and office items.": "design-sketching.webp",
    "Man using a smartphone on stand at a booth with laptops, books, and promotional banners.": "product-event-demo.webp",
    "Man wearing glasses sitting at desk viewing two monitors, one showing code and the other a media app.": "dual-monitor-developer.webp",
    "Man with curly hair and beard sitting at a desk, looking at a laptop, with smartphone on table.": "homepage-focused-analyst.webp",
    "Meeting room with two men discussing a TeleNICU pilot roadmap on a screen and notes on a whiteboard.": "service-roadmap-review.webp",
    "Mockup of an app built by Reincarnation's web app developers, showing the app's internal interface on a desktop.": "web-app-mockup.webp",
    "Person sitting at a desk working on coding software on a laptop with multiple monitors in a tech workspace.": "coding-workspace.webp",
    "Purple 3D humanoid robot figure on a light purple background, raising its right hand as if waving.": "ai-automation-assistant.webp",
    "Reincarnation - Web and mobile app development to optimise processes, improve communication, and scale businesses.": "discovery-business-solutions.webp",
    "Reincarnation team discussing solutions with a client, on app development": "discovery-client-conversation.webp",
    "Reincarnation's mobile app developers discussing the mobile app development process.": "mobile-app-team.webp",
    "Reincarnation's web app developers working together, collaborating on different aspects of the web app development process.": "web-app-team.webp",
    "Silhouette of a man sitting at a desk using a computer with a pink background.": "business-systems-workstation.webp",
    "Silhouette of a person with a bun holding a camera on a stabilizer against a blue background.": "media-technology.webp",
    "Silhouette of a woman sitting at a table, writing on a notepad next to an open laptop in a minimalist room.": "woman-planning-at-laptop.webp",
    "Silhouette of a young plant with leaves growing from soil on a turquoise background.": "growth-systems.webp",
    "Silhouette of person adjusting a mechanical part on an industrial machine against yellow background.": "industrial-operations.webp",
    "Silhouetted group in business meeting with two men shaking hands against yellow background.": "business-partnership-meeting.webp",
    "Silhouetted group of six diverse business people standing in a circle, engaged in discussion against an orange background.": "business-roundtable.webp",
    "Silhouettes of a man and woman facing each other and shaking hands against a purple background.": "client-partnership-handshake.webp",
    "Silhouettes of a man and woman facing each other, both looking at their smartphones.": "mobile-customer-journey.webp",
    "Silhouettes of three people working at a desk with three computer screens against a green background.": "operations-workstation-team.webp",
    "Silhouettes of two construction workers wearing helmets shaking hands against a pink background.": "construction-partnership.webp",
    "Silhouettes of two construction workers wearing helmets working on a building framework.": "construction-delivery.webp",
    "Smiling woman holding an electronic device with display and labeled switches on front panel.": "homepage-hardware-support.webp",
    "Three men in a meeting room watching a flowchart on a large screen against a yellow wall.": "flowchart-review.webp",
    "Two men at a table in an office, one working on a laptop, the other looking at a phone.": "laptop-phone-collaboration.webp",
    "Two men looking thoughtfully to the left against a bright yellow wall background.": "leadership-looking-ahead.webp",
    "Two men smiling and posing with thumbs up in front of a Linkup app billboard on a city street.": "product-launch-moment.webp",
    "Two professionals sitting across a desk, one writing and the other facing them in an office with a laptop and microscope.": "specialist-consultation.webp",
    "Two women in podcast studio, one with phone and black tappable bottle, the other with drink can.": "podcast-studio.webp",
}

img_pattern = re.compile(r"<img\b[^>]*>", re.IGNORECASE)


def attribute(tag: str, name: str) -> str | None:
    match = re.search(rf'(?:^|\s){re.escape(name)}="([^"]*)"', tag, re.IGNORECASE)
    return match.group(1) if match else None


def replacement_for(source: str, alt: str) -> str | None:
    asset = ALT_TO_ASSET.get(alt)
    if not asset:
        return None
    if asset not in UNTILED_ASSETS:
        asset = f"{Path(asset).stem}-tiles-v2.webp"
    return f"{GENERATED_PREFIX}{asset}"


def apply_generated(tag: str, manifest: dict[str, str]) -> str:
    source = attribute(tag, "src")
    alt = attribute(tag, "alt")
    legacy = attribute(tag, "data-legacy-src")
    if source and legacy and source.startswith(GENERATED_PREFIX):
        desired = replacement_for(legacy, alt or "")
        if desired and desired != source:
            tag = tag.replace(f'src="{source}"', f'src="{desired}"', 1)
            source = desired
        manifest[legacy] = source
        return tag
    if not source or not alt or not source.startswith(LEGACY_PREFIX):
        return tag
    replacement = replacement_for(source, alt)
    if not replacement:
        return tag
    manifest[source] = replacement
    tag = tag.replace(
        f'src="{source}"',
        f'data-legacy-src="{source}" src="{replacement}"',
        1,
    )
    tag = re.sub(r'\bsrcset=', 'data-legacy-srcset=', tag, count=1)
    tag = re.sub(r'\bsizes=', 'data-legacy-sizes=', tag, count=1)
    return tag


def restore_legacy(tag: str) -> str:
    legacy = attribute(tag, "data-legacy-src")
    if not legacy:
        return tag
    tag = re.sub(r'\s+src="[^"]*"', '', tag, count=1)
    tag = tag.replace(f'data-legacy-src="{legacy}"', f'src="{legacy}"', 1)
    tag = tag.replace('data-legacy-srcset=', 'srcset=', 1)
    tag = tag.replace('data-legacy-sizes=', 'sizes=', 1)
    return tag


restore = "--restore" in sys.argv
manifest: dict[str, str] = {}
updated_files = 0
updated_tags = 0

for path in sorted(ROOT.rglob("*.html")):
    html = path.read_text(encoding="utf-8")

    def update(match: re.Match[str]) -> str:
        global updated_tags
        original = match.group(0)
        revised = restore_legacy(original) if restore else apply_generated(original, manifest)
        if revised != original:
            updated_tags += 1
        return revised

    revised = img_pattern.sub(update, html)
    if revised != html:
        path.write_text(revised, encoding="utf-8")
        updated_files += 1

manifest_path = ROOT / "assets" / "generated" / "image-manifest.json"
if not restore:
    manifest_path.write_text(
        json.dumps(
            {
                "purpose": "Reversible mapping from legacy section imagery to original AI-generated replacements.",
                "restore_command": "python scripts/sync_generated_images.py --restore",
                "apply_command": "python scripts/sync_generated_images.py",
                "images": dict(sorted(manifest.items())),
            },
            indent=2,
        ) + "\n",
        encoding="utf-8",
    )

mode = "Restored legacy" if restore else "Applied generated"
print(f"{mode} imagery in {updated_files} files ({updated_tags} image tags).")
