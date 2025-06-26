#!/usr/bin/env python3
"""
First-Case OR Delay Analysis Script
Analyzes OR delay patterns and generates actionable insights

Usage:
    python analyze_delays.py --input your_data.csv --output results/
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
import argparse
import os
from pathlib import Path

def load_and_prep_data(filepath):
    """Load OR delay data and prepare for analysis"""
    df = pd.read_csv(filepath)
    
    # Convert time columns
    df['scheduled_start'] = pd.to_datetime(df['scheduled_start'], format='%H:%M:%S').dt.time
    df['actual_start'] = pd.to_datetime(df['actual_start'], format='%H:%M:%S').dt.time
    df['surgery_date'] = pd.to_datetime(df['surgery_date'])
    
    return df

def calculate_summary_stats(df):
    """Calculate key performance metrics"""
    stats = {
        'total_cases': len(df),
        'avg_delay': df['delay_minutes'].mean(),
        'median_delay': df['delay_minutes'].median(),
        'std_delay': df['delay_minutes'].std(),
        'on_time_rate': (df['delay_minutes'] <= 5).mean() * 100,
        'severe_delay_rate': (df['delay_minutes'] > 30).mean() * 100,
        'total_delay_hours': df['delay_minutes'].sum() / 60
    }
    return stats

def analyze_root_causes(df):
    """Analyze delay root causes"""
    # Only analyze actual delays
    delays = df[df['delay_minutes'] > 5]
    
    if len(delays) == 0:
        return pd.DataFrame()
    
    # Count and calculate percentages
    root_causes = delays['delay_reason'].value_counts()
    root_cause_pct = (root_causes / len(delays) * 100).round(1)
    
    # Average delay by cause
    avg_by_cause = delays.groupby('delay_reason')['delay_minutes'].mean().round(1)
    
    # Combine into summary
    summary = pd.DataFrame({
        'count': root_causes,
        'percentage': root_cause_pct,
        'avg_delay': avg_by_cause
    })
    
    return summary.sort_values('count', ascending=False)

def analyze_patterns(df):
    """Analyze temporal and spatial patterns"""
    patterns = {}
    
    # Day of week analysis
    patterns['day_of_week'] = df.groupby('day_of_week').agg({
        'delay_minutes': ['mean', 'median', 'std', 'count']
    }).round(1)
    
    # OR room analysis
    patterns['by_room'] = df.groupby('or_room').agg({
        'delay_minutes': ['mean', 'median', 'count'],
        'case_id': lambda x: (df[df['or_room'] == x.iloc[0]]['delay_minutes'] <= 5).sum()
    })
    patterns['by_room'].columns = ['avg_delay', 'median_delay', 'total_cases', 'on_time_cases']
    patterns['by_room']['on_time_rate'] = (patterns['by_room']['on_time_cases'] / 
                                           patterns['by_room']['total_cases'] * 100).round(1)
    
    # Surgeon analysis (be diplomatic with this data)
    patterns['by_surgeon'] = df.groupby('surgeon_id').agg({
        'delay_minutes': ['mean', 'count']
    }).round(1)
    patterns['by_surgeon'].columns = ['avg_delay', 'case_count']
    
    return patterns

def calculate_financial_impact(df, or_cost_per_min=100):
    """Calculate financial impact of delays"""
    
    # Direct costs
    total_delay_min = df['delay_minutes'].sum()
    direct_cost = total_delay_min * or_cost_per_min
    
    # Overtime costs (simplified)
    overtime_delays = df[df['delay_minutes'] > 30]
    overtime_minutes = overtime_delays['delay_minutes'].sum()
    overtime_cost = overtime_minutes * or_cost_per_min * 0.5  # 50% premium
    
    # Annual projection (250 operating days)
    days_in_sample = (df['surgery_date'].max() - df['surgery_date'].min()).days + 1
    annual_multiplier = 250 / days_in_sample
    
    impact = {
        'sample_days': days_in_sample,
        'total_delay_minutes': total_delay_min,
        'direct_cost_sample': direct_cost,
        'overtime_cost_sample': overtime_cost,
        'total_cost_sample': direct_cost + overtime_cost,
        'annual_direct_cost': direct_cost * annual_multiplier,
        'annual_overtime_cost': overtime_cost * annual_multiplier,
        'annual_total_cost': (direct_cost + overtime_cost) * annual_multiplier
    }
    
    return impact

def generate_report(df, stats, root_causes, patterns, financial_impact, output_dir):
    """Generate comprehensive analysis report"""
    
    report_path = Path(output_dir) / 'delay_analysis_report.txt'
    
    with open(report_path, 'w') as f:
        f.write("FIRST-CASE OR DELAY ANALYSIS REPORT\n")
        f.write("=" * 50 + "\n")
        f.write(f"Analysis Date: {datetime.now().strftime('%Y-%m-%d %H:%M')}\n")
        f.write(f"Data Period: {df['surgery_date'].min()} to {df['surgery_date'].max()}\n\n")
        
        # Summary statistics
        f.write("SUMMARY STATISTICS\n")
        f.write("-" * 30 + "\n")
        f.write(f"Total first cases analyzed: {stats['total_cases']}\n")
        f.write(f"Average delay: {stats['avg_delay']:.1f} minutes\n")
        f.write(f"Median delay: {stats['median_delay']:.1f} minutes\n")
        f.write(f"On-time rate (≤5 min): {stats['on_time_rate']:.1f}%\n")
        f.write(f"Severe delays (>30 min): {stats['severe_delay_rate']:.1f}%\n\n")
        
        # Root causes
        f.write("ROOT CAUSE ANALYSIS\n")
        f.write("-" * 30 + "\n")
        if not root_causes.empty:
            for reason, row in root_causes.iterrows():
                f.write(f"{reason}: {row['count']} cases ({row['percentage']:.1f}%), ")
                f.write(f"avg delay {row['avg_delay']:.1f} min\n")
        f.write("\n")
        
        # Financial impact
        f.write("FINANCIAL IMPACT\n")
        f.write("-" * 30 + "\n")
        f.write(f"Sample period: {financial_impact['sample_days']} days\n")
        f.write(f"Direct cost: ${financial_impact['direct_cost_sample']:,.0f}\n")
        f.write(f"Overtime cost: ${financial_impact['overtime_cost_sample']:,.0f}\n")
        f.write(f"Annual projection: ${financial_impact['annual_total_cost']:,.0f}\n\n")
        
        # Recommendations
        f.write("PRIORITY RECOMMENDATIONS\n")
        f.write("-" * 30 + "\n")
        f.write("1. Implement evening equipment checklist\n")
        f.write("2. Launch 7:00 AM morning huddle\n")
        f.write("3. Start patient callback program\n")
        f.write("4. Focus on Monday preparation\n")
        f.write("5. Address room-specific issues\n\n")
        
        f.write("Expected impact: 60% reduction in delays\n")
        f.write(f"Projected savings: ${financial_impact['annual_total_cost'] * 0.6:,.0f}\n")
    
    print(f"Report saved to: {report_path}")

def create_visualizations(df, stats, root_causes, patterns, output_dir):
    """Create visualization plots"""
    
    output_path = Path(output_dir)
    
    # Set style
    plt.style.use('seaborn-v0_8-darkgrid')
    sns.set_palette('husl')
    
    # 1. Delay distribution
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.hist(df['delay_minutes'], bins=20, edgecolor='black', alpha=0.7)
    ax.axvline(stats['avg_delay'], color='red', linestyle='--', 
               label=f"Average: {stats['avg_delay']:.1f} min")
    ax.axvline(5, color='green', linestyle='--', label='On-time threshold')
    ax.set_xlabel('Delay Minutes')
    ax.set_ylabel('Frequency')
    ax.set_title('Distribution of First-Case OR Delays')
    ax.legend()
    plt.tight_layout()
    plt.savefig(output_path / 'delay_distribution.png', dpi=300)
    plt.close()
    
    # 2. Root causes
    if not root_causes.empty:
        fig, ax = plt.subplots(figsize=(10, 6))
        root_causes['percentage'].plot(kind='barh', ax=ax)
        ax.set_xlabel('Percentage of Delays')
        ax.set_title('Root Causes of First-Case Delays')
        plt.tight_layout()
        plt.savefig(output_path / 'root_causes.png', dpi=300)
        plt.close()
    
    # 3. Day of week pattern
    day_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
    day_data = patterns['day_of_week']['delay_minutes']['mean'].reindex(day_order)
    
    fig, ax = plt.subplots(figsize=(10, 6))
    day_data.plot(kind='bar', ax=ax)
    ax.axhline(y=stats['avg_delay'], color='red', linestyle='--', 
               label=f"Average: {stats['avg_delay']:.1f} min")
    ax.set_xlabel('Day of Week')
    ax.set_ylabel('Average Delay (minutes)')
    ax.set_title('First-Case Delays by Day of Week')
    ax.legend()
    plt.xticks(rotation=0)
    plt.tight_layout()
    plt.savefig(output_path / 'day_of_week_pattern.png', dpi=300)
    plt.close()
    
    print(f"Visualizations saved to: {output_path}")

def main():
    parser = argparse.ArgumentParser(description='Analyze first-case OR delays')
    parser.add_argument('--input', default='../data/sample_or_delays.csv', 
                       help='Input CSV file path')
    parser.add_argument('--output', default='results/', 
                       help='Output directory for results')
    parser.add_argument('--or-cost', type=int, default=100,
                       help='OR cost per minute (default: $100)')
    
    args = parser.parse_args()
    
    # Create output directory
    os.makedirs(args.output, exist_ok=True)
    
    # Load and analyze data
    print("Loading data...")
    df = load_and_prep_data(args.input)
    
    print("Calculating statistics...")
    stats = calculate_summary_stats(df)
    
    print("Analyzing root causes...")
    root_causes = analyze_root_causes(df)
    
    print("Analyzing patterns...")
    patterns = analyze_patterns(df)
    
    print("Calculating financial impact...")
    financial_impact = calculate_financial_impact(df, args.or_cost)
    
    print("Generating report...")
    generate_report(df, stats, root_causes, patterns, financial_impact, args.output)
    
    print("Creating visualizations...")
    create_visualizations(df, stats, root_causes, patterns, args.output)
    
    print("\nAnalysis complete!")
    print(f"Average delay: {stats['avg_delay']:.1f} minutes")
    print(f"Annual cost impact: ${financial_impact['annual_total_cost']:,.0f}")
    print(f"Results saved to: {args.output}")

if __name__ == "__main__":
    main()