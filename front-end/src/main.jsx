import { createRoot } from 'react-dom/client'
import './style/globals.css'
import { BrowserRouter, Link, Route, Routes } from "react-router-dom";
import Index from './pages/home/_index'
import About from './pages/about/About'
import Contact from './pages/contact/Contact'
import Services from './pages/services/Service'
import Start from './pages/start/Start'

const App = () => {
  return (
    <Routes>
      <Route path="/" element={<Index />} />
      <Route path="/about" element={<About />} />
      <Route path="/contact" element={<Contact />} />
      <Route path="/services" element={<Services />} />
      <Route path="/get-started" element={<Start />} />
    </Routes>
  )
}

createRoot(document.getElementById('root')).render(
  <BrowserRouter>
    <App />
  </BrowserRouter>  
)
