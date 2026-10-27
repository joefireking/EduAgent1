# import uvicorn
# from fastapi import FastAPI
#
# app = FastAPI(title="EduAgent Demo")
#
# @app.get("/health")
# async def health_check():
#     return {"status": "ok"}

from fastapi import FastAPI, Depends
from pydantic import BaseModel, Field

app = FastAPI()

# 请求体模型：前端要发来的数据长这样
class LoginRequest(BaseModel):
    username: str = Field(..., description="用户名或邮箱")
    password: str = Field(..., description="密码")

# 响应模型：我们会返回的数据长这样
class TokenResponse(BaseModel):
    access_token: str
    token_type:   str = "bearer"
    role:         str

@app.post("/login", response_model=TokenResponse)
async def login(req: LoginRequest):           # 参数类型是 Pydantic 模型
    # req 已经是解析并校验好的对象，直接用 req.username / req.password
    if req.username == "student01" and req.password == "Student@123456":
        return TokenResponse(access_token="fake-token-abc", role="student")
    return {"access_token": "", "token_type": "bearer", "role": "guest"}

@app.get("/reviews/{review_id}")
async def get_review(review_id: str):
    return {"review_id": review_id, "status": "completed"}
# 访问 GET /reviews/abc-123 → review_id 自动等于 "abc-123"


@app.get("/reviews")
async def list_reviews(page: int = 1, size: int = 10):
    return {"page": page, "size": size}
# 访问 GET /reviews?page=2&size=20 → page=2, size=20
# 不传则用默认值 page=1, size=10


# 这里我们使用文档中的 get_current_user 模拟版本。
async def get_db():
    return {"db": "fake_session"}

# 模拟的当前用户（不校验 Token，直接返回）
async def get_current_user():
    return {"user_id": "test_user", "role": "student"}

@app.get("/my-reviews")
async def my_reviews(
    db = Depends(get_db),
    current_user: dict = Depends(get_current_user),
):
    # return {"user": current_user["user_id"], "data": "这是受保护的数据"}
    return {"db":db["db"], "user": current_user["user_id"], "data": "这是受保护的数据"}


from fastapi import FastAPI, File, UploadFile


@app.post("/upload", status_code=202)
async def upload(file: UploadFile = File(...)):
    content = await file.read()                  # 异步读取文件内容（bytes）
    return {"filename": file.filename, "size": len(content)}


import asyncio
import json
from fastapi import FastAPI
from sse_starlette.sse import EventSourceResponse

app = FastAPI()

@app.post("/chat/stream")
async def chat_stream():
    async def event_generator():
        answer = "装饰器是一种包装函数的语法。"
        for char in answer:                       # 模拟逐字生成
            await asyncio.sleep(0.1)
            # 每个事件是一个字典，data 里放 JSON 字符串
            yield {"data": json.dumps({"type": "token", "content": char}, ensure_ascii=False)}
        yield {"data": json.dumps({"type": "done"})}   # 结束标志

    return EventSourceResponse(event_generator())


from fastapi import HTTPException

def find_review(review_id):
    print('你好')

@app.get("/reviews/{review_id}")
async def get_review(review_id: str):
    review = find_review(review_id)     # 伪代码
    if review is None:
        raise HTTPException(status_code=404, detail="审查记录不存在")
    return review

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=8000)