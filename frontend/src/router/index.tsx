import { Route, Routes } from "react-router-dom";

import HomePage from "../pages/HomePage";
import NotFoundPage from "../pages/NotFoundPage";
import IssueDetailPage from "../pages/Issue/IssueDetailPage";

export default function AppRouter() {
  return (
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
  );
}
