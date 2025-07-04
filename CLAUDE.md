# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This is the **"Vitals & Variables"** project - a comprehensive GitHub repository supporting a LinkedIn Newsletter series focused on healthcare operations analytics. The project aims to translate healthcare operational challenges into data-driven, actionable solutions.

### Publishing Workflow
- **Primary Channel**: LinkedIn Newsletter (full articles published directly on LinkedIn)
- **Repository Role**: Houses all code, toolkits, and supplementary materials
- **Content Flow**: 
  1. README.md contains the full newsletter article (copy/paste into LinkedIn Newsletter editor)
  2. linkedin_post.md contains promotional teasers to drive traffic to the newsletter
  3. GitHub repo serves as the download hub for all code and tools mentioned in the article

## Commands and Development Workflow

### Check Toolkit Readiness
```bash
cd scripts
./check_toolkit.sh <issue_folder>
# Example: ./check_toolkit.sh 01_or_first_start_delay
```

### Publish Toolkit to Public Repository
```bash
cd scripts
python publish_toolkit.py <issue_name>
# Example: python publish_toolkit.py 01_or_first_start_delay
```

### Install Python Dependencies (for analysis)
```bash
cd issues/<issue_name>/code
pip install -r requirements.txt
```

### Publishing Process
1. Develop content in the private repository (`(28) Vitals&Vars/`)
2. Ensure all content in `_toolkit/` folder is production-ready
3. Run `check_toolkit.sh` to validate structure
4. Run `publish_toolkit.py` to push to public `vitals-vars-toolkits` repository
5. Only `_toolkit/` contents are published; all other files remain private

## High-Level Architecture

### Dual Repository System
- **Private Repository** (`(28) Vitals&Vars/`): Development, drafts, full articles
- **Public Repository** (`vitals-vars-toolkits/`): Only toolkit contents for readers

### Issue Structure Pattern
Each newsletter issue is self-contained:
```
issue_name/
├── README.md           # Full newsletter article (600-800 words)
├── linkedin_post.md    # Social media promotional content
├── notes.md           # Internal development notes
├── _meta.yaml         # Publishing configuration
├── code/              # Development code and analysis
├── assets/            # Charts and visualizations
├── refs/              # Research materials
└── _toolkit/          # PUBLIC: Production-ready tools
    ├── README.md      # Toolkit overview (NOT the full article)
    ├── sql/           # SQL queries
    ├── python/        # Analysis scripts
    ├── dashboards/    # BI templates (Tableau/Power BI)
    └── guides/        # Implementation guides
```

### 6-Stage Analysis Blueprint
Every issue follows this framework:
1. **Frame the Pain** - Quantify problem with anchor statistics
2. **Surface the Signals** - Descriptive analysis revealing patterns
3. **Test the Levers** - Causal testing of interventions
4. **Size the Prize** - ROI calculations and impact sizing
5. **Monday Playbook** - Week-by-week implementation steps
6. **Grab-and-Go Asset** - Ready-to-use toolkit

### Key Directories
- `issues/`: Self-contained newsletter issues
- `_drafts/`: Working drafts (gitignored)
- `backlog/`: 50+ healthcare use cases organized by department
- `resources/`: Shared templates and resources
- `scripts/`: Publishing and validation scripts

## Important Guidelines

### Content Creation
- **Issue Naming**: Use format `##_short_description` (e.g., `01_or_first_start_delay`)
- **Article Length**: 600-800 words (coffee-break readable)
- **Toolkit Contents**: Must be production-ready, well-documented
- **Dashboard Templates**: Provide both Tableau and Power BI formats when possible

### Citation Guidelines
**CRITICAL: We can NEVER accept fake/hallucinated peer-reviewed references or attributions.**

- **Absolutely forbidden**:
  - Making up author names, publication titles, or journal names
  - Fabricating DOIs, URLs, or publication details
  - Creating fictional statistics or research findings
  - Falsely attributing quotes or data to real organizations
  
- **Required approach**:
  - Only cite sources that you can verify exist
  - If unsure about exact details, use general language ("research indicates", "industry estimates suggest")
  - Mark unverifiable claims as estimates: "Industry estimates suggest..." or "Based on typical patterns..."
  - Use placeholder text like `[Citation needed]` when a citation would strengthen the claim
  
- **For LinkedIn Newsletter format**:
  - References should be in APA style
  - URLs are often not clickable in LinkedIn, so omit them unless specifically requested
  - Focus on author names, year, and publication title
  - Number references and use superscript numbers in text

### Data & Statistics Guidelines
- **All statistics must be verifiable**:
  - Only use data from real sources (government reports, peer-reviewed studies, industry whitepapers)
  - If presenting estimates, clearly label them as such
  - Never invent specific numbers or percentages
  - Industry benchmarks should cite the source organization
  
- **Handling uncertainty**:
  - "A typical 200-bed hospital" instead of fabricating specific hospital data
  - "Industry estimates range from X to Y" instead of picking a specific unverified number
  - "Based on reported outcomes" when referencing case studies
  - "ROI will vary based on hospital size and implementation" as a disclaimer

### Python Analysis Scripts
- Use pandas, numpy, matplotlib, seaborn for analysis
- Include sample data or data generation scripts
- Provide clear documentation and usage examples
- Follow existing patterns in `resources/analysis_templates/`

### SQL Queries
- Write vendor-agnostic SQL when possible
- Include comments explaining logic
- Provide sample table schemas
- Consider performance implications

### What Goes Public vs. Private
**Public (`_toolkit/`):**
- Production-ready code and queries
- Implementation guides
- Dashboard templates
- Quick start documentation

**Private (everything else):**
- Full newsletter articles
- LinkedIn posts and social media content
- Internal notes and drafts
- Research references
- Development/experimental code

## Current Status
- **Completed Issues**: 00 (launch), 01 (OR first-case delays)
- **In Progress**: 02 (ED boarding)
- **Backlog**: 50+ use cases in `backlog/use_cases.md`

## Target Audience
- Healthcare operations managers
- Chief Operating Officers (COOs) and Chief Medical Information Officers (CMIOs)
- Clinical innovators and process improvement teams
- Anyone working to improve healthcare efficiency

Remember: Focus on practical, implementable solutions with clear ROI. Healthcare professionals need evidence and proven methods, not theoretical approaches.