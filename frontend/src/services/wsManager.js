class WebSocketManager {
  WS_URL = "ws://localhost:8002/api/generate";

  constructor() {
    this.ws = null;
    this.messageQueue = [];
    this.isConnected = false;
  }

  connect(setStatus) {
    if (this.ws && this.ws.readyState === WebSocket.OPEN) {
      return Promise.resolve();
    }

    return new Promise((resolve, reject) => {
      this.ws = new WebSocket(this.WS_URL);

      this.ws.onopen = () => {
        this.isConnected = true;
        setStatus("Connected");
        resolve();
      };

      this.ws.onmessage = (event) => {
        const data = JSON.parse(event.data);
        console.log(data);
        if (data.status) {
          setStatus(data.status);
        }
      };

      this.ws.onclose = (event) => {
        this.isConnected = false;
        setStatus("Connection closed");
        console.log(event);
        reject(new Error("WebSocket connection closed"));
      };

      this.ws.onerror = (error) => {
        this.isConnected = false;
        setStatus("error");
        console.error("WebSocket error:", error);
        reject(error);
      };
    });
  }

  sendMessage(message, setStatus) {
    if (this.isConnected) {
      console.log("Sending message");
      setStatus("Prompt Submitted");
      this.ws.send(JSON.stringify(message));
    }
  }

  disconnect(setStatus) {
    if (this.ws) {
      setStatus("disconnecting");
      this.ws.close();
      this.ws = null;
    }
  }
}

export default new WebSocketManager();
