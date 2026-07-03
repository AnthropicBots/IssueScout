import { Suspense, lazy } from "react";
import { Route, Routes } from "react-router-dom";

const HomePage = lazy(() => import("../pages/HomePage"));
const IssueDetailPage = lazy(
  () => import("../pages/Issue/IssueDetailPage")
);
const NotFoundPage = lazy(() => import("../pages/NotFoundPage"));

export default function AppRouter() {
  return (
    <Suspense
      fallback={
        <div className="flex min-h-[60vh] items-center justify-center">
          <div className="text-sm text-slate-500">Loading...</div>
        </div>
      }
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
