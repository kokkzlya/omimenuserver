import inject
from flask_login import LoginManager

from src.domain.usecases.membership_actions import (
    GetUserAction,
    ValidateAuthTokenAction,
)

login_manager = LoginManager()

@login_manager.request_loader
@inject.autoparams()
def load_user(
    request,
    validate_token_action: ValidateAuthTokenAction,
    get_user_action: GetUserAction,
):
    """
    Load the user from the request.
    """
    auth_header = request.headers.get("Authorization")
    if not auth_header:
        return None
    token = auth_header.split(" ")[1]
    user_id = validate_token_action.execute(token)
    if not user_id:
        return None
    return get_user_action.execute(user_id)
