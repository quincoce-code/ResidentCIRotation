
import matplotlib.pyplot as plt
import numpy as np

def generate_QC_graph(df, analyzer_name, mean, sd, ref_lower, ref_upper, box_color='lightblue'):
    """
    Generate a box-and-whisker plot with QC values using a pandas DataFrame.
    
    Parameters:
    -----------
    df : pandas.DataFrame
        DataFrame with columns: timestamp, qc_value, patient_result
    analyzer_name : str
        Name of the analyzer for the title
    mean : float
        Mean value for control lines
    sd : float
        Standard deviation for control lines
    ref_lower : float
        Lower reference range value
    ref_upper : float
        Upper reference range value
    box_color : str
        Color for the box plot boxes (default: 'lightblue')
    """
    
    # Group by QC timestamp
    grouped = df.groupby('timestamp')
    
    # Prepare data for box plot
    data_to_plot = [group['patient_result'].values for name, group in grouped]
    qc_values_list = [group['qc_value'].iloc[0] for name, group in grouped]
    
    # Create labels for each QC run
    qc_labels = [f"Day {i+1}\nQC: {qc_val}" for i, qc_val in enumerate(qc_values_list)]
    
    # Create box and whisker plot
    plt.figure(figsize=(16, 8))

    # Add control lines
    plt.axhline(y=mean, color='green', linestyle='-', linewidth=2, label='Mean')
    plt.axhline(y=mean + sd, color='yellow', linestyle='--', linewidth=1, label='+1 SD')
    plt.axhline(y=mean - sd, color='yellow', linestyle='--', linewidth=1, label='-1 SD')
    plt.axhline(y=mean + 2*sd, color='orange', linestyle='--', linewidth=1, label='+2 SD')
    plt.axhline(y=mean - 2*sd, color='orange', linestyle='--', linewidth=1, label='-2 SD')
    plt.axhline(y=mean + 3*sd, color='red', linestyle='--', linewidth=1, label='+3 SD')
    plt.axhline(y=mean - 3*sd, color='red', linestyle='--', linewidth=1, label='-3 SD')
    
    # Add reference range lines
    plt.axhline(y=ref_lower, color='purple', linestyle=':', linewidth=1.5, label='Reference Range')
    plt.axhline(y=ref_upper, color='purple', linestyle=':', linewidth=1.5)
    
    
    positions = list(range(1, len(data_to_plot) + 1))
    
    bp = plt.boxplot(data_to_plot, positions=positions, labels=qc_labels, patch_artist=True)
    
    # Plot QC values on same x-axis
    plt.plot(positions, qc_values_list, marker='o', linestyle='-', color='blue', markersize=6, linewidth=2, label='QC Value')
    
    # Color the boxes
    for patch in bp['boxes']:
        patch.set_facecolor(box_color)
    
    plt.xlabel('QC Run (Day and QC Value)')
    plt.ylabel(f'{analyzer_name} Result')
    plt.title(f'Box and Whisker Plot of Patient {analyzer_name} Results by QC Run')
    plt.legend(loc='best')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.grid(True, alpha=0.3, axis='y')
    plt.show()