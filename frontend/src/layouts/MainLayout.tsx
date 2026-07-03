import Header from "../components/common/Header";
import AppRouter from "../router";
import Footer from "../components/common/Footer";

export default function MainLayout() {
  return (
    <div className="min-h-screen bg-slate-50">
      <Header />

      <main className="mx-auto max-w-7xl px-6 py-8">
        <AppRouter />
        <Footer />
      </main>
    </div>
  );
}
