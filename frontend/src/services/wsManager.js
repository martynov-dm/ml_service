export const connectionStatuses = {
  idle: "Idle",
  connected: "Connected",
  closed: "Connection closed",
  error: "Error",
  disconnecing: "Disconnecing",
};

class WebSocketManager {
  WS_URL = "ws://localhost:8002/api/generate";

  constructor() {
    this.ws = null;
    this.messageQueue = [];
    this.isConnected = false;
  }

  connect(setStatus, setImageUrl) {
    if (this.ws && this.ws.readyState === WebSocket.OPEN) {
      return Promise.resolve();
    }

    return new Promise((resolve, reject) => {
      this.ws = new WebSocket(this.WS_URL);

      this.ws.onopen = () => {
        this.isConnected = true;
        setStatus(connectionStatuses.connected);
        resolve();
      };

      this.ws.onmessage = (event) => {
        const data = JSON.parse(event.data);
        console.log(data);
        if (data?.status) {
          setStatus(data.status);
        }
        if (data?.message?.url) {
          setImageUrl(data.message.url);
        }
      };

      this.ws.onclose = (event) => {
        this.isConnected = false;
        setStatus(connectionStatuses.closed);
        console.log(event);
        reject(new Error("WebSocket connection closed"));
      };

      this.ws.onerror = (error) => {
        this.isConnected = false;
        setStatus(connectionStatuses.error);
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
      setStatus(connectionStatuses.disconnecing);
      this.ws.close();
      this.ws = null;
    }
  }
}

export const wsManager = new WebSocketManager();
