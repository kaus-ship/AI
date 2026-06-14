import "./App.css";
import UploadPanel from "./components/UploadPanel";
import ChatBox from "./components/ChatBox";

function App() {
  return (
    <div className="container">
      <h1>AI Learning Assistant</h1>

      <UploadPanel />

      <hr />

      <ChatBox />
    </div>
  );
}

export default App;