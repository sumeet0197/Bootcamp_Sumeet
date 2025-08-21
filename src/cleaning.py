from __future__ import annotations
import pandas as pd

def fill_missing_median(df: pd.DataFrame, cols: list[str]) -> pd.DataFrame:
    """Fill missing numeric values with column median."""
    out = df.copy()
    for c in cols:
        if c in out.columns:
            out[c] = out[c].fillna(out[c].median())
    return out

def drop_missing(df: pd.DataFrame, thresh: float = 0.95) -> pd.DataFrame:
    """Drop rows where non-null fraction < thresh (keep rows mostly complete)."""
    keep = df.notna().mean(axis=1) >= thresh
    return df.loc[keep].copy()

def normalize_data(df: pd.DataFrame, cols: list[str]) -> pd.DataFrame:
    """Min-max scale columns to [0,1]. Ignores non-numeric columns not in cols."""
    out = df.copy()
    for c in cols:
        if c in out.columns:
            mn = out[c].min()
            mx = out[c].max()
            if pd.notna(mn) and pd.notna(mx) and mx != mn:
                out[c] = (out[c] - mn) / (mx - mn)
    return out
