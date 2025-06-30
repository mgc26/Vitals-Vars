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

## Project Mission

"Turning frontline headaches into data-backed fixes—every other Friday."

## Repository Structure (Current)

```
(28) Vitals&Vars/ (PRIVATE - Main Working Repository)
├── README.md                    # Newsletter overview
├── LICENSE                      # MIT license with healthcare addendum
├── issues/                      # Self-contained newsletter issues
│   ├── 00_launch/              # Launch announcement
│   ├── 01_or_first_start_delay/ # First-case OR delays
│   │   ├── README.md           # Full newsletter article
│   │   ├── linkedin_post.md    # Social media drafts
│   │   ├── notes.md            # Internal notes
│   │   ├── code/               # Development code
│   │   ├── assets/             # Visualizations
│   │   ├── references/         # Research materials
│   │   ├── _toolkit/           # PUBLIC: What gets published
│   │   │   ├── README.md       # Toolkit overview (not full article)
│   │   │   ├── sql/            # Production SQL queries
│   │   │   ├── python/         # Analysis scripts & data
│   │   │   ├── dashboards/     # BI templates
│   │   │   └── guides/         # Implementation guides
│   │   └── _meta.yaml          # Publishing configuration
│   └── templates/               # Template for new issues
├── _drafts/                     # GPT outputs, work in progress (git ignored)
├── backlog/                     # 50+ healthcare use cases
│   ├── use_cases.md            # Complete list of problems
│   ├── seasonal_planning.md    # Timing optimization
│   └── complexity_matrix.md    # Quick wins vs deep dives
├── resources/                   # Shared resources
│   ├── analysis_templates/      # Reusable analysis patterns
│   ├── toolkit_templates/       # Tool templates
│   ├── data_sources/           # Data access guide
│   └── linkedin_post_template.md # Social media templates
├── scripts/                     # Automation scripts
│   └── publish_toolkit.py       # Push toolkit to public repo
└── .github/                     # Automation
    ├── workflows/              # GitHub Actions
    └── ISSUE_TEMPLATE.md       # Issue submission template
```

### Public Repository Structure
```
vitals-vars-toolkits/ (PUBLIC - What Readers See)
├── README.md                    # Welcome & overview
├── 01_or_first_start_delay/     # Just the toolkit contents
│   ├── README.md               # Toolkit overview
│   ├── sql/                    # SQL queries
│   ├── python/                 # Scripts & data
│   ├── dashboards/             # BI templates
│   └── guides/                 # Implementation docs
└── 02_ed_boarding/             # Next toolkit...
```

## Current Status

The project has been fully structured with:
- Complete repository framework with self-contained issues
- Launch issue (00) and First-case OR delays issue (01) ready for publication
- 50+ healthcare use cases organized in backlog
- Templates and resources for creating future issues
- LinkedIn-friendly structure where each issue can be shared independently

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
- **Citations & References**: 
  - Never make up URLs or create fake links
  - Never falsely attribute quotes or studies
  - Use placeholder text like `[Citation needed]` or `[Add link]` when URL is unknown
  - Include author names and publication years when known, but don't invent publication details
  - Better to say "studies show" than to fabricate specific citations

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

### Publishing Toolkits

**Important**: Only the `_toolkit/` folder contents get published to the public repository.

To publish a toolkit:
```bash
cd scripts
python publish_toolkit.py 01_or_first_start_delay
```

This will:
- Copy only the `_toolkit/` folder contents
- Push to the public `vitals-vars-toolkits` repository
- Preserve the private repository's internal content

**What goes in _toolkit/**:
- Production-ready code and queries
- Implementation guides
- Dashboard templates
- Quick start documentation

**What stays private**:
- Full newsletter article (README.md)
- LinkedIn posts
- Internal notes
- Draft materials
- References and research

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