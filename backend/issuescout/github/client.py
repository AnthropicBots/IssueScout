from __future__ import annotations

import httpx

from issuescout.core.config import settings


class GitHubClient:
    """Asynchronous GitHub REST API client."""

    def __init__(self) -> None:
        headers = {
            "Accept": "application/vnd.github+json",
            "User-Agent": "IssueScout",
            "X-GitHub-Api-Version": "2022-11-28",
        }

        if settings.GITHUB_TOKEN:
            headers["Authorization"] = (
                f"Bearer {settings.GITHUB_TOKEN}"
            )

        self.client = httpx.AsyncClient(
            base_url=settings.GITHUB_API,
            headers=headers,
            timeout=30.0,
        )

    async def get(
        self,
        endpoint: str,
        headers: dict | None = None,
    ):
        print(f"\nGET {endpoint}")
    
        response = await self.client.get(
            endpoint,
            headers=headers,
        )
    
        if response.status_code >= 400:
            print(f"Status Code : {response.status_code}")
            print("GitHub Response:")
            print(response.text)
    
        response.raise_for_status()
    
        return response.json()

    async def close(self):
        await self.client.aclose()