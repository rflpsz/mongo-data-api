from flask import Blueprint

aggregate_bp = Blueprint("aggregate", __name__)
delete_many_bp = Blueprint("delete_many", __name__)
delete_one_bp = Blueprint("delete_one", __name__)
find_bp = Blueprint("find", __name__)
find_one_bp = Blueprint("find_one", __name__)
insert_many_bp = Blueprint("insert_many", __name__)
insert_one_bp = Blueprint("insert_one", __name__)
update_many_bp = Blueprint("update_many", __name__)
update_one_bp = Blueprint("update_one", __name__)

from . import aggregate
from . import delete_many
from . import delete_one
from . import find
from . import find_one
from . import insert_many
from . import insert_one
from . import update_many
from . import update_one

__all__ = [
    "aggregate",
    "delete_many",
    "delete_one",
    "find",
    "find_one",
    "insert_many",
    "insert_one",
    "update_many",
    "update_one",
]
