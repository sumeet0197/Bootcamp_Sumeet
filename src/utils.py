from __future__ import annotations
import pandas as pd

def _safe_describe(df: pd.DataFrame) -> pd.DataFrame:
    """
    Works on old and new pandas:
    - Tries datetime_is_numeric=True (newer pandas)
    - Falls back to converting datetimes to int64 ns for older pandas
    """
    try:
        return df.describe(include='all', datetime_is_numeric=True)
    except TypeError:
        # Older pandas: convert datetimes to int64 so describe() works
        df2 = df.copy()
        dt_cols = df2.select_dtypes(include=["datetime64[ns]", "datetime64[ns, UTC]"]).columns
        for c in dt_cols:
            df2[c] = df2[c].view("int64")  # ns since epoch
        return df2.describe(include='all')

def get_summary_stats(df: pd.DataFrame, by: str | None = None):
    """Return (.describe table, groupby table) if `by` present, else just describe."""
    summary = _safe_describe(df)
    if by is not None and by in df.columns:
        g = df.groupby(by).agg(['count','mean','std','min','max'])
        # flatten MultiIndex columns
        g.columns = ['_'.join([c for c in col if c]) for col in g.columns.to_flat_index()]
        return summary, g
    return summary
