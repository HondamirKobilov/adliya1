import asyncpg
from typing import Union
from data import config

class Database:
    def __init__(self):
        self.pool: Union[asyncpg.Pool, None] = None

    async def create(self):
        if self.pool is None:
            self.pool = await asyncpg.create_pool(
                user=config.DB_USER,
                password=config.DB_PASS,
                host=config.DB_HOST,
                database=config.DB_NAME
            )
            # Jadval mavjudligini tekshirish va kerak bo'lsa yaratish
            if not await self.table_exists('mehnatMunosabatlari'):
                await self.create_table_mehnatMunosabatlari()

    async def table_exists(self, table_name):
        query = """
        SELECT EXISTS (
            SELECT 1 
            FROM information_schema.tables 
            WHERE table_schema = 'public' 
            AND table_name = $1
        );
        """
        async with self.pool.acquire() as connection:
            result = await connection.fetchval(query, table_name)
            return result

    async def execute(self, command, *args,
                      fetch: bool = False,
                      fetchval: bool = False,
                      fetchrow: bool = False,
                      execute: bool = False):
        if self.pool is None:
            raise ValueError("Connection pool is not initialized.")

        async with self.pool.acquire() as connection:
            connection: asyncpg.Connection
            async with connection.transaction():
                if fetch:
                    result = await connection.fetch(command, *args)
                elif fetchval:
                    result = await connection.fetchval(command, *args)
                elif fetchrow:
                    result = await connection.fetchrow(command, *args)
                elif execute:
                    result = await connection.execute(command, *args)
            return result
    async def create_table_shaxsiyTarkib(self):
        sql = """
           CREATE TABLE IF NOT EXISTS shaxsiyTarkib (
           id SERIAL PRIMARY KEY,
           fayl3 TEXT,
           data3 BYTEA
           );
           """
        await self.execute(sql, execute=True)
    async def create_table_tatil(self):
        sql = """
           CREATE TABLE IF NOT EXISTS tatil (
           id SERIAL PRIMARY KEY,
           fayl4 TEXT,
           data4 BYTEA
           );
           """
        await self.execute(sql, execute=True)
    async def create_table_umumiyMasala(self):
        sql = """
           CREATE TABLE IF NOT EXISTS umumiyMasala(
           id SERIAL PRIMARY KEY,
           fayl5 TEXT,
           data5 BYTEA
           );
           """
        await self.execute(sql, execute=True)
    async def add_shaxsiyTarkib(self, fayl3: str, data3: bytes):
        sql = "INSERT INTO shaxsiyTarkib (fayl3, data3) VALUES ($1, $2) returning *"
        return await self.execute(sql, fayl3, data3, fetchrow=True)
    async def add_tatil(self, fayl4: str, data4: bytes):
        sql = "INSERT INTO tatil (fayl4, data4) VALUES ($1, $2) returning *"
        return await self.execute(sql, fayl4, data4, fetchrow=True)
    async def add_umumiyMasala(self, fayl5: str, data5: bytes):
        sql = "INSERT INTO tatil (fayl5, data5) VALUES ($1, $2) returning *"
        return await self.execute(sql, fayl5, data5, fetchrow=True)

    async def get_all_shaxsiyTarkib(self):
        sql = "SELECT id, fayl3, data3 FROM shaxsiyTarkib"
        return await self.execute(sql, fetch=True)
    async def get_all_tatil(self):
        sql = "SELECT id, fayl4, data4 FROM tatil"
        return await self.execute(sql, fetch=True)
    async def get_all_umumiyMasala(self):
        sql = "SELECT id, fayl5, data5 FROM umumiyMasala"
        return await self.execute(sql, fetch=True)