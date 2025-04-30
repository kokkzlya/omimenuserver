import inject
from flask import Blueprint, jsonify, request

from src.domain.usecases.membership_actions import (
    AuthUserAction,
    CreateAuthTokenAction,
    GetUserAction,
)

bp = Blueprint("auth", __name__)

@bp.route("/auth", methods=["POST"])
@inject.autoparams()
def auth(
    auth_user_action: AuthUserAction,
    get_user_action: GetUserAction,
    create_auth_token_action: CreateAuthTokenAction,
):
    cred = request.get_json()
    username = cred.get("username")
    password = cred.get("password")
    if not auth_user_action.execute(username, password):
        return {"message": "Invalid credentials"}, 401
    user = get_user_action.execute(username)
    if user is None:
        return {"message": "Invalid credentials"}, 401
    token = create_auth_token_action.execute(user.username)
    return jsonify({
        "token": token,
    })
