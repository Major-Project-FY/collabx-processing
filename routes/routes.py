from flask import Flask
from utils.db_utils import get_github_user_info, get_github_user_repo_info
from algos.ranking import calculate_level_on_gh_data

app = Flask(__name__)


@app.route('/processing/rank-user/<user_id>', methods=['GET'])
def rank_user(user_id):
    user_data = get_github_user_info(user_id=user_id)
    repo_data = get_github_user_repo_info(user_id=user_id)
    result = calculate_level_on_gh_data(data=user_data, repo_data=repo_data)
    return {"user_level": result}
