import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import ttest_ind

def calculate_relative_frequencies(input_file='cell-count.csv', output_file='relative_frequencies.csv'):
    # Load data
    df = pd.read_csv(input_file)

    # Calculate total cell count and relative frequencies
    df.loc[:, 'total_count'] = df[['b_cell', 'cd8_t_cell', 'cd4_t_cell', 'nk_cell', 'monocyte']].sum(axis=1)
    
    # Melt to long format for easier processing
    melted_df = df.melt(id_vars=['sample', 'total_count'], 
                         value_vars=['b_cell', 'cd8_t_cell', 'cd4_t_cell', 'nk_cell', 'monocyte'],
                         var_name='population', 
                         value_name='count')

    # Calculate percentages
    melted_df['percentage'] = (melted_df['count'] / melted_df['total_count']) * 100

    # Save to CSV
    melted_df.to_csv(output_file, index=False)
    print(f'Relative frequencies saved to {output_file}')

def plot_boxplots(input_file='cell-count.csv', output_file='boxplots.png'):
    # Load data
    df = pd.read_csv(input_file)
    pbmc_df = df.loc[(df['sample_type'] == 'PBMC') & (df['treatment'] == 'tr1')].copy()

    # Calculate total count and percentages
    pbmc_df.loc[:, 'total_count'] = pbmc_df[['b_cell', 'cd8_t_cell', 'cd4_t_cell', 'nk_cell', 'monocyte']].sum(axis=1)
    melted_df = pbmc_df.melt(id_vars=['sample', 'total_count', 'response'], 
                               value_vars=['b_cell', 'cd8_t_cell', 'cd4_t_cell', 'nk_cell', 'monocyte'],
                               var_name='population', 
                               value_name='count')
    melted_df['percentage'] = (melted_df['count'] / melted_df['total_count']) * 100

    # Plot boxplots
    plt.figure(figsize=(12, 8))
    sns.boxplot(x='population', y='percentage', hue='response', data=melted_df)
    plt.title('Cell Population Relative Frequencies: Responders vs Non-Responders')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(output_file)
    print(f'Boxplots saved to {output_file}\n')

def perform_statistical_analysis(input_file='cell-count.csv'):
    # Load data
    df = pd.read_csv(input_file)
    pbmc_df = df.loc[(df['sample_type'] == 'PBMC') & (df['treatment'] == 'tr1')].copy()

    # Calculate total count and percentages
    pbmc_df.loc[:, 'total_count'] = pbmc_df[['b_cell', 'cd8_t_cell', 'cd4_t_cell', 'nk_cell', 'monocyte']].sum(axis=1)
    melted_df = pbmc_df.melt(id_vars=['sample', 'total_count', 'response'], 
                               value_vars=['b_cell', 'cd8_t_cell', 'cd4_t_cell', 'nk_cell', 'monocyte'],
                               var_name='population', 
                               value_name='count')
    melted_df['percentage'] = (melted_df['count'] / melted_df['total_count']) * 100

    # Perform t-tests for each population
    results = []
    for population in melted_df['population'].unique():
        pop_data = melted_df[melted_df['population'] == population]
        responders = pop_data[pop_data['response'] == 'y']['percentage']
        non_responders = pop_data[pop_data['response'] == 'n']['percentage']
        t_stat, p_val = ttest_ind(responders, non_responders)
        results.append({'population': population, 't_stat': t_stat, 'p_val': p_val})

    results_df = pd.DataFrame(results)
    print('Statistical Analysis Results:')
    print(results_df)

def main():
    # Task 1: Convert counts to percentages
    print("\n---Task 1: Converting cell counts to percentages and analyzing relative frequencies---")
    calculate_relative_frequencies()
    
    # Task 2: Responder vs non-responder analysis
    print("\n---Task 2: Analyzing responders vs non-responders---")
    plot_boxplots()
    perform_statistical_analysis()

if __name__ == "__main__":
    main()