import React from "react";
import { FiCalendar } from "react-icons/fi";
import Draw from "./Drawer";

export default function TopBar() {
  return (
    <div className="border-b px-4 mb-4 mt-2 pb-4 border-stone-200">

      <div className="flex justify-between items-center p-0.5">
        <div>
            <span className="text-sm font-bold block">🚀 good morning, John!</span>
            <span className="text-xs block text-stone-500">
                Tuesday, Aug 8th 2024
            </span>
        </div>
        {/* < button className="flex text-sm items-center gap-2 bg-stone-100 transition-colors
        hover:bg-violet-100 hover:text-violet-700 px-3 py-1.5">
            <FiCalendar/>
            <span>Pre 6 Months</span>
        </button> */}
        <div className="flex text-sm items-center gap-2 transition-color px-3 py-1.5">
          <Draw/>
        </div>
        
      </div>
    </div>
    )
}