class WebSocketManager {
  WS_URL = "ws://localhost:8002/api/generate";

  constructor(onUpdate) {
    this.ws = null;
    this.onUpdate = onUpdate;
    this.messageQueue = [];
    this.isConnected = false;
  }

  connect() {
    if (this.ws && this.ws.readyState === WebSocket.OPEN) {
      return Promise.resolve();
    }

    return new Promise((resolve, reject) => {
      this.ws = new WebSocket(this.WS_URL);

      this.ws.onopen = () => {
        this.isConnected = true;
        this.onUpdate("connected");
        this.flushMessageQueue();
        resolve();
      };

      this.ws.onmessage = (event) => {
        this.onUpdate(event);
      };

      this.ws.onclose = () => {
        this.isConnected = false;
        this.onUpdate("closed");
        console.log("WebSocket connection closed");
        reject(new Error("WebSocket connection closed"));
      };

      this.ws.onerror = (error) => {
        this.isConnected = false;
        this.onUpdate("error");
        console.error("WebSocket error:", error);
        reject(error);
      };
    });
  }

  sendMessage(message) {
    if (this.isConnected) {
      console.log("Sending message");
      this.ws.send(JSON.stringify(message));
    } else {
      console.log("Queuing message");
      this.messageQueue.push(message);
    }
  }

  flushMessageQueue() {
    while (this.messageQueue.length > 0) {
      const message = this.messageQueue.shift();
      this.sendMessage(message);
    }
  }

  disconnect() {
    if (this.ws) {
      this.ws.close();
      this.ws = null;
    }
  }
}

export default WebSocketManager;
