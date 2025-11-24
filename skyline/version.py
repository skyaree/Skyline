"""Represents current userbot version"""





__version__ = "sunshine"

import os

import git
from skyline._internal import restart

try:
    branch = git.Repo(
        path=os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    ).active_branch.name
except Exception:
    branch = "master"


async def check_branch(me_id: int, allowed_ids: list):
    if branch != "master" and me_id not in allowed_ids:
        repo = git.Repo(path=os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
        repo.git.reset("--hard", "HEAD")
        repo.git.checkout("master", force=True)
        restart()

