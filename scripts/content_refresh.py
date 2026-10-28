from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[1]


PAGE_META = {
    "index.html": (
        "Reincarnation | Technology, Design & Operations Studio",
        "Technology, design, operations and research support for organisations that need clearer systems, stronger delivery and practical next steps.",
    ),
    "about/index.html": (
        "About Reincarnation | How We Think and Work",
        "Meet Reincarnation: a multidisciplinary studio focused on clear thinking, practical delivery and work that can be maintained after launch.",
    ),
    "ai-software-development/index.html": (
        "AI Software Development | Reincarnation",
        "Practical AI software development focused on clear use cases, reliable data, human oversight and measurable outcomes.",
    ),
    "android-app-development/index.html": (
        "Android App Development | Reincarnation",
        "Custom Android application design and development, from product discovery and UX to secure delivery, testing and ongoing improvement.",
    ),
    "app-development-cost/index.html": (
        "App Development Cost Guide | Reincarnation",
        "A practical guide to the factors that shape app-development cost, including scope, integrations, platforms, security and ongoing support.",
    ),
    "bespoke-software-development/index.html": (
        "Bespoke Software Development | Reincarnation",
        "Custom software, internal systems, integrations and digital products shaped around your workflows, users and operating constraints.",
    ),
    "blog/index.html": (
        "Technology and Operations Insights | Reincarnation",
        "Practical thinking on software, AI, design, operations and the decisions that make digital projects useful and maintainable.",
    ),
    "bookkeeping/index.html": (
        "Bookkeeping Workflow Support | Reincarnation",
        "Structured bookkeeping workflow support for consistent records, reconciliations and review, with professional boundaries agreed up front.",
    ),
    "business-systems/index.html": (
        "Business Systems and Internal Platforms | Reincarnation",
        "Business systems that reduce duplicate entry, clarify ownership and connect the information teams need to run day-to-day work.",
    ),
    "contact/index.html": (
        "Contact Reincarnation | Start a Conversation",
        "Tell Reincarnation what you are trying to improve, build or organise, and start with a practical conversation about the next step.",
    ),
    "could-technology-help/index.html": (
        "Could Technology Help Your Business? | Reincarnation",
        "Explore whether software, automation or a better process could reduce friction and create a clearer route forward for your organisation.",
    ),
    "design-experience/index.html": (
        "Design and Experience Services | Reincarnation",
        "Research, UX, service journeys, interface design and prototyping shaped around real users and the work they need to complete.",
    ),
    "digital-marketing/index.html": (
        "Digital Marketing Strategy and Support | Reincarnation",
        "Practical digital marketing support across audience strategy, content, search, campaigns and transparent performance measurement.",
    ),
    "discovery/index.html": (
        "Discovery and Project Scoping | Reincarnation",
        "Turn an unclear business, service or technology challenge into a prioritised plan, a realistic scope and an informed next decision.",
    ),
    "ebooks/index.html": (
        "eBook Planning, Design and Production | Reincarnation",
        "Plan and produce useful eBooks with clear structure, editorial support, considered design and files prepared for the intended channel.",
    ),
    "how-we-work/index.html": (
        "How We Work | Reincarnation",
        "A clear delivery process covering discovery, scoping, design, build, handover, support and evidence-led improvement.",
    ),
    "ios-app-development/index.html": (
        "iOS App Development | Reincarnation",
        "Custom iOS product strategy, UX and development, with secure engineering, launch planning and maintainable long-term delivery.",
    ),
    "legal/index.html": (
        "Legal and Website Information | Reincarnation",
        "General website information and the principles covered in a written Reincarnation service agreement before an engagement begins.",
    ),
    "mobile-app-development/index.html": (
        "Mobile App Development | Reincarnation",
        "Custom mobile product discovery, design and development for useful, secure and maintainable iOS and Android applications.",
    ),
    "mvp-development/index.html": (
        "MVP Development | Reincarnation",
        "Define, design and build the smallest credible product that can test a real assumption with real users and useful evidence.",
    ),
    "ops-it-support/index.html": (
        "Operations and IT Support | Reincarnation",
        "Practical operations and IT support shaped around your systems, workplace tools, recurring issues and ownership needs.",
    ),
    "portfolio/index.html": (
        "Case Studies | Reincarnation",
        "Verified Reincarnation case studies will be published here as project permissions and supporting evidence are confirmed.",
    ),
    "portfolio/patientgo/index.html": (
        "Archived Case Study | Reincarnation",
        "This inherited case-study route is withheld from publication until project ownership, permissions and results are verified.",
    ),
    "pos/index.html": (
        "Point-of-Sale Systems and Integration | Reincarnation",
        "Plan POS workflows, platform selection, device integration, reporting and implementation around how the operation actually works.",
    ),
    "privacy/index.html": (
        "Privacy Notice | Reincarnation",
        "How personal information should be handled on the Reincarnation website, including the details that must be confirmed before production launch.",
    ),
    "ready-to-build/index.html": (
        "Ready to Build Your Product? | Reincarnation",
        "Pressure-test the brief, clarify the first release and turn a defined product idea into a maintainable delivery plan.",
    ),
    "reit-data-research/index.html": (
        "REIT Data Research Support | Reincarnation",
        "Structured REIT and property-market research with an explicit question, documented sources, organised data and visible limitations.",
    ),
    "tech-holding-growth-back/index.html": (
        "When Technology Holds Growth Back | Reincarnation",
        "Identify technology and process bottlenecks, prioritise the highest-value changes and plan improvements around evidence rather than assumptions.",
    ),
    "us-property-taxation/index.html": (
        "US Property-Tax Research Support | Reincarnation",
        "Administrative and research support for US property-tax information, with jurisdiction limits and professional responsibilities made explicit.",
    ),
    "web-app-development/index.html": (
        "Web App Development | Reincarnation",
        "Design and build maintainable portals, dashboards, internal tools and web platforms around real users and operational requirements.",
    ),
    "webinar/solve-your-business-challenges-with-apps/index.html": (
        "Digital Product Planning Session | Reincarnation",
        "A practical introduction to identifying business problems that may benefit from web applications, mobile products or process improvement.",
    ),
}


GLOBAL_REPLACEMENTS = {
    "Tappable": "Reincarnation",
    "Let?s": "Let’s",
    "Bedford, UK. Building software for UK businesses since 2011.": "Practical expertise across technology, design, operations and research.",
    "We build products that perform. Let's build yours.": "Bring us the challenge. We’ll help shape the right next step.",
    "Tell us about your project and we'll reply within one working day": "Tell us what you’re working on and we’ll discuss the right next step",
    "Book a Call with Reincarnation’s CEO": "Book a discovery conversation",
    "The Android app agency for bold ideas and real results": "Android products shaped around users and business needs",
    "Apps that are built to scale. Engineered for growth.": "Android applications designed for reliable, maintainable growth",
    "More than coders. Your full iOS app development partner.": "Product thinking, design and engineering in one iOS delivery process",
    "Native iOS apps built to perform and scale": "Native iOS apps designed to remain useful and maintainable",
    "A mobile app department in your corner": "A joined-up mobile product team",
    "Your app department, not just developers": "A joined-up web product team",
}


EXACT_REPLACEMENTS = {
    "Nothing costs more than <span class=\"home-hero_heading_light white\">the wrong software</span>": "Move forward with <span class=\"home-hero_heading_light white\">clearer systems and stronger execution</span>",
    "Get what's worth building right first, and everything after it becomes smarter, faster and costs less. We've started there since 2011.": "Reincarnation brings technology, design, operations and research together to turn complex work into a practical plan and dependable delivery.",
    "Bespoke mobile &amp;&nbsp;web apps": "Software &amp;&nbsp;digital products",
    "Platforms &amp;&nbsp;business systems": "Operations &amp;&nbsp;business systems",
    "AI software development": "Design, marketing &amp;&nbsp;content",
    "href=\"/ai-software-development/\" class=\"pill w-inline-block\"": "href=\"/design-experience/\" class=\"pill w-inline-block\"",
    "Most businesses come to us for one of three reasons": "Support shaped around the problem, not a fixed package",
    "Your technology is holding your growth back": "Your systems are slowing the work down",
    "Your processes are creaking. The business has scaled but the technology hasn't kept up. We work out what needs to change.": "Processes, tools and ownership no longer fit the way the organisation works. We help identify the friction and prioritise what should change first.",
    "You know what you want to build": "You have a clear project to deliver",
    "An app, a platform, an IoT product. We bring technical depth and product experience, and we'll flag anything in the brief that needs adjusting.": "Bring the brief, desired outcome and constraints. We will test the assumptions, clarify the scope and flag decisions that need attention before delivery.",
    "You're not sure where technology fits yet": "You need clarity before committing",
    "Something in the business isn't working as well as it should, and you suspect technology is part of the answer. We help you work out what that looks like before anything gets built.": "When the answer is not obvious, we examine the workflow, users and evidence before recommending software, process change or a simpler alternative.",
    "Let's build something worth building": "Let’s make the next step clear",
    "Reincarnation has been building software products since 2011. We have a reputation worth protecting. Most of our clients don’t leave.": "Reincarnation brings together technology, design, operations and research. We value clear advice, careful delivery and work that remains useful after handover.",
    "Six things we believe about building software that's worth building. They've shaped how we work, what we say yes to, and what we don't.": "Six principles guide how we approach complex work, what we recommend and what we decline.",
    "Tech holding you back? Ideas you want to bring to life? Let us figure it out for you": "Turn uncertainty into a practical plan",
    "Is your tech helping, or holding you back?": "Start with the problem, not the technology",
    "Two-week discovery process run by our senior team": "Focused discovery led by a multidisciplinary team",
    "Every project starts with a discovery , at no upfront cost, and that is where the decision gets made.": "Every project starts by defining the job, the available data, the risks and the result that would make the work worthwhile.",
    "Discovery, at no upfront cost.": "Discovery and scope.",
    "What our clients get from us": "What a useful first conversation gives you",
    "We've helped businesses...": "The right outcome may be simpler than expected",
    "... improve operations with a simple piece of automation. We've helped others realise they didn't need a new app at all, they needed a better process.": "Sometimes the answer is targeted automation. Sometimes it is a clearer process, a better-configured tool or a focused piece of software.",
    "And we've helped others build products that transformed their business. We'll tell you honestly which category you're in.": "The recommendation should match the evidence, budget and operating reality—not a predetermined service.",
    "Over 15 years, we’ve touched almost all industries.": "The same operational patterns appear across many industries.",
    "About half our MVP work is startups. The other half is established companies testing a new product line without betting the company on it.": "MVP discipline is useful for both new ventures and established organisations testing a new service or product line.",
    "We’re trusted by growing startups, scale-ups, and global enterprises. They rely on us because we ask better questions, build smarter apps, and always stick around when it matters most, delivering a quality iOS app development experience from start to finish.": "The delivery process is designed for teams that value clear decisions, maintainable engineering and an honest view of product risk.",
    "We collaborate with scaling startups, lean innovation teams, and enterprise clients who demand more than just a functioning app. They come to us for premium, strategic, and fully bespoke Android app development services that make a real impact, across devices, markets, and user types.": "We work best with teams that want to understand the product decisions as well as the implementation, from early scope through release and improvement.",
    "Every product is custom-crafted. Every experience is premium.": "Each product is shaped around its users, constraints and intended outcome.",
    "This isn’t just app development. It’s high-performance software, designed and delivered by an Android app agency that understands the stakes and delivers to match.": "That means making explicit choices about performance, accessibility, security, device support and long-term maintenance.",
    "Think CTO, product lead, UX designer, developers, all working as one, all focused on your business success.": "Product, design and engineering decisions are considered together so that the scope remains coherent.",
    "Clients include M&amp;S, ITV, Syneos Health and Imperial College London.": "Relevant experience and references should be discussed for the scope and supplied only where permission has been confirmed.",
    "These are the ranges we quote, not an industry average we found somewhere.": "These figures are broad planning examples, not a quote or a promise of market pricing.",
    "We have inherited several of them.": "The apparent saving can disappear when a product must be rebuilt.",
}


SECTION_IDS_TO_REMOVE = {
    "index.html": ["banners", "clients", "client"],
    "about/index.html": ["what-we-are", "executive-team"],
    "blog/index.html": ["blog-posts-list"],
    "portfolio/index.html": ["product-montage", "portfolio"],
    "portfolio/patientgo/index.html": ["intro", "bottom-photo", "app-image"],
}


INHERITED_INTRO_PAGES = {
    "ai-software-development/index.html",
    "android-app-development/index.html",
    "bespoke-software-development/index.html",
    "business-systems/index.html",
    "ios-app-development/index.html",
    "mobile-app-development/index.html",
    "mvp-development/index.html",
    "web-app-development/index.html",
}


FIRST_H1 = {
    "about/index.html": "About Reincarnation",
    "app-development-cost/index.html": "What app development costs—and what changes the number",
    "blog/index.html": "Technology and operations insights",
    "contact/index.html": "Start a conversation",
    "could-technology-help/index.html": "Start with the business problem, not the app",
    "discovery/index.html": "Turn uncertainty into a practical plan",
    "ops-it-support/index.html": "Operations and IT support",
    "portfolio/index.html": "Verified case studies are being prepared",
    "ready-to-build/index.html": "Bring a clear idea. Leave with a stronger plan.",
    "reit-data-research/index.html": "REIT data research support",
    "tech-holding-growth-back/index.html": "When systems start slowing growth",
    "us-property-taxation/index.html": "US property-tax research support",
    "webinar/solve-your-business-challenges-with-apps/index.html": "Solve the right problem before choosing the technology",
}


def replace_meta(html: str, title: str, description: str) -> str:
    html = re.sub(r"<title>.*?</title>", f"<title>{title}</title>", html, count=1, flags=re.I | re.S)
    html = re.sub(r'(<meta\s+content=")[^"]*("\s+name="description")', rf"\g<1>{description}\g<2>", html, count=1, flags=re.I)
    html = re.sub(r'(<meta\s+content=")[^"]*("\s+property="og:title")', rf"\g<1>{title}\g<2>", html, count=1, flags=re.I)
    html = re.sub(r'(<meta\s+content=")[^"]*("\s+property="og:description")', rf"\g<1>{description}\g<2>", html, count=1, flags=re.I)
    html = re.sub(r'(<meta\s+content=")[^"]*("\s+name="twitter:title")', rf"\g<1>{title}\g<2>", html, count=1, flags=re.I)
    html = re.sub(r'(<meta\s+content=")[^"]*("\s+name="twitter:description")', rf"\g<1>{description}\g<2>", html, count=1, flags=re.I)
    return html


def remove_section(html: str, section_id: str) -> str:
    pattern = rf'<section\b(?=[^>]*\bid="{re.escape(section_id)}")[^>]*>.*?</section>'
    return re.sub(pattern, "", html, count=1, flags=re.I | re.S)


def add_noindex(html: str) -> str:
    if 'name="robots"' not in html:
        html = html.replace("</head>", '<meta name="robots" content="noindex, nofollow"></head>', 1)
    return html


def replace_legal_page(html: str) -> str:
    section = '''<section id="product-montage" class="section privacy-legal"><div class="s-container"><div class="legal_rich-text w-richtext"><h1>Legal and website information</h1><p>This website describes the services offered under the Reincarnation brand. Its content is general information, not legal, tax, investment or other regulated advice, and it does not create a contract.</p><h3>Service agreements</h3><p>Before paid work begins, the parties should sign a written agreement covering the legal entities involved, scope, deliverables, fees, payment terms, confidentiality, intellectual-property ownership, data responsibilities, liability, cancellation and dispute handling.</p><h3>Accuracy and third-party material</h3><p>We aim to keep service information clear and current. Any third-party names, marks, links or examples must have confirmed permission and should not be treated as an endorsement.</p><h3>Details required before launch</h3><p>The operating entity, registered address, company number and formal contact details must be inserted and legally reviewed before this website is published as a production service.</p></div></div></section>'''
    return re.sub(r'<section\b(?=[^>]*\bid="product-montage")[^>]*>.*?</section>', section, html, count=1, flags=re.I | re.S)


def replace_privacy_page(html: str) -> str:
    section = '''<section id="product-montage" class="section privacy-legal"><div class="s-container"><div class="legal_rich-text w-richtext"><h1>Privacy notice</h1><p>Reincarnation should collect only the personal information needed to respond to enquiries and deliver an agreed service. Information should not be sold or used for unrelated purposes.</p><h3>Information submitted through this website</h3><p>An enquiry may include your name, contact details, organisation and the information you choose to provide. Do not submit confidential, financial, health or special-category information through the general enquiry form.</p><h3>How information should be used</h3><p>Enquiry information should be used to respond, assess whether the requested service is a suitable fit, maintain necessary business records and meet legal obligations. Access should be limited to people who need it for those purposes.</p><h3>Cookies and external services</h3><p>Analytics, advertising, scheduling, video and anti-spam services may set cookies or receive technical data. Non-essential services should remain disabled until valid consent is recorded.</p><h3>Your rights</h3><p>Depending on the applicable law, you may have rights to access, correct, delete, restrict or object to the use of your personal information and to complain to the relevant supervisory authority.</p><h3>Details required before launch</h3><p>The legal data controller, privacy contact, lawful bases, processors, international transfers, retention periods and complaint route must be confirmed and legally reviewed before the site collects production enquiries.</p></div></div></section>'''
    return re.sub(r'<section\b(?=[^>]*\bid="product-montage")[^>]*>.*?</section>', section, html, count=1, flags=re.I | re.S)


def clean_footer_identity(html: str) -> str:
    html = re.sub(
        r'<div class="footer_copyright-text"><span class="fw_semibold">Reincarnation</span> is a trading name for <span class="fw_semibold">SaBe Interactive Ltd\.</span></div>',
        '<div class="footer_copyright-text"><span class="fw_semibold">Reincarnation</span></div>',
        html,
    )
    html = re.sub(
        r'<div class="footer_copyright-text">Company number: <span class="fw_semibold">07516640</span></div>',
        '<div class="footer_copyright-text">Technology, design, operations and research.</div>',
        html,
    )
    html = re.sub(r'href="tel:\+44\(0\)1234414774"', 'href="/contact/"', html, flags=re.I)
    html = re.sub(r'href="mailto:hello@tappable\.co\.uk[^\"]*"', 'href="/contact/"', html, flags=re.I)
    html = html.replace("+44 (0) 1234 414774", "Start a conversation")
    html = html.replace("hello@tappable.co.uk", "Use the contact form")
    html = html.replace("https://goo.gl/maps/ehSuUVQhjcP7o4a77", "/contact/")
    html = html.replace("Bedford i-Lab, Priory Business Park, Stannard Way, Bedford, MK44 3RZ", "Contact and availability")
    html = html.replace('href="/contact/" target="_blank" class="footer_business-address"', 'href="/contact/" class="footer_business-address"')
    html = re.sub(
        r'<div class="footer_social-links">.*?</div></div><div class="footer_copyright-links">',
        '</div><div class="footer_copyright-links">',
        html,
        flags=re.I | re.S,
    )
    return html


def refresh() -> None:
    files = sorted(ROOT.rglob("index.html"))
    for path in files:
        rel = path.relative_to(ROOT).as_posix()
        html = path.read_text(encoding="utf-8")

        # Remove inherited structured data rather than publishing another company's identity or claims.
        html = re.sub(r'<script\s+type="application/ld\+json">.*?</script>', "", html, flags=re.I | re.S)

        for old, new in GLOBAL_REPLACEMENTS.items():
            html = html.replace(old, new)
        for old, new in EXACT_REPLACEMENTS.items():
            html = html.replace(old, new)

        if rel in PAGE_META:
            html = replace_meta(html, *PAGE_META[rel])

        if rel in FIRST_H1:
            html = re.sub(r'(<h1\b[^>]*>).*?(</h1>)', rf'\g<1>{FIRST_H1[rel]}\g<2>', html, count=1, flags=re.I | re.S)

        for section_id in SECTION_IDS_TO_REMOVE.get(rel, []):
            html = remove_section(html, section_id)

        if rel in INHERITED_INTRO_PAGES:
            html = remove_section(html, "intro")

        # Portfolio cards and inherited project claims do not transfer to the new brand.
        html = remove_section(html, "portfolio-cards")

        if rel == "portfolio/patientgo/index.html":
            html = re.sub(r'<section\b(?![^>]*\bid="(?:hero|bottom-cta)")[^>]*>.*?</section>', "", html, flags=re.I | re.S)
            html = html.replace("Patient management system &amp; back-office tools for clinical trials", "Archived case study awaiting verification")
            html = add_noindex(html)
        elif rel == "portfolio/index.html":
            html = html.replace("Mobile &amp; web apps that drive businesses forward", "Verified case studies are being prepared")
            html = add_noindex(html)
        elif rel == "blog/index.html":
            html = html.replace("App and software development insights", "Technology and operations insights")
            html = add_noindex(html)
        elif rel == "legal/index.html":
            html = replace_legal_page(html)
            html = add_noindex(html)
        elif rel == "privacy/index.html":
            html = replace_privacy_page(html)
            html = add_noindex(html)

        # Remove inherited proof claims that appear in long-form software content.
        html = re.sub(r'We have been designing and building software for UK companies since 2011:[^<]*', 'We design and build software around the workflows, users and constraints that matter to the organisation.', html)
        html = re.sub(r'We have built software for established UK businesses since 2011,[^<]*', 'AI is one tool within a wider software and process decision.', html)
        html = re.sub(r'PatientGo, the clinical trials platform.*?per unit\.', 'Project examples and references are provided only where ownership, results and publication permission have been verified.', html, flags=re.S)
        html = re.sub(r'Illingworth Research Group pays.*?Read the PatientGo case study\.', 'A suitable AI workflow starts with a repeatable decision, usable source data, a clear confidence threshold and human review for uncertain cases.', html, flags=re.S)
        html = re.sub(r'One client came to us with an invoicing cycle.*?six hours\.', 'Bespoke software is most useful when repeated manual work, duplicate entry or disconnected tools create a measurable operational cost.', html, flags=re.S)
        html = re.sub(r'A brick and concrete manufacturer was waiting.*?immediate impact\.', 'A useful first improvement is narrow enough to measure: remove one repeated handoff, capture information once, or automate a well-understood rule. Prove the change in real work before expanding it.', html, flags=re.S)
        html = re.sub(r'Detector Testers came to us.*?would need to grow\.', 'A strong brief covers more than screens and features. It should address users, onboarding, permissions, data ownership, integrations, support and the operating model around the product.', html, flags=re.S)
        html = html.replace("They knew what they wanted to build. We knew how to build it in a way that would work.", "The goal is to keep the original intent while resolving the decisions that make the product viable in practice.")
        html = html.replace("Every project we take on starts with a two-week discovery run by our senior team, at no upfront cost.", "Projects begin with an agreed discovery and scoping stage proportionate to the uncertainty involved.")
        html = html.replace("It is how we start every build, it takes two weeks, and there is no upfront cost.", "The depth, timing and fee are agreed before work begins.")
        html = html.replace("Discovery is how we start every build: two weeks with our senior team, no upfront cost,", "Discovery is scoped around the decisions the project needs to make,")
        html = html.replace("The first conversation is free.", "An initial conversation helps establish fit and the most useful next step.")
        html = html.replace("We have been building first versions since 2011, and the best advice we ever gave a founder was to spend £100,000 less than they had planned.", "The discipline is to spend only what is needed to test the most important assumption, then let evidence shape the next investment.")
        html = html.replace("How we start every build: two weeks with our senior team, working out what's worth building. No upfront cost.", "A focused first stage to understand the problem, test assumptions and define the right next decision.")
        html = html.replace("We cut a client’s invoicing cycle from 6 weeks to 6 hours using an app", "Reduce repeated administration by capturing information once and moving it to the right place")
        html = html.replace("We built a servicing tool (app) that connects to commercial dishwashers for troubleshooting, configuration and maintenance. Decreasing service time by ~60% per unit", "Connect field tools, devices and records so teams can diagnose issues and complete work with less friction")
        html = html.replace("Most of our clients are not tech companies.", "You do not need to be a technology company.")
        html = html.replace("One of our clients has a day-one job sheet system with a scheduling phase behind it, priced and sequenced from the start, so each phase is a decision they can take on its own evidence.", "A good phased plan gives each release a clear purpose, cost and decision point, so the next phase is based on evidence rather than momentum.")
        html = html.replace("One client was handling five hundred expense claims a week and now handles five thousand with the same team.", "As volume grows, a well-designed system should reduce repeated checking and route exceptions to the people who need to review them.")
        html = html.replace("One of our clients ran a six-week invoicing cycle. The system we built for them runs it in six hours, which is six weeks of cash arriving sooner, every month.", "When delivery evidence and invoicing data share one workflow, teams can remove avoidable handoffs and raise accurate invoices sooner.")
        html = html.replace("Most of our clients run trades, estates, clinics and factories.", "This pattern appears in field services, property, healthcare, manufacturing and other operational teams.")
        html = html.replace("Bespoke software projects run from £15,000 to £100,000 excluding VAT, and we do not take on projects under £10,000.", "Bespoke software cost depends on scope, integrations, risk, platforms and the level of operational change involved.")
        html = html.replace("We do not take on projects under £10,000.", "A written estimate should follow discovery and scope.")
        html = html.replace("The evidence behind that position is in <a href=\"/blog/ai-software-development-cost\">our post</a> on what AI has done to software development cost.", "The important control is review: generated code must meet the same security, testing and maintainability standards as any other implementation.")
        html = html.replace("The longer argument is in <a href=\"/blog/should-you-add-ai-to-your-app\">our post</a> \"Should you add AI to your app? Most shouldn't bother\"", "The decision should be documented before a model becomes part of the product or process.")
        html = re.sub(r'Voice-Care listens.*?Read the Voice-Care case study\.', 'AI inside a product should have a defined job, a clear fallback when confidence is low and an interface that helps people understand what happened.', html, flags=re.S)
        html = re.sub(r'Yes, and it usually has to\. PatientGo.*?through an API,', 'Yes. Integration requirements should be assessed early, including ownership, authentication, rate limits, failure handling and audit needs,', html, flags=re.S)
        html = re.sub(r'Based in Bedford, just outside London, trusted across the UK and globally, we’re the iOS app agency businesses call when they want things done properly, the first time\.', 'The right iOS partner should make product, design, engineering, release and maintenance decisions visible throughout delivery.', html)
        html = html.replace('<a href="/blog/real-price-of-cheap-offshore-app-development">Cheap</a>', 'A low-cost approach')
        html = html.replace('<a href="/blog/top-5-custom-mobile-app-development-services-for-2025"><strong>custom mobile app development</strong></a>', '<strong>custom mobile app development</strong>')
        html = clean_footer_identity(html)

        # The enquiry form should target a first-party endpoint rather than silently use inherited Webflow handling.
        if rel == "contact/index.html":
            html = re.sub(r'(<form\s+id="contact-form"[^>]*?)method="get"', r'\1action="/api/contact" method="post"', html, count=1, flags=re.I)

        if rel == "portfolio/patientgo/index.html":
            html = html.replace(">PatientGo<", ">Archived project<")
            html = re.sub(r'(<meta\s+content=")[^"]*patientgo[^"]*("\s+(?:property|name)="(?:og:image|twitter:image)")', r'\1/assets/brand/logo.png\2', html, flags=re.I)

        path.write_text(html, encoding="utf-8", newline="")

    print(f"Refreshed {len(files)} pages")


if __name__ == "__main__":
    refresh()
