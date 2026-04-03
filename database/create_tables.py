from database.connect import Cursor


def create_table_produtos() -> None:
    with Cursor() as cursor:
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS produtos (
                id SERIAL PRIMARY KEY,
                nome VARCHAR(100) NOT NULL,
                tipo_id INTEGER NOT NULL,
                quantidade INTEGER NOT NULL CHECK (quantidade >= 0),
                preco NUMERIC(10,2) NOT NULL CHECK (preco >= 0),
                descricao TEXT,
            
                CONSTRAINT fk_tipo
                    FOREIGN KEY (tipo_id)
                    REFERENCES tipos(id)
                    ON DELETE RESTRICT
            );""")
    return None

def create_table_tipos() -> None:
    with Cursor() as cursor:
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS tipos (
                id SERIAL PRIMARY KEY,
                nome VARCHAR(50) NOT NULL UNIQUE
            );""")
    return None

def seeder_table_produtos() -> None:
    with Cursor() as cursor:
        cursor.execute("""
            SELECT * FROM produtos;
        """)
        if cursor.rowcount > 0:
            return None
        cursor.execute("""
            INSERT INTO produtos (nome, tipo_id, quantidade, preco, descricao) VALUES
            ('Rosa Vermelha', 1, 10, 15.50, 'Flor clássica para presentes'),
            ('Vaso Ceramico Médio', 2, 5, 45.00, 'Vaso resistente para plantas médias'),
            ('Pá de Jardinagem', 3, 8, 25.90, 'Ferramenta ideal para pequenos plantios'),
            ('Adubo Orgânico 1kg', 4, 12, 18.75, 'Fertilizante natural para plantas');
        """)
    return None


def seeder_table_tipos() -> None:
    with Cursor() as cursor:
        cursor.execute("""
            INSERT INTO tipos (nome) VALUES
            ('Planta'),
            ('Vaso'),
            ('Ferramenta'),
            ('Acessorio')
            ON CONFLICT (nome) DO NOTHING;
        """)
    return None

def create_tables():
    create_table_tipos()
    create_table_produtos()
    seeder_table_tipos()
    seeder_table_produtos()
    return None

if __name__ == '__main__':
    create_tables()

