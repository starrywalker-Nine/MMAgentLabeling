// import Layout from "../../components/LayOut";

// function Index({Component, pageProps}) {
//   return (
//     <Layout>
//       <Component {...pageProps} />
//     </Layout>
//     );
// }
// export default Index;

import GradientWrapper from "../../components/GradientWrapper";
import CTA from "../../components/ui/CTA";
import Features from "../../components/ui/Features";
import FooterCTA from "../../components/ui/FooterCTA";
import Hero from "../../components/ui/Hero";
import LogoGrid from "../../components/ui/LogoGrid";
import Testimonials from "../../components/ui/Testimonials";
import ToolKit from "../../components/ui/ToolKit";
import Navbar from "../../components/ui/Navbar";
import Footer from "../../components/ui/Footer";
import "../../style/globals.css";

export default function Index() {
  return (
    <>
      <Navbar/>
      <Hero />
      <LogoGrid />
      <GradientWrapper>
        <Features />
        <CTA />
      </GradientWrapper>
      <ToolKit />
      <GradientWrapper>
        <Testimonials />
      </GradientWrapper>
      <FooterCTA />
      <Footer />
    </>
  );
}


