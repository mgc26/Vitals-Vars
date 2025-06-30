# Your 7:30 Knife Time is Actually 7:47

*Vitals & Variables Issue #1: First-Case On-Time Starts*

## The Hook

Your 7:30 knife time is actually 7:47—here's how to win those 17 minutes back and save seven-figures.

## 1. Frame the Pain

OR minutes run $22-$150 a pop—yet half of first cases still drift late, bleeding cash and goodwill.

Nationally, median first-case-on-time start (FCOTS) is just **65%**, far from the 88-90% benchmark of top performers. At one 10-room suite, running 15 minutes late with 50% FCOTS torched **$1.56M** a year in dead overhead.

And the root cause? Mostly human: surgeon stroll-ins, missing labs, gear gremlins. Every late wheel-in jams the whole day, spikes overtime, and tanks patient satisfaction. That's real money and morale circling the drain.

## 2. Surface the Signals

Crunch the delay codes and you'll see a Pareto cliff:
- **Surgeon-related factors** drive ≈52% of delays
- **Pre-op process gaps** ~18%
- **Room-setup flubs** ~13%
- **Anesthesia holds** 7-15%

In one 3,604-case audit, 55% of first cases were late (median 12 min)—631 hours of OR time vaporized.

The takeaway: fix surgeon punctuality and pre-op readiness first; everything else is noise by comparison.

## 3. Test the Levers

Quality-improvement war stories prove which levers actually move the needle:

| Lever | Intervention | Result |
|-------|-------------|--------|
| **Dedicated "first-case facilitator"** | RN + text nudges | Yale New Haven Children's: FCOTS 62→77%, delay mins –33%, $4K/week freed |
| **Mandatory 07:15 huddle** | Extra pre-op staff | SickKids Toronto: FCOTS 6→60% in 9 months |
| **Surgeon bonus** | $1–2K for ≥90% on-time | MetroHealth: 57% FCOTS lift, $751K saved |
| **Real-time readiness dashboard** | Visual status board | John Muir: Tripled FCOTS, crushed hidden delays |

Notice the pattern: visibility + accountability + quick feedback loops.

## 4. Size the Prize

Do the math:
- 10 ORs × 15 late minutes = **150 lost minutes per morning**
- At $100/min (middle of the cost range) that's **$15K/day**, **$3.8M annually**—more than the hospital's MRI budget
- Boosting FCOTS from 50% to 85% reclaims two full surgical days per month
- Enough capacity for ~120 extra cases a year without a brick of new real estate

CFOs love when "quality" prints money.

## 5. Monday Playbook

1. **Declare the metric**: FCOTS % at wheels-in, goal 85%+ within 90 days.

2. **Daily 15-min huddle (14:00)**: Review this morning's misses, clear tomorrow's landmines.

3. **Golden-Patient Checklist**: One nurse owns "patient green across the board" by 06:30.

4. **Night-Before Room Ready**: Charge RN signs off that every first-case tray & gadget is in the room—no 07:28 scavenger hunts.

5. **Surgeon Scorecards**: Weekly email + lounge leaderboard; tie bonus if politics allow.

6. **Real-Time Dashboard**: Traffic-light board shows patient, surgeon, anesthesia, equipment status at T-30. Red light? escalate.

7. **Celebrate Wins**: Coffee tokens for 100% on-time mornings; public shout-outs keep momentum.

## 6. Grab-and-Go Asset

### Quick Run Chart Analysis

Drop this into `analysis.py` to visualize your FCOTS trend:

```python
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load your EMR extract
df = pd.read_csv('fcots_daily.csv', parse_dates=['date'])
df['on_time_flag'] = (df['delay_minutes'] <= 0)

# Calculate daily on-time percentage
daily = df.groupby('date')['on_time_flag'].mean() * 100

# Create run chart
plt.figure(figsize=(10, 4))
plt.plot(daily.index, daily.values, marker='o', markersize=4)
plt.axhline(85, linestyle='--', color='green', label='Target: 85%')
plt.title('First-Case On-Time %')
plt.ylabel('% On-Time')
plt.xlabel('Date')
plt.legend()
plt.tight_layout()
plt.show()
```

Point it at a CSV with columns: `date, delay_minutes` and watch your trendline bend north.

### Get the Full Toolkit

Visit our GitHub repo [Add link] for:
- Complete analysis code with mock data generator
- SQL queries for common EMR systems
- Dashboard templates (Tableau/Power BI)
- Implementation checklist

---

## References

1. Saul, B., Ketelaar, E., Yaish, A., Wagner, M., Comrie, R., Brannan, G.D., Restini, C. and Balancio, M., 2022. Assessing Root Causes of First Case On-time Start (FCOTS) delay in the orthopedic department at a busy level II community teaching hospital. Spartan Medical Research Journal, 7(2), p.36719.

2. Pashankar, D.S., Zhao, A.M., Bathrick, R., Taylor, C., Boules, H., Cowles, R.A. and Grossman, M., 2020. A quality improvement project to improve first case on-time starts in the pediatric operating room. Pediatric Quality & Safety, 5(4), p.e305.

3. Cox Bauer, C.M., Greer, D.M., Vander Wyst, K.B. and Kamelle, S.A., 2016. First-case operating room delays: patterns across urban hospitals of a single health care system. Journal of Patient-Centered Research and Reviews, 3(3), pp.125-135.

4. Hicks, K.B., Glaser, K., Scott, C., Sparks, D. and McHenry, C.R., 2020. Enumerating the causes and burden of first case operating room delays. The American Journal of Surgery, 219(3), pp.486-489.

5. Halim, U.A., Khan, M.A. and Ali, A.M., 2018. Strategies to improve start time in the operating theatre: a systematic review. Journal of Medical Systems, 42, pp.1-11.

6. John Muir Health Case Study - "Data-Driven Operations: Timely Data to Triple First Case On-Time Starts" - HealthCatalyst, 2021. https://www.healthcatalyst.com/learn/success-stories/operating-room-efficiency-john-muir-health

7. Plante Moran. "First-Case On-Time Starts: A Proven Strategy to Improve OR Efficiency", 2023. https://www.plantemoran.com/explore-our-thinking/areas-of-focus/reimagining-the-future-of-healthcare-systems

8. Knox, C., Harper, J., McMillan, L., Vining, B. and White, T., 2024. Increasing first case on time starts in the operating room using an electronic readiness dashboard: A quality improvement project. Perioperative Care and Operating Room Management, 35, p.100412.

---

*Next Issue: ED Boarding - When Your Waiting Room Becomes a Ward*