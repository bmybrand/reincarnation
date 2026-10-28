from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[1]

FOOTER = """<footer id="footer" class="footer brand-footer">
  <div class="brand-footer__inner">
    <div class="brand-footer__lead">
      <a class="brand-footer__brand" href="/" aria-label="Reincarnation home">
        <img src="/assets/brand/logo.png" alt="" class="brand-footer__logo">
      </a>
      <p class="brand-footer__statement">Business process outsourcing, customer experience, consulting, training and technology solutions.</p>
      <div class="brand-footer__contact">
        <a href="mailto:reincarnation852@gmail.com">reincarnation852@gmail.com</a>
        <a href="https://reincarnationpk.com/" target="_blank" rel="noopener">reincarnationpk.com</a>
      </div>
      <a rel="" aria-label="Start a conversation" title="Contact Reincarnation" role="" target="" data-wf--btn-primary--variant="filled" href="/contact/" class="btn-primary w-inline-block"><div class="btn-primary_text">Start a conversation</div></a>
    </div>

    <nav class="brand-footer__nav" aria-label="Footer navigation">
      <div class="brand-footer__column">
        <h2>Technology</h2>
        <a href="/bespoke-software-development/">Bespoke software</a>
        <a href="/ai-software-development/">AI development</a>
        <a href="/mobile-app-development/">Mobile apps</a>
        <a href="/web-app-development/">Web applications</a>
        <a href="/business-systems/">Business systems</a>
        <a href="/mvp-development/">MVP development</a>
      </div>
      <div class="brand-footer__column">
        <h2>Business services</h2>
        <a href="/ops-it-support/">Customer experience &amp; BPO</a>
        <a href="/business-systems/">BPO consulting</a>
        <a href="/about/">Training &amp; workforce development</a>
        <a href="/digital-marketing/">Digital marketing</a>
        <a href="/bookkeeping/">Bookkeeping</a>
        <a href="/reit-data-research/">Data research</a>
      </div>
      <div class="brand-footer__column">
        <h2>Company</h2>
        <a href="/how-we-work/">How we work</a>
        <a href="/portfolio/">Portfolio</a>
        <a href="/blog/">Insights</a>
        <a href="/about/">About us</a>
        <a href="/contact/">Contact us</a>
      </div>
    </nav>
  </div>

  <div class="brand-footer__bottom">
    <p>&copy; 2026 Reincarnation. All rights reserved.</p>
    <div class="brand-footer__legal">
      <a href="/privacy/">Privacy</a>
      <a href="/legal/">Legal</a>
      <a href="#main">Back to top <span aria-hidden="true">&uarr;</span></a>
    </div>
  </div>
</footer>"""


footer_pattern = re.compile(r'<footer id="footer"[^>]*>.*?</footer>', re.DOTALL)
changed = 0

for html_path in sorted(ROOT.rglob("*.html")):
    original = html_path.read_text(encoding="utf-8")
    updated, replacements = footer_pattern.subn(FOOTER, original, count=1)
    updated = re.sub(
        r'/assets/brand/theme\.css(?:\?v=[^"\']*)?',
        '/assets/brand/theme.css?v=20261028-9',
        updated,
    )
    if replacements:
        html_path.write_text(updated, encoding="utf-8")
        changed += 1

print(f"Refreshed footer in {changed} HTML files.")
