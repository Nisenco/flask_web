from app import login_manager


@login_manager.user_loader
def load_user(user_id):
    from app.todoism.model import User
    return User.query.get(int(user_id))
