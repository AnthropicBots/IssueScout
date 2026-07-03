export function formatRepositoryName(
  owner: string,
  repo: string,
) {
  return `${owner}/${repo}`;
}

export function repositoryUrl(
  owner: string,
  repo: string,
) {
  return `https://github.com/${owner}/${repo}`;
}

export function issueUrl(
  owner: string,
  repo: string,
  issue: number,
) {
  return `${repositoryUrl(
    owner,
    repo,
  )}/issues/${issue}`;
}

export function pullRequestUrl(
  owner: string,
  repo: string,
  pull: number,
) {
  return `${repositoryUrl(
    owner,
    repo,
  )}/pull/${pull}`;
}
