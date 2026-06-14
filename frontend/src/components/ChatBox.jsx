import { useState } from "react";

import Message from "./Message";

import {
  askQuestion
} from "../services/api";

function ChatBox() {

  const [question,
    setQuestion] =
    useState("");

  const [messages,
    setMessages] =
    useState([]);

  const handleAsk =
    async () => {

      if (!question) return;

      const response =
        await askQuestion(
          question
        );

      const newMessage = {

        question,

        answer:
          response.data.answer,

        sources:
          response.data.sources
      };

      setMessages(
        [...messages,
        newMessage]
      );

      setQuestion("");
    };

  return (
    <div>

      <h2>
        Ask Questions
      </h2>

      <input
        type="text"
        value={question}
        onChange={(e) =>
          setQuestion(
            e.target.value
          )
        }
        placeholder="Ask something..."
      />

      <button
        onClick={handleAsk}
      >
        Ask
      </button>

      {messages.map(
        (msg, index) => (
          <Message
            key={index}
            message={msg}
          />
        )
      )}

    </div>
  );
}

export default ChatBox;