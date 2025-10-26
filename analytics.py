import pandas as pd
from scipy.stats import pearsonr

def top_m_crops_for_state(crop_df, state, years, m=5):
    """
    Returns the top m crops by total production for a given state and list of years.
    """
    df = crop_df[(crop_df['State'] == state) & (crop_df['Year'].isin(years))]
    agg = df.groupby('Crop')['Production'].sum().sort_values(ascending=False).head(m)
    return agg.reset_index().rename(columns={'Production':'TotalProduction'})

def compare_avg_rainfall(rain_df, state_list, years):
    """
    Returns average annual rainfall for each state in state_list over the given years.
    """
    out = {}
    for s in state_list:
        df = rain_df[(rain_df['State'] == s) & (rain_df['Year'].isin(years))]
        out[s] = df['Rainfall_mm'].mean()
    return out

def correlate_production_rainfall(production_ts, rainfall_ts):
    """
    Returns Pearson correlation between production and rainfall series.
    Both should be pandas Series indexed by Year.
    """
    common = production_ts.index.intersection(rainfall_ts.index)
    if len(common) < 5:
        return None, None
    r, p = pearsonr(production_ts.loc[common], rainfall_ts.loc[common])
    return r, p
