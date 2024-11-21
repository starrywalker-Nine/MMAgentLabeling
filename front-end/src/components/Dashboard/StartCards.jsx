import React from "react";
import { FiTrendingDown, FiTrendingUp } from "react-icons/fi";
import bot1 from "../../public/agent/robot.png";
import bot2 from "../../public/agent/robot2.png";
import bot3 from "../../public/agent/robot3.png";


export default function StartCards() {
  return (
    <>
      <Card img={bot1} AgentName="清洗机器人" description="负责对文件内容进行处理并切分" buttonLink="#" />
      <Card img={bot2} AgentName="标注机器人" description="负责对文件内容进行标注" buttonLink="#" />
      <Card img={bot3} AgentName="审查机器人" description="负责对标注结果进行审查" buttonLink="#" />
    </>
  );
}

const Card = ({ img, AgentName, description, buttonLink }) => {
  return (
    <div className="col-span-4 rounded border-stone-200 shadow transition-shadow duration-300 ease-in-out">
      <div className="card card-side bg-base-100 shadow-xl">
        <figure>
          <img src={img} alt="description" className="w-36 h-36 object-cover rounded-full" />
        </figure>

        <div className="card-body">
          <h2 className="card-title">{AgentName}</h2>
          <p>{description}</p>
          <div className="card-actions justify-end">
            <button className="btn btn-primary">详细设置</button>
          </div>
        </div>
      </div>
    </div>
  );
};
