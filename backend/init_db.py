import sqlite3

DATABASE = 'database.db'

def create_database():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    
    # Création de la table des hôpitaux
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS hospitals (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            address TEXT NOT NULL,
            phone TEXT NOT NULL,
            availability TEXT NOT NULL,
            services TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()
    print("Base de données initialisée avec succès!")

if __name__ == '__main__':
    create_database()
