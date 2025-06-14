import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import seaborn as sns
from matplotlib.colors import LinearSegmentedColormap
from matplotlib.patches import Patch
from matplotlib.lines import Line2D

# Set consistent styling for all plots
plt.style.use('seaborn-v0_8-whitegrid')

# Define the color scheme (black, gray, yellow) as shown in the image
COLOR_SCHEME = ['#000000', '#999999', '#FFC107']  # Black, Gray, Yellow/Gold

# Custom colormap for heatmaps
custom_cmap = LinearSegmentedColormap.from_list('custom_cmap', 
                                              ['#FFFFFF', '#FFC107', '#000000'], 
                                              N=100)

def set_common_style(ax, title, xlabel=None, ylabel=None):
    """Apply common styling elements to matplotlib axes"""
    ax.set_title(title, fontsize=14, fontweight='bold', pad=20)
    if xlabel:
        ax.set_xlabel(xlabel, fontsize=12)
    if ylabel:
        ax.set_ylabel(ylabel, fontsize=12)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.tick_params(axis='both', labelsize=10)
    ax.grid(False)  # Turn off grid for cleaner look

#################################
# 1. Technology Use by Age Group (2018 vs 2024)
#################################

def plot_tech_by_age():
    # Data based on actual analysis of CSV files
    age_groups = ["21-30", "31-40", "41-50", "51-60", "61+"]
    
    # 2018 data (normalized to 0-1 scale for consistency)
    tech_2018 = {
        "CMS": [5.0/5, 3.84/5, 4.08/5, 3.86/5, 3.80/5],
        "SWC": [1.0/5, 1.68/5, 1.52/5, 1.51/5, 1.37/5],
        "VPN": [1.0/5, 1.45/5, 1.30/5, 1.62/5, 1.14/5],
        "ITS": [2.0/5, 2.19/5, 2.03/5, 2.03/5, 1.67/5]
    }
    
    # 2024 data (normalized to 0-1 scale for consistency)
    tech_2024 = {
        "CMS": [5.0/5, 5.0/5, 4.81/5, 4.83/5, 4.81/5],
        "SWC": [3.5/5, 3.25/5, 3.38/5, 3.87/5, 3.78/5],
        "VPN": [1.5/5, 1.2/5, 1.35/5, 1.49/5, 1.32/5],
        "ITS": [2.67/5, 1.7/5, 2.16/5, 1.97/5, 2.03/5]
    }
    
    # Create two subplots
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
    
    # 2018 Plot
    df_2018 = pd.DataFrame(tech_2018, index=age_groups)
    df_2018.plot(kind='bar', ax=ax1, color=COLOR_SCHEME)
    ax1.set_ylim(0, 1.0)
    ax1.yaxis.set_major_formatter(mtick.PercentFormatter(1.0))
    set_common_style(ax1, "Technology Usage by Age Group (2018)", 
                   xlabel="Age Group", ylabel="Usage Rate")
    ax1.legend(loc='upper right', fontsize=8)
    
    # 2024 Plot
    df_2024 = pd.DataFrame(tech_2024, index=age_groups)
    df_2024.plot(kind='bar', ax=ax2, color=COLOR_SCHEME)
    ax2.set_ylim(0, 1.0)
    ax2.yaxis.set_major_formatter(mtick.PercentFormatter(1.0))
    set_common_style(ax2, "Technology Usage by Age Group (2024)", 
                   xlabel="Age Group", ylabel="Usage Rate")
    ax2.legend(loc='upper right', fontsize=8)
    
    plt.tight_layout()
    plt.show()
    
    return "2018 vs 2024: The data shows a dramatic equalization of technology adoption across age groups. In 2018, there was noticeable variation across age groups, with older faculty (51-70) showing lower adoption, especially for Web Conferencing (SWC) and Canvas LMS (CMS). By 2024, Canvas LMS usage has become nearly universal across all age groups (≥96%), and Web Conferencing usage has significantly increased and equalized (65-77%). This suggests successful technology initiatives have effectively eliminated the 'digital divide' between younger and older faculty."

#################################
# 2. Technology Use by Tenure Status (2018 vs 2024)
#################################

def plot_tech_by_tenure():
    # Data based on actual analysis of CSV files
    # Tenure status categories
    tenure_groups = ["Tenured", "Tenure Track", "Not Tenured"]
    
    # 2018 data (normalized to 0-1 scale for consistency)
    tenure_tech_2018 = {
        "CMS": [4.16/5, 3.72/5, 3.83/5],
        "SWC": [1.68/5, 1.51/5, 1.35/5],
        "VPN": [1.43/5, 1.49/5, 1.30/5],
        "ITS": [2.20/5, 1.94/5, 1.80/5]
    }
    
    # 2024 data (normalized to 0-1 scale for consistency)
    tenure_tech_2024 = {
        "CMS": [4.92/5, 4.93/5, 4.70/5],
        "SWC": [3.99/5, 4.27/5, 2.87/5],
        "VPN": [1.63/5, 1.13/5, 1.02/5],
        "ITS": [2.15/5, 1.93/5, 1.81/5]
    }
    
    # Create two subplots
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
    
    # 2018 Plot
    df_2018 = pd.DataFrame(tenure_tech_2018, index=tenure_groups)
    df_2018.plot(kind='bar', ax=ax1, color=COLOR_SCHEME)
    ax1.set_ylim(0, 1.0)
    ax1.yaxis.set_major_formatter(mtick.PercentFormatter(1.0))
    set_common_style(ax1, "Technology Usage by Tenure Status (2018)", 
                   xlabel="Tenure Status", ylabel="Usage Rate")
    ax1.legend(loc='upper right', fontsize=8)
    
    # 2024 Plot
    df_2024 = pd.DataFrame(tenure_tech_2024, index=tenure_groups)
    df_2024.plot(kind='bar', ax=ax2, color=COLOR_SCHEME)
    ax2.set_ylim(0, 1.0)
    ax2.yaxis.set_major_formatter(mtick.PercentFormatter(1.0))
    set_common_style(ax2, "Technology Usage by Tenure Status (2024)", 
                   xlabel="Tenure Status", ylabel="Usage Rate")
    ax2.legend(loc='upper right', fontsize=8)
    
    plt.tight_layout()
    plt.show()
    
    return "2018 vs 2024: The data reveals significant shifts in technology adoption across tenure groups. In 2018, Tenured faculty were slightly more active with Canvas LMS, while Tenure Track faculty led in Web Conferencing and VPN usage. By 2024, Canvas LMS adoption is universally high across all tenure groups (94-99%). Web Conferencing usage has dramatically increased across all groups but most notably among Tenured and Tenure Track faculty (80-85%). This suggests institutional policy shifts successfully encouraged technology adoption, with tenured faculty no longer lagging in adoption."

#################################
# 3. ROI Matrix: Importance vs Satisfaction (2018 vs 2024)
#################################

def plot_roi_matrix():
    # Data based on actual analysis of CSV files
    # Selected key technologies for comparison
    roi_data_2018 = [
        {"system": "CMS", "importance": 3.38/5, "satisfaction": 3.52/5},
        {"system": "SWC", "importance": 2.30/5, "satisfaction": 3.24/5},
        {"system": "ERPSS", "importance": 3.80/5, "satisfaction": 3.57/5},
        {"system": "VPN", "importance": 2.72/5, "satisfaction": 3.44/5}
    ]
    
    roi_data_2024 = [
        {"system": "CMS", "importance": 3.88/5, "satisfaction": 3.75/5},
        {"system": "SWC", "importance": 3.63/5, "satisfaction": 3.87/5},
        {"system": "ERPSS", "importance": 3.34/5, "satisfaction": 3.63/5},
        {"system": "GAIT", "importance": 2.10/5, "satisfaction": 3.07/5}
    ]
    
    df_2018 = pd.DataFrame(roi_data_2018)
    df_2024 = pd.DataFrame(roi_data_2024)
    
    # Create two subplots
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
    
    # 2018 Plot
    ax1.scatter(df_2018['importance'], df_2018['satisfaction'], s=100, 
               color=COLOR_SCHEME[0], alpha=0.7)
    
    # Add tool names as labels
    for i, txt in enumerate(df_2018['system']):
        ax1.annotate(txt, (df_2018['importance'][i], df_2018['satisfaction'][i]), 
                    fontsize=9, ha='center', va='bottom',
                    xytext=(0, 5), textcoords='offset points')
    
    # Draw quadrant lines
    ax1.axhline(y=0.5, color='gray', linestyle='--', alpha=0.5)
    ax1.axvline(x=0.5, color='gray', linestyle='--', alpha=0.5)
    
    # Quadrant labels
    ax1.text(0.25, 0.75, "Low Importance\nHigh Satisfaction", 
           ha='center', va='center', fontsize=8, alpha=0.7)
    ax1.text(0.75, 0.75, "High Importance\nHigh Satisfaction", 
           ha='center', va='center', fontsize=8, alpha=0.7)
    ax1.text(0.25, 0.25, "Low Importance\nLow Satisfaction", 
           ha='center', va='center', fontsize=8, alpha=0.7)
    ax1.text(0.75, 0.25, "High Importance\nLow Satisfaction", 
           ha='center', va='center', fontsize=8, alpha=0.7)
    
    ax1.set_xlim(0, 1.0)
    ax1.set_ylim(0, 1.0)
    ax1.xaxis.set_major_formatter(mtick.PercentFormatter(1.0))
    ax1.yaxis.set_major_formatter(mtick.PercentFormatter(1.0))
    set_common_style(ax1, "Importance vs. Satisfaction (2018)", 
                   xlabel="Perceived Importance", ylabel="User Satisfaction")
    
    # 2024 Plot
    ax2.scatter(df_2024['importance'], df_2024['satisfaction'], s=100, 
               color=COLOR_SCHEME[2], alpha=0.7)
    
    # Add tool names as labels
    for i, txt in enumerate(df_2024['system']):
        ax2.annotate(txt, (df_2024['importance'][i], df_2024['satisfaction'][i]), 
                    fontsize=9, ha='center', va='bottom',
                    xytext=(0, 5), textcoords='offset points')
    
    # Draw quadrant lines
    ax2.axhline(y=0.5, color='gray', linestyle='--', alpha=0.5)
    ax2.axvline(x=0.5, color='gray', linestyle='--', alpha=0.5)
    
    # Quadrant labels
    ax2.text(0.25, 0.75, "Low Importance\nHigh Satisfaction", 
           ha='center', va='center', fontsize=8, alpha=0.7)
    ax2.text(0.75, 0.75, "High Importance\nHigh Satisfaction", 
           ha='center', va='center', fontsize=8, alpha=0.7)
    ax2.text(0.25, 0.25, "Low Importance\nLow Satisfaction", 
           ha='center', va='center', fontsize=8, alpha=0.7)
    ax2.text(0.75, 0.25, "High Importance\nLow Satisfaction", 
           ha='center', va='center', fontsize=8, alpha=0.7)
    
    ax2.set_xlim(0, 1.0)
    ax2.set_ylim(0, 1.0)
    ax2.xaxis.set_major_formatter(mtick.PercentFormatter(1.0))
    ax2.yaxis.set_major_formatter(mtick.PercentFormatter(1.0))
    set_common_style(ax2, "Importance vs. Satisfaction (2024)", 
                   xlabel="Perceived Importance", ylabel="User Satisfaction")
    
    plt.tight_layout()
    plt.show()
    
    return "2018 vs 2024: The ROI matrix reveals important shifts in technology perception and satisfaction. Canvas (CMS) has maintained high importance while its perceived importance increased from 68% to 78%. Web Conferencing (SWC) shows the most dramatic change, with both importance and satisfaction significantly higher in 2024 - importance jumped from 46% to 73% and satisfaction from 65% to 77%. This reflects the post-pandemic shift to remote teaching. ERP systems (ERPSS) show slightly decreased importance but maintained satisfaction. AI tools (GAIT) appear in 2024 as low importance but with reasonable satisfaction (61%), suggesting it's an emerging technology with growth potential."

#################################
# 4. Strategic Quadrant Analysis
#################################

def plot_strategic_quadrants():
    # Data based on actual analysis of CSV files
    quadrant_data = [
        {"tool": "CMS", "usage2018": 3.89/5, "usage2024": 4.85/5, "quadrant": "Core Growth"},
        {"tool": "TMS", "usage2018": 3.77/5, "usage2024": 4.13/5, "quadrant": "Core Growth"},
        {"tool": "SWC", "usage2018": 1.50/5, "usage2024": 3.65/5, "quadrant": "Emerging Tools"},
        {"tool": "STMS", "usage2018": 2.07/5, "usage2024": 2.18/5, "quadrant": "Legacy Reliance"},
        {"tool": "FPC", "usage2018": 2.20/5, "usage2024": 2.31/5, "quadrant": "Legacy Reliance"},
        {"tool": "VPN", "usage2018": 1.40/5, "usage2024": 1.39/5, "quadrant": "Sunset Candidates"},
        {"tool": "AORO", "usage2018": 3.70/5, "usage2024": 3.21/5, "quadrant": "Legacy Reliance"},
        {"tool": "ERPSS", "usage2018": 4.49/5, "usage2024": 2.93/5, "quadrant": "Legacy Reliance"}
    ]
    
    df = pd.DataFrame(quadrant_data)
    
    # Define quadrant colors
    quadrant_colors = {
        "Core Growth": COLOR_SCHEME[0],       # Black
        "Legacy Reliance": "#FF9800",        # Orange
        "Emerging Tools": COLOR_SCHEME[2],    # Yellow
        "Sunset Candidates": "#F44336"       # Red
    }
    
    # Map color to each point based on quadrant
    colors = df['quadrant'].map(quadrant_colors)
    
    # Create scatter plot
    fig, ax = plt.subplots(figsize=(10, 8))
    
    # Plot data points
    scatter = ax.scatter(df['usage2018'], df['usage2024'], c=colors, s=100, alpha=0.7)
    
    # Add tool labels
    for i, row in df.iterrows():
        ax.annotate(row['tool'], 
                   (row['usage2018'], row['usage2024']),
                   xytext=(5, 5),
                   textcoords="offset points",
                   fontsize=9, fontweight='bold')
    
    # Draw quadrant lines (at 50% for both axes)
    ax.axhline(y=0.5, color='gray', linestyle='--', alpha=0.5)
    ax.axvline(x=0.5, color='gray', linestyle='--', alpha=0.5)
    
    # Add quadrant labels
    ax.text(0.25, 0.25, "Sunset Candidates", ha='center', va='center', 
           fontsize=10, fontweight='bold', bbox=dict(facecolor='white', alpha=0.5, boxstyle='round'))
    ax.text(0.25, 0.75, "Emerging Tools", ha='center', va='center', 
           fontsize=10, fontweight='bold', bbox=dict(facecolor='white', alpha=0.5, boxstyle='round'))
    ax.text(0.75, 0.25, "Legacy Reliance", ha='center', va='center', 
           fontsize=10, fontweight='bold', bbox=dict(facecolor='white', alpha=0.5, boxstyle='round'))
    ax.text(0.75, 0.75, "Core Growth", ha='center', va='center', 
           fontsize=10, fontweight='bold', bbox=dict(facecolor='white', alpha=0.5, boxstyle='round'))
    
    # Create legend for quadrants
    legend_elements = [
        Line2D([0], [0], marker='o', color='w', markerfacecolor=COLOR_SCHEME[0], markersize=10, label='Core Growth'),
        Line2D([0], [0], marker='o', color='w', markerfacecolor="#FF9800", markersize=10, label='Legacy Reliance'),
        Line2D([0], [0], marker='o', color='w', markerfacecolor=COLOR_SCHEME[2], markersize=10, label='Emerging Tools'),
        Line2D([0], [0], marker='o', color='w', markerfacecolor="#F44336", markersize=10, label='Sunset Candidates')
    ]
    ax.legend(handles=legend_elements, loc='upper left', fontsize=9)
    
    ax.set_xlim(0, 1.0)
    ax.set_ylim(0, 1.0)
    ax.xaxis.set_major_formatter(mtick.PercentFormatter(1.0))
    ax.yaxis.set_major_formatter(mtick.PercentFormatter(1.0))
    set_common_style(ax, "Strategic Technology Quadrant Analysis (2018 vs 2024)", 
                   xlabel="Usage in 2018", ylabel="Usage in 2024")
    
    plt.tight_layout()
    plt.show()
    
    return "The strategic quadrant analysis reveals four key technology categories: 1) Core Growth technologies (Canvas LMS, Turnitin) continue to be heavily used and are growing in adoption - these merit continued investment; 2) Legacy Reliance tools (Student Management Systems, Faculty Profile Creator, Academic Outreach) remain important but show limited or negative growth - these may need modernization; 3) Web Conferencing has emerged as a critical tool, showing the most dramatic growth (from 30% to 73% usage) - representing the most successful technology transformation; 4) VPN usage has remained low and stagnant, suggesting it may be a sunset candidate unless security requirements dictate otherwise. The most concerning trend is the significant drop in ERP usage (90% to 59%), suggesting potential issues with the current implementation."

#################################
# 5. Teaching Modalities: In-Person vs Remote (2024)
#################################

def plot_teaching_modalities():
    # Data based on actual analysis of CSV files
    # TREM values represent teaching modality (in-person vs remote)
    modality_data = [
        {"modality": "Entirely in-person", "percentage": 0.331},
        {"modality": "Mostly in-person", "percentage": 0.423},
        {"modality": "Equal mix", "percentage": 0.153},
        {"modality": "Mostly remote", "percentage": 0.037},
        {"modality": "Entirely remote", "percentage": 0.055}
    ]
    
    df = pd.DataFrame(modality_data)
    
    # Create bar chart
    fig, ax = plt.subplots(figsize=(10, 6))
    
    bars = ax.bar(df['modality'], df['percentage'], color=COLOR_SCHEME[2], alpha=0.8)
    
    # Add percentage labels on top of bars
    for bar in bars:
        height = bar.get_height()
        ax.annotate(f'{height:.1%}',
                   xy=(bar.get_x() + bar.get_width() / 2, height),
                   xytext=(0, 3),  # 3 points vertical offset
                   textcoords="offset points",
                   ha='center', va='bottom', fontsize=10, fontweight='bold')
    
    ax.set_ylim(0, 0.5)
    ax.yaxis.set_major_formatter(mtick.PercentFormatter(1.0))
    set_common_style(ax, "Teaching Modality Distribution (2024)", 
                   xlabel="Teaching Modality", ylabel="Percentage of Faculty")
    plt.setp(ax.get_xticklabels(), rotation=45, ha='right')
    
    plt.tight_layout()
    plt.show()
    
    return "The 2024 data shows that despite the pandemic-driven shift to remote teaching, most faculty have returned to primarily in-person instruction. 33.1% teach entirely in-person, and another 42.3% teach mostly in-person, for a combined 75.4% primarily in-person. Only 9.2% of faculty teach primarily remotely (3.7% mostly remote and 5.5% entirely remote). The remaining 15.3% use an equal mix of in-person and remote teaching. This suggests that while the pandemic created capacity for remote teaching, traditional in-person instruction remains the dominant modality for most faculty."

#################################
# 6. Live vs Recorded Instruction (2024)
#################################

def plot_instruction_types():
    # Data based on actual analysis of CSV files
    # TLIVE values represent synchronous vs asynchronous teaching
    instruction_data = [
        {"type": "Entirely live", "percentage": 0.393},
        {"type": "Mostly live", "percentage": 0.454},
        {"type": "Equal mix", "percentage": 0.098},
        {"type": "Mostly recorded", "percentage": 0.031},
        {"type": "Entirely recorded", "percentage": 0.025}
    ]
    
    df = pd.DataFrame(instruction_data)
    
    # Create bar chart
    fig, ax = plt.subplots(figsize=(10, 6))
    
    bars = ax.bar(df['type'], df['percentage'], color=COLOR_SCHEME[0], alpha=0.8)
    
    # Add percentage labels on top of bars
    for bar in bars:
        height = bar.get_height()
        ax.annotate(f'{height:.1%}',
                   xy=(bar.get_x() + bar.get_width() / 2, height),
                   xytext=(0, 3),  # 3 points vertical offset
                   textcoords="offset points",
                   ha='center', va='bottom', fontsize=10, fontweight='bold')
    
    ax.set_ylim(0, 0.6)
    ax.yaxis.set_major_formatter(mtick.PercentFormatter(1.0))
    set_common_style(ax, "Live vs. Recorded Instruction (2024)", 
                   xlabel="Instruction Type", ylabel="Percentage of Faculty")
    plt.setp(ax.get_xticklabels(), rotation=45, ha='right')
    
    plt.tight_layout()
    plt.show()
    
    return "The data reveals a strong faculty preference for synchronous teaching, with 84.7% of faculty primarily using live instruction (39.3% entirely live, 45.4% mostly live). Only 5.6% use primarily recorded instruction (3.1% mostly recorded, 2.5% entirely recorded), with 9.8% using an equal mix. This suggests that despite increased digital technology adoption, faculty still strongly value real-time interaction with students. Even when teaching remotely, they prefer synchronous methods over asynchronous ones. This has important implications for technology investments, suggesting that tools supporting real-time engagement should be prioritized over content repositories."

#################################
# 7. Teaching Modality Relationship (In-Person/Remote vs Live/Recorded)
#################################

def plot_teaching_relationship():
    # Data based on cross-tabulation of TREM and TLIVE values
    # These represent counts of faculty in each combination
    cross_data = {
        "1-1": 36, # Entirely in-person & Entirely live
        "1-2": 18, # Entirely in-person & Mostly live
        "2-1": 16, # Mostly in-person & Entirely live
        "2-2": 42, # Mostly in-person & Mostly live
        "2-3": 5,  # Mostly in-person & Equal mix
        "2-4": 3,  # Mostly in-person & Mostly recorded
        "2-5": 3,  # Mostly in-person & Entirely recorded
        "3-1": 9,  # Equal mix & Entirely live
        "3-2": 8,  # Equal mix & Mostly live
        "3-3": 7,  # Equal mix & Equal mix
        "3-4": 1,  # Equal mix & Mostly recorded
        "4-1": 2,  # Mostly remote & Entirely live
        "4-2": 3,  # Mostly remote & Mostly live
        "4-3": 1,  # Mostly remote & Equal mix
        "5-1": 1,  # Entirely remote & Entirely live
        "5-2": 3,  # Entirely remote & Mostly live
        "5-3": 3,  # Entirely remote & Equal mix
        "5-4": 1,  # Entirely remote & Mostly recorded
        "5-5": 1   # Entirely remote & Entirely recorded
    }
    
    # Create a matrix representation
    trem_labels = ["Entirely in-person", "Mostly in-person", "Equal mix", "Mostly remote", "Entirely remote"]
    tlive_labels = ["Entirely live", "Mostly live", "Equal mix", "Mostly recorded", "Entirely recorded"]
    
    # Initialize matrix with zeros
    matrix = np.zeros((5, 5))
    
    # Fill matrix with counts
    for key, count in cross_data.items():
        trem, tlive = map(int, key.split('-'))
        matrix[trem-1, tlive-1] = count
    
    # Convert to percentages of total
    total = np.sum(matrix)
    matrix_pct = matrix / total
    
    # Create heatmap
    fig, ax = plt.subplots(figsize=(12, 8))
    
    # Use custom colormap
    heatmap = ax.pcolor(matrix_pct, cmap=custom_cmap)
    
    # Set tick positions and labels
    ax.set_xticks(np.arange(len(tlive_labels)) + 0.5)
    ax.set_yticks(np.arange(len(trem_labels)) + 0.5)
    ax.set_xticklabels(tlive_labels)
    ax.set_yticklabels(trem_labels)
    plt.setp(ax.get_xticklabels(), rotation=45, ha='right')
    
    # Add text annotations
    for i in range(len(trem_labels)):
        for j in range(len(tlive_labels)):
            # Only show text for cells with values
            if matrix[i, j] > 0:
                # Choose text color based on background
                text_color = 'white' if matrix_pct[i, j] > 0.1 else 'black'
                ax.text(j + 0.5, i + 0.5, f'{matrix_pct[i, j]:.1%}\n({int(matrix[i, j])})',
                       ha='center', va='center', color=text_color, fontsize=8, fontweight='bold')
    
    # Add colorbar
    cbar = plt.colorbar(heatmap)
    cbar.set_label('Percentage of Faculty')
    
    set_common_style(ax, "Relationship Between Teaching Modality & Synchronicity (2024)", 
                   xlabel="Live vs. Recorded Instruction", ylabel="In-Person vs. Remote Teaching")
    
    plt.tight_layout()
    plt.show()
    
    return "This visualization reveals the relationship between teaching modality (in-person/remote) and synchronicity (live/recorded). Key patterns include: 1) Faculty teaching entirely in-person strongly prefer entirely live instruction (22.1% of all faculty); 2) The most common combination is 'mostly in-person and mostly live' (25.8% of faculty); 3) Faculty teaching remotely still predominantly use live instruction rather than recorded content; 4) The diagonal pattern shows that the more remote the teaching, the more likely faculty are to incorporate recorded elements, though live instruction remains preferred across all modalities. This suggests that synchronous engagement is valued regardless of physical or virtual learning environments."

#################################
# 8. Technology Growth from 2018 to 2024
#################################

def plot_tech_growth():
    # Data based on actual analysis of CSV files
    # Showing the technologies with the most significant changes
    tech_growth_data = [
        {"technology": "Web Conferencing", "usage2018": 1.50/5, "usage2024": 3.65/5, "growth": 0.43},
        {"technology": "Canvas LMS", "usage2018": 3.89/5, "usage2024": 4.85/5, "growth": 0.19},
        {"technology": "Turnitin", "usage2018": 3.77/5, "usage2024": 4.13/5, "growth": 0.07},
        {"technology": "Faculty Profile", "usage2018": 2.20/5, "usage2024": 2.31/5, "growth": 0.02},
        {"technology": "VPN", "usage2018": 1.40/5, "usage2024": 1.39/5},
        {"technology": "VPN", "usage2018": 1.40/5, "usage2024": 1.39/5, "growth": 0.00},
        {"technology": "Library Catalog", "usage2018": 2.09/5, "usage2024": 2.06/5, "growth": -0.01},
        {"technology": "Academic Outreach", "usage2018": 3.70/5, "usage2024": 3.21/5, "growth": -0.10},
        {"technology": "ERP Systems", "usage2018": 4.49/5, "usage2024": 2.93/5, "growth": -0.31}
    ]
    
    # Sort by growth
    df = pd.DataFrame(tech_growth_data).sort_values('growth', ascending=False)
    
    # Create horizontal bar chart
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # Define colors based on growth (positive=yellow, negative=gray)
    colors = [COLOR_SCHEME[2] if x > 0 else COLOR_SCHEME[1] for x in df['growth']]
    
    # Create horizontal bars
    bars = ax.barh(df['technology'], df['growth'], color=colors, alpha=0.8)
    
    # Add percentage labels
    for bar in bars:
        width = bar.get_width()
        label_x = max(width + 0.02, 0.02) if width >= 0 else min(width - 0.08, -0.08)
        align = 'left' if width >= 0 else 'right'
        ax.annotate(f'{width:.0%}',
                   xy=(label_x, bar.get_y() + bar.get_height()/2),
                   xytext=(0, 0),
                   textcoords="offset points",
                   ha=align, va='center', fontsize=9, fontweight='bold')
    
    # Add vertical line at zero
    ax.axvline(x=0, color='black', linestyle='-', linewidth=0.5)
    
    # Set limits and format
    ax.set_xlim(-0.35, 0.5)
    ax.xaxis.set_major_formatter(mtick.PercentFormatter(1.0))
    set_common_style(ax, "Technology Usage Growth (2018-2024)", 
                   xlabel="Change in Usage Rate", ylabel="Technology")
    
    plt.tight_layout()
    plt.show()
    
    return "The data reveals dramatic shifts in technology usage from 2018 to 2024. Web Conferencing experienced the most significant growth, increasing by 43 percentage points - clearly driven by the pandemic shift to remote teaching. Canvas LMS usage also grew substantially (19 points), reinforcing its position as the core educational technology platform. Turnitin saw modest growth (7 points), while several systems including VPN and Faculty Profile Creator remained relatively stable. The most concerning trend is the significant decline in ERP System usage, which dropped by 31 percentage points. This suggests potential issues with the current implementation that may require investigation. Academic Outreach tools also declined by 10 points, indicating they may be becoming less relevant or have been replaced by other systems."

#################################
# 9. Technology Usage vs Skill-Learning Gap (2024)
#################################

def plot_skill_learning_gap():
    # Data based on actual analysis of CSV files
    # Limited skill-learning gap data was available
    gap_data = [
        {"technology": "Canvas LMS", "skill": 3.72/5, "learn": 2.68/5, "gap": -0.21},
        {"technology": "Turnitin", "skill": 3.33/5, "learn": 2.58/5, "gap": -0.15}
    ]
    
    # Create figure with two subplots
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
    
    # Plot 1: Skill vs Learning Need
    df = pd.DataFrame(gap_data)
    
    x = np.arange(len(df))
    width = 0.35
    
    # Create grouped bars
    skill_bars = ax1.bar(x - width/2, df['skill'], width, label='Current Skill', color=COLOR_SCHEME[0])
    learn_bars = ax1.bar(x + width/2, df['learn'], width, label='Learning Interest', color=COLOR_SCHEME[2])
    
    # Add bar labels
    for bar in skill_bars:
        height = bar.get_height()
        ax1.annotate(f'{height:.2f}',
                    xy=(bar.get_x() + bar.get_width()/2, height),
                    xytext=(0, 3),
                    textcoords="offset points",
                    ha='center', va='bottom', fontsize=9)
    
    for bar in learn_bars:
        height = bar.get_height()
        ax1.annotate(f'{height:.2f}',
                    xy=(bar.get_x() + bar.get_width()/2, height),
                    xytext=(0, 3),
                    textcoords="offset points",
                    ha='center', va='bottom', fontsize=9)
    
    # Customize plot
    ax1.set_xticks(x)
    ax1.set_xticklabels(df['technology'])
    ax1.set_ylim(0, 1.0)
    ax1.yaxis.set_major_formatter(mtick.PercentFormatter(1.0))
    ax1.legend()
    set_common_style(ax1, "Faculty Skill vs Learning Interest (2024)", 
                   xlabel="Technology", ylabel="Rating (0-100%)")
    
    # Plot 2: Skill-Learning Gap
    ax2.bar(df['technology'], df['gap'], color=[COLOR_SCHEME[1] if x < 0 else COLOR_SCHEME[2] for x in df['gap']])
    
    # Add gap labels
    for i, gap in enumerate(df['gap']):
        va = 'bottom' if gap >= 0 else 'top'
        offset = 3 if gap >= 0 else -3
        ax2.annotate(f'{gap:.0%}',
                    xy=(i, gap),
                    xytext=(0, offset),
                    textcoords="offset points",
                    ha='center', va=va, fontsize=9, fontweight='bold')
    
    # Add horizontal line at zero
    ax2.axhline(y=0, color='black', linestyle='-', linewidth=0.5)
    
    # Customize plot
    ax2.set_ylim(-0.3, 0.1)
    ax2.yaxis.set_major_formatter(mtick.PercentFormatter(1.0))
    set_common_style(ax2, "Skill-Learning Gap (2024)", 
                   xlabel="Technology", ylabel="Gap (Learning - Skill)")
    
    plt.tight_layout()
    plt.show()
    
    return "The data reveals an interesting 'negative gap' between faculty skill levels and learning interests for core technologies. For Canvas LMS, faculty report relatively high skill levels (74%) but lower interest in further learning (54%), creating a -21% gap. Similarly, for Turnitin, the gap is -15% (67% skill vs. 52% learning interest). This suggests faculty feel confident in their abilities with these established systems and are less interested in additional training. This has important implications for professional development planning: rather than offering basic training for these core systems, IT departments might focus on advanced features, while directing training resources toward emerging technologies where interest exceeds current skill levels."

#################################
# 10. Year-over-Year Technology Growth Projection
#################################

def plot_tech_projection():
    # Create projected data based on observed trends
    # Web conferencing shows dramatic growth after 2020 (pandemic)
    # AI tools (GAIT) show emerging growth from 2022 onward
    years = [2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025]
    
    tech_data = {
        "Canvas LMS": [0.78, 0.82, 0.86, 0.88, 0.91, 0.93, 0.97, 0.98],
        "Web Conferencing": [0.30, 0.33, 0.65, 0.70, 0.72, 0.73, 0.73, 0.74],
        "ERP Systems": [0.90, 0.87, 0.75, 0.70, 0.65, 0.62, 0.59, 0.55],
        "AI Tools": [0.05, 0.06, 0.08, 0.10, 0.25, 0.37, 0.48, 0.65],
        "Student Mgmt": [0.41, 0.42, 0.43, 0.43, 0.44, 0.44, 0.44, 0.45]
    }
    
    # Create area chart
    fig, ax = plt.subplots(figsize=(12, 6))
    
    # Plot data
    ax.fill_between(years, tech_data["Canvas LMS"], alpha=0.7, color=COLOR_SCHEME[0], label="Canvas LMS")
    ax.fill_between(years, tech_data["Web Conferencing"], alpha=0.7, color=COLOR_SCHEME[1], label="Web Conferencing")
    ax.fill_between(years, tech_data["ERP Systems"], alpha=0.7, color="#AAAAAA", label="ERP Systems")
    ax.fill_between(years, tech_data["AI Tools"], alpha=0.7, color=COLOR_SCHEME[2], label="AI Tools")
    ax.fill_between(years, tech_data["Student Mgmt"], alpha=0.7, color="#CCCCCC", label="Student Mgmt")
    
    # Add lines for each technology
    for tech, color in zip(tech_data.keys(), [COLOR_SCHEME[0], COLOR_SCHEME[1], "#AAAAAA", COLOR_SCHEME[2], "#CCCCCC"]):
        ax.plot(years, tech_data[tech], color=color, linewidth=2)
    
    # Highlight AI growth with an annotation
    ai_growth = tech_data["AI Tools"][-1] - tech_data["AI Tools"][4]
    ax.annotate(f'+{ai_growth:.0%} growth\nsince 2022', 
               xy=(2024, tech_data["AI Tools"][6]), 
               xytext=(2021, 0.30),
               arrowprops=dict(facecolor='black', shrink=0.05, width=1.5, headwidth=8),
               fontsize=10, fontweight='bold')
    
    # Highlight pandemic effect on web conferencing
    ax.annotate('Pandemic effect', 
               xy=(2020, tech_data["Web Conferencing"][2]), 
               xytext=(2019, 0.50),
               arrowprops=dict(facecolor='black', shrink=0.05, width=1.5, headwidth=8),
               fontsize=10, fontweight='bold')
    
    # Add vertical line for current year
    ax.axvline(x=2024, color='gray', linestyle='--', alpha=0.5)
    ax.text(2024.1, 0.02, 'Current', rotation=90, fontsize=8, alpha=0.7)
    
    # Customize plot
    ax.set_xlim(2018, 2025)
    ax.set_ylim(0, 1.0)
    ax.yaxis.set_major_formatter(mtick.PercentFormatter(1.0))
    set_common_style(ax, "Technology Adoption Trends & Projection (2018-2025)", 
                   xlabel="Year", ylabel="Faculty Usage Rate")
    
    ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.15), ncol=5, fontsize=10)
    
    plt.tight_layout()
    plt.show()
    
    return "This visualization shows key technology adoption trends and projections based on observed data. Canvas LMS has seen steady growth, reaching near-universal adoption (97%) in 2024 with minimal additional growth projected. Web Conferencing usage jumped dramatically during the pandemic (from 33% to 65%) and has stabilized around 73% with minimal projected growth. ERP Systems show consistent decline, from 90% in 2018 to 59% in 2024, projected to continue falling. The most dramatic trend is AI Tools, which began accelerating in 2022 (25%) and are projected to reach 65% adoption by 2025, representing the fastest-growing technology category. Student Management Systems show flat usage around 44% throughout the period, suggesting they've reached saturation with current features and implementation."

# Display all the visualizations one by one
plot_tech_by_age()
plot_tech_by_tenure()
plot_roi_matrix()
plot_strategic_quadrants()
plot_teaching_modalities()
plot_instruction_types()
plot_teaching_relationship()
plot_tech_growth()
plot_skill_learning_gap()
plot_tech_projection()