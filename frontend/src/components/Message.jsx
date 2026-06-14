import ReactMarkdown from "react-markdown";

function Message({ message }) {
  return (
    <div className="message">

      <p>
        <strong>You:</strong> {message.question}
      </p>

      <div className="answer">
        <ReactMarkdown>
          {message.answer}
        </ReactMarkdown>
      </div>

      {message.sources?.length > 0 && (
        <>
          <h4>Sources</h4>

          <ul>
            {message.sources.map((source, index) => (
              <li key={index}>{source}</li>
            ))}
          </ul>
        </>
      )}

    </div>
  );
}

export default Message;