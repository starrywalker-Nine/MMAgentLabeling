import React from 'react';
import SideBar from '../../components/SideBar/SideBar';
import DashBoard from '../../components/Dashboard/DashBoard'; // 假设这是一个主仪表盘组件
// import AnotherDashBoard from '../../components/Dashboard/AnotherDashBoard'; // 假设这是另一个仪表盘组件
import { useState } from 'react';
import WorkFlow from '../../components/Dashboard/Template/WorkFlow';

export default function Start() {
  const [selectedIndex, setSelectedIndex] = useState(0);

  // 用于处理按钮点击的函数
  const handleButtonClick = (index) => {
    setSelectedIndex(index);
  };

  // 根据 selectedIndex 渲染不同的 DashBoard
  const renderDashBoard = () => {
    switch (selectedIndex) {
      case 0:
        return <DashBoard main={<WorkFlow/>}/>;
      case 1:
        return <DashBoard main={'1'}/>;
      // 你可以添加更多的 case 以支持更多的仪表盘
      case 2:
        return <DashBoard main={'2'}/>;
      case 3:
        return <DashBoard main={'3'}/>;
      case 4:
        return <DashBoard main={'4'}/>;
      default:
        return <DashBoard main={'5'}/>;
    }
  };

  return (
    <main className='grid gap-4 p-4 grid-cols-[220px,_1fr]'>
      <SideBar selectedIndex={selectedIndex} handleButtonClick={handleButtonClick} />
      <div className="dashboard-content">
        {renderDashBoard()}  {/* 根据 selectedIndex 渲染对应的仪表盘 */}
      </div>
    </main>
  );
}
