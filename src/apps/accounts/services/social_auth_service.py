from abc import ABC, abstractmethod
from pprint import pprint
from typing import Literal, NoReturn

from google.auth.transport.requests import Request
from google.oauth2 import id_token
from requests_oauthlib import OAuth2Session

from apps.common.exceptions import TokenIsInvalidError
from apps.common.types import SocialUserDataType


class SocialAuthService(ABC):
    provider: Literal["google", "github"]

    @abstractmethod
    def exchange_code_for_access_token(self, code: str) -> str | NoReturn:
        """
        Exchange the authorization code for an access token.

        Args:
            code (str): The authorization code.

        Returns:
            str: The access token.

        Raises:
            ValueError: If the authorization code is invalid.
        """
        ...

    @abstractmethod
    def retrieve_user_data(self, access_token: str) -> SocialUserDataType | NoReturn: ...


class GoogleSocialAuthService(SocialAuthService):
    provider = "google"
    SCOPES = [
        "openid",
        "https://www.googleapis.com/auth/userinfo.profile",
        "https://www.googleapis.com/auth/userinfo.email",
    ]
    GOOGLE_TOKEN_ENDPOINT = "https://oauth2.googleapis.com/token"

    def __init__(self, google_client_id: str, google_client_secret: str, redirect_uri: str) -> None:
        self.google_client_id = google_client_id
        self.google_client_secret = google_client_secret
        self.redirect_uri = redirect_uri

    def exchange_code_for_access_token(self, code: str) -> str | NoReturn:
        try:
            oauth2_session = OAuth2Session(
                client_id=self.google_client_id,
                redirect_uri=self.redirect_uri,
                scope=GoogleSocialAuthService.SCOPES,
            )

            token = oauth2_session.fetch_token(
                token_url=GoogleSocialAuthService.GOOGLE_TOKEN_ENDPOINT,
                client_secret=self.google_client_secret,
                code=code,
            )
            return token["id_token"]
        except Exception as err:
            raise TokenIsInvalidError("Google authorization code is invalid") from err

    def retrieve_user_data(self, access_token: str) -> SocialUserDataType | NoReturn:
        try:
            id_info = id_token.verify_oauth2_token(id_token=access_token, request=Request(), audience=self.google_client_id)
            if "accounts.google.com" in id_info["iss"]:
                print()
                pprint(id_info)
                print()
                return {
                    "email": id_info["email"],
                    "first_name": id_info["given_name"],
                    "last_name": id_info["family_name"],
                }
        except Exception as err:
            raise TokenIsInvalidError("Google token is invalid") from err
