import { useState } from "react";

import { useRepositoryScan } from "../../hooks/useRepositoryScan";

import Button from "../ui/Button";
import Input from "../ui/Input";
import Card from "../ui/Card";
import LoadingSpinner from "../ui/LoadingSpinner";

import RepositoryResults from "./RepositoryResults";

export default function RepositorySearchForm() {
  const [owner, setOwner] = useState("");
  const [repository, setRepository] = useState("");

  const scan = useRepositoryScan();

  return (
    <Card className="mt-10">
      <div className="grid gap-4 md:grid-cols-[1fr_1fr_auto]">
        <Input
          placeholder="GitHub Owner (e.g. fastapi)"
          value={owner}
          onChange={(e) => setOwner(e.target.value)}
        />

        <Input
          placeholder="Repository (e.g. fastapi)"
          value={repository}
          onChange={(e) => setRepository(e.target.value)}
        />

        <Button
          className="h-full"
          onClick={() =>
            scan.mutate({
              owner,
              repository,
            })
          }
        >
          Scan Repository
        </Button>

        {scan.isPending && <LoadingSpinner />}

        {scan.error && (
          <p className="font-medium text-red-600">
            Unable to scan repository.
          </p>
        )}

        {scan.data && (
          <RepositoryResults result={scan.data} />
        )}
      </div>
    </Card>
  );
}
