"""
Commitment Space Visualization for Smart Tangibles
Plots hardware vs software decisions on a Risk/Cost quadrant chart
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

# Set up the figure
fig, ax = plt.subplots(figsize=(14, 11))

# Define decision data: (cost, risk, label, is_hardware)
# Cost scale: 0-100 (in $K equivalent, log-ish scale)
# Risk scale: 0-100 (severity if wrong)

decisions = [
    # HARDWARE DECISIONS (Q1 - Danger Zone) - Red squares
    (95, 95, 'Battery chemistry', True),
    (90, 92, 'Safety certifications', True),
    (88, 88, 'Core processor/SoC', True),
    (85, 80, 'Injection molds', True),
    (82, 85, 'Form factor', True),
    (78, 75, 'Wireless protocol', True),
    (72, 70, 'PCB layout', True),
    (68, 65, 'Display selection', True),
    (65, 68, 'Antenna design', True),
    (60, 60, 'Connector types', True),
    (55, 55, 'Sensor specs', True),
    (70, 50, 'Packaging design', True),

    # FIRMWARE DECISIONS (Q2 - Validate Heavily) - Orange diamonds
    (35, 85, 'FOTA mechanism', 'firmware'),
    (38, 80, 'Bootloader design', 'firmware'),
    (32, 75, 'Firmware architecture', 'firmware'),
    (40, 65, 'Core RTOS selection', 'firmware'),
    (30, 55, 'Firmware features', 'firmware'),
    (25, 45, 'Algorithm tuning', 'firmware'),
    (20, 35, 'Config parameters', 'firmware'),

    # SOFTWARE DECISIONS (Q3 - Experiment Freely) - Blue circles
    (15, 40, 'Cloud API design', False),
    (12, 35, 'App architecture', False),
    (18, 30, 'Onboarding flow', False),
    (10, 25, 'App UI/UX', False),
    (8, 28, 'Dashboard layouts', False),
    (12, 22, 'Push notifications', False),
    (6, 18, 'Feature flags', False),
    (5, 15, 'Pricing experiments', False),
    (8, 12, 'Email templates', False),
    (4, 10, 'Marketing copy', False),
    (3, 8, 'A/B test variants', False),
    (2, 5, 'Analytics events', False),

    # Q4 DECISIONS (Avoid) - Gray X marks
    (75, 25, 'Over-engineered\npackaging', 'avoid'),
    (65, 20, 'Custom connectors\n(unnecessary)', 'avoid'),
    (70, 15, 'Premium materials\n(non-differentiating)', 'avoid'),
    (60, 18, 'Unnecessary\ncertifications', 'avoid'),
]

# Add fuzzy clouds around each point using scatter with jitter
np.random.seed(42)

for cost, risk, label, category in decisions:
    # Determine color and marker based on category
    if category == True:  # Hardware
        color = '#DC3545'  # Red
        marker = 's'  # Square
        size = 180
        alpha = 0.85
        cloud_color = '#DC354520'
    elif category == 'firmware':
        color = '#FD7E14'  # Orange
        marker = 'D'  # Diamond
        size = 150
        alpha = 0.85
        cloud_color = '#FD7E1420'
    elif category == 'avoid':
        color = '#6C757D'  # Gray
        marker = 'X'  # X mark
        size = 150
        alpha = 0.7
        cloud_color = '#6C757D15'
    else:  # Software
        color = '#0D6EFD'  # Blue
        marker = 'o'  # Circle
        size = 150
        alpha = 0.85
        cloud_color = '#0D6EFD20'

    # Skip fuzzy clouds - show only labeled points
    # n_cloud_points = 25
    # cloud_cost = cost + np.random.normal(0, 4, n_cloud_points)
    # cloud_risk = risk + np.random.normal(0, 4, n_cloud_points)
    # ax.scatter(cloud_cost, cloud_risk, c=cloud_color, s=300, alpha=0.3, marker='o', edgecolors='none')

    # Draw the main point
    ax.scatter(cost, risk, c=color, s=size, marker=marker, alpha=alpha, edgecolors='white', linewidths=1.5, zorder=5)

    # Add label with offset
    offset_x = 2.5
    offset_y = 2.5
    fontsize = 7.5

    # Adjust label position based on quadrant to avoid overlap
    if cost > 50 and risk > 50:  # Q1
        ha, va = 'right', 'bottom'
        offset_x = -2
    elif cost < 50 and risk > 50:  # Q2
        ha, va = 'left', 'bottom'
    elif cost < 50 and risk < 50:  # Q3
        ha, va = 'left', 'top'
        offset_y = -2
    else:  # Q4
        ha, va = 'right', 'top'
        offset_x = -2
        offset_y = -2

    ax.annotate(label, (cost + offset_x, risk + offset_y), fontsize=fontsize,
                ha=ha, va=va, color='#333333', alpha=0.9)

# Draw quadrant dividing lines
ax.axhline(y=50, color='#333333', linestyle='-', linewidth=1.5, alpha=0.4)
ax.axvline(x=50, color='#333333', linestyle='-', linewidth=1.5, alpha=0.4)

# Add quadrant labels with background boxes
quadrant_style = dict(boxstyle='round,pad=0.5', facecolor='white', alpha=0.8, edgecolor='#CCCCCC')

ax.text(75, 92, 'Q1: DANGER ZONE\nValidate Exhaustively', fontsize=11, fontweight='bold',
        ha='center', va='top', color='#DC3545', bbox=quadrant_style)
ax.text(25, 92, 'Q2: HIGH STAKES\nValidate Heavily', fontsize=11, fontweight='bold',
        ha='center', va='top', color='#FD7E14', bbox=quadrant_style)
ax.text(25, 8, 'Q3: SAFE ZONE\nExperiment Freely', fontsize=11, fontweight='bold',
        ha='center', va='bottom', color='#0D6EFD', bbox=quadrant_style)
ax.text(75, 8, 'Q4: WASTE ZONE\nAvoid or Simplify', fontsize=11, fontweight='bold',
        ha='center', va='bottom', color='#6C757D', bbox=quadrant_style)

# Add shaded regions for quadrants
ax.fill_between([50, 100], [50, 50], [100, 100], alpha=0.08, color='#DC3545')  # Q1 - Red tint
ax.fill_between([0, 50], [50, 50], [100, 100], alpha=0.08, color='#FD7E14')    # Q2 - Orange tint
ax.fill_between([0, 50], [0, 0], [50, 50], alpha=0.08, color='#0D6EFD')        # Q3 - Blue tint
ax.fill_between([50, 100], [0, 0], [50, 50], alpha=0.08, color='#6C757D')      # Q4 - Gray tint

# Draw strategic movement arrows
arrow_style = dict(arrowstyle='->', color='#28A745', lw=2, mutation_scale=15)

# Arrow from Q1 to Q3 (the goal)
ax.annotate('', xy=(30, 35), xytext=(70, 70),
            arrowprops=dict(arrowstyle='->', color='#28A745', lw=2.5,
                          connectionstyle='arc3,rad=-0.2'))
ax.text(45, 58, 'Push to\nSoftware', fontsize=9, ha='center', va='center',
        color='#28A745', fontweight='bold', style='italic')

# Set axis labels and title
ax.set_xlabel('Cost to Reverse ($K equivalent, log scale)', fontsize=12, fontweight='bold', labelpad=10)
ax.set_ylabel('Risk if Wrong (Severity)', fontsize=12, fontweight='bold', labelpad=10)
ax.set_title('The Commitment Space: Hardware vs Software Decisions\n',
             fontsize=16, fontweight='bold', color='#1a1a1a')

# Add subtitle
ax.text(50, 105, 'Smart tangibles succeed by architecturally shifting decisions from Q1 → Q3',
        fontsize=10, ha='center', va='bottom', style='italic', color='#666666')

# Set axis limits and ticks
ax.set_xlim(-5, 105)
ax.set_ylim(-5, 108)

# Custom tick labels for cost axis (representing actual $ ranges)
cost_ticks = [0, 25, 50, 75, 100]
cost_labels = ['<$1K', '$10K', '$50K', '$100K', '>$250K']
ax.set_xticks(cost_ticks)
ax.set_xticklabels(cost_labels)

# Custom tick labels for risk axis
risk_ticks = [0, 25, 50, 75, 100]
risk_labels = ['Trivial', 'Minor', 'Significant', 'Major', 'Existential']
ax.set_yticks(risk_ticks)
ax.set_yticklabels(risk_labels)

# Create legend
legend_elements = [
    mpatches.Patch(facecolor='#DC3545', edgecolor='white', label='Hardware (frozen at ship)'),
    mpatches.Patch(facecolor='#FD7E14', edgecolor='white', label='Firmware (FOTA updatable)'),
    mpatches.Patch(facecolor='#0D6EFD', edgecolor='white', label='Software (freely iterable)'),
    mpatches.Patch(facecolor='#6C757D', edgecolor='white', label='Avoid (over-engineered)'),
]
ax.legend(handles=legend_elements, loc='upper left', framealpha=0.95, fontsize=10)

# Style the plot
ax.set_facecolor('#FAFAFA')
fig.patch.set_facecolor('white')
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_color('#CCCCCC')
ax.spines['bottom'].set_color('#CCCCCC')
ax.tick_params(colors='#666666')
ax.grid(True, alpha=0.3, linestyle='--', color='#CCCCCC')

plt.tight_layout()
plt.savefig('/sessions/lucid-upbeat-heisenberg/mnt/chapters/commitment_space_chart.png', dpi=150, bbox_inches='tight',
            facecolor='white', edgecolor='none')
plt.savefig('/sessions/lucid-upbeat-heisenberg/mnt/chapters/commitment_space_chart.svg', format='svg', bbox_inches='tight',
            facecolor='white', edgecolor='none')
print("Chart saved to commitment_space_chart.png and .svg")
plt.show()
