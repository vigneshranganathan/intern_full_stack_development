import React, { useState, useEffect } from 'react';

function Sessions({ user_id, setCurrentSession }) {
    const [sessions, setSessions] = useState([]);

    useEffect(() => {
        // Fetch sessions for the user
        fetchSessions();
    }, [user_id]);

    const fetchSessions = async () => {
        console.log("Fetching sessions for user ID:", user_id);
        if (!user_id) {
            alert("User ID not found. Please login again.");
            return;
        }
        
        const userIdInt = parseInt(user_id, 10);
        
        const response = await fetch("http://127.0.0.1:8000/get_sessions/", {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ user_id: userIdInt }),
        });
        
        const data = await response.json();
        setSessions(data.sessions);
        console.log("Sessions:", data.sessions);
    };

    const addSession = async () => {
        const response = await fetch("http://127.0.0.1:8000/add_session/", {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ user_id }),
        });
        const data = await response.json();
        setSessions([...sessions, data.new_session]);
        fetchSessions();
    };

    const selectSession = (session_id) => {
        setCurrentSession(session_id);
    };

    const [selectedSession, setSelectedSession] = useState(null);

    const handleSelectSession = (session) => {
        setSelectedSession(session);
        selectSession(session);
    };

    return (
        <div className="w-full bg-grey h-80 overflow-y-scroll">
            <button
                onClick={addSession}
                className="transition transition-all block py-3 px-4 w-full text-white font-bold rounded cursor-pointer bg-gradient-to-r from-indigo-600 to-purple-400 hover:from-indigo-700 hover:to-purple-500 focus:bg-indigo-900 transform hover:-translate-y-1 hover:shadow-lg"
            >
                Add Session
            </button>
            <ul>
                {sessions.map((session, index) => (
                    <li
                        key={index}
                        onClick={() => handleSelectSession(session)}
                        className={`block font-bold w-full text-lg text-center cursor-pointer rounded-lg p-4 transition duration-500 ${
                            selectedSession === session
                                ? 'bg-neutral-100 text-neutral-500 dark:bg-neutral-600 dark:text-neutral-200'
                                : 'hover:bg-neutral-100 hover:text-neutral-500 focus:bg-neutral-100 focus:text-neutral-500 dark:hover:bg-neutral-600 dark:hover:text-neutral-200 dark:focus:bg-neutral-600 dark:focus:text-neutral-200'
                        }`}
                    >
                        Session: {session}
                    </li>
                ))}
            </ul>
        </div>
    );
}

export default Sessions;