import getApiUrl from "../utils/getApiUrl";

class GenerateService {
  url = `${getApiUrl()}/generate`;
  eventSource = null;

  constructor() {}

  connect(prompt, setStatus) {
    const urlWithPrompt = `${this.url}?prompt=${prompt}`;
    this.eventSource = new EventSource(urlWithPrompt, {
      withCredentials: true,
    });

    this.eventSource.onopen = () => {
      console.log("Connected to server");
      setStatus("Connected");
    };

    this.eventSource.onmessage = (e) => {
      console.log("message received", e.data);

      setStatus(e.data);

      if (e.data == "Image.jpg") {
        setStatus(e.data);
        this.disconnect();
      }
    };
  }

  disconnect() {
    if (this.eventSource) {
      this.eventSource.close();
      this.eventSource = null;
    }
  }
}

export default GenerateService;
