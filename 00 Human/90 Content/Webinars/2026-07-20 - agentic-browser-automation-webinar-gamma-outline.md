---
type: content
channel: webinar
status: planning
date: "2026-07-20"
topic: Gamma slide-deck outline for the agentic browser automation webinar
pillar: "Adopting AI well: where it creates value, where the hype fails"
tags: [content, webinar, gamma-outline]
---

# Gamma Outline - Agentic browser automation webinar

Companion to [[2026-07-20 - agentic-browser-automation|Webinar - The Browser Does the Busywork]] and [[2026-07-20 - agentic-browser-automation-webinar-demo-script|the demo script]].

**How to use:** paste everything below the divider line into Gamma's "Paste in text" outline import. Each `---` starts a new slide. First line is the slide title, bullets are the body. Suggested slide count: 14.

---

The Browser Does the Busywork

Agentic Automation, Minus the Hype

Chris Monnat | Dual Logic

A 45-minute honest look at what AI browser agents actually do for your team

---

Somewhere in your company, right now

- A smart person is clicking through the same seven web pages they clicked yesterday
- Logging into vendor portals, copying numbers between systems that refuse to talk
- Pulling the same report, filling the same form
- You keep hearing "AI agents will handle it"
- You cannot tell the real capability from the demo-day magic trick

---

What you will leave with

- What agentic browser automation actually does, in plain terms
- The three questions that tell you if a task is a good fit
- Where it quietly falls apart, so you do not learn that lesson in production
- The honest version, not the sizzle reel

---

What it actually is

- An AI that drives a web browser the way a person does
- It reads the page, decides the next step, clicks, types, and checks its own work
- It works across multiple sites, not one
- Not a smarter script. It reacts to the page, so small changes do not break it

---

The old way, and why it broke

- Brittle scripts that break the moment a button moves
- RPA that needs a specialist to babysit every change
- Every layout tweak meant a support ticket
- The new part: the agent reads and reacts, so it survives small changes

---

The Three-Question Fit Test

- 1. Is the task repetitive and high-volume?
- 2. Are the rules clear enough to write on an index card?
- 3. Is a wrong move recoverable, or does it wire real money out the door?
- Fit is a business decision, not a tech decision

---

Score a task, live

- Take a real task from the room
- Run it through the three questions
- Three yeses means it is a candidate
- One no means keep the human in the loop, for now

---

Live Demo

Multi-portal invoice consolidation

- Two vendor portals, one Google Sheet, one human who copies numbers every week
- Watch the agent do it instead
- Everything on screen is a sandbox, fake data, no real accounts

---

What to watch in the demo

- I did not write code. I described the task like I would to a new hire
- It reads a messy invoice page and pulls structured data
- It moves across two different sites on its own
- It flags a total that does not add up instead of trusting the page

---

The agent checks its own work

- It caught a total that did not match quantity times unit price
- It flagged the row instead of copying a wrong number through
- That flag is the guardrail
- The agent is not just doing the work, it is checking the work

---

Where the Hype Fails

The part nobody demos

- Logins and MFA
- Pages that change under it
- Confidently wrong actions
- No audit trail unless you build one
- Compliance and data exposure

---

The rule to remember

- An agent that can click can also click the wrong thing, faster than any human
- Trust is earned in narrow lanes
- Start with recoverable, low-stakes tasks, watch it work, then widen the lane
- Oversight is a feature you have to build: logs, approvals, a stop button

---

Q&A

- What does this cost to run?
- Does this replace my ops team?
- Short answer to the second: no. It removes their worst hour
- The humans keep the judgment work only humans should do

---

Your next step

Free 30-minute Automation Fit Review

- Bring one browser task you hate
- Leave knowing if it is a fit and what it would take
- Dual Logic | chris@duallogic.ai
- Teach first, pitch last, pitch once
