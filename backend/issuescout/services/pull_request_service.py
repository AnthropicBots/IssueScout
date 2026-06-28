from urllib.parse import quote

from issuescout.github.client import GitHubClient


class PullRequestService:
    def __init__(self):
        self.client = GitHubClient()

    async def search_issue_references(
        self,
        owner: str,
        repo: str,
        issue_number: int,
    ):
        query = f'repo:{owner}/{repo} is:pr "{issue_number}"'

        print(f"\nScanning Issue #{issue_number}")
        print(f"Search Query : {query}")
        
        endpoint = f"/search/issues?q={quote(query)}"
        
        print(f"Endpoint : {endpoint}")
        
        return await self.client.get(endpoint)
    
    async def list_open_pull_requests(
        self,
        owner: str,
        repo: str,
    ):
        endpoint = (
            f"/repos/{owner}/{repo}/pulls"
            "?state=open"
            "&per_page=100"
        )

        print("\nFetching open pull requests")
        print(f"Endpoint : {endpoint}")

        return await self.client.get(endpoint)
    
    async def get_pull_request_files(
        self,
        owner: str,
        repo: str,
        number: int,
    ):
        endpoint = (
            f"/repos/{owner}/{repo}/pulls/"
            f"{number}/files?per_page=100"
        )
    
        return await self.client.get(endpoint)
    
    async def get_pull_request_commits(
        self,
        owner: str,
        repo: str,
        number: int,
    ):
        endpoint = (
            f"/repos/{owner}/{repo}/pulls/"
            f"{number}/commits?per_page=100"
        )

        return await self.client.get(endpoint)

    async def close(self):
        await self.client.close()