
import logging
import typing

import git
import skylinetl

parser = skylinetl.utils.sanitize_parse_mode("html")
logger = logging.getLogger(__name__)

def get_git_info() -> typing.Tuple[str, str]:
    """
    Get git info
    :return: Git info
    """
    hash_ = get_git_hash()
    return (
        hash_,
        f"https://github.com/coddrago/Skyline/commit/{hash_}" if hash_ else "",
    )

def get_git_hash() -> typing.Union[str, bool]:
    """
    Get current Skyline git hash
    :return: Git commit hash
    """
    try:
        return git.Repo().head.commit.hexsha
    except Exception:
        return False


def get_commit_url() -> str:
    """
    Get current Skyline git commit url
    :return: Git commit url
    """
    try:
        hash_ = get_git_hash()
        return f'<a href="https://github.com/coddrago/Skyline/commit/{hash_}">#{hash_[:7]}</a>'
    except Exception:
        return "Unknown"