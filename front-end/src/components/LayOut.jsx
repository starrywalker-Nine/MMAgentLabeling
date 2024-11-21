import Navbar from './ui/Navbar/index';
import Footer from './ui/Footer/index';

function LayOut({children}) {
  return (
    <>
      <Navbar/>
        <main>{children}</main>
      <Footer/>
    </>
    )
}

export default LayOut;
