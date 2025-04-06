import { useState } from "react";
import { Html } from "@react-three/drei";

const TextField = () => {
  const [messages, setMessages] = useState([]);
  const [text, setText] = useState("");

  const handleSend = async () => {
    if (text.trim() === "") return;

    const userMessage = { text, sender: "user" };
    setMessages([...messages, userMessage]);

    try {
      const response = await fetch("http://127.0.0.1:5000/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message: text }),
      });

      const data = await response.json();
      const botMessage = { text: data.response, sender: "bot" };

      setMessages((prevMessages) => [...prevMessages, botMessage]);
    } catch (error) {
      console.error("Error:", error);
    }

    setText(""); // Clear input
  };

  const handleKeyPress = (e) => {
    if (e.key === "Enter") {
      handleSend();
    }
  };

  return (
    <Html center>
      <div style={styles.container}>
        <div style={styles.chatContainer}>
          <div style={styles.chatBox}>
            {messages.map((msg, index) => (
              <div
                key={index}
                style={{
                  ...styles.message,
                  alignSelf: msg.sender === "user" ? "flex-end" : "flex-start",
                  backgroundColor: msg.sender === "user" ? "#0A74DA" : "#5DADE2",
                }}
              >
                {msg.text}
              </div>
            ))}
          </div>
          <div style={styles.inputContainer}>
            <input
              type="text"
              value={text}
              onChange={(e) => setText(e.target.value)}
              onKeyDown={handleKeyPress}
              placeholder="Type a message..."
              style={styles.inputField}
            />
            <button onClick={handleSend} style={styles.sendButton}>Send</button>
          </div>
        </div>
      </div>
    </Html>
  );
};

const styles = {
  container: { position: "absolute", top: "50%", left: "400px", transform: "translateY(-40%)" },
  chatContainer: { display: "flex", flexDirection: "column", width: "400px", height: "500px", borderRadius: "10px", border: "2px solid gray", backgroundColor: "#121212", padding: "15px", boxShadow: "0px 4px 10px rgba(0,0,0,0.3)" },
  chatBox: { flex: 1, display: "flex", flexDirection: "column", gap: "10px", overflowY: "auto", padding: "10px", backgroundColor: "#1E1E1E", borderRadius: "8px", color: "white" },
  message: { padding: "10px", borderRadius: "10px", maxWidth: "80%", color: "white", fontSize: "14px" },
  inputContainer: { display: "flex", gap: "5px", marginTop: "10px" },
  inputField: { flex: 1, padding: "12px", fontSize: "16px", borderRadius: "5px", border: "1px solid gray", backgroundColor: "black", color: "white", outline: "none" },
  sendButton: { padding: "12px", fontSize: "16px", borderRadius: "5px", border: "none", backgroundColor: "#0A74DA", color: "white", cursor: "pointer" },
};

export default TextField;