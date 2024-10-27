// frontend/src/App.js
import React, { useState } from 'react';
import UserForm from './UserForm';
import { io } from 'socket.io-client';
import './FriendCard.css';


// サーバーのURLを指定
const socket = io('http://localhost:5000');

socket.on('connect', () => {
  console.log('Socket connected');
});

function App() {
  const [setFriends] = useState([]);

  // フレンドリストに友達を追加
  const addFriend = (friendData) => {
    setFriends((prevFriends) => [...prevFriends, friendData]);
  };

  return (
    <div className="app-container" style={{ display: 'flex', justifyContent: 'flex-start', alignItems: 'center', height: '100vh'}}>
      <header style={{ width: '50%' , backgroundcolor: '#4CAF50' }}>会話促進アプリへようこそ</header>
      <h2>入力してください</h2>
      <UserForm addFriend={addFriend} />
    </div>
  );
}

export default App;
