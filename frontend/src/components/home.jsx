import React, { useState } from 'react';
import { useLocation } from 'react-router-dom';
import Sessions from './sessions';
import Chat from './chat';

function Home() {
    const location = useLocation();
    const { user_id } = location.state || {};
    console.log("User ID in Home:", user_id);

    const [currentSession, setCurrentSession] = useState(null);
    if(currentSession){
        console.log("Current Session ID:", currentSession);
    }

    return (
        <div className='items-center '>
    <h2>Home</h2>
    <p>Welcome to the home page!</p>

    <br></br>
    <br/>
    <div className="flex space-x-4   border border-black p-4">
        <div className="h-4/5 w-1/2 rounded border border-pruple p-7 items-center justify-center">
            <Sessions user_id={user_id} setCurrentSession={setCurrentSession} />
        </div>
        {currentSession && (
            <div className=" h-70 w-full rounded border border-black p-4">
                <Chat user_id={user_id} session_id={currentSession} />
            </div>
        )}
    </div>
</div>
    );
}

export default Home;