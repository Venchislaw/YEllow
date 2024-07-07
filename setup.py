from setuptools import find_packages, setup
from typing import List


SPECIAL_OCCASION = "-e ."
def get_requirements(file_path: str) -> List[str]:
    """
    function returns list of requirements from file
    """

    reqs = []

    with open(file_path) as file_obj:
        reqs = file_obj.readlines()
        reqs = [req.replace("\n", "") for req in reqs]

        if SPECIAL_OCCASION in reqs:
            reqs.remove(SPECIAL_OCCASION)

    return reqs


setup(
    name="YEllow",
    version="0.0.1",
    author="Venchislav",
    author_email="venchislavcodes@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt")
)