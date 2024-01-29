import PointDeVente from './views/PoinDeVente/PvPage'
import { BrowserRouter, Routes, Route } from 'react-router-dom'
import PageNavigation from './views/accueil/PageEvenement'
import CreationEvenement from './views/createEvent/CreationEvenement'
import SingleEvent from './views/singleEvent/SingleEvent'
import Header from "./component/HeaderMain"

function App() {
  return(
  <BrowserRouter>  
    <Header/>
    <Routes>     
      <Route path='/' element={ <PageNavigation/> }/>
      <Route path='/creation-event' element={ <CreationEvenement/> }/>
      <Route path='/single-event' element={ <SingleEvent/> }/>
      <Route path='/point-de-vente' element={ <PointDeVente/> }/>
    </Routes>
  </BrowserRouter>
  )
}

export default App
