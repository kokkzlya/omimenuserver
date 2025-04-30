import logging

import inject

from src.domain.models import NewUser
from src.domain.usecases.membership_actions import RegisterUserAction

logger = logging.getLogger(__name__)

users = [
    {
        "username": "abrahanvivo",
        "password": "2335027",
    },
    {
        "username": "adindasatyarani",
        "password": "2335001",
    },
    {
        "username": "agnesavrillia",
        "password": "2335006",
    },
    {
        "username": "angelinelisupadang",
        "password": "2335017",
    },
    {
        "username": "chyntiaevrisela",
        "password": "2335020",
    },
    {
        "username": "clearentiwow",
        "password": "2335004",
    },
    {
        "username": "damargalih",
        "password": "2335005",
    },
    {
        "username": "davinnatanael",
        "password": "2335023",
    },
    {
        "username": "denzelparhusip",
        "password": "2335016",
    },
    {
        "username": "dianyayak",
        "password": "2335008",
    },
    {
        "username": "einchrystle",
        "password": "2335028",
    },
    {
        "username": "gabrielgabe",
        "password": "2335003",
    },
    {
        "username": "jeremialpin",
        "password": "2335019",
    },
    {
        "username": "josefredrik",
        "password": "2335015",
    },
    {
        "username": "mellisunshine",
        "password": "2335009",
    },
    {
        "username": "rahmatfilemon",
        "password": "2335026",
    },
    {
        "username": "rickosalempang",
        "password": "2335002",
    },
    {
        "username": "sherwinayakeding",
        "password": "2335011",
    },
    {
        "username": "timotiusreven",
        "password": "2335012",
    },
    {
        "username": "vikrimartin",
        "password": "2335029",
    },
]

@inject.autoparams()
def run(register_user: RegisterUserAction = None):
    for user in users:
        register_user.execute(NewUser(
            name=user["username"],
            email=f"{user['username']}@example.com",
            username=user["username"],
            password=user["password"],
            password_hash=None,
        ))
        logger.info("User %s created", user["username"])
