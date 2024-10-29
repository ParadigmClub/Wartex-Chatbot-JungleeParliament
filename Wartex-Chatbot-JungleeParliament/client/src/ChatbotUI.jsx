import { useState, useEffect, useRef } from "react";
import { Bot, User } from "lucide-react";
import "boxicons";
import backgroundImage from './bg.jpg'; // Import the image

export default function ChatbotUI() {
  // State initialization
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState("");
  const [isLoading, setIsLoading] = useState(false);
  const [showGreeting] = useState(true); // Static greeting state
  const messagesEndRef = useRef(null);

  // Predefined prompts
  const prompts = [
    "Who is the President of the Sabha ",
    "How will the water crisis be solved? ",
    "Who will be the leader? ",
    "What is the future of the Sabha? ",
  ];

  // Scroll to bottom of messages on update
  useEffect(() => {
    scrollToBottom();
  }, [messages]);

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: "smooth" });
  };

  // Function to handle bullet points and bold formatting
  const formatMessageContent = (content) => {
    const formattedContent = content.split("\n").map((line, index) => {
      if (line.startsWith("* ")) {
        return <li key={index}>{applyBold(line.replace("* ", ""))}</li>;
      }
      return <p key={index}>{applyBold(line)}</p>;
    });
    return <ul className="list-disc pl-5 space-y-1">{formattedContent}</ul>;
  };

  // Function to apply bold formatting
  const applyBold = (text) => {
    const parts = text.split(/(\*\*[^*]+\*\*)/g);
    return parts.map((part, index) =>
      part.startsWith("**") && part.endsWith("**") ? (
        <strong key={index}>{part.slice(2, -2)}</strong>
      ) : (
        part
      )
    );
  };

  // Handle preset prompt click
  const handlePresetClick = (prompt) => {
    setInput(prompt);
  };

  // Handle user message submission
  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!input.trim()) return;

    setMessages((prev) => [...prev, { role: "user", content: input }]);
    setInput("");
    setIsLoading(true);

    try {
      const response = await fetch("/api/send_message", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message: input }),
      });
      const data = await response.json();
      setMessages((prev) => [...prev, { role: "bot", content: data.response }]);
    } catch (error) {
      console.error("Error sending message:", error);
    } finally {
      setIsLoading(false);
    }
  };

  // Function to generate random styles for leaves
  const randomizeStyle = () => {
    const randomDelay = Math.random() * 5; // Random delay
    const randomDuration = 5 + Math.random() * 5; // Random duration
    const randomPosition = Math.random() * 100; // Random horizontal position

    return {
      animationDelay: `${randomDelay}s`,
      animationDuration: `${randomDuration}s`,
      left: `${randomPosition}vw`, // Positioning leaves randomly across the width
    };
  };

  // JSX layout
  return (
    <div
      className="flex flex-col h-screen relative overflow-hidden w-screen animated-background "
      style={{
        backgroundImage: `url(${backgroundImage})`,
        backgroundSize: 'cover',
        backgroundPosition: 'center',

      }}
    >
      {/* Leaf Animation */}
      <div className="absolute top-0 left-0 right-0 h-full flex justify-between overflow-hidden pointer-events-none">
        {Array.from({ length: 10 }).map((_, index) => (
          <div
            key={`leaf-${index}`}
            className="inline-block w-[30px] h-[23px] bg-gradient-to-br from-leafGreen-dark to-leafGreen-light rounded-[5%_40%_70%] shadow-inner border border-[#333] animate-falling opacity-70"
            style={randomizeStyle()}
          />
        ))}
      </div>

      {/* Chat Messages */}
      <div className="flex-1 overflow-y-auto pl-36 pr-36 pt-18 max-xl:p-10 space-y-6 items-center">
        {showGreeting && (
          <div className="flex flex-col justify-center items-center h-[95%] text-center">
            <section>
              <p className="text-6xl max-lg:text-4xl text-white">
                Welcome to <span className="font-bold">The PAWLIAMENT - The Beast Sabha</span>
              </p>
              <p className="text-lg text-white mt-4">
                Try one of these prompts:
              </p>
              <div className="flex flex-wrap items-center justify-center mt-2 space-x-2">
                {prompts.map((prompt, index) => (
                  <span
                    key={index}
                    className="text-white cursor-pointer hover:underline"
                    onClick={() => handlePresetClick(prompt)}
                  >
                    {prompt}
                    {index < prompts.length - 1 && (
                      <span className="mx-3 hover:outline-none">•</span>
                    )}
                  </span>
                ))}
              </div>
            </section>
          </div>
        )}

        {/* Messages */}
        {messages.map((message, index) => (
          <div
            key={index}
            className={`flex ${message.role === "user" ? "justify-end" : "justify-start"}`}
          >
            <div className="flex items-start space-x-4">
              {message.role === "bot" && (
                <div className="p-2 rounded-3xl bg-green-500 text-black">
                  <Bot className="w-6 h-6" />
                </div>
              )}
              <div
                className={`p-[0.7rem] rounded-2xl max-w-2xl ${
                  message.role === "user" ? "bg-[#F5F5F5] text-black self-center" : "bg-[#383838] text-white"
                }`}
              >
                {formatMessageContent(message.content)}
              </div>
              {message.role === "user" && (
                <div className="p-2 rounded-3xl bg-blue-500 text-white">
                  <User className="w-6 h-6" />
                </div>
              )}
            </div>
          </div>
        ))}

        {/* Loading indicator */}
        {isLoading && (
          <div className="flex justify-start">
            <div className="flex items-center space-x-2">
              <div className="p-2 rounded-3xl bg-white animate-pulseColor text-white">
                <Bot className="w-6 h-6 animate-pulse" />
              </div>
              <div className="p-3 rounded-lg bg-[#383838]">Thinking...</div>
            </div>
          </div>
        )}
        <div ref={messagesEndRef} />
      </div>

      {/* Input Section */}
      <div className="flex items-center justify-center p-10 transparent ">
        <div className="absolute bottom-5 left-1/2 transform -translate-x-1/2 overflow-hidden z-0 rounded-full p-[0.3rem] w-3/5">
          <form
            onSubmit={handleSubmit}
            role="form"
            className="relative flex z-50 bg-black rounded-full items-center"
          >
            <input
              type="text"
              value={input}
              onChange={(e) => setInput(e.target.value)}
              placeholder="Type your message..."
              className="rounded-full flex-1 px-4 py-2 text-white focus:outline-none"
            />
            <button type="submit">
              <i className="bx bxs-up-arrow-circle text-4xl px-4 text-white rounded-full py-2"></i>
            </button>
          </form>

          {/* Glowing background effects */}
          <div className="glow glow-1 z-10 bg-[#1e6091] absolute"></div>
          <div className="glow glow-2 z-20 bg-[#34a0a4] absolute"></div>
          <div className="glow glow-3 z-30 bg-[#99d98c] absolute"></div>
          <div className="glow glow-4 z-40 bg-[#1e6091] absolute"></div>
        </div>
      </div>
    </div>
  );
}

// CSS for falling leaves animation
const styles = `
@keyframes falling {
  0% {
    transform: translateY(-100px);
    opacity: 1;
  }
  100% {
    transform: translateY(100vh);
    opacity: 0;
  }
}

.animate-falling {
  animation-name: falling;
  animation-timing-function: ease-in;
  animation-iteration-count: infinite;
}
.leafGreen-light {
  background-color: #e2f0cb;
}
.leafGreen-dark {
  background-color: #4b8a1d;
}
`;
