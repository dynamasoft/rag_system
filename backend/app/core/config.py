from pydantic import BaseSettings

class Settings(BaseSettings):
    # Application settings
    app_name: str = "RAG System"
    api_version: str = "v1"
    debug: bool = True

    # Database settings
    faiss_index_path: str = "path/to/faiss/index"
    
    # LLM settings
    llm_api_key: str
    llm_model: str = "gpt-4"

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings()