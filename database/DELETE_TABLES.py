from database.connect import Cursor


def delete_table_produtos() -> None:
    with Cursor() as cursor:
        cursor.execute("""
            DROP TABLE IF EXISTS produtos;
        """)
    return None


def delete_table_tipos() -> None:
    with Cursor() as cursor:
        cursor.execute("""
            DROP TABLE IF EXISTS tipos;
        """)
    return None


def delete_tables():
    delete_table_produtos()
    delete_table_tipos()
    return None


if __name__ == '__main__':
    delete_tables()

