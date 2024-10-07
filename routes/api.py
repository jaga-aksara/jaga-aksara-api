from flask import (Blueprint, g)
from controllers import (UserController, PegonScriptController)
from middlewares.auth_middleware import authenticate
from models import User


# Main blueprint
api_bp = Blueprint('api', __name__, url_prefix='/api')

# Additional blueprint(s)
user_bp = Blueprint('user', __name__, url_prefix='/users')
pegon_script_bp = Blueprint('pegon_script', __name__, url_prefix='/pegon-scripts')
api_bp.register_blueprint(user_bp)
api_bp.register_blueprint(pegon_script_bp)


@user_bp.route('/register', methods=(['POST']))
def register():
    return UserController.register()    

@user_bp.route('/login', methods=(['POST']))
def login():
    return UserController.login()    

@user_bp.route('/logout', methods=(['DELETE']))
@authenticate
def logout():
    return UserController.logout()    


@user_bp.route('/self', methods=(['GET']))
@authenticate
def show_self():
    return UserController.show_self()


@user_bp.route('/<int:user_id>', methods=(['PUT']))
@authenticate
def update(user_id: int):
    return UserController.update(user_id)

@user_bp.route('/self', methods=(['PUT']))
@authenticate
def update_self():
    return UserController.update(user_id=g.user.id)

@user_bp.route('/self/password', methods=(['PUT']))
@authenticate
def update_password_self():
    return UserController.update_password_self()

@pegon_script_bp.route('/translate', methods=(['POST']))
def pegon_script_translate():
    return PegonScriptController.translate()