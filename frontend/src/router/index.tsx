import { Suspense, lazy } from "react";

import LoadingState from "../components/status/LoadingState";
import { Route, Routes } from "react-router-dom";

const HomePage = lazy(() => import("../pages/HomePage"));
const IssueDetailPage = lazy(
  () => import("../pages/Issue/IssueDetailPage")
);
const NotFoundPage = lazy(() => import("../pages/NotFoundPage"));

export default function AppRouter() {
  return (
    <Suspense
      fallback={<LoadingState />}
    >
      <Routes>
        <Route
          path="/"
          element={<HomePage />}
        />

        <Route
          path="/:owner/:repo/issues/:issueNumber"
          element={<IssueDetailPage />}
        />

        <Route
          path="*"
          element={<NotFoundPage />}
        />
      </Routes>
    </Suspense>
  );
}
