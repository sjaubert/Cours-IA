import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Set style
sns.set_theme(style="whitegrid")
plt.rcParams['figure.figsize'] = (12, 8)

# Load data
file_path = 'annual-industrial-robots-installed.csv'
df = pd.read_csv(file_path)

# Separate World data and Country data
df_world = df[df['Entity'] == 'World']
df_countries = df[df['Entity'] != 'World']

# Ensure Year is integer
df['Year'] = df['Year'].astype(int)

# Create output directory for images if it doesn't exist
output_dir = 'analysis_output'
os.makedirs(output_dir, exist_ok=True)

# --- Plot 1: Evolution of Annual Installations by Country ---
plt.figure()
sns.lineplot(data=df_countries, x='Year', y='Annual industrial robots installed', hue='Entity', marker='o', linewidth=2.5)
plt.title('Evolution of Annual Industrial Robot Installations (Top 5 Countries)', fontsize=16)
plt.ylabel('Number of Robots Installed', fontsize=12)
plt.xlabel('Year', fontsize=12)
plt.legend(title='Country', title_fontsize='12', fontsize='10')
plt.tight_layout()
plt.savefig(f'{output_dir}/1_evolution_by_country.png')
plt.close()

# --- Plot 2: Installations in 2023 ---
df_2023 = df_countries[df_countries['Year'] == 2023].sort_values('Annual industrial robots installed', ascending=False)
plt.figure()
sns.barplot(data=df_2023, x='Annual industrial robots installed', y='Entity', palette='viridis')
plt.title('Industrial Robot Installations in 2023', fontsize=16)
plt.xlabel('Number of Robots Installed', fontsize=12)
plt.ylabel('Country', fontsize=12)
for index, value in enumerate(df_2023['Annual industrial robots installed']):
    plt.text(value, index, f' {value:,}', va='center')
plt.tight_layout()
plt.savefig(f'{output_dir}/2_installations_2023.png')
plt.close()

# --- Plot 3: Market Share Evolution (Stacked Area) ---
# Pivot data for stacked plot
df_pivot = df_countries.pivot(index='Year', columns='Entity', values='Annual industrial robots installed')
df_pivot = df_pivot.fillna(0)

plt.figure()
df_pivot.plot(kind='area', stacked=True, alpha=0.8, colormap='tab10', figsize=(12, 8))
plt.title('Cumulative Evolution of Installations (Top 5 Countries)', fontsize=16)
plt.ylabel('Number of Robots Installed', fontsize=12)
plt.xlabel('Year', fontsize=12)
plt.legend(title='Country', loc='upper left')
plt.tight_layout()
plt.savefig(f'{output_dir}/3_cumulative_evolution.png')
plt.close()

# --- Plot 4: World Total Evolution ---
plt.figure()
sns.lineplot(data=df_world, x='Year', y='Annual industrial robots installed', marker='o', color='black', linewidth=3)
plt.title('Global Annual Industrial Robot Installations', fontsize=16)
plt.ylabel('Number of Robots Installed', fontsize=12)
plt.xlabel('Year', fontsize=12)
plt.grid(True, linestyle='--')

# Annotate values
for x, y in zip(df_world['Year'], df_world['Annual industrial robots installed']):
    plt.text(x, y+10000, f'{y:,}', ha='center', fontsize=9)

plt.tight_layout()
plt.savefig(f'{output_dir}/4_world_evolution.png')
plt.close()

print("Analysis complete. Images saved in 'analysis_output' directory.")
