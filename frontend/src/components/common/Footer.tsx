export default function Footer() {
  return (
    <footer className="mt-20 border-t py-8 text-center text-sm text-slate-500">
      © {new Date().getFullYear()} IssueScout

      <p className="mt-2">
        Intelligent GitHub Issue Discovery Platform
      </p>
    </footer>
  );
}
