// RouteSelect.jsx
import React from "react";
import { FiDollarSign, FiHome, FiLink, FiPaperclip, FiUser } from "react-icons/fi";

export default function RouteSelect({ selectedIndex, handleButtonClick }) {
    return (
        <div className="space-y-1">
            <RouteButton
                select={selectedIndex === 0}
                Icon={FiHome}
                title="Features"
                onClick={() => handleButtonClick(0)}
            />
            <RouteButton
                select={selectedIndex === 1}
                Icon={FiUser}
                title="Our toolkit"
                onClick={() => handleButtonClick(1)}
            />
            <RouteButton
                select={selectedIndex === 2}
                Icon={FiPaperclip}
                title="Testimonials"
                onClick={() => handleButtonClick(2)}
            />
            <RouteButton
                select={selectedIndex === 3}
                Icon={FiLink}
                title="Links"
                onClick={() => handleButtonClick(3)}
            />
            <RouteButton
                select={selectedIndex === 4}
                Icon={FiDollarSign}
                title="Pricing"
                onClick={() => handleButtonClick(4)}
            />
        </div>
    );
}

const RouteButton = ({ select, Icon, title, onClick }) => {
    return (
        <button 
            className={`flex items-center justify-start gap-2 w-full py-2 rounded px-1.5 text-sm transition-[box-shadow,_background-color,_color] ${
                select ? "bg-white text-stone-950 shadow" : "hover:bg-stone-200 bg-transparent text-stone-500 shadow-none"
            }`} 
            onClick={onClick}
        >
            <Icon className={select ? "text-violet-500" : ""}/>
            <span>{title}</span>
        </button>
    );
}
