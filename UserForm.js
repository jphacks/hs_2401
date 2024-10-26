// UserForm.js

import React, { useState } from 'react';
import axios from 'axios';

function UserForm({ onUserAdded }) {
  const [name, setName] = useState('');
  const [hometown, setHometown] = useState('');
  const [mbti, setMbti] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      await axios.post('http://127.0.0.1:5000/api/users', {
        name,
        hometown,
        mbti,
      });
      // フォームをリセット
      setName('');
      setHometown('');
      setMbti('');
      // ユーザー一覧を再取得
      onUserAdded();
    } catch (error) {
      console.error('ユーザーの作成に失敗しました:', error);
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <div>
        <label>名前:</label>
        <input type="text" value={name} onChange={(e) => setName(e.target.value)} required />
      </div>
      <div>
        <label>出身地:</label>
        <input type="text" value={hometown} onChange={(e) => setHometown(e.target.value)} required />
      </div>
      <div>
        <label>MBTIタイプ:</label>
        <input type="text" value={mbti} onChange={(e) => setMbti(e.target.value)} />
      </div>
      <button type="submit">送信</button>
    </form>
  );
}

export default UserForm;