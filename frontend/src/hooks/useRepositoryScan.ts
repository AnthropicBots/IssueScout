import { useMutation } from "@tanstack/react-query";

import { scanRepository } from "../api/repository";

export function useRepositoryScan() {
  return useMutation({
    mutationFn: ({
      owner,
      repository,
    }: {
      owner: string;
      repository: string;
    }) =>
      scanRepository(
        owner,
        repository,
      ),
  });
}
