# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This is the **"Vitals & Variables"** project - a comprehensive GitHub repository supporting a LinkedIn newsletter/podcast series focused on healthcare operations analytics. The project aims to translate healthcare operational challenges into data-driven, actionable solutions.

## Project Mission

"Turning frontline headaches into data-backed fixes—every other Friday."

## Repository Structure (Planned)

```
(28) Vitals&Vars/
├── README.md                    # Newsletter overview + blueprint
├── issues/                      # Each newsletter issue
│   ├── 00_launch/              # Launch issue
│   ├── 01_or_first_start_delay/ # Current issue (OR delays)
│   └── templates/               # Issue creation templates
├── backlog/                     # 50+ healthcare use cases
├── resources/                   # Reusable assets and templates
│   ├── analysis_templates/      # Reusable analysis patterns
│   ├── toolkit_templates/       # SQL, Python, dashboard starters
│   └── data_sources/           # Common healthcare datasets guide
└── .github/                     # Automation and workflows
    ├── workflows/              # GitHub Actions
    └── ISSUE_TEMPLATE.md       # Issue templates
```

## Current Status

The project currently has:
- Word documents about OR delays in `Issues/1_OR_FirstStartDelay/`
- An implementation punch list (IMPLEMENTATION_PUNCHLIST.md) outlining the development phases
- This CLAUDE.md file

## Development Phases

### Phase 1: Foundation Setup (Week 1)
- Create repository structure
- Establish core templates
- Organize backlog of 50+ use cases

### Phase 2: Launch Issue Setup (Week 1-2)
- Create launch issue
- Convert existing OR delay Word documents to markdown
- Restructure content into 6-stage blueprint

### Phase 3: Content Pipeline Setup (Week 2-3)
- Create issue templates
- Set up resource library
- Build reusable analysis patterns

### Phase 4: Automation & Workflow (Week 3-4)
- GitHub Actions for publishing
- Quality assurance workflows
- Asset versioning system

### Phase 5: Content Creation Pipeline (Ongoing)
- Issue planning system
- Asset development process

## 6-Stage Analysis Blueprint

Each newsletter issue follows this structure:
1. **Frame the Pain** - Anchor stats and impact
2. **Surface the Signals** - Descriptive analysis
3. **Test the Levers** - Causal testing
4. **Size the Prize** - Impact sizing
5. **Monday Playbook** - Actionable steps
6. **Grab-and-Go Asset** - Ready-to-use toolkit

## Content Guidelines

- **Length**: 600-800 words per issue (coffee-break readable)
- **Format**: Markdown with supporting assets
- **Deliverables**: Analysis, toolkits (SQL scripts, dashboard templates), implementation guides
- **Complexity**: Scales from quick wins to deep dives based on problem complexity

## Technical Stack

- **Documentation**: Markdown
- **Version Control**: Git/GitHub
- **Automation**: GitHub Actions
- **Analysis Tools**: SQL templates, Python notebooks, dashboard starters
- **Asset Formats**: Markdown, SQL, Python, dashboard templates (Tableau/Power BI)

## Working with This Repository

1. **Converting Word Documents**: Use appropriate tools to convert .docx files to markdown
2. **Following Templates**: Use templates in `issues/templates/` for new content
3. **Asset Creation**: Place reusable assets in `resources/` directories
4. **Quality Checks**: Follow quality assurance checklists before publishing

## Key Tasks for Development

- Convert existing Word documents to markdown format
- Implement the 6-stage blueprint structure
- Create reusable templates and assets
- Set up automation workflows
- Build out the backlog of 50+ healthcare use cases

## Notes

- This project bridges healthcare operations and data analytics
- Target audience includes healthcare managers, executives, and clinical innovators
- Focus on practical, implementable solutions rather than theoretical approaches