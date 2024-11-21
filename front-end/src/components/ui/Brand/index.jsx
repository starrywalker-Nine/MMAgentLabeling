import { Link } from "react-router-dom";
import NavLink from '../NavLink'
import Logo from  "../../../public/blinder.svg"

const Brand = () => (
    <NavLink href="/">
        <img
            src= {Logo}
            width={120}
            height={50}
            alt="Blinder logo"
        />
    </NavLink>
)
export default Brand