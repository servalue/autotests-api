import asyncio
import websockets

# Запуск клиента
async def client():
    uri = "ws://localhost:8765" # URI сервера
    async with websockets.connect(uri) as websocket: # Соединение с сервером
        message = "Привет, сервер!" # Сообщение для отправки серверу
        print(message)
        await websocket.send(message) # Отправка сообщения серверу
        
        # Получаем 5 сообщений от сервера
        for _ in range(5):
            response = await websocket.recv() # Получение ответа от сервера
            print(response)        


if __name__ == "__main__":
    asyncio.run(client()) # Запуск клиента
