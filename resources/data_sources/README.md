# Healthcare Data Sources Guide

## Overview
This guide helps you identify and access data sources commonly needed for healthcare operations analysis.

## Internal Data Sources

### Electronic Health Records (EHR)
**Common Systems**: Epic, Cerner, Allscripts, Athena
**Typical Tables/Views**:
- Patient demographics
- Encounter/visit data
- Order details
- Results (lab, imaging)
- Medication administration
- Clinical documentation

**Access Tips**:
- Work with your analytics team
- Request read-only access to reporting database
- Use Clarity (Epic) or PowerChart (Cerner) for easier queries

### Operational Systems

#### OR Management
- OR scheduling systems (Epic OpTime, Cerner SurgiNet)
- Anesthesia information systems
- Instrument tracking systems

#### ED Systems  
- ED tracking boards
- Triage systems
- Patient flow/RTLS data

#### Bed Management
- Bed board/ADT systems
- Environmental services tracking
- Transport systems

### Financial Systems
- Patient accounting/billing
- Cost accounting
- Supply chain/materials management
- Payroll/timekeeping

### Quality/Safety Systems
- Incident reporting systems
- Infection control databases
- Patient satisfaction surveys
- Regulatory reporting systems

## External Data Sources

### Public Datasets
1. **CMS Data**
   - Hospital Compare
   - Provider utilization files
   - Cost reports
   - Quality measures

2. **HCUP Databases**
   - National Inpatient Sample (NIS)
   - State Emergency Department Databases (SEDD)
   - State Inpatient Databases (SID)

3. **CDC Resources**
   - NHSN (infection data)
   - NCHS (health statistics)
   - WISQARS (injury data)

### Benchmarking Sources
- Vizient Clinical Database
- Premier QualityAdvisor
- Press Ganey benchmarks
- MGMA productivity data
- Sullivan Cotter compensation data

### Real-Time Data Feeds
- HL7 interfaces
- FHIR APIs
- ADT feeds
- Results feeds

## Data Access Checklist

### Before Requesting Access
- [ ] Define specific use case
- [ ] Identify minimum data elements needed
- [ ] Determine time range required
- [ ] Check if aggregate data sufficient
- [ ] Review privacy/security requirements

### Access Request Should Include
- [ ] Business justification
- [ ] Data elements needed
- [ ] Frequency of access
- [ ] Storage/security plan
- [ ] IRB approval (if needed)

## Common Data Challenges

### Data Quality Issues
- Missing timestamps
- Inconsistent coding
- Duplicate records
- Free-text fields

### Integration Challenges
- Different patient identifiers
- Timing mismatches
- System boundaries
- Historical changes

## SQL Query Patterns

### Join Patterns
```sql
-- EHR to Financial
FROM encounters e
LEFT JOIN billing b ON e.encounter_id = b.encounter_id

-- Multiple timestamp sources
FROM or_cases o
LEFT JOIN anesthesia_events a ON o.case_id = a.case_id
LEFT JOIN nursing_documentation n ON o.case_id = n.case_id
```

### Time Calculations
```sql
-- Business hours only
CASE 
  WHEN DAYOFWEEK(date) IN (1,7) THEN 0
  ELSE TIMESTAMPDIFF(MINUTE, start_time, end_time)
END

-- Shift-based analysis
CASE
  WHEN HOUR(event_time) BETWEEN 7 AND 14 THEN 'Day'
  WHEN HOUR(event_time) BETWEEN 15 AND 22 THEN 'Evening'
  ELSE 'Night'
END
```

## Privacy & Security

### PHI Handling
- Always use minimum necessary principle
- De-identify when possible
- Aggregate to safe harbor levels
- Follow organizational policies

### Best Practices
- Use secure connections
- Don't store PHI locally
- Clear audit trail
- Regular access reviews

## Getting Started

1. **Identify your question** - Be specific
2. **Map to data sources** - Use this guide
3. **Request access** - Follow org process
4. **Validate data** - Check reasonableness
5. **Document sources** - For reproducibility