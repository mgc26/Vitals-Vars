# ED Boarding Issue - Development Notes

## Status
- Created: 2024-12-27
- Target publish: Mid-January 2024
- Stage: Initial framework complete

## Key Messages
1. ED boarding is a discharge problem, not a capacity problem
2. Making boarding visible to all units is the key unlock
3. The "discharge lag" is the hidden culprit
4. Solutions don't require new technology or major investment

## Data Points Needed
- [ ] Validate average boarding hours (currently using 6.8 hours)
- [ ] Confirm cost per boarding hour ($137 + $82)
- [ ] Get more specific adverse event data
- [ ] Find studies on boarding impact on satisfaction scores

## Toolkit Components to Build

### SQL Queries Needed
- [ ] ED boarding duration calculator
- [ ] Discharge lag analyzer (order time vs departure time)
- [ ] Hourly capacity snapshot
- [ ] Boarding cost calculator
- [ ] Day-of-week pattern analyzer

### Python Scripts Needed
- [ ] Boarding pattern visualizer (heatmap by day/hour)
- [ ] Predictive discharge model
- [ ] ROI calculator with customizable parameters
- [ ] Automated daily boarding report generator

### Templates to Create
- [ ] Morning boarding huddle agenda
- [ ] Escalation protocol flowchart
- [ ] Unit-level boarding dashboard mockup
- [ ] Executive summary template

### Implementation Guides
- [ ] 90-day rollout plan
- [ ] Change management tips
- [ ] Common objections and responses
- [ ] Success metrics tracking

## Research/References Needed
- Studies on ED boarding impact
- Best practices from high-performing hospitals
- CMS guidelines on ED throughput
- Joint Commission standards

## Visual Assets Ideas
1. Heatmap of boarding hours by day/time
2. Before/after discharge lag visualization
3. ROI calculation infographic
4. Boarding cascade effect diagram

## Questions to Address
- How to handle behavioral health boarding (different issue)?
- Should we address ICU boarding separately?
- How to calculate true cost including opportunity cost?
- What about hospitals without hospitalists?

## Differentiation from Issue 01
- More complex problem (medium vs quick win)
- Requires cross-department coordination
- Winter timing makes it urgent
- Focuses on system visibility vs process change

## Next Steps
1. Build out SQL queries with sample schemas
2. Create Python analysis notebook
3. Design dashboard mockups
4. Write implementation guides
5. Add sample data for toolkit