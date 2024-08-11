import asyncio
import asyncpg
from datetime import datetime
from dataclasses import dataclass
import configparser

config = configparser.ConfigParser()
config.read('database.ini')


@dataclass
class Summary:
    id: int
    published: datetime
    message: str

async def get_summarize():
    conn = await asyncpg.connect(
        host=config.get('postgresdb', 'host'),
        user=config.get('postgresdb', 'user'),
        password=config.get('postgresdb', 'password'),
        database=config.get('postgresdb', 'database')
    )
    cursor = await conn.fetch(
        """
        SELECT 
            id AS id, 
            published AS published, 
            message AS message
        FROM 
            message 
        WHERE 
            id = 1
        """
    )
    sums = []
    for row in cursor:
        sums.append(Summary(
            id=row["id"],
            published=row["published"],
            message=row["message"]
        ))
    return sums
