#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  8 17:59:31 2025

@author: rishabhjain
"""


import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# Load the most recent dataset
df = pd.read_csv('cleaned_c24.csv')

# Define your specific color scheme
color_black = '#000000'  # Black
color_gray = '#979797'   # Gray
color_gold = '#FFBA08'   # Gold/Yellow

# Function to prepare importance-satisfaction data
def prepare_imp_sat_data(df):
    result = []
    
    # Find matching IMP and DS column pairs
    imp_cols = [col for col in df.columns if col.startswith('IMP_')]
    ds_cols = [col for col in df.columns if col.startswith('DS_')]
    
    for imp_col in imp_cols:
        service_code = imp_col[4:]  # Remove 'IMP_'
        ds_col = f'DS_{service_code}'
        
        # Check if we have both importance and satisfaction data
        if ds_col in ds_cols:
            # Calculate average importance and satisfaction
            imp_avg = df[imp_col].mean()
            ds_avg = df[ds_col].mean()
            
            # Calculate gap
            gap = imp_avg - ds_avg
            
            result.append({
                'service': service_code,
                'importance': imp_avg,
                'satisfaction': ds_avg,
                'gap': gap
            })
    
    return pd.DataFrame(result)

# Prepare the data
imp_sat_data = prepare_imp_sat_data(df)

# Create custom colormap using your exact colors
colors = [color_black, color_gray, color_gold]
custom_cmap = plt.matplotlib.colors.LinearSegmentedColormap.from_list("custom", colors)

# Create the matrix plot
plt.figure(figsize=(12, 10), facecolor='white')

# Create the scatter plot with your color scheme
scatter = plt.scatter(
    imp_sat_data['satisfaction'], 
    imp_sat_data['importance'], 
    s=100,  # Fixed size for all points
    alpha=0.8,
    c=imp_sat_data['gap'],
    cmap=custom_cmap,
    edgecolor='white',
    linewidth=0.5
)

# Add a colorbar
cbar = plt.colorbar(scatter)
cbar.set_label('Gap (Importance - Satisfaction)', color=color_black)

# Add quadrant lines
plt.axvline(x=3, color=color_gray, linestyle='--', alpha=0.7)
plt.axhline(y=3, color=color_gray, linestyle='--', alpha=0.7)

# Label quadrants
plt.text(1.5, 4.5, 'Concentrate here', fontsize=12, color=color_black)
plt.text(4.5, 4.5, 'Keep up the good work', fontsize=12, ha='right', color=color_black)
plt.text(1.5, 1.5, 'Low priority', fontsize=12, color=color_black)
plt.text(4.5, 1.5, 'Possible overkill', fontsize=12, ha='right', color=color_black)

# Add labels for each point
for _, row in imp_sat_data.iterrows():
    plt.annotate(
        row['service'],
        (row['satisfaction'], row['importance']),
        xytext=(3, 3),
        textcoords='offset points',
        fontsize=8,
        color=color_black
    )

# Set titles and labels
plt.title('Importance-Satisfaction Matrix (2024)', fontsize=16, color=color_black)
plt.xlabel('Satisfaction Rating', fontsize=14, color=color_black)
plt.ylabel('Importance Rating', fontsize=14, color=color_black)

# Set axis limits
plt.xlim(1, 5)
plt.ylim(1, 5)
plt.grid(True, linestyle='--', alpha=0.3, color=color_gray)

# Style the tick parameters
plt.tick_params(colors=color_black)

plt.tight_layout()
plt.show()





##222222



# Define your color scheme
color_black = '#000000'  # Black
color_gray = '#979797'   # Gray
color_gold = '#FFBA08'   # Yellow/Gold

# Function to prepare usage by division data
def prepare_usage_by_division():
    # Get all USE_ columns
    use_cols = [col for col in df.columns if col.startswith('USE_')]
    
    # Make sure we have the ADIV column
    if 'ADIV' not in df.columns:
        print("Academic division column (ADIV) not found in dataset")
        return None
    
    # Get unique divisions
    divisions = df['ADIV'].dropna().unique()
    
    # Create a DataFrame to store results
    result_data = []
    
    # Calculate average usage for each service by division
    for div in divisions:
        div_data = df[df['ADIV'] == div]
        
        for col in use_cols:
            service_code = col[4:]  # Remove 'USE_'
            avg_usage = div_data[col].mean()
            
            result_data.append({
                'division': div,
                'service': col,
                'service_name': get_service_name(service_code),
                'usage': avg_usage
            })
    
    return pd.DataFrame(result_data)

# Get service name function (reused from previous code)
def get_service_name(code):
    # Same implementation as before
    service_map = {
        'CMS': 'Content Management System',
        'CMSGB': 'Canvas Grade Book',
        'TMS': 'Technology in Meeting Spaces',
        'STMS': 'Support for Technology in Meeting Spaces',
        'ITS': 'Instructional Technology Support',
        'IDS': 'Instructional Design Services',
        'SWC': 'Web Conferencing',
        'CS': 'Classroom Support',
        'OAV': 'Online Audio/Video',
        'GAIT': 'Generative AI Tools',
        'LSG': 'Learning Support Group',
        'LC': 'Learning Commons',
        'LEC': 'Learning Environment Configuration',
        'FPC': 'Faculty Professional Community',
        'CFUS': 'Copyright and Fair Use Support',
        'BL': 'Borrowing Laptops',
        'VPN': 'Virtual Private Network',
        'AORO': 'Access to Online Resources Off-campus',
        'ERPSS': 'Enterprise Resource Planning System',
        'CWS': 'Campus Wireless System'
    }
    return service_map.get(code, code)

# Prepare the data
usage_by_division = prepare_usage_by_division()

# Create a pivot table for the heatmap
pivot_df = usage_by_division.pivot_table(
    index='division', 
    columns='service_name', 
    values='usage',
    aggfunc='mean'
)

# Sort services by overall usage
service_means = pivot_df.mean().sort_values(ascending=False)
# Select top 10 services for readability
top_services = service_means.head(10).index
pivot_df = pivot_df[top_services]

# Create a custom colormap using your colors (black to gold)
cmap = plt.matplotlib.colors.LinearSegmentedColormap.from_list(
    "custom", [color_black, color_gray, color_gold]
)

# Create the heatmap with your color scheme
plt.figure(figsize=(14, 8), facecolor='white')
heatmap = sns.heatmap(
    pivot_df,
    annot=True,
    cmap=cmap,
    cbar_kws={'label': 'Average Usage (1-5 scale)'},
    fmt='.2f',
    linewidths=0.5,
    linecolor=color_black,
    annot_kws={"color": "white" if color_black else "black"}
)

# Style the colorbar
cbar = heatmap.collections[0].colorbar
cbar.ax.yaxis.set_tick_params(color=color_black)
cbar.outline.set_edgecolor(color_black)
cbar.ax.set_ylabel('Average Usage (1-5 scale)', color=color_black)

# Rotate x-axis labels for better readability
plt.xticks(rotation=45, ha='right', color=color_black)
plt.yticks(color=color_black)

# Set titles and labels
plt.title('Technology Adoption by Academic Division (2024)', fontsize=16, color=color_black)

# Set the figure facecolor
plt.gcf().set_facecolor('white')

plt.tight_layout()

plt.show()



###

# Define your color scheme
color_black = '#000000'  # Black
color_gray = '#979797'   # Gray
color_gold = '#FFBA08'   # Yellow/Gold

# Create a color list using your scheme
colors = [color_black, color_gold, color_gray]

# Prepare service quality data
def prepare_service_quality_data():
    # Define the staff attributes to analyze
    staff_attributes = [
        {'prefix': 'DAHD_', 'name': 'Help Desk Staff'},
        {'prefix': 'DAERPS_', 'name': 'ERP System Support Staff'},
        {'prefix': 'DAIT_', 'name': 'Instructional Technology Staff'},
        {'prefix': 'DAMMS_', 'name': 'Multimedia Services Staff'}
    ]
    
    attribute_types = [
        {'suffix': 'F', 'name': 'Friendly'},
        {'suffix': 'K', 'name': 'Knowledgeable'},
        {'suffix': 'RL', 'name': 'Reliable'},
        {'suffix': 'RS', 'name': 'Responsive'}
    ]
    
    result_data = []
    
    for staff in staff_attributes:
        staff_data = {'service': staff['name']}
        
        has_data = False
        for attr in attribute_types:
            col = staff['prefix'] + attr['suffix']
            if col in df.columns:
                staff_data[attr['name']] = df[col].mean()
                has_data = True
            else:
                # Check if we have the column without the suffix (some may vary in format)
                col_alt = staff['prefix']
                if col_alt in df.columns:
                    staff_data[attr['name']] = df[col_alt].mean()
                    has_data = True
                else:
                    staff_data[attr['name']] = np.nan
        
        if has_data:
            result_data.append(staff_data)
    
    return pd.DataFrame(result_data)

# Create radar chart function
def radar_chart(df, categories, title):
    # Number of variables
    N = len(categories)
    
    # Create angles for each category
    angles = [n / float(N) * 2 * np.pi for n in range(N)]
    angles += angles[:1]  # Close the loop
    
    # Create figure with white background
    fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(polar=True), facecolor='white')
    
    # Draw one axis per variable and add labels
    plt.xticks(angles[:-1], categories, size=12, color=color_black)
    
    # Draw ylabels (setting the limits based on the data)
    ax.set_rlabel_position(0)
    max_val = df[categories].max()
    plt.yticks([1, 2, 3, 4], ['1', '2', '3', '4'], color=color_gray, size=10)
    plt.ylim(0, 5)
    
    # Set grid color
    ax.grid(color=color_gray, linestyle='--', alpha=0.7)
    
    # Color the y-axis labels
    for label in ax.get_yticklabels():
        label.set_color(color_black)
    
    # Plot data
    for i, (idx, row) in enumerate(df.iterrows()):
        values = [row[cat] for cat in categories]
        values += values[:1]  # Close the loop
        
        # Plot values with your custom colors
        color = colors[i % len(colors)]
        ax.plot(angles, values, linewidth=2, linestyle='solid', color=color, label=row['service'])
        ax.fill(angles, values, color=color, alpha=0.2)
    
    # Add legend with custom colors
    plt.legend(loc='upper right', bbox_to_anchor=(0.1, 0.1), frameon=True, 
               facecolor='white', edgecolor=color_black, labelcolor=color_black)
    
    # Add title with custom color
    plt.title(title, size=16, y=1.1, color=color_black)
    
    # Color the spines
    for spine in ax.spines.values():
        spine.set_edgecolor(color_black)
    
    return fig

# Prepare the data
service_quality = prepare_service_quality_data()

# Define the categories (attributes)
categories = ['Friendly', 'Knowledgeable', 'Reliable', 'Responsive']

# Create the radar chart
fig = radar_chart(
    service_quality, 
    categories, 
    'Service Quality Assessment (2024)'
)

plt.tight_layout()

plt.show()

###


# Define your color scheme
color_black = '#000000'  # Black
color_gray = '#979797'   # Gray
color_gold = '#FFBA08'   # Yellow/Gold

# Prepare skill gap data
def prepare_skill_gap_data():
    # Get skill and learning interest columns
    skl_cols = [col for col in df.columns if col.startswith('SKL_')]
    lrn_cols = [col for col in df.columns if col.startswith('LRN_')]
    
    result_data = []
    
    for skl_col in skl_cols:
        service_code = skl_col[4:]  # Remove 'SKL_'
        lrn_col = f'LRN_{service_code}'
        
        # Check if we have matching learning interest data
        if lrn_col in lrn_cols:
            # Calculate average skill and learning interest
            skill_avg = df[skl_col].mean()
            learn_avg = df[lrn_col].mean()
            
            # Get service name
            service_name = get_service_name(service_code)
            
            result_data.append({
                'service': service_code,
                'service_name': service_name,
                'skill': skill_avg,
                'interest': learn_avg,
                'gap': learn_avg - skill_avg  # Positive = interest > skill
            })
    
    return pd.DataFrame(result_data)

# Get service name function (reused from previous code)
def get_service_name(code):
    # Same implementation as before
    service_map = {
        'ERP': 'Enterprise Resource Planning',
        'CMS': 'Content Management System',
        'TMS': 'Technology in Meeting Spaces',
        'OLC': 'Online Learning Commons',
        'SWC': 'Web Conferencing',
        'LCS': 'Lecture Capture Software',
        'PIRO': 'Protecting Identity/Reputation Online',
        'IFE': 'Identifying Fraudulent Emails'
    }
    return service_map.get(code, code)

# Prepare the data
skill_gap_data = prepare_skill_gap_data()

# Sort by absolute gap value for better visualization
skill_gap_data['abs_gap'] = skill_gap_data['gap'].abs()
skill_gap_data = skill_gap_data.sort_values('abs_gap', ascending=False)

# Create the figure with white background
plt.figure(figsize=(12, 8), facecolor='white')

# Plot skill and interest as grouped bars with your color scheme
bar_width = 0.35
x = np.arange(len(skill_gap_data))

plt.bar(x - bar_width/2, skill_gap_data['skill'], bar_width, label='Current Skill Level', 
        color=color_black, edgecolor=color_black)
plt.bar(x + bar_width/2, skill_gap_data['interest'], bar_width, label='Learning Interest', 
        color=color_gold, edgecolor=color_black)

# Add gap lines and labels
for i, row in skill_gap_data.iterrows():
    idx = skill_gap_data.index.get_loc(i)
    plt.plot([idx-bar_width/2, idx+bar_width/2], [row['skill'], row['interest']], 
             color=color_gray, linestyle='-', linewidth=1.5, alpha=0.8)
    plt.annotate(f"{row['gap']:.2f}", 
                 xy=(idx, min(row['skill'], row['interest'])), 
                 xytext=(0, -20 if row['gap'] < 0 else 10), 
                 textcoords='offset points',
                 ha='center',
                 color=color_black,
                 fontweight='bold')

# Set x-axis labels and ticks
plt.xticks(x, skill_gap_data['service_name'], rotation=45, ha='right', color=color_black)
plt.yticks(color=color_black)

# Set titles and labels
plt.title('Faculty Technology Skill vs. Learning Interest (2024)', fontsize=16, color=color_black)
plt.ylabel('Rating (1-5 scale)', fontsize=14, color=color_black)
plt.legend(facecolor='white', edgecolor=color_black, framealpha=1, labelcolor=color_black)
plt.grid(axis='y', linestyle='--', alpha=0.3, color=color_gray)

# Style the axes
for spine in plt.gca().spines.values():
    spine.set_edgecolor(color_black)

plt.tight_layout()

plt.show()




##



# Define your color scheme
color_black = '#000000'  # Black
color_gray = '#979797'   # Gray
color_gold = '#FFBA08'   # Yellow/Gold

# Function to prepare usage comparison data
def prepare_usage_comparison():
    # Get common USE_ columns between both datasets
    use_cols_c18 = [col for col in df_c18.columns if col.startswith('USE_')]
    use_cols_c24 = [col for col in df_c24.columns if col.startswith('USE_')]
    
    common_cols = list(set(use_cols_c18) & set(use_cols_c24))
    
    result_data = []
    
    for col in common_cols:
        service_code = col[4:]  # Remove 'USE_'
        avg_2018 = df_c18[col].mean()
        avg_2024 = df_c24[col].mean()
        
        service_name = get_service_name(service_code)
        
        result_data.append({
            'service': service_code,
            'service_name': service_name,
            '2018': avg_2018,
            '2024': avg_2024,
            'change': avg_2024 - avg_2018
        })
    
    return pd.DataFrame(result_data)

# Get service name function (reused from previous code)
def get_service_name(code):
    # Same implementation as before
    service_map = {
        'CMS': 'Content Management System',
        'TMS': 'Technology in Meeting Spaces',
        'STMS': 'Support for Technology in Meeting Spaces',
        'ITS': 'Instructional Technology Support',
        'SWC': 'Web Conferencing',
        'FPC': 'Faculty Professional Community',
        'VPN': 'Virtual Private Network',
        'AORO': 'Access to Online Resources Off-campus',
        'ERPSS': 'Enterprise Resource Planning System',
        'CWS': 'Campus Wireless System'
    }
    return service_map.get(code, code)

# Prepare the data
usage_comparison = prepare_usage_comparison()

# Sort by 2024 usage for better visualization
usage_comparison = usage_comparison.sort_values('2024', ascending=False)

# Create the figure with white background
plt.figure(figsize=(14, 8), facecolor='white')

# Plot usage comparison as grouped bars with your color scheme
bar_width = 0.35
x = np.arange(len(usage_comparison))

plt.bar(x - bar_width/2, usage_comparison['2018'], bar_width, label='2018', 
        color=color_gray, edgecolor=color_black)
plt.bar(x + bar_width/2, usage_comparison['2024'], bar_width, label='2024', 
        color=color_gold, edgecolor=color_black)

# Add change arrows and percentages
for i, row in usage_comparison.iterrows():
    idx = usage_comparison.index.get_loc(i)
    if not np.isnan(row['change']):
        # Calculate percentage change
        if row['2018'] > 0:
            pct_change = (row['change'] / row['2018']) * 100
            pct_label = f"{pct_change:.1f}%"
        else:
            pct_label = "N/A"
            
        y_pos = max(row['2018'], row['2024']) + 0.2
        arrow_color = color_black
        
        # Add arrow
        plt.annotate(
            pct_label,
            xy=(idx, y_pos),
            xytext=(0, 5),
            textcoords='offset points',
            ha='center',
            va='bottom',
            color=arrow_color,
            fontweight='bold'
        )

# Set x-axis labels and ticks
plt.xticks(x, usage_comparison['service_name'], rotation=45, ha='right', color=color_black)
plt.yticks(color=color_black)

# Set titles and labels
plt.title('Technology Usage Comparison (2018 vs 2024)', fontsize=16, color=color_black)
plt.ylabel('Average Usage (1-5 scale)', fontsize=14, color=color_black)
plt.legend(facecolor='white', edgecolor=color_black, framealpha=1, labelcolor=color_black)
plt.grid(axis='y', linestyle='--', alpha=0.3, color=color_gray)

# Style the axes
for spine in plt.gca().spines.values():
    spine.set_edgecolor(color_black)

plt.tight_layout()

plt.show()



#@

# Define your color scheme
color_black = '#000000'  # Black
color_gray = '#979797'   # Gray
color_gold = '#FFBA08'   # Yellow/Gold

# Calculate device ownership percentages
devices = ['Laptop Computer', 'Smart Phone']
ownership_percentages = [
    df['OWN_LC'].mean() * 100,
    df['OWN_PDA'].mean() * 100
]

# Create figure with white background
plt.figure(figsize=(10, 6), facecolor='white')

# Create bars with your colors
bars = plt.bar(devices, ownership_percentages, color=[color_black, color_gold], 
               edgecolor=color_black, linewidth=1)

# Add percentage labels on top of bars
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2., height + 1,
             f'{height:.1f}%',
             ha='center', va='bottom', fontsize=12, 
             color=color_black, fontweight='bold')

# Set titles and labels with your colors
plt.title('Faculty Device Ownership (2024)', fontsize=16, color=color_black)
plt.ylabel('Percentage of Faculty (%)', fontsize=14, color=color_black)
plt.ylim(0, 105)  # Set y-axis limit to accommodate percentages and labels

# Style the tick labels
plt.xticks(color=color_black)
plt.yticks(color=color_black)

# Style the grid
plt.grid(axis='y', linestyle='--', alpha=0.3, color=color_gray)

# Style the axes
for spine in plt.gca().spines.values():
    spine.set_edgecolor(color_black)

plt.tight_layout()
plt.savefig('device_ownership.png', dpi=300, facecolor='white')
plt.show()







