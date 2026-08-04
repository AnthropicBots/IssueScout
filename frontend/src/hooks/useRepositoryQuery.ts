import { useQuery } from "@tanstack/react-query";

import { scanRepository } from "../api/repository";

export function useRepositoryQuery(
  owner: string,
  repository: string,
) {
  return useQuery({
    queryKey: [
      "repository-scan",
      owner,
      repository,
    ],
    queryFn: () =>
      scanRepository(
        owner,
        repository,
      ),
    enabled:
      owner.trim().length > 0 &&
      repository.trim().length > 0,
  });
}
