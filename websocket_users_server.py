import asyncio
import websockets

# Обработчик сообщений от клиента
# Принимает сообщение от клиента и отправляет его обратно
async def echo(websocket):
    async for message in websocket: # Ожидание сообщений от клиента
        print(f"Получено сообщение от пользователя: {message}")
        
        # Отправка пяти ответных сообщений
        for i in range(1, 6):
            response = f"{i} Сообщение пользователя: {message}" # Сообщение для отправки клиенту
            await websocket.send(response)  # Отправка сообщения обратно клиенту


# Запуск WebSocket-сервера
async def main():
    server = await websockets.serve(echo, "localhost", 8765) # Запуск WebSocket-сервера на порту 8765
    print("WebSocket сервер запущен на ws://localhost:8765")
    await server.wait_closed() # Ожидание закрытия сервера


if __name__ == "__main__":
    asyncio.run(main()) # Запуск WebSocket-сервера  
