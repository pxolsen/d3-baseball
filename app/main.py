import asyncio
from ingestion.ingest_teams import check_and_populate_teams

asyncio.run(check_and_populate_teams())