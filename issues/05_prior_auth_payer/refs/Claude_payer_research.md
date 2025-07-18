# The business of prior authorization: Why payers persist, what it costs, and where AI is taking us

## Executive Summary

U.S. health plans invest $1.3 billion annually in prior authorization (PA) programs that return $8.30 for every dollar spent on program integrity, with individual payers like CVS saving $660 million in a single year. Manual PA transactions cost payers $14.49 each, while AI-powered automation drops this to $0.05—a 98% reduction. The industry processes 280 million PA requests annually, with denial rates averaging 6.4% for Medicare Advantage, though 81.7% of appeals succeed. By 2027, CMS mandates will force electronic PA adoption projected to save $15 billion over 10 years. Major payers are racing to implement AI solutions: UnitedHealth's OptumRx PreCheck covers 25+ drug classes, while competitors report 1,400x faster processing speeds. The endgame? Real-time, API-driven approvals for 80% of requests by 2027, fundamentally reshaping the $1.3 billion PA industry.

## 1. Payer-side economics: The math behind the persistence

### Cost per transaction drives automation urgency

The fully loaded cost structure reveals why payers are rushing toward automation. Manual PA transactions cost the industry $14.49 per request (2023 CAQH Index), with payers bearing $3.52 and providers $10.97. Portal-based semi-automation cuts this to $8.09, while fully electronic processes achieve $5.84 per transaction. The holy grail—AI-powered full automation—achieves remarkable efficiency at $0.05 per transaction, representing a 98% cost reduction.

These economics become stark at scale. The industry processes 280 million PA transactions annually, creating a $1.3 billion market. Full electronic adoption could save $515 million annually, explaining the aggressive technology investments across major payers. **UnitedHealth reported a $340 million impact** from the Change Healthcare cyberattack disrupting care management activities, underscoring both the criticality and vulnerability of PA infrastructure.

### Medical Loss Ratio pressures intensify focus

Prior authorization directly impacts MLR calculations, with administrative expense ratios increasing 0.3% at UnitedHealthcare to 1.4% at Cigna due to PA burden. This seemingly small percentage represents hundreds of millions in costs for large payers. CVS Health's MLR climbed to 92.1% in 2024 from 86.2% in 2023, partly attributed to utilization management challenges.

The deny-vs-automate decision matrix reveals sophisticated risk scoring. **EviCore's "The Dial" algorithm** assigns approval probabilities (75% vs 95%), with payers adjusting thresholds to optimize denial rates. Arkansas data shows 20% denial rates versus the 7% Medicare Advantage average, demonstrating how algorithm tuning impacts financial outcomes. Auto-approve thresholds typically sit at 90%+ probability, auto-deny below 20%, with human review for the 20-90% range.

### False positive economics create hidden costs

The financial exposure from inappropriate denials proves substantial. Each denied claim costs providers $43.84 to appeal, contributing to $19.7 billion in annual appeal spending industry-wide. With 54.3% of denials ultimately overturned, false positives create massive inefficiency. **Revenue at risk reaches 12% of hospital income** due to denied claims, while 78% of patients may abandon treatment entirely due to PA barriers.

Conversely, false negatives (inappropriate approvals) directly impact MLR. Industry estimates suggest PA prevents $3 in inappropriate spending for every $1 invested, explaining payer commitment despite provider frustration. The challenge lies in calibrating systems to minimize both error types while maintaining efficiency.

## 2. Internal utilization management workflows: The human-technology interface

### Organizational structure reflects complexity

UM departments typically employ 1-2 FTEs per 10,000 members in sophisticated hierarchical structures. The workforce comprises 40-50% clinical nurses processing 15-25 cases daily, 10-15% physician advisors handling 8-12 complex cases, and 35-45% administrative staff. **Large health plans process 100,000-500,000 PAs annually**, with Medicare Advantage alone generating 50 million determinations in 2023.

The standard workflow spans four phases consuming 2-7 business days: intake and screening (1-2 hours), clinical review (6-24 hours), decision-making (12-48 hours), and potential appeals. Auto-adjudication achieves 20-35% approval rates for straightforward cases, while complex determinations require physician review and peer-to-peer consultation.

### Technology pain points persist despite modernization

Remarkably, 70% of PA submissions still arrive via fax, creating massive inefficiency. Only 28% of medical PAs process electronically via X12-278 standards. Manual chart review, duplicate data entry across systems, and fragmented vendor ecosystems compound the challenge. **Processing time averages 18.7 hours manually versus 5.7 hours electronically**—a 69% reduction driving automation investments.

Integration gaps between payer systems and provider EHRs force redundant work. Limited API adoption, inconsistent data formats, and legacy system constraints create bottlenecks. The 2024 CMS Interoperability Rule mandates FHIR-based APIs by 2027, forcing overdue standardization.

### AI transforms workflow efficiency

Natural language processing now extracts clinical data from unstructured documents, reducing manual processing costs by 50%. Intelligent routing directs requests to appropriate reviewers based on complexity and expertise. **Predictive analytics enable 20-35% auto-adjudication rates**, while quality assurance algorithms monitor compliance automatically.

Generative AI applications emerging in 2024-2025 include automated PA form generation from EHR data, clinical summary creation, and decision letter composition. Advanced pattern recognition identifies inappropriate utilization patterns, while predictive modeling forecasts authorization outcomes. Organizations report 50-75% automation of manual tasks, 55% processing time reduction, and 25% fewer regulatory-related denials.

## 3. Clinical guideline lifecycle: The evidence engine

### Duopoly dynamics shape the market

InterQual (owned by UnitedHealth's Optum) and MCG Health (Hearst Corporation) dominate clinical criteria licensing. Health plans face strategic decisions: Highmark, Anthem, and Horizons BCBS use MCG for its user-friendliness, while Wellcare and some Centene markets prefer InterQual's comprehensive criteria. **Single guideline development costs $200,000+**, with annual updates and continuous evidence review required.

Governance structures ensure clinical credibility through utilization management committees, medical policy assessment panels, and external review by board-certified specialists. NCCN's cancer guidelines limit panel members to $20,000 from single entities and $50,000 aggregate, ensuring independence. Transparency initiatives include searchable clinical policy websites and external submission processes for guideline modifications.

### Technology struggles with scale

The challenge of maintaining criteria for thousands of CPT/HCPCS codes across 50+ benefit designs proves formidable. Commercial, Medicare, and Medicaid populations require different approaches, while state-specific mandates add complexity. **Epic Payer Platform achieves 53% instant PA completion** at Ochsner/Humana through clinical data exchange, demonstrating integration potential.

Business process management engines model clinical pathways using BPMN notation. Decision trees branch through complex scenarios, while knowledge graphs integrate structured content. Yet these rule-based systems remain brittle and expensive to maintain. LLM-interactive decision trees and if-elif-else structures enable AI interpretation, pointing toward more flexible futures.

### AI revolutionizes guideline management

Natural language processing ingests clinical literature for automated evidence review, while machine learning identifies patterns requiring guideline updates. **99% of healthcare organizations report using GenAI applications** as of 2024, with 87.6% leveraging AI for knowledge access and filtering. Oracle Clinical AI reduces documentation time by 30%, while Microsoft's DAX Copilot saves 5 minutes per patient encounter.

The future points toward AI-generated treatment recommendations based on continuously updated guidelines, automated authorization reviews against dynamic criteria, and real-time evidence synthesis. The challenge lies in maintaining clinical accuracy while achieving the scale necessary for millions of authorization decisions.

## 4. Fraud, waste, and abuse controls: The financial firewall

### Quantified impact justifies investment

CMS program integrity activities saved $14.9 billion in 2023, achieving an **$8.30 return for every dollar spent**. Prior authorization specifically prevented $660 million in inappropriate payments for CVS's Medicare Advantage business in 2018 through denied post-acute facility admissions. The broader healthcare fraud landscape saw $2.9 billion in False Claims Act recoveries in 2024, with healthcare representing 50-70% of total recoveries.

High-risk service categories drawing PA scrutiny include post-acute care (UnitedHealth and CVS deny at 3x overall rates), specialty medications (Express Scripts targets prior authorization fraud), wound care ($14.3 million fraudulent billing uncovered), and genetic testing (15-40% coded inaccurately). **Humana's post-acute denial rate runs 16x higher** than their overall rate, demonstrating targeted controls.

### PA effectiveness versus other controls

Comparing fraud prevention tools reveals PA's unique position. The CMS Fraud Prevention System saved $1.5 billion since launch, though OIG certified only $133 million in adjusted savings. Prepayment edits denied 324,000 claims saving $20.4 million in FY2016—immediate but limited scope. Prior authorization provides proactive clinical review but remains resource-intensive, while retrospective audits offer comprehensive analysis after payment.

The calculus favors PA for high-risk, high-cost services where clinical judgment adds value. Low-complexity, high-volume services benefit more from automated edits. **AI fraud detection markets project $31.69 billion by 2029** (19.3% CAGR), with healthcare organizations reporting $2.4 million average ROI from medical AI implementations.

### Residual leakage highlights imperfection

Despite controls, significant inappropriate payments persist. OIG found $7.5 billion in questionable Medicare Advantage risk-adjusted payments from health risk assessments in 2024. Troublingly, 13% of denied PA requests actually met Medicare coverage rules, while 18% of payment denials were inappropriate. With only 11.7% of denials appealed despite an 81.7% overturn rate, access barriers may exceed fraud prevention benefits for some services.

## 5. Payer-provider collaboration models: The path forward

### FHIR APIs enable real-time transformation

The Regence-MultiCare pilot demonstrates FHIR's transformative potential, reducing patient wait times from 15 days to near real-time decisions. By eliminating fax-based workflows and 150-page manual submissions, the collaboration earned a 2023 KLAS Points of Light award. **HL7 FHIR standards enable coverage requirements discovery**, documentation templates, and end-to-end prior authorization support within EHR workflows.

Success required three cross-functional teams meeting weekly, significant technology investment, and fundamental process redesign. The payoff: eliminated manual data entry, reduced staffing requirements, and prevented care delays that could cause adverse events.

### Gold-carding recognizes provider performance

UnitedHealth's October 2024 national gold card program sets the industry standard: providers achieving 92% approval rates over two consecutive years with 10+ annual requests earn exemption from documentation requirements. Following their 2023 elimination of 20% of prior authorizations, this program covers commercial, exchange, Medicare Advantage, and Medicaid populations. **Less than 2% of members experience PA denials annually**, with 99%+ experiencing no delays or quick approvals.

Highmark's program demonstrates impressive scale, growing from 400 providers in 2022 to 21,000+ gold-carded providers by September 2024. These clinicians processed 400,000+ authorizations in 12 months with 85% time reduction. Multi-modal coverage allows 50%+ of providers exemption for multiple service types, while an active coaching pathway helps borderline performers improve. **Processing time drops to under 3 minutes** for prenotification and approval.

### Strategic PA elimination gains momentum

Cigna's August 2023 announcement to remove 600+ codes representing 25% of PA requirements built on 1,100+ codes eliminated since 2020. With PA requirements dropping to less than 4% of medical services, the insurer demonstrates competitive advantage through reduced friction. **Electronic submission achieves 70% faster turnaround** (18.7 to 5.7 hours), while manual PA costs average $11 versus $2-4 electronically.

These initiatives respond directly to provider feedback while maintaining cost controls through value-based care integration. With 98% of programs using peer-reviewed evidence and 90%+ reporting positive quality impact, strategic elimination proves sustainable when coupled with alternative controls.

### AI acceleration promises radical efficiency

Large insurers report **1,400x faster processing** through AI automation, with 10-day reductions in decision timeframes. Clear-cut medical necessity cases achieve auto-approval without human intervention, dramatically scaling capacity. However, some AI tools show 16x higher denial rates, necessitating oversight.

The regulatory framework evolves rapidly, with CMS requiring AI to assist but not override medical necessity standards. Multiple states implement AI oversight requirements, mandating transparency in automated decision-making. Human review remains essential for complex cases and appeals, with AI augmenting rather than replacing clinical judgment.

## Looking ahead: The 2025-2027 transformation

The prior authorization landscape faces unprecedented change. CMS mandates effective 2026-2027 require 72-hour urgent and 7-day standard response times, FHIR-based APIs, public metric reporting, and patient-facing status systems. Eight states have enacted gold-carding legislation with federal bills pending, while industry commitments cover 257 million lives pledging 80% real-time decisions by 2027.

Technology investments accelerate as payers race to comply. Enterprise API development, staff retraining, and compliance monitoring create significant costs. Yet the payoff appears substantial: $15 billion in projected savings over 10 years, dramatically reduced administrative burden, and improved patient access.

Success requires balancing competing imperatives. Payers must maintain program integrity while reducing friction, invest in technology while controlling costs, and satisfy regulators while serving members. Organizations excelling at this balance—through AI automation, strategic collaboration, and evidence-based reform—will define healthcare's administrative future.

**The bottom line:** Prior authorization isn't disappearing—it's evolving from manual friction to intelligent automation. Payers investing now in FHIR APIs, AI capabilities, and provider partnerships position themselves for a market where real-time, transparent authorization becomes table stakes. Those clinging to fax machines and manual review face obsolescence as surely as Blockbuster faced Netflix.


References
ADVOCATE Radiology & Billing. (n.d.). CAQH index shows mixed trends in electronic transaction adoption. https://advocatercm.com/caqh-index-shows-mixed-trends-in-electronic-transaction-adoption/
American College of Physicians. (n.d.). Toolkit: Addressing the administrative burden of prior authorization. https://www.acponline.org/advocacy/state-health-policy/toolkit-addressing-the-administrative-burden-of-prior-authorization
American Hospital Association. (2024, October 17). Senate report scrutinizes Medicare Advantage prior authorization denials for post-acute care services. https://www.aha.org/news/headline/2024-10-17-senate-report-scrutinizes-medicare-advantage-prior-authorization-denials-post-acute-care-services
American Hospital Association. (2024, September 20). Increasing administrative costs, burdensome commercial insurer practices create patient care challenges. https://www.aha.org/news/perspective/2024-09-20-increasing-administrative-costs-burdensome-commercial-insurer-practices-create-patient-care
American Hospital Association. (2025, April 28). 2024 costs of caring. https://www.aha.org/guidesreports/2025-04-28-2024-costs-caring
American Medical Association. (n.d.). Fixing prior auth: Nearly 40 prior authorizations a week is way too many. https://www.ama-assn.org/practice-management/prior-authorization/fixing-prior-auth-nearly-40-prior-authorizations-week-way
American Medical Association. (n.d.). Prior authorization delays care—and increases health care costs. https://www.ama-assn.org/practice-management/prior-authorization/prior-authorization-delays-care-and-increases-health-care
American Society of Clinical Oncology. (n.d.). Guidelines, tools, & resources. https://society.asco.org/practice-patients/guidelines
Axis Intelligence. (n.d.). Healthcare AI implementation: $2.4M ROI blueprint for medical organizations in 2025. https://axis-intelligence.com/healthcare-ai-implementation-ai-health-2025/
Business process model and notation and openEHR task planning for clinical pathway standards in infections: Critical analysis. (2022). NCBI. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9523526/
CAQH. (2022). 2022 CAQH index: Health plans and providers can save nearly $25 billion annually by automating administrative transactions. https://www.caqh.org/blog/2022-caqh-index-health-plans-and-providers-can-save-nearly-25-billion-annually-automating
CAQH. (n.d.). New CAQH report reveals significant differences in administrative costs. https://www.caqh.org/news/new-caqh-report-reveals-significant-differences-in-administrative-costs
CAQH. (n.d.). Prior authorization. https://www.caqh.org/core/prior-authorization
CAQH. (n.d.). The CAQH index report. https://www.caqh.org/insights/caqh-index-report
Center for Medicare Advocacy. (n.d.). Office of Inspector General (OIG) issues another report highlighting inappropriate Medicare Advantage denials. https://medicareadvocacy.org/office-of-inspector-general-oig-issues-another-report-highlighting-inappropriate-medicare-advantage-denials/
Centers for Medicare & Medicaid Services. (2024). CMS finalizes rule to expand access to health information and improve the prior authorization process. https://www.cms.gov/newsroom/press-releases/cms-finalizes-rule-expand-access-health-information-and-improve-prior-authorization-process
Centers for Medicare & Medicaid Services. (n.d.). CMS interoperability and prior authorization final rule (CMS-0057-F). https://www.cms.gov/priorities/burden-reduction/overview/interoperability/policies-and-regulations/cms-interoperability-and-prior-authorization-final-rule-cms-0057-f/cms-interoperability-and-prior-authorization-final-rule-cms-0057-f
Centers for Medicare & Medicaid Services. (n.d.). Prior authorization for certain hospital outpatient department (OPD) services. https://www.cms.gov/data-research/monitoring-programs/medicare-fee-service-compliance-programs/prior-authorization-and-pre-claim-review-initiatives/prior-authorization-certain-hospital-outpatient-department-opd-services
2024 CAQH index foresees major opportunity for health care savings. (2024). The American Journal of Managed Care. https://www.ajmc.com/view/2024-caqh-index-foresees-major-opportunity-for-health-care-savings
The extent and growth of prior authorization in Medicare Advantage. (n.d.). The American Journal of Managed Care. https://www.ajmc.com/view/the-extent-and-growth-of-prior-authorization-in-medicare-advantage
Epic. (n.d.). Epic payer platform support & staffing: EPP implementation experts. Healthcare Tech Resources Inc. https://healthtechresourcesinc.com/epic-payer-platform
Fierce Healthcare. (n.d.). Editor's corner: CMS probably didn't save $42B through fraud prevention. https://www.fiercehealthcare.com/antifraud/editor-s-corner-cms-probably-didn-t-save-42-billion-fraud-prevention
Fierce Healthcare. (n.d.). UnitedHealth institutes gold card program to address prior authorization concerns. https://www.fiercehealthcare.com/payers/unitedhealth-institutes-gold-card-program-address-prior-authorization-concerns
Healthcare Dive. (2023). Cigna removes prior authorizations for 25% of services. https://www.healthcaredive.com/news/cigna-prior-authorization-rollback/691729/
Healthcare Finance News. (n.d.). Aetna's high medical costs hammer CVS earnings. https://www.healthcarefinancenews.com/news/aetnas-high-medical-losses-hammer-cvs-earnings
Highmark Health. (n.d.). Simplifying prior authorization with active gold carding and other innovations. https://www.highmarkhealth.org/blog/future/Simplifying-Prior-Authorization-with-Active-Gold-Carding-and-Other-Innovations.shtml
Holland & Knight. (2024, October). Regulation of AI in healthcare utilization management and prior authorization increases. https://www.hklaw.com/en/insights/publications/2024/10/regulation-of-ai-in-healthcare-utilization-management
How to leverage AI-enabled automation to solve biggest challenges in prior authorization. (n.d.). Productive Edge. https://www.productiveedge.com/blog/ai-enabled-automation-to-solve-biggest-challenges-in-prior-authorization
KFF. (2024). Medicare Advantage in 2024: Premiums, out-of-pocket limits, supplemental benefits, and prior authorization. https://www.kff.org/medicare/issue-brief/medicare-advantage-in-2024-premiums-out-of-pocket-limits-supplemental-benefits-and-prior-authorization/
KFF. (2024). Medicare Advantage insurers made nearly 50 million prior authorization determinations in 2023. https://www.kff.org/medicare/issue-brief/nearly-50-million-prior-authorization-requests-were-sent-to-medicare-advantage-insurers-in-2023/
KFF. (n.d.). Medicare program integrity and efforts to root out improper payments, fraud, waste and abuse. https://www.kff.org/medicare/issue-brief/medicare-program-integrity-and-efforts-to-root-out-improper-payments-fraud-waste-and-abuse/
MCG Health. (n.d.). KLAS case study: Prior authorization automation. https://www.mcg.com/klas-prior-authorization-automation/
MedCity News. (2023, August). Cigna cuts 25% of medical services from prior authorization requirements. https://medcitynews.com/2023/08/cigna-prior-authorization-requirements/
Medical Economics. (n.d.). Prior authorization: How it evolved, why it burdens physicians and patients, and the promise of AI. https://www.medicaleconomics.com/view/prior-authorization-history-burden-ai-future
Morgan Lewis. (2025, January). DOJ announces over $2.9 billion in False Claims Act recoveries in fiscal year 2024. https://www.morganlewis.com/pubs/2025/01/doj-announces-over-2-9-billion-in-false-claims-act-recoveries-in-fiscal-year-2024
National Law Review. (n.d.). Departments announce 2025 national health care fraud takedown. https://natlawreview.com/article/first-national-health-care-fraud-takedown-second-trump-administration-what-stayed
Pharmacy Healthcare Solutions LLC. (n.d.). Gold carding – A new approach to improving prior authorizations. https://phslrx.com/gold-carding-a-new-approach-to-improving-prior-authorizations/
Rise Health. (n.d.). Medicare Advantage prior authorization investigation: Senate report uncovers scope of denials among largest insurers. https://www.risehealth.org/insights-articles/medicare-advantage-prior-authorization-investigation-senate-report-uncovers-scope-of-denials-among-largest-insurers/
TechTarget. (2024). Healthcare administrative spending increased by 50%. https://www.techtarget.com/revcyclemanagement/news/366600214/Healthcare-Administrative-Spending-Increased-by-50
TechTarget. (n.d.). 5 use cases for generative AI in healthcare documentation. https://www.techtarget.com/searchhealthit/feature/Use-cases-for-generative-AI-in-healthcare-documentation
TechTarget. (n.d.). Pros and cons of prior authorization for value-based contracting. https://www.techtarget.com/healthcarepayers/news/366604489/Pros-and-Cons-of-Prior-Authorization-for-Value-Based-Contracting
UnitedHealth Group. (2024, October 22). Optum Rx automates prior authorization process for prescription drugs to improve the patient and provider experience. https://www.unitedhealthgroup.com/newsroom/posts/2024/2024-10-22-optumrx-prior-authorization-process-to-improve.html
UnitedHealthcare. (n.d.). How the UnitedHealthcare Gold Card program helps modernize prior authorization. https://www.uhc.com/news-articles/newsroom/gold-card
U.S. Department of Health and Human Services. (2024). Medicare Advantage: Questionable use of health risk assessments continues to drive up payments to plans by billions. Office of Inspector General. https://oig.hhs.gov/reports/all/2024/medicare-advantage-questionable-use-of-health-risk-assessments-continues-to-drive-up-payments-to-plans-by-billions/
U.S. Department of Health and Human Services. (n.d.). HHS Secretary Kennedy, CMS Administrator Oz secure industry pledge to fix broken prior authorization system. https://www.hhs.gov/press-room/kennedy-oz-cms-secure-healthcare-industry-pledge-to-fix-prior-authorization-system.html
U.S. Department of Justice. (2024). False Claims Act settlements and judgments exceed $2.9B in fiscal year 2024. https://www.justice.gov/archives/opa/pr/false-claims-act-settlements-and-judgments-exceed-29b-fiscal-year-2024
U.S. Government Accountability Office. (2017). Medicare: CMS fraud prevention system uses claims analysis to address fraud (GAO-17-710). https://www.gao.gov/products/gao-17-710