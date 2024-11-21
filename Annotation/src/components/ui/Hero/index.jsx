import NavLink from "../NavLink"

const Hero = () => (
    <section>
        <div className="custom-screen py-28 text-gray-600">
            <div className="space-y-5 max-w-4xl mx-auto text-center">
                
                <h1 className="text-4xl text-gray-800 font-extrabold mx-auto sm:text-6xl">
                    门客三千<br/>
                    多智能体自动标注平台
                </h1>
                <p className="max-w-xl mx-auto">
                借助智能数据标注工具集与项目管理系统，我们将助力标注团队和机器学习工程师制作各式各样的训练数据集。
                </p>
                <div className="flex items-center justify-center gap-x-3 font-medium text-sm">
                    <NavLink
                        href="/get-started"
                        className="text-white bg-gray-800 hover:bg-gray-600 active:bg-gray-900 "
                    >
                        开始标注
                    </NavLink>
                    <NavLink
                        href="#docs"
                        className="text-gray-700 border hover:bg-gray-50"
                        scroll={false}
                    >
                        演示示例
                    </NavLink>
                </div>
            </div>
        </div>
    </section>
)

export default Hero