import React ,{useState} from "react";
;
import { useNavigate } from "react-router-dom";



  

const  register=()=>{

    const [username, setUsername] = useState("");
    const [password, setPassword] = useState("");
    const [email, setEmail] = useState("");
  
  const navigate = useNavigate();
  const handleregister = async (e) => {
    e.preventDefault();
    try {
        console.log({ username, password, email });
        const response = await fetch("http://127.0.0.1:8000/register/", {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({ username, password, email }),
        });
  
        if (response.ok) {
          const data = await response.json();
          if (data.status === 1) {
            // Registration successful, navigate to another page
            alert("Registration successful. Please login to continue.");
            navigate('/');
          } else {
            console.error("Registration failed:", data);
          }
        } else {
          console.error("Failed to register:", response.statusText);
        }
      } catch (error) {
        console.error("Error registering:", error);
      }
  };

  const loginnav = () => {
    navigate("/");
  }
  
    return (
        <>
    <div className="bg-gray-200 flex justify-center items-center h-screen w-screen">
      <div className=" border-t-8 rounded-sm border-indigo-600 bg-white p-12 shadow-2xl w-96">
        <h1 className="font-bold text-center block text-2xl">Register here</h1>
        <form onSubmit={handleregister}>
         <label className="text-gray-500 block mt-3">Username
        <input
          autoFocus={true}
          type="text"
          id="username" 
          name="username"
          placeholder="myuseranme"
          onChange={(e) => setUsername(e.target.value)}
          className="rounded px-4 py-3 w-full mt-1 bg-white text-gray-900 border border-gray-200 focus:border-indigo-400 focus:outline-none focus:ring focus:ring-indigo-100"/>
      </label>
      <label className="text-gray-500 block mt-3">Email
        <input
          autoFocus={true}
          type="email" 
          id="email" 
          name="email"
          placeholder="me@gmail.com"
          onChange={(e) => setEmail(e.target.value)}
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
          Register
        </button>

        
        </form>
        <button type="button" onClick={loginnav} className="mt-6 transition transition-all block py-3 px-4 w-full text-white font-bold rounded cursor-pointer bg-gradient-to-r from-indigo-600 to-purple-400 hover:from-indigo-700 hover:to-purple-500 focus:bg-indigo-900 transform hover:-translate-y-1 hover:shadow-lg">
          Login</button>
        
      </div>
    </div>


        </>
    );
    }



export default register;