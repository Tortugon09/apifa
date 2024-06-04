from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def get_hello_world_and_teemo_image():
    # URL de una imagen de Teemo
    teemo_image_url = "https://static.wikia.nocookie.net/leagueoflegends/images/d/d5/Teemo_OriginalSquare.png"
    
    # Crea el contenido HTML con el mensaje y la imagen
    html_content = f"""
    <html>
        <head>
            <title>Hello World with Teemo</title>
        </head>
        <body>
            <h1>Hello World</h1>
            <img src="{teemo_image_url}" alt="Teemo">
        </body>
    </html>
    """
    return HTMLResponse(content=html_content)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

