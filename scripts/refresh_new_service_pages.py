from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[1]


def card(number: str, title: str, text: str) -> str:
    return f"""<article class="svc-card"><span class="svc-card__number">{number}</span><h3>{title}</h3><p>{text}</p></article>"""


def step(number: str, title: str, text: str) -> str:
    return f"""<article class="svc-step"><span>{number}</span><div><h3>{title}</h3><p>{text}</p></div></article>"""


PAGES = {
    "design-experience": {
        "layout": "design",
        "html": f"""
<section id="design-brief" class="section svc-section svc-intro svc-intro--split">
  <div class="s-container svc-shell svc-split">
    <div><p class="svc-kicker">Design starts before the screen</p><h2>Good design begins with understanding people.</h2></div>
    <div class="svc-lede"><p>A useful digital experience starts with understanding the people using it and the job they need to get done. We explore the problem, clarify the important journeys and shape an interface your team can confidently build and improve.</p><ul class="svc-checks"><li>Real users and real tasks</li><li>Business goals and constraints</li><li>Decisions your delivery team can use</li></ul></div>
  </div>
</section>
<section id="design-studio" class="section svc-section svc-capabilities svc-capabilities--bento">
  <div class="s-container svc-shell"><header class="svc-heading"><p class="svc-kicker">Inside the studio</p><h2>Design the experience around the real need</h2></header><div class="svc-card-grid svc-card-grid--bento">
    {card('01', 'Research &amp; discovery', 'Learn about users, workflows and pain points before committing to a solution or detailed design.')}
    {card('02', 'UX &amp; service journeys', 'Map key tasks and simplify the steps people take across a digital service.')}
    {card('03', 'Interface design &amp; prototyping', 'Explore visual directions and test a clickable prototype before development.')}
  </div></div>
</section>
<section id="design-path" class="section dark svc-section svc-process svc-process--ribbon">
  <div class="s-container svc-shell"><header class="svc-heading svc-heading--wide"><p class="svc-kicker">A visible design path</p><h2>From open questions to a design you can act on</h2><p>We share decisions early and test assumptions as we go. The right depth depends on the product, its users and what you already know.</p></header><div class="svc-steps svc-steps--horizontal">
    {step('01', 'Understand', 'Align on users, business goals and the moments that matter.')}
    {step('02', 'Explore', 'Develop journeys and interface concepts, then use feedback to refine them.')}
    {step('03', 'Handoff', 'Document decisions and prepare the work for delivery and iteration.')}
  </div></div>
</section>""",
    },
    "digital-marketing": {
        "layout": "marketing",
        "html": f"""
<section id="marketing-signal" class="section svc-section svc-intro svc-intro--signal">
  <div class="s-container svc-shell"><div class="svc-signal-copy"><p class="svc-kicker">Useful before loud</p><h2>Start with the audience and the outcome you want.</h2><p>Good marketing connects the right audience with something genuinely useful. We review the current position, clarify the message and plan activity your team can sustain.</p></div><div class="svc-signal-strip"><span>Audience</span><span>Offer</span><span>Channel</span><span>Evidence</span></div></div>
</section>
<section id="marketing-system" class="section svc-section svc-capabilities svc-capabilities--stacked">
  <div class="s-container svc-shell svc-two-column"><header class="svc-heading svc-heading--sticky"><p class="svc-kicker">A connected system</p><h2>A clearer plan for reaching and serving customers</h2><p>The channel mix follows the goal, not the other way around.</p></header><div class="svc-card-stack">
    {card('01', 'Strategy &amp; audience', 'Clarify who you want to reach, the offer you are making and how marketing supports wider business goals.')}
    {card('02', 'Content &amp; search', 'Plan useful content and improve how people discover and understand your services online.')}
    {card('03', 'Campaigns &amp; measurement', 'Run focused activity with practical tracking and a regular review of what is working.')}
  </div></div>
</section>
<section id="marketing-loop" class="section dark svc-section svc-process svc-process--loop">
  <div class="s-container svc-shell"><header class="svc-heading"><p class="svc-kicker">The improvement loop</p><h2>Start with the evidence, then improve steadily</h2></header><div class="svc-loop">
    {step('01', 'Review', 'Understand the current position, audience and available performance data.')}
    {step('02', 'Prioritise', 'Choose the channels and messages that best fit your goals and resources.')}
    {step('03', 'Measure', 'Review outcomes and use what you learn to guide the next activity.')}
  </div></div>
</section>""",
    },
    "ops-it-support": {
        "layout": "ops",
        "html": f"""
<section id="ops-overview" class="section svc-section svc-intro svc-intro--console">
  <div class="s-container svc-shell svc-console"><div><p class="svc-kicker">Customer experience and operations</p><h2>Keep customer and business operations running smoothly.</h2><p>Reincarnation supports customer-care workflows, business-process operations and the technology behind them. The service is scoped around the channels, teams, systems and outcomes your organisation needs.</p></div><aside class="svc-status"><div><span>Operating focus</span><strong>People, process and technology working together</strong></div><ul><li>Clear service ownership</li><li>Connected customer channels</li><li>Visible operational performance</li></ul></aside></div>
</section>
<section id="ops-control-room" class="section svc-section svc-capabilities svc-capabilities--rows">
  <div class="s-container svc-shell"><header class="svc-heading"><p class="svc-kicker">Business process operations</p><h2>Customer care, consulting and enabling technology</h2></header><div class="svc-row-list">
    {card('A', 'Customer care operations', 'Scope inbound and outbound service, telesales, collections, retention, product support and technical support around the required customer journey.')}
    {card('B', 'CRM &amp; channel integration', 'Plan how customer records and workflows connect across CRM, chat, messaging, IVR, chatbot and other service channels.')}
    {card('C', 'Performance &amp; workforce planning', 'Clarify service ownership, workforce needs, analytics, dashboards and the operating rhythm used to review performance.')}
  </div></div>
</section>
<section id="ops-rhythm" class="section dark svc-section svc-process svc-process--handoff">
  <div class="s-container svc-shell svc-two-column"><header class="svc-heading"><p class="svc-kicker">A clear operating model</p><h2>Define the operation before choosing the solution</h2><p>Responsibilities, channels, service expectations and reporting are agreed before implementation or ongoing delivery begins.</p></header><div class="svc-steps svc-steps--vertical">
    {step('01', 'Understand', 'Map the customer journey, service volumes, channels, systems and current operating constraints.')}
    {step('02', 'Design', 'Define workflows, roles, technology needs, measures and the appropriate delivery model.')}
    {step('03', 'Operate &amp; improve', 'Launch the agreed scope, review performance and prioritise practical improvements.')}
  </div></div>
</section>""",
    },
    "reit-data-research": {
        "layout": "reit",
        "html": f"""
<section id="research-question" class="section svc-section svc-intro svc-intro--query">
  <div class="s-container svc-shell"><p class="svc-kicker">Research starts with a precise question</p><div class="svc-query"><div><h2>Begin with a clear property research question.</h2><p>Property-market research is useful when definitions and sources are explicit. We structure the brief, organise relevant information and present findings with their context and limitations visible.</p></div><dl><div><dt>Geography</dt><dd>What market?</dd></div><div><dt>Period</dt><dd>What timeframe?</dd></div><div><dt>Measure</dt><dd>Which data points?</dd></div><div><dt>Use</dt><dd>What decision?</dd></div></dl></div></div>
</section>
<section id="research-workbench" class="section svc-section svc-capabilities svc-capabilities--table">
  <div class="s-container svc-shell"><header class="svc-heading"><p class="svc-kicker">Research workbench</p><h2>Research shaped around your property question</h2></header><div class="svc-data-table"><div class="svc-data-table__head"><span>Stage</span><span>Work</span><span>Purpose</span></div>
    <div><span>01</span><strong>Research scoping</strong><p>Define the question, geography, time period and data points needed for useful analysis.</p></div>
    <div><span>02</span><strong>Source review &amp; organisation</strong><p>Identify relevant sources, record provenance and organise information for review.</p></div>
    <div><span>03</span><strong>Analysis &amp; reporting</strong><p>Summarise patterns, comparisons and limitations in an agreed format.</p></div>
  </div></div>
</section>
<section id="research-trail" class="section dark svc-section svc-process svc-process--trail">
  <div class="s-container svc-shell"><header class="svc-heading svc-heading--wide"><p class="svc-kicker">Traceable by design</p><h2>Keep the research question and source trail visible</h2><p>Source choices and assumptions remain explicit so findings can be checked, updated and interpreted in context.</p></header><div class="svc-steps svc-steps--trail">
    {step('01', 'Frame', 'Agree the research question, definitions, geography and period.')}
    {step('02', 'Gather', 'Collect and organise relevant data, noting sources and any gaps.')}
    {step('03', 'Report', 'Present findings and limitations clearly for discussion and review.')}
  </div></div>
</section>""",
    },
    "us-property-taxation": {
        "layout": "tax",
        "html": f"""
<section id="tax-boundary" class="section svc-section svc-intro svc-intro--boundary">
  <div class="s-container svc-shell svc-two-column"><div><p class="svc-kicker">Structured administrative support</p><h2>Organise information while keeping professional advice in the right hands.</h2><p>US property-tax processes vary by jurisdiction. We organise records and research information for agreed workflows while keeping the role of qualified US tax and legal professionals clear.</p></div><aside class="svc-boundary-note"><span>Important boundary</span><strong>Research and administration, not tax preparation or legal advice.</strong><p>Your qualified advisers verify and use the work.</p></aside></div>
</section>
<section id="tax-file" class="section svc-section svc-capabilities svc-capabilities--documents">
  <div class="s-container svc-shell"><header class="svc-heading"><p class="svc-kicker">A reviewable property file</p><h2>Structured support for property-tax information</h2></header><div class="svc-document-grid">
    {card('FILE 01', 'Record &amp; data organisation', 'Bring property details and supporting documents together in a consistent, reviewable format.')}
    {card('FILE 02', 'Jurisdiction research', 'Gather and organise publicly available information relevant to an agreed property or workflow.')}
    {card('FILE 03', 'Process &amp; reporting support', 'Track information, adviser-supplied deadlines and outstanding administrative tasks.')}
  </div></div>
</section>
<section id="tax-handoff" class="section dark svc-section svc-process svc-process--gates">
  <div class="s-container svc-shell"><header class="svc-heading svc-heading--wide"><p class="svc-kicker">Controlled handoff</p><h2>Careful scoping, with professional boundaries made clear</h2></header><div class="svc-gates">
    {step('01', 'Scope', 'Confirm locations, properties, information needs and who provides professional advice.')}
    {step('02', 'Organise', 'Gather and structure agreed records and publicly available information.')}
    {step('03', 'Review', 'Present the work for your team and qualified advisers to verify and use.')}
  </div></div>
</section>""",
    },
    "pos": {
        "layout": "pos",
        "html": f"""
<section id="pos-floor" class="section svc-section svc-intro svc-intro--checkout">
  <div class="s-container svc-shell svc-two-column"><div><p class="svc-kicker">The checkout is one part of the system</p><h2>Build around how your team serves customers.</h2><p>A POS setup connects stock, staff workflows, devices, reporting and existing systems. We map those needs first, then scope an appropriate setup or integration.</p></div><div class="svc-receipt"><div><span>SALE FLOW</span><strong>Customer → Checkout</strong></div><div><span>OPERATIONS</span><strong>Stock → Reporting</strong></div><div><span>TEAM</span><strong>Roles → Handover</strong></div></div></div>
</section>
<section id="pos-system-map" class="section svc-section svc-capabilities svc-capabilities--nodes">
  <div class="s-container svc-shell"><header class="svc-heading svc-heading--wide"><p class="svc-kicker">System map</p><h2>Plan the complete point-of-sale workflow</h2></header><div class="svc-node-map">
    {card('01', 'Checkout &amp; staff workflows', 'Understand how sales, returns and daily tasks need to work for staff and customers.')}
    {card('02', 'Systems &amp; device integration', 'Review the POS platform, devices and connected tools that may need to share information.')}
    {card('03', 'Reporting &amp; operations', 'Clarify what information the team needs and how it should support routine decisions.')}
  </div></div>
</section>
<section id="pos-route" class="section dark svc-section svc-process svc-process--route">
  <div class="s-container svc-shell"><header class="svc-heading"><p class="svc-kicker">Route to rollout</p><h2>Choose the right route before changing checkout</h2><p>Platform selection, integrations and delivery follow the operating requirements—not the other way around.</p></header><div class="svc-route">
    {step('01', 'Map', 'Understand locations, users, checkout tasks and current systems.')}
    {step('02', 'Assess', 'Compare suitable options and identify integration or data questions.')}
    {step('03', 'Plan', 'Agree a practical implementation, testing and handover scope.')}
  </div></div>
</section>""",
    },
    "ebooks": {
        "layout": "ebooks",
        "html": f"""
<section id="ebook-editorial" class="section svc-section svc-intro svc-intro--editorial">
  <div class="s-container svc-shell svc-editorial"><div class="svc-book-cover"><span>READER</span><strong>Purpose<br>before<br>pages.</strong><small>Editorial planning</small></div><div><p class="svc-kicker">A publication, not just a file</p><h2>Start with the reader, the message and the format.</h2><p>An eBook brings together a clear purpose, well-structured content and a format that works for its readers. We coordinate planning, writing, editing, design and production to the scope you need.</p></div></div>
</section>
<section id="ebook-chapters" class="section svc-section svc-capabilities svc-capabilities--chapters">
  <div class="s-container svc-shell"><header class="svc-heading"><p class="svc-kicker">Three production chapters</p><h2>A considered route from idea to eBook</h2></header><div class="svc-chapters">
    {card('CHAPTER 01', 'Structure &amp; editorial planning', 'Define the audience, purpose, outline and content requirements before production.')}
    {card('CHAPTER 02', 'Writing, editing &amp; design', 'Shape supplied or newly developed material into a coherent, readable publication.')}
    {card('CHAPTER 03', 'Digital production', 'Prepare agreed output formats and review how the eBook will be distributed or published.')}
  </div></div>
</section>
<section id="ebook-production" class="section dark svc-section svc-process svc-process--colophon">
  <div class="s-container svc-shell svc-two-column"><header class="svc-heading"><p class="svc-kicker">Production notes</p><h2>Plan the content before polishing the pages</h2><p>We agree who supplies and approves content, what formats are needed and how revisions will be handled.</p></header><div class="svc-colophon">
    {step('01', 'Brief', 'Agree the reader, purpose, content, rights and intended formats.')}
    {step('02', 'Create', 'Develop and review the structure, copy and visual direction.')}
    {step('03', 'Prepare', 'Check final files against the agreed formats and distribution plan.')}
  </div></div>
</section>""",
    },
    "bookkeeping": {
        "layout": "bookkeeping",
        "html": f"""
<section id="books-overview" class="section svc-section svc-intro svc-intro--ledger">
  <div class="s-container svc-shell"><div class="svc-ledger-head"><div><p class="svc-kicker">Records you can follow</p><h2>Reliable records start with repeatable routines.</h2></div><p>We review the current workflow, organise agreed information and identify practical improvements, with responsibilities and professional boundaries confirmed up front.</p></div><div class="svc-ledger-summary"><span>Capture</span><span>Check</span><span>Reconcile</span><span>Review</span></div></div>
</section>
<section id="books-system" class="section svc-section svc-capabilities svc-capabilities--ledger">
  <div class="s-container svc-shell"><header class="svc-heading"><p class="svc-kicker">The bookkeeping system</p><h2>Support for consistent, reviewable bookkeeping</h2></header><div class="svc-ledger-table">
    <div><span>01</span><h3>Record organisation</h3><p>Agree a consistent approach to gathering and categorising the records your process requires.</p></div>
    <div><span>02</span><h3>Reconciliation workflow</h3><p>Review how transactions and supporting information are checked and exceptions followed up.</p></div>
    <div><span>03</span><h3>Routine reporting</h3><p>Define the regular information your team needs and how it is prepared for review.</p></div>
  </div></div>
</section>
<section id="books-cycle" class="section dark svc-section svc-process svc-process--cycle">
  <div class="s-container svc-shell"><header class="svc-heading svc-heading--wide"><p class="svc-kicker">A repeatable cycle</p><h2>Make the routine clear, then keep it consistent</h2><p>Tasks, access, approvals and work reserved for your accountant are documented in the agreed scope.</p></header><div class="svc-cycle">
    {step('01', 'Understand', 'Review your workflow, systems and the records that need attention.')}
    {step('02', 'Agree', 'Define tasks, access, approvals and work reserved for your accountant.')}
    {step('03', 'Support', 'Follow the agreed process and keep records organised for review.')}
  </div></div>
</section>""",
    },
}


old_pattern = re.compile(
    r'<section id="intro".*?</section><section id="service-capabilities".*?</section><section id="service-process".*?</section>',
    re.DOTALL,
)
custom_pattern = re.compile(
    r'<!-- custom-service-start -->.*?<!-- custom-service-end -->',
    re.DOTALL,
)

for route, config in PAGES.items():
    path = ROOT / route / "index.html"
    source = path.read_text(encoding="utf-8")
    body_attr = f'data-service-layout="{config["layout"]}"'
    if re.search(r'data-service-layout="[^"]+"', source):
        source = re.sub(r'data-service-layout="[^"]+"', body_attr, source, count=1)
    else:
        source = source.replace('<body class="', f'<body {body_attr} class="', 1)

    block = f'<!-- custom-service-start -->{config["html"]}<!-- custom-service-end -->'
    if custom_pattern.search(source):
        updated = custom_pattern.sub(block, source, count=1)
    else:
        updated, count = old_pattern.subn(block, source, count=1)
        if count != 1:
            raise RuntimeError(f"Could not find replaceable service sections in {path}")

    path.write_text(updated, encoding="utf-8")
    print(f"Updated {route}")
