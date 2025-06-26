# Issue Templates

This directory contains the template structure for creating new Vitals & Variables newsletter issues.

## Using the Template

1. **Copy the template**:
   ```bash
   cp -r issue_template ../XX_your_issue_name
   ```

2. **Update the README.md** with issue-specific content

3. **Add your tools** to the `/toolkit/` directory

4. **Add code and data** to the `/code/` directory

5. **Add visualizations** to the `/assets/` directory

## Template Structure

```
issue_template/
├── README.md           # Self-contained issue overview
├── code/              # Analysis code and data
│   ├── data/         # Sample datasets
│   ├── notebooks/    # Jupyter notebooks
│   ├── scripts/      # Python/R scripts
│   └── sql/         # SQL queries
├── toolkit/          # Ready-to-use tools
└── assets/          # Charts and visualizations
```

## Key Principles

1. **Self-Contained**: Each issue must work independently
2. **LinkedIn-Friendly**: Readers should land in a focused, clear directory
3. **Action-Oriented**: Emphasize tools and implementation
4. **ROI-Focused**: Always include financial impact
5. **Quick Wins**: Offer immediate value alongside deeper analysis

## Checklist for New Issues

- [ ] README provides complete context without repository knowledge
- [ ] Toolkit contains at least 3 ready-to-use tools
- [ ] Code includes sample data for testing
- [ ] All SQL queries are well-commented
- [ ] Expected ROI is clearly stated
- [ ] Quick Start guide offers 3 implementation options
- [ ] Success stories or quotes included
- [ ] Technical requirements clearly listed
- [ ] Links are relative within the issue directory
- [ ] Mobile-friendly formatting in README

## Content Guidelines

### README Sections
1. **Problem Statement** (with shocking statistic)
2. **Repository Contents** (clear directory explanation)
3. **Quick Start Guide** (3 options: quick/medium/full)
4. **Expected Results** (metrics and ROI)
5. **Science/Data Behind It** (credibility)
6. **Technical Requirements** (accessibility)
7. **Success Stories** (social proof)
8. **Stay Connected** (newsletter promotion)

### Toolkit Requirements
- Immediately usable (no complex setup)
- Clear instructions included
- Expected impact stated
- Time to implement noted

### Code Standards
- Sample data included
- Requirements.txt provided
- Comments explain healthcare context
- Works with common systems (Epic, Cerner)

## Testing Your Issue

Before publishing:
1. Navigate to the issue directory in GitHub
2. Ensure README displays correctly
3. Test all download links
4. Verify code runs with sample data
5. Check mobile view
6. Test sharing the direct link