import asyncpg
import os
from dotenv import load_dotenv
from scraping.team_scraper import scrape_teams, save_teams_to_json
from utils.s3_utils import upload_file_to_s3
from config import DATA_RAW_DIR

load_dotenv() 

async def check_and_populate_teams():
    conn = await asyncpg.connect(dsn=os.getenv("DATABASE_URL"))

    count = await conn.fetchval("SELECT COUNT(*) FROM team;")
    if count == 0:
        print("No team data found. Running team scraper...")
        teams = scrape_teams()
        filepath = save_teams_to_json(teams, DATA_RAW_DIR)
        s3_key = f"teams/{os.path.basename(filepath)}"
        upload_file_to_s3(filepath, s3_key)

        for team in teams:
            await conn.execute(
                """
                INSERT INTO team (name, city, state, type, conference, division)
                VALUES ($1, $2, $3, $4, $5, $6)
                """,
                team['name'],
                team['city'],
                team['state'],
                team['type'],
                team['conference'],
                team['division']
            )
    else:
        print(f"{count} teams already exist in the database.")
    await conn.close()