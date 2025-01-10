import websocket
import json
from setting import config
# Define the WebSocket URL for Deriv
DERIV_WS_URL = "wss://ws.binaryws.com/websockets/v3?app_id="  +config["key"]

def on_message(ws, message):
    """
    Callback function that handles incoming messages from the WebSocket.
    """
    data = json.loads(message)
    print("Received data:", data)

def on_error(ws, error):
    """
    Callback function that handles any errors that occur.
    """
    print("Error:", error)

def on_close(ws):
    """
    Callback function that handles the WebSocket connection closure.
    """
    print("### Connection closed ###")

def on_open(ws):
    """
    Callback function that handles the opening of the WebSocket connection.
    """
    print("### Connection opened ###")
    
    # Example subscription request for a specific market
    subscribe_request = json.dumps({
        "ticks": "R_100",
        "subscribe": 1
    })
    
    ws.send(subscribe_request)

if __name__ == "__main__":
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp(DERIV_WS_URL,
                                on_message=on_message,
                                on_error=on_error,
                                on_close=on_close)
    ws.on_open = on_open
    ws.run_forever()
