// App.js

import React, { useState, useEffect } from 'react';
import UserForm from './UserForm';
import UserList from './UserList';
import axios from 'axios';

function App() {
  const [users, setUsers] = useState([]);

  // ユーザー一覧を取得する関数
  const fetchUsers = async () => {
    try {
      const response = await axios.get('http://127.0.0.1:5000/api/users');
      setUsers(response.data);
    } catch (error) {
      console.error('ユーザー一覧の取得に失敗しました:', error);
    }
  };

  // 初回レンダリング時とユーザーが追加されたときにユーザー一覧を取得
  useEffect(() => {
    fetchUsers();
  }, []);

  return (
    <div>
      <h1>会話促進アプリへようこそ</h1>
      <UserForm onUserAdded={fetchUsers} />
      <UserList users={users} />
    </div>
  );
}

export default App;