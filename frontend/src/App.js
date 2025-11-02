import React, {useEffect, useState, useCallback} from 'react';
import axios from 'axios';
import './App.css';

function App(){
  const [users,setUsers]=useState([]);
  const [form,setForm]=useState({name:'',email:''});
  const API = process.env.REACT_APP_API || 'http://localhost:5000/api';

  const fetchUsers = useCallback(async () => {
    try{
      const res = await axios.get(`${API}/users`);
      setUsers(res.data);
    }catch(e){ console.error(e); }
  }, [API]);

  useEffect(()=>{ fetchUsers() },[fetchUsers]);

  async function submit(e){
    e.preventDefault();
    await axios.post(`${API}/users`, form);
    setForm({name:'',email:''}); fetchUsers();
  }

  return (
    <div className="container">
      <h1>Cloud App Dashboard</h1>
      <form onSubmit={submit}>
        <input required placeholder="Name" value={form.name} onChange={e=>setForm({...form,name:e.target.value})}/>
        <input required placeholder="Email" value={form.email} onChange={e=>setForm({...form,email:e.target.value})}/>
        <button>Add</button>
      </form>
      <table>...
      {users.map(u=>(
        <tr key={u.id}><td>{u.id}</td><td>{u.name}</td><td>{u.email}</td></tr>
      ))}
      </table>
    </div>
  );
}
export default App;
