# Messy email signatures for testing the contact-extraction CLI tool.
# Each entry is messy in a DIFFERENT way, the comment says what it stresses.
# Use these as your test cases: feed each to your tool, check the JSON it returns.
#
# Suggested schema to extract: name, email, company, title, phone  (missing -> null)

test_signatures = [

    # 1. Clean baseline — everything present, well formatted. Should be easy.
    """Best regards,
Sarah Chen
Senior Product Manager
Brightwave Analytics
sarah.chen@brightwave.io
(415) 555-0192""",

    # 2. No company — the org is simply absent. Tool must return company=null, not invent one.
    """Thanks,
Marcus Reid
marcus.reid@gmail.com
+1 312-555-0148""",

    # 3. First name only, no email even — almost nothing to extract. Most fields null.
    """Cheers,
Mike""",

    # 4. Everything crammed onto one line. No line breaks to lean on.
    "Priya Nair | Head of Design | Nimbus Labs | priya@nimbuslabs.co | 020 7946 0958",

    # 5. Buried in a legal disclaimer — the real fields are surrounded by noise the tool must ignore.
    """Regards,
David O'Connor, VP Engineering, Halcyon Systems Inc.
d.oconnor@halcyonsystems.com  |  Direct: 646.555.0117

CONFIDENTIALITY NOTICE: This email and any attachments are confidential and
may be legally privileged. If you are not the intended recipient, please delete
it and notify the sender. Halcyon Systems Inc. accepts no liability for the
content of this email.""",

    # 6. Credentials attached to the name (Dr., PhD) — is the name "Elena Vasquez" or "Dr. Elena Vasquez, PhD"?
    """Dr. Elena Vasquez, PhD
Chief Data Scientist
Meridian Health
evasquez@meridianhealth.org
Tel: +1 (206) 555-0173 ext. 402""",

    # 7. Two email addresses — a personal and a work one. Which does the tool pick?
    """— Jordan Blake
jordan.blake@acme-corp.com (work)
jblake87@yahoo.com (personal)
Acme Corp""",

    # 8. Company has a suffix (LLC) and the title is fused with the company line.
    """Warmly,
Aisha Rahman
Founder & CEO, Saffron Kitchen LLC
aisha@saffronkitchen.com
917-555-0164""",

    # 9. Email embedded mid-sentence, not on its own line. Formatting gives no hint.
    """Hi again — feel free to reach me directly at t.nakamura@orbit-systems.jp
if anything comes up. Thanks!
Taro Nakamura, Solutions Architect, Orbit Systems""",

    # 10. International: non-US phone format, accented characters in the name.
    """Mit freundlichen Grüßen,
Björn Müller
Vertriebsleiter
Adlerstein GmbH
b.mueller@adlerstein.de
+49 30 901820""",

    # 11. Social handles and a website mixed in with the real contact fields.
    """Stay awesome,
Chloe Adebayo
Growth Lead @ Loop
chloe@loop.app
loop.app  •  @chloe_grows  •  linkedin.com/in/chloeadebayo""",

    # 12. Marketing banner + emoji noise wrapped around the actual info.
    """🚀 Ship faster with Cobalt 🚀
------------------------------
Ryan Kowalski
Account Executive
Cobalt Software, Inc.
ryan.k@cobalt.software
Book a call: cal.com/ryank""",

    # 13. Forwarded-header noise bleeding into the signature. Must not grab "From:" fields.
    """From: notifications@service.com
Sent: Tuesday
To: me

Nina Petrova
Operations Manager, Vantage Freight
nina.petrova@vantagefreight.com
Cell 713-555-0135""",

    # 14. Title present, company absent, phone absent — partial data, mixed presence.
    """Talk soon,
Samuel Adeyemi
Freelance Illustrator
sam.draws@protonmail.com""",

    # 15. Name in "Last, First" order, unusual arrangement.
    """Okafor, Chidi
Regional Sales Director — Zenith Beverages
c.okafor@zenithbev.com | +234 803 555 0100""",

    # 16. Almost pure noise, only an email hidden in it. Everything else null.
    """thanks!! sent from my phone sorry for typos
reach me here k.sullivan.contact@fastmail.com ttyl""",
]


# A few expected outputs to grade against (spot-check your tool on these).
# Only listed for a couple; write more as you refine the schema.
expected = {
    0: {"name": "Sarah Chen", "email": "sarah.chen@brightwave.io",
        "company": "Brightwave Analytics", "title": "Senior Product Manager",
        "phone": "(415) 555-0192"},
    2: {"name": "Mike", "email": None, "company": None, "title": None, "phone": None},
    5: {"name": "Elena Vasquez", "email": "evasquez@meridianhealth.org",
        "company": "Meridian Health", "title": "Chief Data Scientist",
        "phone": "+1 (206) 555-0173 ext. 402"},
}