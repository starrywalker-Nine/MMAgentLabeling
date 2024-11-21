import { Link } from "react-router-dom";

const NavLink = ({ children, href, scroll, ...props }) => (
    <Link 
        to={href} 
        {...props} 
        scroll={typeof scroll === "boolean" ? scroll.toString() : scroll} 
        className={`py-2.5 px-4 text-center rounded-lg duration-150 ${props?.className || ""}`}
    >
        {children}
    </Link>
)

export default NavLink
