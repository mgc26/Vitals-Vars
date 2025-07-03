# LinkedIn Posts for Methods Minute: Buddy Agent Workflow

## Main Launch Post (Monday Morning)

### Stop stuffing Claude with Epic documentation—let Gemini eat the 500-page manual while Claude ships the code

*(Methods Minute drop — because good hacks shouldn't wait for Friday)*

Picture this: You need to build ED throughput metrics across 47 Epic Clarity tables, 200+ stored procedures, and a data dictionary that would make Tolstoy jealous.

**Old way:** Cry. Copy-paste. Context window explodes. Start over.

**Buddy way:** Two LLMs, one mission:
• **Gemini** = The reader (2M token context window)
• **Claude Code** = The writer (your local execution ninja)
• **You** = The conductor (point and laugh)

### Real healthcare ops example:

"Analyze our entire surgical scheduling system and optimize block utilization"

1. Claude gathers every .sql file, scheduling policy PDF, and utilization report
2. Dumps it all into one mega-context file (38,000 lines)
3. Gemini reads it ALL, returns a 50-step optimization plan with exact SQL
4. Claude executes each step, validates, adjusts
5. You take credit at the Monday meeting

**Result:** What took a consulting team 3 weeks now takes 3 hours.

### The 5-step recipe:
1. Hit a wall ("this is too complex")
2. Gather everything into context.tmp
3. Ask Gemini for the master plan
4. Let Claude execute step-by-step
5. Delete the evidence

No new infra. No fancy tooling. Just `gemini --file context.tmp --prompt "solve my life"`

**Grab the full playbook:** [Newsletter Link]

What 100-page healthcare nightmare would you feed to this beast?

#VitalsAndVariables #HealthcareAnalytics #TwoHeadsBetterThanOne

---

## Teaser Post (30 minutes before)

Your Epic consultant: "That'll be 6 weeks and $180K"

Me with Gemini reading Chronicles documentation while Claude writes the queries: "Give me 90 minutes"

Methods Minute dropping in 30. 

Today's hack: How to build a two-headed AI that reads everything and forgets nothing.

#HealthcareIT #AIAgents

---

## Follow-up Post (Tuesday)

Plot twist from yesterday's Buddy Agent post:

Hospital CTO tried it on their "unsolvable" charge master reconciliation problem. 

Fed Gemini:
- 15 years of charge build documentation
- 300+ Excel files
- Every pricing committee meeting note

Gemini found $2.3M in missed charges from a rule conflict buried on page 847.

The AI didn't find the money. Making the AI read everything did.

Anyone else finding gold in their context dumps?

---

## Visual Post (Wednesday)

[Simple diagram]
```
Your Problem (too big) 
    ↓
Claude (gathers the mess)
    ↓
Gemini (reads the mess)
    ↓
Master Plan (structured markdown)
    ↓
Claude (executes the plan)
    ↓
You (hero of the story)
```

Seeing wild variations already:
• "Triple threat" - add GPT-4 as the validator
• "Specialist squad" - different models for SQL vs Python
• "The loop" - feeding execution results back to Gemini

Drop your remix below 👇

---

## Thursday Momentum Post

4 days since launching the Buddy Agent workflow.

Coolest implementation so far:

Nurse manager fed it:
- 2 years of staffing data
- Union contract (187 pages)
- State regulations
- Historical PTO patterns

Got back: Complete staffing prediction model with shift-swap optimization algorithm.

Time saved: 6 weeks → 6 hours

The kicker? The model caught a contract violation their lawyers missed.

Who's next?