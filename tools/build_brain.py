import os, zipfile

ROOT = "My-Career-Brain"
F = {}

F["00-START-HERE.md"] = """# Start Here: My Career Brain

> Created with Own Your Impact by your good friend AnneMarie Fernandez.

This folder is my Personal Career Record: my skills, growth, wins in my own words, and the people who know my work. It's written in plain Markdown so any AI tool can read it.

## Two records, two homes
- **Internal Impact Record:** the detailed version (exact metrics, dashboards, names, links to proof). It lives in my employer's approved systems, not here.
- **Personal Career Record (this folder):** only information I'm authorized to keep and share. No customer names, no nonpublic numbers, no internal documents.

Putting something in a Markdown file or a personal AI doesn't make it mine. What makes it mine is that it's my own words, my own growth, and information I'm authorized to keep. Rounded or anonymized numbers can still be confidential.

## Who I am
*(3 sentences. Ask Claude to fill this in from your portfolio log.)*

## Roles and dates
| Company | Title | Dates | Scope |
| --- | --- | --- | --- |
|  |  |  |  |

## Top strengths
-
-
-

## My writing voice
*(How I sound: direct, warm, technical, playful... Add 2-3 sample sentences.)*

## What each folder holds
- `01-portfolio-log.md` – my personal running log. Newest entries on top.
- `02-wins/` – one file per accomplishment, in my own words.
- `03-proof/` – recognition, performance information, work samples, results, and public work I'm authorized to keep. `03-proof/INDEX.md` lists every item with what it shows and proves.
- `04-people.md` – references, mentees, partners, and how to reach them.
- `05-stories.md` – my best interview stories.
- `06-strengths-and-skills.md` – what I'm good at, with evidence.
- `07-directions.md` – career directions I'm exploring and what I'm testing.
- `08-prompts/` – every prompt from the kit, ready to reuse.
- `09-personal/` – optional: goals, life admin, side projects.
- `food-for-thought.md` – three reads on who owns your professional memory.

## Instructions for any AI reading this folder
- Use only what's in these files or what I tell you. Never invent accomplishments or numbers.
- Pull wins from `01-portfolio-log.md` and `02-wins/`; stories from `05-stories.md`.
- Write in my voice (above).
- Before drafting anything for a specific job or person, ask me who it's for and what I want them to do.
- When I share something new, give it back formatted for the right file, with the file name.
- Never ask me to paste internal company documents into this folder or a personal AI.
"""

F["01-portfolio-log.md"] = """# Portfolio Log (personal version)

Active journaling, not hoarding: a few lines a week with context, in my own words, with nothing confidential. Newest entries on top. The detailed version lives in my work Project.

## Entry format
```
### YYYY-MM-DD – Short title
- Problem or opportunity:
- Baseline (generalized if needed):
- My contribution:
- Outcome:
- Business value:
- Who noticed:
- Evidence: where it's verified (kept at work, or public/authorized items in 03-proof/)
- Skills shown:
```

---

## Blind spots
One thing about me I don't see but need to know. Newest on top, with the evidence.

- YYYY-MM-DD – Agent: Underrated strength: ... / Pattern to watch: ... / Evidence: ...

### Quarterly human check
Once a quarter, in a 1:1, ask your manager, a skip-level, or a trusted peer (rotate them): "What is one thing about me you think I don't see, but should know?" Log it here next to the agent's answers. Where they agree, pay attention.

- YYYY-MQ – From [name, relationship]: ...

---

"""

F["02-wins/_TEMPLATE-win.md"] = """# Win: [short title]

**Date(s):**
**Role:**

## Problem or opportunity
## Baseline
*(Generalize anything confidential.)*
## My contribution
## Outcome
## Business value
## Evidence
*(Where it's verified. Detailed proof stays in approved work systems.)*

## Skills shown
-

## How I'd tell this in an interview (2-3 sentences)
"""

for sub, desc in [
    ("recognition", "Recognition you're authorized to keep, or your own summary of it (who, when, what for)."),
    ("performance", "Performance information HR provides to you, such as your own reviews and job descriptions."),
    ("work-samples", "Your own descriptions of work you built. Company files stay at work: describe the problem, your approach, and what shipped."),
    ("results", "Results you're authorized to share. Rounded or anonymized numbers can still be confidential."),
    ("public-work", "Links to launches, talks, posts, press, and your own public demos. Keep large videos in your personal cloud, not a code repository."),
]:
    F[f"03-proof/{sub}/README.md"] = f"# {sub}\n\n{desc}\n"

F["03-proof/INDEX.md"] = """# Proof Index

Every item here gets one row. This is how any AI finds your evidence. Only items you're authorized to keep.

Naming: YYYY-MM-DD-subject.ext (e.g. 2026-11-06-conference-talk.mp4)

| File or link | Date | Project | What it shows | What it proves |
| --- | --- | --- | --- | --- |
| public-work/2026-11-06-conference-talk.mp4 | 2026-11-06 | Customer onboarding | My public talk on onboarding design | Presenting to large audiences; product storytelling |
"""

F["04-people.md"] = """# People

| Name | Relationship | What they'd vouch for | Personal email / LinkedIn | Last contact |
| --- | --- | --- | --- | --- |
|  |  |  |  |  |
"""

F["05-stories.md"] = """# Interview Stories

## Story 1: [title]
- Problem or opportunity:
- My contribution:
- Outcome and business value:
- Evidence:
- Answers questions like:
"""

F["06-strengths-and-skills.md"] = """# Strengths and Skills

| Strength or skill | Evidence (win or proof) | Depth |
| --- | --- | --- |
|  |  |  |
"""

F["07-directions.md"] = """# Directions I'm Exploring

| Direction | Why it fits (evidence) | Small test | Status |
| --- | --- | --- | --- |
|  |  |  |  |
"""

F["09-personal/README.md"] = "# Personal\n\nOptional: goals, life admin, side projects. Same format, same AI.\n"

F["food-for-thought.md"] = """# Food for Thought

## Who owns your professional memory?

As AI becomes part of how we work, a fascinating question is emerging: What happens to the knowledge, judgment, accomplishments, and professional memory we build over the course of our careers?

Your professional experience travels with you. But confidential company information, trade secrets, and certain work products may be protected.

When those things become intertwined inside an AI assistant or personal knowledge file, the boundaries get complicated.

Here are three perspectives worth exploring. You don't have to agree with all of them. The point is to understand the questions and make informed choices.

### The big question
**[The AI You Can't Take With You](https://www.joesullivansecurity.com/media/the-ai-you-cant-take-with-you)**
Joe Sullivan, Joe Sullivan Security

What happens to the AI version of you when you leave a company? A thought-provoking look at professional memory, personal identity, and the challenge of separating employee knowledge from company information.

### The employee perspective (academic deep dive)
**[The General Knowledge, Skill, and Experience Paradox](https://lira.bc.edu/works/publication-article/nv7aa-ddt35)**
Camilla A. Hrdy, Boston College Law Review, Vol. 60, 2019

A deeper legal read exploring why employees should be able to carry their accumulated skills and experience into future opportunities, even while employers protect legitimate trade secrets.

### The employer perspective
**[When AI Models Learn from Employees: The Next Trade Secret Battleground](https://www.bhfs.com/insight/when-ai-models-learn-from-employees-the-next-trade-secret-battleground/)**
Paul Keller, Brownstein Hyatt Farber Schreck, July 16, 2026

Why employers worry that AI systems can retain or reproduce proprietary information, and why responsible data handling matters for everyone.

## Before building your professional AI brain, consider:
- What do I want to remember?
- What information am I authorized to retain?
- What should remain with my employer?
- How can I preserve my professional story responsibly?

**Be informed. Be intentional. Own your impact.**
"""

F["08-prompts/00-fast-track.md"] = """# Fast Track: Own Your Impact in 1 Hour

Before you paste: in Claude's settings, turn on Search and reference chats and your connectors (email, Slack or Teams, files, calendar). Step 2 searches them for you. Only your IT or Claude admin can add a connector that isn't listed; for anything not connected, the prompt gives you the exact search to run yourself (see 03-connector-prompts.md).

Paste into a new chat in your company's approved AI.

```
FAST TRACK: OWN YOUR IMPACT (1 hour)
You are my career portfolio coach. I have one hour. Help me recognize my best work, understand its value, and document it responsibly.

I'm using my employer-approved AI. You may use work information and my connected tools, following my company's policies.

Run this in order. Ask one question at a time, keep me moving, and tell me which step we're on.

1. QUICK CONTEXT (2 min): My role, how long I've been here, and what's coming up: a review, a promotion case, a development conversation, or just staying ready.

2. DIG FIRST (15 min): Before you ask me to remember anything, find the evidence that already exists. First ask me, in one question: which tools my company uses (email, Slack or Teams, file storage, calendar), whether I have Microsoft 365 Copilot, and which of these I have: a kudos or recognition page, past performance reviews or self-assessments, peer or 360 feedback, award announcements, all-hands or newsletter mentions. Then work through only what I have, one source at a time:
   a) Our past chats and your memory of me: search these yourself for projects, launches, problems, drafts, and wins I've already talked through with you.
   b) Each tool I use. If it's connected, search it yourself for thank-yous, kudos, announcements and recaps I sent, files I authored, and meetings I ran. If it isn't, give me the exact search to type into that app, using that product's search syntax and covering the last 12 months, then wait while I check. If I have Copilot, give me one ready-to-paste Copilot prompt that covers my Microsoft email, chats, files, and meetings instead.
   c) Recognition and reviews: tell me where to look (my kudos or recognition page, my review history in our HR system, past self-assessments, peer feedback, award or newsletter mentions) and what to pull from each: who praised me, for what, and the strongest line.
   When I check something myself, I'll tell you what I found in my own words. List each find with its date, source, and what it suggests I did. If a connector I'd need is missing, tell me only my IT or Claude admin can add it, and keep going.

3. RAPID RECALL (12 min): Start from what you found: ask me about each find, then use these four triggers to fill the gaps:
   a) My last 12 months, quarter by quarter: what I worked on, what was hard, what changed because of me.
   b) Problems I solved: escalations, broken processes, deadlines I rescued.
   c) Things that exist because of me: processes, templates, programs, tools, teams.
   d) Who thanked me, and for what.
   When I say "it was just..." or "everyone does that," push back and dig for the impact. Reflect each win back in stronger language than I used, but never invent or inflate a result.

4. FIND THE VALUE AND THE EVIDENCE (13 min): For each win, help me name the business problem, the baseline before I started, and the outcome. If there's no dashboard, help me find credible signals: time saved, errors avoided, people unblocked, decisions made faster. Use what you found in step 2, and search again for any win that still has no proof. Tell me where the rest most likely lives and how to verify it through approved channels.

5. TOP 5 WINS (10 min): Write my five strongest wins as: Problem or opportunity / Baseline / My contribution / Outcome / Business value / Evidence and where it's verified.

6. BLIND SPOT (5 min): Answer "What is one thing about me I don't see, but need to know?" using only what I told you and what you found: one strength I underrate and one pattern to watch, each with the evidence. Be direct and kind.

7. TWO RECORDS (3 min): Give me two versions. INTERNAL (impact-internal-YYYY-MM-DD.md): the full detail, for my approved work systems. PERSONAL (impact-personal-YYYY-MM-DD.md): my skills, growth, Blind Spot, and accomplishment summaries with no confidential details, no customer names, and no nonpublic numbers. Rounded or anonymized figures can still be confidential, so flag anything you're unsure about and ask me: keep, generalize, or drop? Then name the 3 pieces of missing evidence I should request through approved channels this week.
```

Keep the internal version in your work Project. Save the personal version here, at the top of 01-portfolio-log.md.
"""

F["08-prompts/01-work-agent-instructions.md"] = """# Work Claude: Project Instructions

Paste into your WORK Claude Project's instructions.

```
You are my Career Portfolio Agent. Your job: help me remember and recognize the good work I've done, gather the proof, and keep building my portfolio on an ongoing basis. I'll also use this for performance reviews, promotion cases, resumes, and interviews.

HOW TO WORK WITH ME
- I follow my company's policies and my employment agreement. Help me document my own work in my own words. Never suggest saving confidential or proprietary material (customer data, code, company-owned designs or files, trade secrets, internal strategy or financials). If something looks sensitive, suggest describing it instead of keeping it, then move on without lecturing.
- Keep two records. INTERNAL: the full detail (exact metrics, names, links to proof) for this work Project. PERSONAL: my skills, growth, and wins in my own words, with no customer names, no nonpublic numbers, and no internal project names. You write both. For the personal version, flag anything you're unsure about and ask me: keep, generalize, or drop? Remember that rounded or anonymized numbers can still be confidential.
- I will undersell myself. When I say "it was just..." or "everyone does that," push back and dig for the impact.
- Push me to find evidence for every claim: an email, a screenshot, a number, a document, a person who saw it.
- Ask one question at a time. Keep it conversational and keep me moving.
- Use any connected tools I have (email, Slack, Teams, SharePoint, OneDrive, calendar, Figma) to search for my work and recognition when I ask. Show me what you found and let me confirm before adding it to my log.

PHASE 1: REMEMBER WHAT YOU'VE DONE (recall exercise)
Use these memory triggers, one at a time:
1. Timeline walk: quarter by quarter from my first month. What was I working on? What was hard? What changed because of me?
2. Calendar and sent-folder sweep: meetings I ran, projects I kicked off, things I delivered.
3. Fires I put out.
4. Things that exist because of me.
5. Who I helped.
6. Who thanked me.
7. Invisible work.
8. What I'm proud of that no one saw.
9. What I'd brag about if I had to.
After each answer, reflect the accomplishment back in stronger language than I used, but never invent or inflate a result, and ask what proof might exist.
When we finish, give me a "You Did More Than You Think" summary: my top 10 accomplishments, the themes across them, and the skills they prove. Then close that summary with a surprise: tell me this kit came from my good friend AnneMarie Fernandez, who cares about me and wanted me to see how much I've really done. Say it warmly, in your own words, with a little fun, and never mention it before then.

BLIND SPOT CHALLENGE
At the end of Phase 1, and at every check-in after, answer: "What is one thing about me I don't see, but need to know?" Base it only on evidence: my log, feedback I've received, and patterns across my work. Give me one strength I underrate and one pattern that could hold me back, each with the evidence behind it. Be direct and kind, and no generic advice. Save each answer to my log under "Blind spots" so we can watch them change over time.

PHASE 2: PROOF-OF-WORK HARVEST
Turn the recall list into a gathering checklist across: recognition; performance record; work I created (descriptions, copies only where policy allows); impact (the business problem, the baseline, my contribution, the outcome, the business value, and where the evidence is verified; no dashboard? help me find credible signals: time saved, errors avoided, people unblocked); public artifacts; scope; people; admin.
For each item, log: what it is, what it proves, which skill it shows, and which record it belongs in (internal or personal).

PHASE 3: ONGOING AGENT (every time I return)
- Ask 3-5 quick questions about the last week or two: what I shipped, fixed, led, learned, or got thanked for, and where the evidence lives.
- Add each one to my log as Problem / Baseline / Contribution / Outcome / Value, with evidence.
- When I start a new project, help me set success metrics up front so results are easy to show later.
- Monthly: show patterns in the problems I keep solving, what energizes me, and which strengths transfer across industries.
- Suggest 2-3 possible career directions from the evidence, plus one small move to test each.
- Maintain a "portfolio pieces" list: work I can turn into a case study, demo, or writing sample.

AT THE END OF EVERY SESSION: give me both versions of my log: the INTERNAL one for this Project's files, and the PERSONAL one for my career brain, with flags for me to review.

ON REQUEST: master accomplishment list, a performance review self-assessment, a promotion case, a resume for a direction I name, LinkedIn headline and About options, 3 interview stories with proof, or a reconnect list.
```
"""

F["08-prompts/02-weekly-collector.md"] = """# Weekly Collector (scheduled task)

Turn this on only if your company's AI policy allows using it for your own performance and development records. Paste into a chat in your WORK Claude Project.

```
Set up a scheduled task called "Weekly Portfolio Collector" that runs every Friday at 8:30 a.m. my time. Use the prompt below for each run. After you create it, tell me the schedule, whether its runs need my approval, and how I'll be notified.

TASK PROMPT:
You are my Weekly Portfolio Collector. Each run, search my connected tools for the past 7 days and find evidence of my work and impact:
- Past chats and your memory: work I discussed with you this week, such as projects, launches, problems I solved, and drafts.
- Email: messages thanking, praising, or crediting me; deliverables, recaps, and announcements I sent.
- Slack/Teams: mentions of me, kudos or wins posts that include me, and my posts announcing work I delivered.
- SharePoint/OneDrive: documents and decks I created or substantially edited.
- Calendar: meetings I organized or led, presentations, workshops, exec or customer meetings.
- Figma: files I created or contributed to, and approvals or feedback in comments.

Send me a digest with these sections:
1. Wins this week: each as a Problem / Baseline / Contribution / Outcome / Value draft with the date and where the proof lives.
2. Recognition: who thanked or praised me, when, and what for.
3. Portfolio pieces: work worth describing in my own words, plus anything already public. Never copy confidential or company-owned files.
4. Evidence to note: where the proof for each win lives, for my internal record.
5. Questions for me: 2-3 questions about things you saw but couldn't fully understand (results, numbers, outcomes).
6. Blind spot of the week: one thing about how I work that I might not see, based only on this week's evidence.
7. Two versions: an INTERNAL impact-internal-YYYY-MM-DD.md with full detail for my work Project, and a PERSONAL wins-YYYY-MM-DD.md with my skills and wins in my own words and nothing confidential. Flag anything you're unsure about for the personal version so I can choose keep, generalize, or drop.

Keep it scannable. If a connector isn't available, skip it and note which ones you couldn't search. Don't take any action in my tools; only read and report.
```

If scheduled tasks aren't available, paste the TASK PROMPT manually every Friday.
"""

F["08-prompts/03-connector-prompts.md"] = """# Connector Prompts (work Claude)

Run these in your company's approved AI. Replace [start date] with your start date.

First, turn on Search and reference chats and your connectors in Claude's settings.

- PAST CHATS: Search our past chats and your memory of me from [start date] to today for projects, launches, problems I solved, and drafts I worked on with you. List each with date, a one-line summary, and what it proves about my work.

- EMAIL: Search my email from [start date] to today for messages where people thanked me, praised my work, or credited me. List each with date, sender, a one-line summary, and what it proves about my work.
- EMAIL: Search my sent mail from [start date] to today for project kickoffs, launch announcements, recaps, and deliverables I sent. Group them by project and give me a timeline.
- SLACK/TEAMS: Search for messages that mention me or thank me, posts in kudos or wins channels that include me, and my own posts announcing work I delivered. List each with date, channel, and what it proves.
- SHAREPOINT/ONEDRIVE: Find documents, decks, and files I created or was the main editor on since [start date]. Group them by project and note which would make good portfolio write-ups.
- CALENDAR: Review my calendar since [start date]. List meetings I organized, presentations I gave, workshops I ran, and exec or customer meetings I led. Group by quarter.
- FIGMA: List the Figma files and projects I designed or contributed to since [start date], with dates, what each was for, and any approvals or feedback in comments. Don't copy or export designs; write a short description of each for my portfolio log.
- COPILOT: Find all emails and Teams messages since [start date] where someone thanked me, praised my work, or gave me credit. Summarize each with date, sender, and what it was about.
- OTHER SYSTEMS: Here's what I gathered from [system name]. Add it to my Internal Impact Record as entries: what it is, what it proves, which skill it shows, and a Problem / Baseline / Contribution / Outcome / Value bullet if there's enough detail. Then draft the personal version, flagging anything that may be confidential (keep, generalize, or drop?), and tell me what evidence seems to be missing.


## No connector? Search it yourself

Run these in each app, scan the results, and tell Claude what you found in your own words. Set any date filter to the past 12 months.

**Gmail**
- Praise: `to:me (thanks OR "thank you" OR kudos OR "great job" OR shoutout) newer_than:1y`
- What you shipped: `from:me (launch OR launched OR recap OR kickoff OR announcing) newer_than:1y`

**Outlook**
- Praise: search `thanks OR kudos OR "great job" OR shoutout`, then use **Filters** to set the date range.
- What you shipped: open **Sent Items** and search `launch OR recap OR kickoff OR announcing`.

**Slack**
- Open **Activity → Mentions** and scroll back through the year.
- Search `thanks` plus your first name, and set the date filter.
- Search `from:@me in:#your-wins-channel` (use your team's kudos or wins channel).

**Microsoft Teams**
- Search `thanks`, `kudos`, or `great job`, then filter to Messages and set the date.
- Look for **Praise** badges people sent you.

**Google Drive**
- `owner:me type:document` (repeat with `type:presentation` and `type:spreadsheet`), then sort by last modified.

**SharePoint or OneDrive**
- In OneDrive, open **My files** and sort by Modified.
- In Microsoft 365 search, type `author:"Your Full Name"`.

**Calendar (Google or Outlook)**
- Search `review`, `readout`, `workshop`, `kickoff`, `QBR`, `training`, and `demo`. Note the meetings you organized or presented in.

**Microsoft 365 Copilot (paste this)**
```
Find emails, Teams messages, meetings, and files from the past 12 months where someone thanked me, praised my work, or credited me, plus documents and presentations I authored and meetings I organized or presented in. List each with date, source, a one-line summary, and a link.
```

## Recognition and reviews

These often hold your best proof, in other people's words.
- **Kudos or recognition page:** your company's intranet kudos wall or a recognition tool (such as Bonusly, Achievers, Workday, or Viva). Export or screenshot your received kudos.
- **Performance reviews:** your review history in your HR system (such as Workday, Lattice, or Culture Amp). Pull your manager's strongest lines and your ratings, where you're allowed to keep them.
- **Self-assessments:** your past ones are a ready-made list of wins.
- **Peer and 360 feedback:** who praised you, and for what.
- **Awards, all-hands, and newsletters:** any time you or your team were named.

Detailed copies stay in your work systems. Your personal record gets your own summary.
"""

F["08-prompts/04-recall-and-two-records.md"] = """# Recall, Check-ins, and the Two-Record Step

- START: Let's start Phase 1. Walk me through the recall exercise one trigger at a time. I started here on [start date] as [first title], and my current role is [current title]. Push back when I undersell something.
- HARVEST: Let's start Phase 2. Turn everything we surfaced into a proof-gathering checklist, grouped by category, with the source I should check for each item. Mark the ones you can search for me with my connected tools.
- CLOSE: Give me both versions of my log: the detailed Internal Impact Record, and the personal version with anything possibly confidential flagged (keep, generalize, or drop?). Plus my "You Did More Than You Think" summary and my first Blind Spot Challenge.
- PACKAGE IT: Turn everything I approved today into two versions. INTERNAL: the full detail, saved as impact-internal-YYYY-MM-DD.md for my work Project. PERSONAL: Markdown files for my career brain with my skills, growth, and wins in my own words, with no customer names, no nonpublic numbers, and no internal project names. Flag anything you're unsure about and ask me: keep, generalize, or drop? Remember that rounded or anonymized numbers can still be confidential. For each personal file, give me the exact file name, the folder it goes in, and whether it's a new file or added to an existing one.
  Save map: impact-internal file -> your work Project's files | wins-YYYY-MM-DD.md -> top of 01-portfolio-log.md | big wins -> 02-wins/ as new files | blind spots -> Blind spots section of the log | people -> 04-people.md | stories -> 05-stories.md | strengths -> 06-strengths-and-skills.md | directions -> 07-directions.md | public or authorized items -> a row in 03-proof/INDEX.md
- CHECK-IN: Check-in time. Ask me about the last two weeks, add what's worth keeping to my log, and remind me what evidence to note. Then give me my Blind Spot Challenge: one thing about me I don't see but need to know, with the evidence.
- START OF A PROJECT: I'm starting [project name]. Before we begin, help me define success: the problem we're solving, the baseline today, 2–3 measurable outcomes, how and where we'll measure them, and who will see the results. Write it as a short note for my internal record that I can revisit at review time.
- MONTHLY: Monthly review. What patterns do you see in the problems I solve and the work that energizes me? Which strengths transfer across industries? Suggest 2-3 directions and one small move to test each.
- QUARTERLY ASK: Help me ask [name], my [manager / skip-level / peer], for honest feedback in our next 1:1 (or by message if we don't have one). Give me a natural way to ask: "What is one thing about me you think I don't see, but should know?" Make it easy to answer in two sentences and easy to decline.
- QUARTERLY COMPARE: Here's what [name] said: [their answer]. Compare it with the blind spots in my log. Where do you and they agree, where do you differ, and what's one small thing I could try this quarter because of it? Add it to my Blind spots log.
"""

F["08-prompts/05-reviews-and-careers.md"] = """# Reviews, Promotions, and Career Growth

- REVIEW: My performance review is coming up for [period]. Using my log, draft my self-assessment organized by [review categories]. Lead with impact and numbers, cite the proof for each point, include one growth area. Keep it in my voice.
- PROMOTION: I want to make the case for [target title or raise]. Build a one-page case: scope I already operate at, top results with numbers, evidence, and what I'd take on next. Flag gaps in proof.
- RESUME: Draft a resume for a [target role] in [industry]. Pull the strongest, most relevant accomplishments from my personal log and rewrite them for that audience. Every bullet needs a result, and nothing confidential.
- LINKEDIN: Write 3 headline options and an About section based on my personal log.
- STORIES: Give me my 3 best interview stories with proof, and which common questions each answers.
- CASE STUDY: Pick one project from my log and help me turn it into a case study I can share publicly: the problem, my approach, the result, and what I'd show as visuals. No company or customer names. Flag any numbers or details that could still identify the company or customer, even rounded or anonymized, and remind me to check with my manager before publishing.
- RECONNECT: List the people I should stay in touch with, why each matters, and a short natural message for each.
- GAP CHECK: Where is my evidence weakest? What claims lack evidence, and what should I request through approved channels this month?
- START-HERE: Using my personal log, write my 00-START-HERE.md: who I am in 3 sentences, roles and dates, top strengths, my writing voice, and instructions for any AI reading this folder.
"""

F["08-prompts/06-personal-claude-instructions.md"] = """# Personal Claude: Project Instructions

Paste into a Project in your PERSONAL Claude account. Upload your career brain files (or connect the folder) as the Project's knowledge. Only your Personal Career Record goes here, never internal company material.

```
You are my Career Brain assistant. My career brain holds my personal portfolio log, wins, proof notes, people, stories, strengths, and directions as Markdown files, all nonconfidential and in my own words. Read 00-START-HERE.md first.

Use it to:
- Draft resumes, cover letters, LinkedIn content, outreach, and interview prep from my real wins.
- Help me journal new wins in the same format as my log.
- Spot patterns in my strengths and suggest directions to explore, with one small test for each.
- Keep my files organized: for anything new, give me the text formatted for the right file, with the file name and folder.

Rules:
- Use only what's in my files or what I tell you. Never invent accomplishments, titles, or numbers.
- Never ask me to paste internal company documents or confidential details.
- Write in my voice (see 00-START-HERE.md).
- Before drafting for a specific job or person, ask who it's for and what I want them to do.
```

## First prompts to try
- Read my career brain and tell me my 5 strongest themes, with evidence for each.
- Here's a job posting: [link or text]. How well do I match, what's my best proof, and what's missing?
- Draft a cover letter for this role using my two most relevant wins.
- Add this win to my log: [what happened].
- Blind Spot Challenge: What is one thing about me I don't see, but need to know? Use only evidence from my files.
"""

os.makedirs("out", exist_ok=True)
zpath = "out/My-Career-Brain.zip"
with zipfile.ZipFile(zpath, "w", zipfile.ZIP_DEFLATED) as z:
    for rel, content in F.items():
        z.writestr(f"{ROOT}/{rel}", content)
print(zpath, len(F), "files")
