import React,{useState} from "react";
import { useNavigate } from "react-router-dom";



  

const  Login=()=>{

  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");

  const navigate = useNavigate();
  const handleLogin = async (e) => {
    e.preventDefault();
    try {
      console.log({ username,password});
      const response = await fetch("http://127.0.0.1:8000/login/", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ username, password }),
        
      });
      const data = await response.json();
      if (data.status === 1) {
        navigate("/home", { state: { user_id: data.user_id } });
      } else {
        alert("Login failed. Please check your credentials.");
      }
    } catch (error) {
      
      console.error("Error during login:", error);
    }
  };

  const regsiternav = () => {
    navigate("/register");
  }

    return (
        <>
    <div className="bg-gray-200 flex justify-center items-center h-screen w-screen">
      <div className=" border-t-8 rounded-sm border-indigo-600 bg-white p-12 shadow-2xl w-96">
        <h1 className="font-bold text-center block text-2xl">Log In</h1>
        <form onSubmit={handleLogin}>
         <label className="text-gray-500 block mt-3">Username
        <input
          autoFocus={true}
          type="text"
          id="username" 
          name="username"
          placeholder="myusername"
          onChange={(e) => setUsername(e.target.value)}
          className="rounded px-4 py-3 w-full mt-1 bg-white text-gray-900 border border-gray-200 focus:border-indigo-400 focus:outline-none focus:ring focus:ring-indigo-100"/>
      </label>
      <label className="text-gray-500 block mt-3">Password
        <input
          autoFocus={true}
          type="password" 
          id="password" 
          name="password"
          placeholder="**********"
          onChange={(e) => setPassword(e.target.value)}
          className="rounded px-4 py-3 w-full mt-1 bg-white text-gray-900 border border-gray-200 focus:border-indigo-400 focus:outline-none focus:ring focus:ring-indigo-100"/>
      </label>
        <button type="submit"
        className="mt-6 transition transition-all block py-3 px-4 w-full text-white font-bold rounded cursor-pointer bg-gradient-to-r from-indigo-600 to-purple-400 hover:from-indigo-700 hover:to-purple-500 focus:bg-indigo-900 transform hover:-translate-y-1 hover:shadow-lg">
          Submit
        </button>

        
        </form>
        <button type="button" onClick={regsiternav} className="mt-6 transition transition-all block py-3 px-4 w-full text-white font-bold rounded cursor-pointer bg-gradient-to-r from-indigo-600 to-purple-400 hover:from-indigo-700 hover:to-purple-500 focus:bg-indigo-900 transform hover:-translate-y-1 hover:shadow-lg">
          Register</button>
        
      </div>
    </div>


        </>
    );
    }

export default Login;