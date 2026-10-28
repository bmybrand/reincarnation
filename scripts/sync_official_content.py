from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[1]


def load(route: str) -> tuple[Path, str]:
    path = ROOT / route
    return path, path.read_text(encoding="utf-8")


def save(path: Path, html: str) -> None:
    path.write_text(html, encoding="utf-8")
    print(f"Updated {path.relative_to(ROOT)}")


def replace_many(html: str, pairs: dict[str, str]) -> str:
    for old, new in pairs.items():
        html = html.replace(old, new)
    return html


def set_metadata(html: str, title: str, description: str) -> str:
    html = re.sub(r'<title>.*?</title>', f'<title>{title}</title>', html, count=1, flags=re.DOTALL)
    html = re.sub(r'<meta content="[^"]*" name="description">', f'<meta content="{description}" name="description">', html, count=1)
    html = re.sub(r'<meta content="[^"]*" property="og:title">', f'<meta content="{title}" property="og:title">', html, count=1)
    html = re.sub(r'<meta content="[^"]*" property="og:description">', f'<meta content="{description}" property="og:description">', html, count=1)
    html = re.sub(r'<meta content="[^"]*" name="twitter:title">', f'<meta content="{title}" name="twitter:title">', html, count=1)
    html = re.sub(r'<meta content="[^"]*" name="twitter:description">', f'<meta content="{description}" name="twitter:description">', html, count=1)
    return html


# Homepage: align the lead message and service pillars with the official site.
path, html = load("index.html")
html = replace_many(
    html,
    {
        "Reincarnation | Technology, Design &amp; Operations Studio": "Reincarnation | BPO, Customer Experience &amp; Technology",
        "Technology, design, operations and research support for organisations that need clearer systems, stronger delivery and practical next steps.": "Business process outsourcing, customer experience, consulting, training and technology solutions for organisations that want stronger operations and better service.",
        'Move forward with <span class="home-hero_heading_light white">clearer systems and stronger execution</span>': 'Build better customer operations with <span class="home-hero_heading_light white">the right people, process and technology</span>',
        "Reincarnation brings technology, design, operations and research together to turn complex work into a practical plan and dependable delivery.": "Reincarnation combines business process outsourcing, customer experience consulting, workforce development and practical technology solutions.",
        '<a href="/bespoke-software-development/" class="pill w-inline-block">': '<a href="/ops-it-support/" class="pill w-inline-block">',
        '<a href="/design-experience/" class="pill w-inline-block">': '<a href="/about/" class="pill w-inline-block">',
        "Software &amp;&nbsp;digital products": "Technology &amp;&nbsp;digital solutions",
        "Operations &amp;&nbsp;business systems": "Customer experience &amp;&nbsp;BPO",
        "Design, marketing &amp;&nbsp;content": "Consulting, training &amp;&nbsp;growth",
        "Support shaped around the problem, not a fixed package": "Business process outsourcing, consulting, training and technology",
        "Your systems are slowing the work down": "Customer experience operations",
        "Processes, tools and ownership no longer fit the way the organisation works. We help identify the friction and prioritise what should change first.": "Support for inbound and outbound customer care, telesales, collections, retention, product support and technical support—scoped around the operation you need to run.",
        "You have a clear project to deliver": "BPO consulting and optimisation",
        "Bring the brief, desired outcome and constraints. We will test the assumptions, clarify the scope and flag decisions that need attention before delivery.": "Plan or improve efficient operations through workflow design, analytics, dashboarding, workforce management and clear service ownership.",
        "You need clarity before committing": "Training and technology solutions",
        "When the answer is not obvious, we examine the workflow, users and evidence before recommending software, process change or a simpler alternative.": "Develop stronger teams and operations through practical training, CRM and channel integrations, productivity tools, monitoring and automation.",
        "Let's build something<strong> worth building</strong>": "Let&apos;s improve the way your business<strong> serves and operates</strong>",
    },
)
html = set_metadata(
    html,
    "Reincarnation | BPO, Customer Experience &amp; Technology",
    "Business process outsourcing, customer experience, consulting, training and technology solutions for organisations that want stronger operations and better service.",
)
save(path, html)


# Operations page: connect the service to the customer-care and BPO offer.
path, html = load("ops-it-support/index.html")
html = replace_many(
    html,
    {
        "Operations and IT support": "Business process operations &amp; IT support",
        "Operational and IT support that helps teams improve recurring workflows, workplace systems and day-to-day service ownership.": "Customer experience operations, BPO consulting and enabling technology for customer care, workforce planning and service performance.",
    },
)
html = set_metadata(
    html,
    "Business Process Operations &amp; IT Support | Reincarnation",
    "Customer experience operations, BPO consulting and enabling technology for customer care, workforce planning and service performance.",
)
save(path, html)


# About page: replace inherited software-studio principles with the official business story.
ABOUT_SECTION = """<!-- official-about-start --><section id="why-reincarnation" class="section official-about">
  <div class="s-container official-about__intro">
    <div><p class="official-eyebrow">Why Reincarnation</p><h2>A technology-enabled customer experience and business operations partner.</h2></div>
    <div><p>Reincarnation was founded by leaders with experience in global outsourcing. The business supports organisations through customer experience operations, BPO consulting, workforce development and technology solutions.</p><p>Our approach is practical: understand the operating need, define responsibilities clearly and combine people, process and technology in a way the client can sustain.</p></div>
  </div>
  <div class="s-container official-pillars">
    <article><span>01</span><h3>Customer care operations</h3><p>Inbound and outbound service, telesales, collections, retention, product support and technical support.</p></article>
    <article><span>02</span><h3>BPO consulting</h3><p>Operational setup, workflow improvement, analytics, dashboarding and workforce-management planning.</p></article>
    <article><span>03</span><h3>Training &amp; workforce development</h3><p>Programs designed to strengthen service capability, support internal growth and help close practical talent gaps.</p></article>
    <article><span>04</span><h3>Technology solutions</h3><p>CRM, digital channels, productivity tools, monitoring, automation and other solutions that support modern operations.</p></article>
  </div>
</section>
<section id="how-we-deliver" class="section dark official-delivery">
  <div class="s-container official-delivery__grid">
    <div><p class="official-eyebrow">How we deliver</p><h2>Solutions shaped around the operation.</h2></div>
    <ul><li><strong>Start with the workflow.</strong><span>Understand customers, teams, systems and service expectations before defining the solution.</span></li><li><strong>Connect the channels.</strong><span>Plan customer care and CRM workflows across the communication tools the operation actually uses.</span></li><li><strong>Make performance visible.</strong><span>Use clear reporting, dashboards and ownership so teams can review and improve the work.</span></li></ul>
  </div>
</section><!-- official-about-end -->"""

path, html = load("about/index.html")
html = replace_many(
    html,
    {
        "About Reincarnation | How We Think and Work": "About Reincarnation | BPO, CX &amp; Technology",
        "Meet Reincarnation: a multidisciplinary studio focused on clear thinking, practical delivery and work that can be maintained after launch.": "Reincarnation is a business process outsourcing, customer experience, consulting, training and technology-solutions company.",
        "Reincarnation brings together technology, design, operations and research. We value clear advice, careful delivery and work that remains useful after handover.": "Business process outsourcing, customer experience, consulting, training and technology solutions shaped around real operating needs.",
        "<strong>If you’ve got a product problem, </strong>talk to us": "<strong>Ready to improve customer experience or operations? </strong>Talk to us",
    },
)
html = set_metadata(
    html,
    "About Reincarnation | BPO, CX &amp; Technology",
    "Reincarnation is a business process outsourcing, customer experience, consulting, training and technology-solutions company.",
)
if '<!-- official-about-start -->' in html:
    pattern = r'<!-- official-about-start -->.*?<!-- official-about-end -->'
elif 'id="why-reincarnation"' in html:
    # The sections contain nested layout markup, so use the following stable
    # page boundary instead of trying to pair closing section tags.
    pattern = r'<section id="why-reincarnation".*?(?=<section id="bottom-cta")'
else:
    pattern = r'<section id="how-we-think".*?</section>'
html, count = re.subn(pattern, ABOUT_SECTION, html, count=1, flags=re.DOTALL)
if count != 1:
    raise RuntimeError("Could not replace the About page content section")
save(path, html)


# Contact page: publish the contact details present on the official site.
path, html = load("contact/index.html")
html = replace_many(
    html,
    {
        "We'd love to hear from you": "Tell us what you need from your customer experience, outsourcing, training or technology partner.",
        "<h1>Start a conversation</h1>": "<h1>Contact Reincarnation</h1>",
        "<strong>Get in touch</strong>": "<strong>Pakistan office</strong>",
    },
)
html = set_metadata(
    html,
    "Contact Reincarnation | Pakistan Office",
    "Contact Reincarnation about customer experience operations, BPO consulting, training or technology solutions.",
)
contact_links = """<div class="sec_head-v-links-wrapper"><a title="Email Reincarnation" href="mailto:reincarnation852@gmail.com" class="text-link_default contact-page w-inline-block"><div class="text-link_txt contact-page">reincarnation852@gmail.com</div></a><a title="Visit the official Reincarnation website" href="https://reincarnationpk.com/" target="_blank" rel="noopener" class="text-link_default contact-page w-inline-block"><div class="text-link_txt contact-page">reincarnationpk.com</div></a></div>"""
html, count = re.subn(
    r'<div class="sec_head-v-links-wrapper">.*?</div></div></div><div id="w-node-_5e304c5b',
    contact_links + '</div></div><div id="w-node-_5e304c5b',
    html,
    count=1,
    flags=re.DOTALL,
)
if count != 1:
    raise RuntimeError("Could not replace the Contact page details")
save(path, html)
