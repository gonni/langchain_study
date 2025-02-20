from dotenv import load_dotenv
import os

load_dotenv()
print(os.environ["LANGCHAIN_TRACING_V2"])