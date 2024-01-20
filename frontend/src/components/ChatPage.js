import React, { useState } from 'react';
import axios from 'axios';

const ChatPage = () => {
  const [message, setMessage] = useState('');
  const [responses, setResponses] = useState([]);

  const sendMessage = async () => {
    try {
      const response = await axios.post('http://localhost:5000/chatbot', { message });
      setResponses([...
responses, response.data]);
} catch (error) {
console.error('Error in sending message:', error);
}
};

return (
<div>
<input
type="text"
value={message}
onChange={(e) => setMessage(e.target.value)}
/>
<button onClick={sendMessage}>Send</button>
<div>
{responses.map((res, index) => (
<p key={index}>{res.message.content}</p>
))}
</div>
</div>
);
};

export default ChatPage;