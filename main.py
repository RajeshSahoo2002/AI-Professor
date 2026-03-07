from fastapi import FastAPI # type: ignore

app=FastAPI()

@app.get("/")
def health_check():
    return{"status":"Application running successfully!"}
# def main():
#     print("Hello from ai-professor!")


# if __name__ == "__main__":
#     main()
