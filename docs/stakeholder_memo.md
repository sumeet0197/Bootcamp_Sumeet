# Stakeholder Memo (1-pager)

**Project:** Market & Macro Mini-Pipeline  
**Stakeholder:** Portfolio Manager (PM)  
**User:** Junior Analyst  

## Pain Points
- Needs quick, reproducible data for daily questions (prices & company table).
- Prefers outputs they can trust (validated shapes/dtypes, clear file names).
- Limited time; wants a single, simple notebook per task.

## What We Deliver
- Reproducible ingestion (AAPL via yfinance, S&P 500 table via Wikipedia).
- Validations (required columns, NA counts) and timestamped raw files.
- Cleaned dataset and summaries/plots for descriptive questions.

## Decisions Unlocked
- “How did AAPL move in a specific window?”
- “Which sectors dominate the S&P 500?”
- “Can we export reliable CSV/Parquet for other tools?”

## Risks & Assumptions
- Wikipedia table layout may change → resilient selectors, checks.
- Internet required; fallback guidance provided.
- No PII; licensing is public and educational use.
