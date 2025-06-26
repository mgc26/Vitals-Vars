# Analysis Templates

This directory contains reusable analysis templates for common healthcare operations problems.

## Available Templates

### Time-Based Analysis
- `delay_analysis_template.sql` - Generic delay analysis queries
- `throughput_analysis.py` - Patient flow calculations
- `capacity_utilization.R` - Resource utilization analysis

### Quality Analysis  
- `outcome_comparison.sql` - Pre/post intervention comparisons
- `variation_analysis.py` - Process variation detection
- `control_charts.R` - Statistical process control

### Financial Analysis
- `roi_calculator.xlsx` - ROI calculation template
- `cost_benefit_analysis.py` - Detailed cost modeling
- `sensitivity_analysis.R` - Multi-scenario testing

### Predictive Analysis
- `demand_forecasting.py` - Volume prediction models
- `risk_stratification.sql` - Patient risk scoring
- `staffing_prediction.R` - Workforce needs forecasting

## Usage Guidelines

1. Each template includes:
   - Purpose and use cases
   - Required data inputs
   - Customization instructions
   - Example outputs

2. Templates are designed to be:
   - Database agnostic (with notes on adjustments)
   - Minimally dependent on external libraries
   - Well-commented for learning

3. Start with simpler templates and progress to advanced as needed

## Contributing

To add a new template:
1. Follow naming convention: `analysis_type.extension`
2. Include comprehensive documentation
3. Add sample data if applicable
4. Test with at least 2 different datasets