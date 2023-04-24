import json
from flask.json import jsonify
from bson import json_util
from utils.db_init import gh_info, repo_info



def get_github_user_info(user_id):
    return gh_info.find_one({'userID': user_id})


def get_github_user_repo_info(user_id):
    return repo_info.find({'userID': user_id})
