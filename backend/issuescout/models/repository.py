from pydantic import BaseModel


class Repository(BaseModel):
    owner: str
    name: str

    description: str | None = None
    homepage: str | None = None

    license_name: str | None = None

    language: str | None = None

    default_branch: str = "main"

    stars: int = 0
    forks: int = 0
    watchers: int = 0

    open_issues: int = 0

    archived: bool = False
    disabled: bool = False

    topics: list[str] = []
