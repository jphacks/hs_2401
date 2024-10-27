// frontend/src/UserForm.js
import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { io } from 'socket.io-client';
import FriendList from './FriendList';
import FriendCard from './FriendCard';

const socket = io('http://localhost:5000');

function UserForm() {
  const [name, setName] = useState('');
  const [hometown, setHometown] = useState('');
  const [mbti, setMbti] = useState('');
  const [hobby, setHobby] = useState('');
  const [favoriteFood, setFavoriteFood] = useState('');
  const [friends, setFriends] = useState([]); // friendsの定義
  const [showCard, setShowCard] = useState(false);
  const [selectedFriend, setSelectedFriend] = useState(null);

  useEffect(() => {
    socket.on('connect', () => {
      console.log('サーバーに接続しました');
    });
    return () => {
      socket.disconnect();
    };
  }, []);

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post('http://localhost:5000/api/users', {
        name,
        hometown,
        mbti,
        hobby,
        favoriteFood,
      });
      console.log('ユーザーが作成されました:', response.data);
      socket.emit('join', response.data);

      // 友達を追加
      setFriends((prevFriends) => [...prevFriends, response.data]); // 友達を追加する処理

      // 入力をクリア
      setName('');
      setHometown('');
      setMbti('');
      setHobby('');
      setFavoriteFood('');
    } catch (error) {
      console.error('ユーザーの作成に失敗しました:', error);
    }
  };

  const handleShowCard = (friend) => {
    setSelectedFriend(friend);
    setShowCard(true);
  };

  const handleCloseCard = () => {
    setShowCard(false);
    setSelectedFriend(null);
  };

  return (
    <div>
      <form onSubmit={handleSubmit}>
        <div>
          <label>名前:</label>
          <input type="text" value={name} onChange={(e) => setName(e.target.value)} required />
        </div>
        <div>
          <label>出身地:</label>
          <select value={hometown} onChange={(e) => setHometown(e.target.value)} required>
            <option value="">選択してください</option>
            <option value="北海道">北海道</option>
            <option value="東北">東北</option>
            <option value="関東">関東</option>
            <option value="中部">中部</option>
            <option value="近畿">近畿</option>
            <option value="中国">中国</option>
            <option value="四国">四国</option>
            <option value="九州">九州</option>
            <option value="海外">海外</option>
          </select>
        </div>
        <div>
          <label>MBTI:</label>
          <select value={mbti} onChange={(e) => setMbti(e.target.value)} required>
            <option value="">選択してください</option>
            <option value="INTJ">INTJ:建築家</option>
            <option value="INTP">INTP:論理学者</option>
            <option value="ENTJ">ENTJ:指揮官</option>
            <option value="ENTP">ENTP:討論者</option>
            <option value="INFJ">INFJ:提唱者</option>
            <option value="INFP">INFP:仲介者</option>
            <option value="ENFJ">ENFJ:主人公</option>
            <option value="ENFP">ENFP:運動家</option>
            <option value="ISTJ">ISTJ:管理者</option>
            <option value="ISFJ">ISFJ:擁護者</option>
            <option value="ESTJ">ESTJ:幹部</option>
            <option value="ESFJ">ESFJ:領事</option>
            <option value="ISTP">ISTP:巨匠</option>
            <option value="ISFP">ISFP:冒険家</option>
            <option value="ESTP">ESTP:起業家</option>
            <option value="ESFP">ESFP:エンターテイナー</option>
          </select>
        </div>
        <div>
          <label>趣味:</label>
          <select value={hobby} onChange={(e) => setHobby(e.target.value)} required>
            <option value="">選択してください</option>
            <option value="アウトドア">アウトドア</option>
            <option value="インドア">インドア</option>
          </select>
        </div>
        <div>
          <label>好きな食べ物:</label>
          <select value={favoriteFood} onChange={(e) => setFavoriteFood(e.target.value)} required>
            <option value="">選択してください</option>
            <option value="ジンギスカン">ジンギスカン</option>
            <option value="寿司">寿司</option>
            <option value="お好み焼き">お好み焼き</option>
            <option value="みかん">みかん</option>
            <option value="神戸牛">神戸牛</option>
            <option value="その他">その他</option>
          </select>
        </div>
        <button type="submit">送信</button>
      </form>
      <FriendList friends={friends} onShowCard={handleShowCard} />
      {showCard && selectedFriend && (
        <FriendCard friend={selectedFriend} onClose={handleCloseCard} />
      )}
    </div>
  );
}

export default UserForm;
