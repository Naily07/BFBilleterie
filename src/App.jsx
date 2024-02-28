import PointDeVente from "./pages/PoinDeVente/PvPage";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import PageNavigation from "./pages/accueil/Accueil";
import CreationEvenement from "./pages/creationEvenement/CreationEvenement";
import SingleEvent from "./pages/singleEvent/SingleEvent";
import Header from "./component/Header/HeaderMain";
import Accueil from "./pages/accueil/Accueil";
import PageEvenement from "./pages/pageEvenement/PageEvenement";
import SingleEventUser from "./pages/singleEventUser/SingleEventUser";
import "./index.css";

function App() {
  return (
    <BrowserRouter>
      <Header />
      <Routes>
        <Route path="/" element={<PageNavigation />} />
        <Route path="/accueil" element={<Accueil />} />
        <Route path="/creation-event" element={<CreationEvenement />} />
        <Route path="/single-event" element={<SingleEvent />} />
        <Route path="/user" element={<SingleEventUser />} />
        <Route path="/point-de-vente" element={<PointDeVente />} />
        <Route path="/point-de-vente" element={<PointDeVente />} />
        <Route path="/page-evenement" element={<PageEvenement />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
