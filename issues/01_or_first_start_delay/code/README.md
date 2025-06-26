# OR Delay Analysis Code

This directory contains all the code and data needed to analyze first-case OR delays at your hospital.

## Directory Structure

```
code/
├── data/           # Sample datasets
├── notebooks/      # Jupyter notebooks for interactive analysis
├── scripts/        # Python scripts for automated analysis
└── sql/           # SQL queries for data extraction
```

## Quick Start

### Option 1: Use Jupyter Notebook (Recommended for exploration)
```bash
cd notebooks/
jupyter notebook or_delay_analysis.ipynb
```

### Option 2: Run Python Script (Recommended for automation)
```bash
cd scripts/
python analyze_delays.py --input ../data/sample_or_delays.csv --output results/
```

### Option 3: Use SQL Queries
Copy queries from `sql/delay_tracking_queries.sql` and run on your OR system

## Data Requirements

Your data should include these columns:
- `case_id`: Unique identifier
- `surgery_date`: Date of surgery
- `or_room`: Operating room identifier
- `scheduled_start`: Scheduled start time
- `actual_start`: Actual start time
- `delay_minutes`: Calculated delay in minutes
- `delay_reason`: Root cause of delay (if tracked)
- `surgeon_id`: Surgeon identifier
- `procedure_type`: Type of procedure
- `case_duration_min`: Case duration in minutes

## Outputs

The analysis generates:
1. **Statistical Summary**: Average delays, on-time rates
2. **Root Cause Analysis**: What's causing delays
3. **Pattern Analysis**: Day-of-week and room variations
4. **Financial Impact**: Cost of delays in dollars
5. **Visualizations**: Charts for presentations
6. **Recommendations**: Prioritized action items

## Customization

### Adjusting Financial Calculations
Edit the `or_cost_per_min` parameter (default: $100/minute):
```python
python analyze_delays.py --or-cost 150
```

### Adding Your Hospital's Data
1. Export your OR data to CSV format
2. Ensure column names match the template
3. Run the analysis on your data:
```python
python analyze_delays.py --input your_hospital_data.csv
```

## Requirements

- Python 3.7+
- pandas
- numpy  
- matplotlib
- seaborn
- jupyter (for notebooks)

Install all requirements:
```bash
pip install -r requirements.txt
```