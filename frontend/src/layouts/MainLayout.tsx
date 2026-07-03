import Header from "../components/common/Header";
import Footer from "../components/common/Footer";
import AppRouter from "../router";

export default function MainLayout() {
  return (
    <div className="flex min-h-screen flex-col bg-slate-50">
      <Header />

      <main className="mx-auto w-full max-w-7xl flex-1 px-6 py-8">
        <AppRouter />
      </main>

      <Footer />
    </div>
  );
}
