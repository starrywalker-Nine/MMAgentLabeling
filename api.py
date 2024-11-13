import os
import uvicorn
from fastapi import FastAPI, UploadFile, File
from main import reg_tool, start
from Agent_config import AgentFactory
from Database import db_writer

app = FastAPI()
shared_data = {}

# 创建保存文件的目录（如果不存在）
os.makedirs("source_file", exist_ok=True)


@app.post("/uploadfiles", tags=["文件上传接口"],
          description="文件上传接口：选择文件传输到后台",
          response_description="返回 code:1 表示成功")
async def get_uploadfiles(file: UploadFile = File(...)):
    print("file", file)
    # 定义文件保存路径
    path = os.path.join("source_file", file.filename)
    shared_data["path"] = path
    # 文件保存
    with open(path, "wb") as f:
        for line in file.file:
            f.write(line)

    return {
        "code": 1,
        "message": "文件上传成功",
        "file_path": path
    }


@app.post('/run', tags=["后台运行结果接口"],
          description="后台运行结果接口：根据返回值确认后台是否成功运行",
          response_description="返回 code:1 表示成功，code:0 表示失败")
async def deal():
    try:
        # 检查 shared_data 中的路径是否存在
        if "path" not in shared_data or not os.path.exists(shared_data["path"]):
            raise FileNotFoundError("指定的文件路径不存在或未提供文件路径")
        # 文件读取
        with open(shared_data["path"], 'r', encoding='utf-8') as file:
            raw_data = file.read()
        print(raw_data)

        # 实例化和注册代理
        agent = AgentFactory()
        reg_tool(agent)
        # 处理数据并保存结果
        shared_data["answer"] = start(agent, raw_data)
    except FileNotFoundError as e:
        return {"code": 0, "message": str(e)}
    except Exception as e:
        # 记录其他类型的异常，返回错误信息
        print(f"发生错误: {str(e)}")
        return {"code": 0, "message": "处理过程中出现错误"}
    # 如果一切正常，返回成功代码
    return {
        "code": 1,
        "message": "处理成功",
    }


# shared_data["answer"] = "这是一个测试"


@app.post('/answer', tags=["返回运行结果接口"],
          description="返回运行结果接口：返回后台运行结果",
          response_description="返回 code:1 表示成功")
async def answer():
    return {

        "answer": shared_data["answer"],
        "code": 1
    }


if __name__ == '__main__':
    uvicorn.run("api:app", port=8000, reload=True)
