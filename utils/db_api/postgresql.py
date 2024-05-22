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

    async def create_table_kelishuvBitim(self):
        sql = """
        CREATE TABLE IF NOT EXISTS kelishuvBitimlari (
        id SERIAL PRIMARY KEY,
        fayl TEXT,
        data BYTEA
        );
        """
        await self.execute(sql, execute=True)

    async def create_table_mehnatMunosabatlari(self):
        sql = """
           CREATE TABLE IF NOT EXISTS mehnatMunosabatlari (
           id SERIAL PRIMARY KEY,
           fayl1 TEXT,
           data1 BYTEA
           );
           """
        await self.execute(sql, execute=True)

    async def create_table_fuqorolikShartnomasi(self):
        sql = """
           CREATE TABLE IF NOT EXISTS fuqorolikShartnomasi (
           id SERIAL PRIMARY KEY,
           fayl2 TEXT,
           data2 BYTEA
           );
           """
        await self.execute(sql, execute=True)

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

    async def add_kelishuvBitimlari(self, fayl: str, data: bytes):
        sql = "INSERT INTO kelishuvBitimlari (fayl, data) VALUES ($1, $2) returning *"
        return await self.execute(sql, fayl, data, fetchrow=True)

    async def add_mehnatMunosabatlari(self, fayl1: str, data1: bytes):
        sql = "INSERT INTO mehnatMunosabatlari (fayl1, data1) VALUES ($1, $2) returning *"
        return await self.execute(sql, fayl1, data1, fetchrow=True)

    async def add_fuqorolikShartnomasi(self, fayl2: str, data2: bytes):
        sql = "INSERT INTO fuqorolikShartnomasi (fayl2, data2) VALUES ($1, $2) returning *"
        return await self.execute(sql, fayl2, data2, fetchrow=True)

    async def add_shaxsiyTarkib(self, fayl3: str, data3: bytes):
        sql = "INSERT INTO shaxsiyTarkib (fayl3, data3) VALUES ($1, $2) returning *"
        return await self.execute(sql, fayl3, data3, fetchrow=True)

    async def add_tatil(self, fayl4: str, data4: bytes):
        sql = "INSERT INTO tatil (fayl4, data4) VALUES ($1, $2) returning *"
        return await self.execute(sql, fayl4, data4, fetchrow=True)

    async def add_umumiyMasala(self, fayl5: str, data5: bytes):
        sql = "INSERT INTO umumiyMasala (fayl5, data5) VALUES ($1, $2) returning *"
        return await self.execute(sql, fayl5, data5, fetchrow=True)

    async def get_all_kelishuvBitimlari(self):
        sql = "SELECT id, fayl, data FROM kelishuvBitimlari"
        return await self.execute(sql, fetch=True)

    async def get_all_mehnatMunosabatlari(self):
        sql = "SELECT id, fayl1, data1 FROM mehnatMunosabatlari"
        return await self.execute(sql, fetch=True)

    async def get_all_fuqorolikShartnomasi(self):
        sql = "SELECT id, fayl2, data2 FROM fuqorolikShartnomasi"
        return await self.execute(sql, fetch=True)

    async def get_all_shaxsiyTarkib(self):
        sql = "SELECT id, fayl3, data3 FROM shaxsiyTarkib"
        return await self.execute(sql, fetch=True)

    async def get_all_tatil(self):
        sql = "SELECT id, fayl4, data4 FROM tatil"
        return await self.execute(sql, fetch=True)

    async def get_all_umumiyMasala(self):
        sql = "SELECT id, fayl5, data5 FROM umumiyMasala"
        return await self.execute(sql, fetch=True)

    # Jadvaldagi barcha yozuvlarni o'chirish
    async def delete_all_kelishuvBitimlari(self, table_name: str):
        table_name = await self.table_exists(table_name)
        if table_name:
            sql = "DELETE FROM kelishuvBitimlari"
            return await self.execute(sql, execute=True)
        else:
            return f"Bunday bazza mavud emas yoki bazaga ma'lumot joylanmagan. Bazaga malumot joylang"
    async def delete_all_mehnatMunosabatlari(self, table_name: str):
        table_name = await self.table_exists(table_name)
        if table_name:
            sql = "DELETE FROM mehnatMunosabatlari"
            print("uchdi mehnat munosabatlari")
            return await self.execute(sql, execute=True)
        else:
            return f"Bunday bazza mavud emas yoki bazaga ma'lumot joylanmagan. Bazaga malumot joylang"
    async def delete_all_fuqorolikShartnomasi(self, table_name: str):
        table_name = await self.table_exists(table_name)
        if table_name:
            sql = "DELETE FROM fuqorolikShartnomasi"
            return await self.execute(sql, execute=True)
        else:
            return f"Bunday bazza mavud emas yoki bazaga ma'lumot joylanmagan. Bazaga malumot joylang"
    async def delete_all_shaxsiyTarkib(self, table_name: str):
        table_name = await self.table_exists(table_name)
        if table_name:
            sql = "DELETE FROM shaxsiyTarkib"
            return await self.execute(sql, execute=True)
        else:
            return f"Bunday bazza mavud emas yoki bazaga ma'lumot joylanmagan. Bazaga malumot joylang"
    async def delete_all_tatil(self, table_name: str):
        table_name = await self.table_exists(table_name)
        if table_name:
            sql = "DELETE FROM tatil"
            print("qale")
            return await self.execute(sql, execute=True)
        else:
            return f"Bunday bazza mavud emas yoki bazaga ma'lumot joylanmagan. Bazaga malumot joylang"
    async def delete_all_umumiyMasala(self, table_name: str):
        table_name = await self.table_exists(table_name)
        if table_name:
            sql = "DELETE FROM umumiyMasala"
            return await self.execute(sql, execute=True)
        else:
            return f"Bunday bazza mavud emas yoki bazaga ma'lumot joylanmagan. Bazaga malumot joylang"
# Bazani ishga tushirish misol
# db = Database()
# await db.create()

    # async def select_all_users(self):
    #     sql = "SELECT * FROM Users"
    #     return await self.execute(sql, fetch=True)
    #
    # async def select_user(self, **kwargs):
    #     sql = "SELECT * FROM Users WHERE"
    #     sql, parametrs = self.format_args(sql, parametrs=kwargs)
    #     return await self.execute(sql, *parametrs, fetchrow=True)
    #
    # async def count_users(self):
    #     sql = "SELECT COUNT(*) FROM Users"
    #     return await self.execute(sql, fetchval=True)
    #
    # async def update_user_username(self, full_name, tel, parol):
    #     sql = "UPDATE Users SET tel = $1 WHERE full_name = $2 AND parol = $3"
    #     return await self.execute(sql, full_name, tel, parol, execute=True)
    #
    # async def delete_user(self):
    #     await self.execute("DELETE FROM Users WHERE TRUE", execute=True)
    #
    # async def drop_users(self):
    #     await self.execute("DROP TABLE Users", execute=True)
    #
    # async def select_ariza_by_user_id(self, user_id: int):
    #     sql = "SELECT * FROM Ariza WHERE user_id = $1"
    #     return await self.execute(sql, user_id, fetch=True)
    #
    # async def add_ariza(self, user_id: int, ariza_matni: str):
    #     sql = "INSERT INTO Ariza (user_id, ariza_matni) VALUES ($1, $2) returning *"
    #     return await self.execute(sql, user_id, ariza_matni, fetchrow=True)
    #
    # async def connect_to_db(self):
    #     return await asyncpg.connect(user='postgres', password='123',
    #                                  database='jdpu', host='localhost')
    #
    # async def check_login(self, tel: str):
    #     db = await self.connect_to_db()
    #     try:
    #         query = "SELECT * FROM users WHERE tel = $1"
    #         result = await db.fetchrow(query, tel)
    #         return bool(result)
    #     finally:
    #         await db.close()
    #
    # async def authenticate_user(self, tel: str, parol: int):
    #     db = await self.connect_to_db()
    #     try:
    #         query = "SELECT * FROM users WHERE tel = $1 AND parol = $2"
    #         result = await db.fetchrow(query, tel, parol)
    #         if result:
    #             user_id = result['id']
    #             return user_id
    #         else:
    #             return None
    #     finally:
    #         await db.close()
    #
    # async def check_tel_in_db(self, tel: str):
    #     sql = "SELECT * FROM Users WHERE tel = $1"
    #     result = await self.execute(sql, tel, fetchrow=True)
    #     return result is not None  # Agar foydalanuvchi bazada mavjud bo'lsa True, aks holda False qaytaradi
