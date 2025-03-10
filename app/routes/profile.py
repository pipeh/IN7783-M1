from flask import Blueprint, request, render_template

main = Blueprint('profile', __name__)

@main.route('/profile')
def profile():
    # Implementa tu endpoint aquí

    return render_template('profile.html', user={ 'fecha': 'fecha_ejemplo' })
