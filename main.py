from robyn import Robyn
from dotenv import load_dotenv
import os

load_dotenv()

PORT = os.environ.get("PORT")

app = Robyn(__file__)

@app.get("/")
async def h(request):
    return "Hello, world!"


if __name__ == '__main__':
    app.start(debug=True, port=os.getenv("PORT", default=5000))
