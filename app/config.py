from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent  # d3_baseball/
DATA_RAW_DIR = BASE_DIR / 'data' / 'raw'
DATA_PROCESSED_DIR = BASE_DIR / 'data' / 'processed'