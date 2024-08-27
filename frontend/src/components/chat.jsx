import React, { useEffect, useState } from 'react';

const Chat = ({ session_id, user_id }) => {
    const [messages, setMessages] = useState([]);
    const [input, setInput] = useState('');

    useEffect(() => {
        const fetchMessages = async () => {
            const response = await fetch("http://127.0.0.1:8000/get_messages/", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({
                    session_id: session_id,
                    user_id: user_id
                })
            });
            const data = await response.json();
            const formattedMessages = data.messages.map(([text, sender]) => ({ text, sender }));
            setMessages(formattedMessages);
            console.log(formattedMessages);
        };

        fetchMessages();
    }, [session_id, user_id]);

    const sendMessage = async () => {
        // Add the user message to the state immediately
        setMessages((prevMessages) => [...prevMessages, { text: input, sender: 'user' }]);
    
        try {
            const response = await fetch("http://127.0.0.1:8000/chat/", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({
                    message_text: input,
                    session_id: session_id,
                    user_id: user_id
                })
            });
    
            if (response.ok) {
                const data = await response.json();
                if (data.system_reply) {
                    // Add the system reply to the state
                    setMessages((prevMessages) => [...prevMessages, { text: data.system_reply, sender: 'system' }]);
                } else {
                    console.error("API response does not contain 'system_reply' field:", data);
                }
            } else {
                console.error("Failed to send message:", response.statusText);
            }
        } catch (error) {
            console.error("Error sending message:", error);
        } finally {
            // Clear the input field
            setInput('');
        }
    };

    return (
        <div>
            <div className="mx-auto  max-w-full h-80 [&>*:nth-child(even)]:ml-auto overflow-y-scroll">
    {messages.map((message, index) => (
        <div
            key={index}
            className={`my-1.5 p-2.5  max-w-[60%] ${
                message.sender === 'user' ? 'w-max max-w-sm m-4 px-4 py-2 text-white rounded-2xl rounded-br-none bg-pink-500' : 'w-max max-w-sm m-4 px-4 py-2 rounded-2xl rounded-bl-none bg-gray-200'
            }`}
        >
            <strong>{message.sender}:</strong> {message.text}
        </div>
    ))}
    
    
    </div><div className="flex flex-col w-full sm:flex-row items-center mt-2">
            <input
            type="text"
            value={input}
            onChange={(e) => setInput(e.target.value)}
            className="border p-3 w-full sm:w-auto flex-grow sm:flex-grow-5"
        />
        <button
            onClick={sendMessage}
            className="transition transition-all block py-3 px-4 w-1/4 text-white font-bold rounded cursor-pointer bg-gradient-to-r from-indigo-600 to-purple-400 hover:from-indigo-700 hover:to-purple-500 focus:bg-indigo-900"
        >
            Send
        </button>
    </div>
    </div>
        
    );
};

export default Chat;