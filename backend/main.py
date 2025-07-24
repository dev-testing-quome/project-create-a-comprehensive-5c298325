import uvicorn
from fastapi import FastAPI, Request, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
import os
from fastapi.routing import APIRoute

from database import engine, Base  # Assuming database.py is in the same directory
from routers import users, appointments # Example routers, adjust as needed

Base.metadata.create_all(bind=engine)

app = FastAPI()

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],  # Replace with your allowed origins
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

# Register routers
app.include_router(users.router)
app.include_router(appointments.router)

# Health check endpoint
@app.get('/health')
def health_check():
    return {'status': 'ok'}

# Static file serving
if os.path.exists("static"):
    app.mount("/static", StaticFiles(directory="static"), name="static")

    @app.get("/{{"file_path:path}}")
    async def serve_frontend(file_path: str, request: Request):
        if file_path.startswith("api"):
            return await request.app.dispatch(request)
        static_file = os.path.join("static", file_path)
        if os.path.isfile(static_file):
            return FileResponse(static_file)
        return FileResponse("static/index.html")

# Exception handling
@app.exception_handler(HTTPException)
def http_exception_handler(request: Request, exc: HTTPException):
    return JSONResponse({'detail': exc.detail}, status_code=exc.status_code)

# Custom exception handler (for other exceptions)
@app.exception_handler(Exception)
def exception_handler(request: Request, exc: Exception):
    return JSONResponse({'detail': 'Internal Server Error'}, status_code=500)

# Start the server (for development)
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
