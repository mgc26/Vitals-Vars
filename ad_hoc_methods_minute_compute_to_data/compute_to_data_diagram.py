import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch, Rectangle, FancyArrowPatch
import numpy as np

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10))
fig.suptitle('Healthcare Data Paradigm Shift: From Data Movement to Compute Movement', 
             fontsize=16, fontweight='bold')

# Traditional Approach (Top)
ax1.set_xlim(0, 10)
ax1.set_ylim(0, 5)
ax1.set_title('Traditional Approach: Moving Data to Compute', fontsize=14, pad=20)
ax1.axis('off')

# Traditional flow boxes
traditional_boxes = [
    {'pos': (0.5, 2.5), 'text': 'EHR\nData', 'color': '#FF6B6B'},
    {'pos': (2.5, 2.5), 'text': 'Lab\nData', 'color': '#FF6B6B'},
    {'pos': (4.5, 2.5), 'text': 'Claims\nData', 'color': '#FF6B6B'},
    {'pos': (6.5, 2.5), 'text': 'Data\nWarehouse', 'color': '#4ECDC4'},
    {'pos': (8.5, 2.5), 'text': 'Analytics\nPlatform', 'color': '#45B7D1'}
]

for box in traditional_boxes:
    fancy_box = FancyBboxPatch(
        (box['pos'][0]-0.4, box['pos'][1]-0.4),
        0.8, 0.8,
        boxstyle="round,pad=0.1",
        facecolor=box['color'],
        edgecolor='black',
        alpha=0.8
    )
    ax1.add_patch(fancy_box)
    ax1.text(box['pos'][0], box['pos'][1], box['text'], 
             ha='center', va='center', fontsize=10, fontweight='bold')

# Traditional arrows with labels
arrows_traditional = [
    {'start': (0.9, 2.5), 'end': (6.1, 2.5), 'label': 'ETL\n(Days/Weeks)'},
    {'start': (2.9, 2.5), 'end': (6.1, 2.5), 'label': ''},
    {'start': (4.9, 2.5), 'end': (6.1, 2.5), 'label': ''},
    {'start': (6.9, 2.5), 'end': (8.1, 2.5), 'label': 'Process\n(Hours)'}
]

for i, arrow in enumerate(arrows_traditional):
    ax1.annotate('', xy=arrow['end'], xytext=arrow['start'],
                 arrowprops=dict(arrowstyle='->', lw=2, color='red'))
    if arrow['label']:
        mid_x = (arrow['start'][0] + arrow['end'][0]) / 2
        ax1.text(mid_x, 3.2, arrow['label'], ha='center', fontsize=9, color='red')

# Risk indicators
ax1.text(5, 1.2, '⚠️ HIPAA Risk at Every Transfer', ha='center', fontsize=11, color='red')
ax1.text(5, 0.7, '🕐 6-18 Month Integration Timeline', ha='center', fontsize=11, color='red')
ax1.text(5, 0.2, '💰 High Infrastructure Cost', ha='center', fontsize=11, color='red')

# Compute-to-Data Approach (Bottom)
ax2.set_xlim(0, 10)
ax2.set_ylim(0, 5)
ax2.set_title('Compute-to-Data Approach: Moving Compute to Data', fontsize=14, pad=20)
ax2.axis('off')

# Compute-to-data boxes
compute_boxes = [
    {'pos': (1.5, 2.5), 'text': 'EHR\nData', 'color': '#FF6B6B'},
    {'pos': (4, 2.5), 'text': 'Lab\nData', 'color': '#FF6B6B'},
    {'pos': (6.5, 2.5), 'text': 'Claims\nData', 'color': '#FF6B6B'},
    {'pos': (8.5, 2.5), 'text': 'Results\nDashboard', 'color': '#95E1D3'}
]

for box in compute_boxes:
    fancy_box = FancyBboxPatch(
        (box['pos'][0]-0.4, box['pos'][1]-0.4),
        0.8, 0.8,
        boxstyle="round,pad=0.1",
        facecolor=box['color'],
        edgecolor='black',
        alpha=0.8
    )
    ax2.add_patch(fancy_box)
    ax2.text(box['pos'][0], box['pos'][1], box['text'], 
             ha='center', va='center', fontsize=10, fontweight='bold')

# Compute functions
compute_functions = [
    {'pos': (1.5, 3.8), 'text': '📊 Compute\nFunction'},
    {'pos': (4, 3.8), 'text': '📊 Compute\nFunction'},
    {'pos': (6.5, 3.8), 'text': '📊 Compute\nFunction'}
]

for func in compute_functions:
    ax2.text(func['pos'][0], func['pos'][1], func['text'], 
             ha='center', va='center', fontsize=9, 
             bbox=dict(boxstyle="round,pad=0.3", facecolor='#FECA57', alpha=0.8))

# Compute arrows
compute_arrows = [
    {'start': (1.5, 3.5), 'end': (1.5, 2.9)},
    {'start': (4, 3.5), 'end': (4, 2.9)},
    {'start': (6.5, 3.5), 'end': (6.5, 2.9)}
]

for arrow in compute_arrows:
    ax2.annotate('', xy=arrow['end'], xytext=arrow['start'],
                 arrowprops=dict(arrowstyle='<->', lw=2, color='green'))

# Result arrows
result_arrows = [
    {'start': (1.9, 2.5), 'end': (8.1, 2.5), 'label': 'Only Results\n(Seconds)'},
    {'start': (4.4, 2.5), 'end': (8.1, 2.5), 'label': ''},
    {'start': (6.9, 2.5), 'end': (8.1, 2.5), 'label': ''}
]

for arrow in result_arrows:
    ax2.annotate('', xy=arrow['end'], xytext=arrow['start'],
                 arrowprops=dict(arrowstyle='->', lw=1.5, color='green', linestyle='dashed'))
    if arrow['label']:
        ax2.text(5.5, 1.8, arrow['label'], ha='center', fontsize=9, color='green')

# Benefits
ax2.text(5, 1.2, '✅ Data Never Leaves Source System', ha='center', fontsize=11, color='green')
ax2.text(5, 0.7, '⚡ Deploy in Days, Not Months', ha='center', fontsize=11, color='green')
ax2.text(5, 0.2, '💡 90% Lower Infrastructure Cost', ha='center', fontsize=11, color='green')

plt.tight_layout()
plt.savefig('compute_to_data_paradigm.png', dpi=300, bbox_inches='tight', 
            facecolor='white', edgecolor='none')
plt.close()

# Create a simpler comparison diagram
fig, ax = plt.subplots(figsize=(10, 6))
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.axis('off')

# Title
ax.text(5, 9, 'The Compute-to-Data Revolution', 
        ha='center', fontsize=18, fontweight='bold')

# Traditional side
ax.text(2.5, 7.5, 'Traditional ETL', ha='center', fontsize=14, fontweight='bold')
traditional_rect = Rectangle((0.5, 3), 4, 4, fill=False, edgecolor='red', linewidth=2)
ax.add_patch(traditional_rect)

ax.text(2.5, 6.2, '📦 Move massive datasets', ha='center', fontsize=10)
ax.text(2.5, 5.6, '🔄 Multiple copies & transforms', ha='center', fontsize=10)
ax.text(2.5, 5.0, '⏱️ Batch processing delays', ha='center', fontsize=10)
ax.text(2.5, 4.4, '🔓 Security vulnerabilities', ha='center', fontsize=10)
ax.text(2.5, 3.8, '💸 Expensive infrastructure', ha='center', fontsize=10)

# Compute-to-Data side
ax.text(7.5, 7.5, 'Compute-to-Data', ha='center', fontsize=14, fontweight='bold')
modern_rect = Rectangle((5.5, 3), 4, 4, fill=False, edgecolor='green', linewidth=2)
ax.add_patch(modern_rect)

ax.text(7.5, 6.2, '🎯 Deploy lightweight functions', ha='center', fontsize=10)
ax.text(7.5, 5.6, '🔒 Data stays in place', ha='center', fontsize=10)
ax.text(7.5, 5.0, '⚡ Real-time processing', ha='center', fontsize=10)
ax.text(7.5, 4.4, '🛡️ Minimal attack surface', ha='center', fontsize=10)
ax.text(7.5, 3.8, '📉 Fraction of the cost', ha='center', fontsize=10)

# Key insight
ax.text(5, 2, '"Stop moving data. Start moving intelligence."', 
        ha='center', fontsize=12, style='italic',
        bbox=dict(boxstyle="round,pad=0.5", facecolor='yellow', alpha=0.3))

# Bottom line
ax.text(5, 0.5, 'Healthcare organizations using compute-to-data report 85% faster deployments', 
        ha='center', fontsize=10, fontweight='bold')

plt.savefig('compute_to_data_comparison.png', dpi=300, bbox_inches='tight', 
            facecolor='white', edgecolor='none')
plt.close()

print("Diagrams created successfully!")
print("- compute_to_data_paradigm.png: Shows the flow comparison")
print("- compute_to_data_comparison.png: Shows the key differences")