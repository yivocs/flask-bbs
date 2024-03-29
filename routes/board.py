from flask import (
    render_template,
    request,
    redirect,
    url_for,
    Blueprint,
)

from routes import *

from models.board import Board


main = Blueprint('board', __name__)


# 无效
@main.route("/admin")
def index():
    return render_template('board/admin_index.html')

# 增加板块操作
@main.route("/add", methods=["POST"])
def add():
    form = request.form
    u = current_user()
    m = Board.new(form)
    return redirect(url_for('topic.index'))

