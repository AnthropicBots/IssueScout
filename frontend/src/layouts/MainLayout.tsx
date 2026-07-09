import Header from "../components/common/Header";
import Footer from "../components/common/Footer";
import AppRouter from "../router";

export default function MainLayout() {
  return (
    <div className="flex min-h-screen flex-col bg-slate-50 text-slate-900">
      <Header />

      <main
        className="
          mx-auto
          flex
          w-full
          max-w-7xl
          flex-1
          px-4
          py-8
          sm:px-6
          lg:px-8
        "
      >
        <div className="w-full">
          <AppRouter />
        </div>
      </main>

      <Footer />
    </div>
  );
}
