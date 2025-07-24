# Gemini Interview Notes: Prior Authorization Provider Perspective

**Date:** January 24, 2025  
**Topic:** Prior Authorization from Provider Perspective (Issue #04)

## Key Insights Captured

### 1. The Core Problem: "Administrative Surrender"
- **Headline Statistic:** 300-bed hospitals write off $7.9M annually in legitimate revenue
- Not a cost problem, but a **forced revenue abandonment** problem
- 80%+ of appeals would succeed, but only 12% are pursued
- The system is designed to make providers fail

### 2. Financial Model Breakdown (300-bed hospital)
- **Total denials:** $36M (8% of $450M gross revenue)
- **PA-related denials:** $9M (25% of total denials)
- **What they fight:** $1.05M (11.7% of PA denials)
- **What they surrender:** $7.95M in legitimate revenue
- **Appeal ROI:** 1650% return (spend $70/claim, recover 81.7%)

### 3. Why 2025 is the Inflection Point
1. **Regulatory deadline:** CMS Interoperability Rule compliance in 2026-2027
2. **Technology maturity:** AI/automation now delivering real ROI (80% automation, <90 sec responses)
3. **Unsustainable pain:** Direct impact on physician burnout and patient safety

### 4. Current State Reality
**Department Profile:**
- 8-12 FTEs (experienced specialists, not clerks)
- 150-200 new requests daily
- 6+ month learning curve per specialist
- High burnout and turnover

**Technology Stack:**
- EHR with limited PA functionality
- 10-20 different payer portals
- Fax machines and phones still prevalent
- Spreadsheets for tracking

**Biggest Bottlenecks:**
1. Manual status checking (non-value-added work)
2. Documentation chase from physicians
3. Peer-to-peer scheduling delays

### 5. Why "Just Hire More People" Doesn't Work
1. **CFO resistance:** Adding overhead to recover revenue "we should have been paid"
2. **Talent scarcity:** Requires clinical + coding + payer knowledge
3. **Complexity trap:** More people ≠ less complexity
4. **Physician bottleneck:** Can't scale surgeon time for peer-to-peers (THE ultimate constraint)

### 6. Success Story: "Midwest Health System" Case Study
**400-bed facility that recovered $6.5M (vs. $1.1M baseline)**

**Phase 1: Centralize & Standardize (30-60 days)**
- Created centralized PA Center of Excellence reporting to Revenue Cycle VP
- Implemented Power BI Denial Dashboard (3 metrics: denial rate by payer, TAT by service, denial reasons)
- Started with highest-volume service (Cardiology) - standardized documentation templates

**Phase 2: Automate the Workflow (60-90 days)**
- Leveraged Epic Payer Platform + clearinghouse (Availity)
- Real-time eligibility checks at scheduling
- RPA bot for automated status checking
- **Key innovation: P2P Gatekeeper** - Senior clinical nurse who preps all documentation before physician involvement

**Results After 6 Months:**
- First-pass approval: 82% → 96%
- Auth TAT: 6 days → <24 hours
- PA denial rate: 14% → <4%
- Manual follow-up time: 40% → <5% of day
- Revenue recovered: $1.1M → $6.5M

### 7. The 2-Week Quick Win Plan
1. **Convene "Denial Triage" War Room** (Day 1)
   - 1-hour meeting with Revenue Cycle, Patient Access, top 2 service lines
   - Mandate 48-hour report: Top 5 denying payers, Top 5 denied procedures

2. **Launch "Checklist Sprint"** (Days 3-6)
   - Pick #1 most-denied procedure
   - Create one-page documentation checklist
   - Laminate and standardize

3. **Implement 15-Minute Daily PA Huddle** (Day 2 ongoing)
   - Review all requests >48 hours old
   - Ask: "What's the holdup?" and "Who owns resolution today?"

4. **Appoint P2P Gatekeeper** (Day 1)
   - No physician scheduled until documentation complete
   - Immediate win with medical staff

### 8. Analytics Toolkit Components

**Analysis 1: Denial Hotspot Dashboard**
- Metrics: Denial rate %, denied value $, top 5 payers/procedures
- Data: Billing system + 835 remittance files
- Insight: Focus for war room and contract negotiations

**Analysis 2: TAT & Bottleneck Analysis**
- Metrics: Request-to-decision time, decision-to-appeal time
- Data: PA tracking system with timestamps
- Insight: Identifies payer vs. internal delays

**Analysis 3: Authorization Complexity Score**
Simple rule-based system:
- Payer in top 3 deniers: +3 points
- Procedure cost >$5K: +2 points
- Surgical service: +2 points
- Urgent request: +1 point
- Recent denial history: +2 points

Thresholds:
- 0-3: Standard workflow
- 4-6: Senior specialist review
- 7+: P2P Gatekeeper review

**Denial Prediction Model:**
- Uses historical data (payer, CPT, cost, urgency)
- RandomForest classifier
- Outputs probability of denial
- Enables proactive intervention for high-risk auths

---

## Emerging Themes for Article

### Frame the Pain
- Lead with $7.9M "administrative surrender" statistic
- Position as strategic failure, not operational inefficiency
- Highlight the 1650% ROI paradox

### Surface the Signals
- Only 28-31% electronic submission rate
- 81.7% appeal success rate proves medical necessity
- Physician time is the ultimate bottleneck

### Test the Levers
- Technology automation (not more staff)
- Process redesign (not incremental improvement)
- Strategic partnerships with payers
- P2P Gatekeeper role as game-changer

### Size the Prize
- $6.5M recovery possible (Midwest Health example)
- <24 hour TAT achievable
- 96% first-pass approval rate

### Monday Playbook
- 2-week quick win plan ready to implement
- Specific roles and responsibilities
- Measurable outcomes

### Grab-and-Go Asset
Priority toolkit components:
1. Denial Hotspot Dashboard SQL
2. Authorization Complexity Score calculator
3. P2P Gatekeeper job description/workflow
4. Checklist templates
5. Denial prediction model framework

---

## Next Questions
1. What dashboard platform recommendations (Power BI vs Tableau)?
2. Sample documentation templates for top procedures?
3. Vendor comparison insights for automation tools?
4. Change management tips for physician adoption?