from tortoise import Tortoise, run_async

async def main():
    await Tortoise.init(
        db_url='sqlite://db.sqlite3',
        modules={'models': ['main']}
    )
    await Tortoise.generate_schemas()

if __name__ == '__main__':
    run_async(main())
