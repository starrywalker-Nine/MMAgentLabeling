import React from "react";
import { FiChevronDown, FiChevronUp } from 'react-icons/fi'

export default function AccountToggle() {
  return (
    <div className="border-b mb-4 pb-4 border-stone-300">
        <button className="flex p-0.5 hover:bg-stone-200 rounded
        transition-colors relative gap-2 w-full items-center
        ">
            <img src="https://i.pravatar.cc/150?img=13"
            alt="avatar"
            className="size-8 rounded shrink-0 bg-violet-500 shadow" />
            <div className="text-start">
                <span className="text-sm font-semibold block">Tom Is loading...</span>
                <span className="text-xs text-stone-500 block">Last seen 2 hours ago</span>
            </div>
            <FiChevronDown className="absolute right-2 top-1/2 translate-y-[calc(-50%+4px)] text-xs"/>
            <FiChevronUp className="absolute right-2 top-1/2 translate-y-[calc(-50%-4px)] text-xs" />
        </button>
    </div>
  )
};