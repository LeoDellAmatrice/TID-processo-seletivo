from typing import Any

from database.connect import Cursor

def get_all() -> list[dict[str, Any]]:
    with Cursor(commit=False, dict_cursor=True) as cursor:
        cursor.execute("""
            SELECT 
                p.id,
                p.nome,
                t.nome AS tipo,
                p.quantidade,
                p.preco
            FROM produtos p
            JOIN tipos t ON p.tipo_id = t.id;
        """)
        return cursor.fetchall()

def get_produto(produto_id: int) -> dict[str, Any]:
    with Cursor(commit=False, dict_cursor=True) as cursor:
        cursor.execute("""
            SELECT 
                p.id,
                p.nome,
                t.nome AS tipo,
                p.quantidade,
                p.preco
            FROM produtos p
            JOIN tipos t ON p.tipo_id = t.id
            WHERE p.id = %s;
        """, (produto_id,))
        return cursor.fetchone()

def get_tipos() -> list[dict[str, int]]:
    with Cursor(commit=False, dict_cursor=True) as cursor:
        cursor.execute("""
            SELECT id, nome FROM tipos;
        """)
        return cursor.fetchall()


def post_produto(dados: dict[str, Any]) -> None:
    with Cursor() as cursor:
        cursor.execute("""
            INSERT INTO 
                produtos (nome, tipo_id, 
                          quantidade, preco) 
            VALUES (%s, %s, %s, %s);
        """, (dados['nome'], dados['tipo'], dados['quantidade'], dados['preco']))
    return None

def put_produto(dados: dict[str, Any]) -> None:
    with Cursor() as cursor:
        cursor.execute("""
            UPDATE produtos SET 
                nome = %s, tipo_id = %s, 
                quantidade = %s, preco = %s
            WHERE id = %s;
        """, (dados['nome'], dados['tipo'], dados['quantidade'], dados['preco'], dados['id']))
    return None

def delete_produto(produto_id: int) -> None:
    with Cursor() as cursor:
        cursor.execute("""
            DELETE FROM produtos WHERE id = %s;
        """, (produto_id,))
    return None

if __name__ == '__main__':
    print(get_all())
    print(get_tipos())

