from flask import Flask, request, jsonify, render_template, redirect,url_for
import sqlite3

app = Flask(__name__, template_folder='../frontend/templates', static_folder='frontend/static')
DATABASE = 'database.db'

#Connection à la base de données
def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

#La route pour l'API
@app.route('/')
def index():
    return render_template('index.html')

#Route pour l'API qui va permettre de récolter tous les hôpitaux
@app.route('/api/hospitals', methods=['GET'])
def get_hospitals():
    conn = get_db_connection()
    hospitals = conn.execute('SELECT * FROM hospitals').fetchall()
    conn.close()
    return jsonify([dict(hospital) for hospital in hospitals])

# Route pour afficher la page du formulaire d'ajout
"""
@app.route('/add-hospital')
def add_hospital_form():
    return render_template('hospital_form.html')

"""

# Route pour afficher la liste des hôpitaux
@app.route('/hospitals')
def hospital_list():
    conn = get_db_connection()  # Connexion à la base de données
    hospitals = conn.execute('SELECT * FROM hospitals').fetchall()  # Récupérer tous les hôpitaux
    conn.close()  # Fermer la connexion à la base de données
    
    return render_template('hospital_list.html', hospitals=hospitals)  # Passer les hôpitaux au modèle


#Route pour l'API d'ajout des hopitaux
@app.route('/add-hospital', methods=['GET', 'POST'])
def add_hospital_form():
    if request.method == 'POST':
        name = request.form.get('name')  # Utilisation de .get() pour éviter l'AttributeError
        address = request.form.get('address')
        phone = request.form.get('phone')
        availability = request.form.get('availability')
        services = request.form.get('services')

        # Vérification de l'existence des données
        if not name or not address or not phone or not availability or not services:
            return "Tous les champs doivent être remplis", 400  # Retourner une erreur si un champ est manquant

        # Connexion à la base de données et ajout des données
        conn = get_db_connection()
        conn.execute(
            'INSERT INTO hospitals (name, address, phone, availability, services) VALUES (?,?,?,?,?)',
            (name, address, phone, availability, services)
        )
        conn.commit()
        conn.close()
        #return jsonify({'message': 'Hôpital ajouté avec succès!'}), 201

        return redirect(url_for('index'))  # Rediriger vers la page d'accueil après ajout

    return render_template('hospital_form.html')  # Afficher le formulaire en GET

# Route pour supprimer un hôpital
@app.route('/delete-hospital/<int:hospital_id>', methods=['GET', 'POST'])
def delete_hospital(hospital_id):
    conn = get_db_connection()  # Connexion à la base de données
    conn.execute('DELETE FROM hospitals WHERE id = ?', (hospital_id,))  # Supprimer l'hôpital par ID
    conn.commit()
    conn.close()  # Fermer la connexion à la base de données

    return redirect(url_for('hospital_list'))  # Rediriger vers la liste des hôpitaux


if __name__ == '__main__':
    app.run(debug=True)


""" 
cardiographie
réanimation
accouchement

"""
