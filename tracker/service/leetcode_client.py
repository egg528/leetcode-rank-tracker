import requests
from requests import Response
from typing import Dict
from tracker.meta.singleton import SingletonMeta


class LeetCodeClient(metaclass=SingletonMeta):
    _LEETCODE_API_URL = 'https://leetcode.com/graphql'

    def __init__(self, username: str) -> None:
        if not hasattr(self, '_initialized'):
            self._username = username
            self._initialized = True

    def get_rank(self) -> int:
        query = """
            query userProfile($username: String!) {
                matchedUser(username: $username) {
                    profile {
                        ranking
                    }
                }
            }
        """
        variables = {'username': self._username}
        response = self._make_graphql_request(query, variables)

        if 'errors' in response:
            raise Exception(f"GraphQL query failed with errors: {response['errors']}")

        return int(response['data']['matchedUser']['profile']['ranking'])

    def _make_graphql_request(self, query: str, variables: Dict[str, str]) -> Dict:
        resp: Response = requests.post(
            url=self._LEETCODE_API_URL,
            json={
                'query': query,
                'variables': variables
            }
        )
        resp.raise_for_status()
        return resp.json()