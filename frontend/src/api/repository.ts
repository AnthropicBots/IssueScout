import { api } from "./client";
import type { ScanResult } from "../types/api";

export async function scanRepository(
  owner: string,
  repository: string,
): Promise<ScanResult> {
  const response = await api.get<ScanResult>(
    `/scan/repository/${owner}/${repository}`,
  );

  return response.data;
}
