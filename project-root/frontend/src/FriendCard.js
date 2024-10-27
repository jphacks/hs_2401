// frontend/src/FriendCard.js
import React from 'react';
import './FriendCard.css'; // CSSファイルをインポート

const FriendCard = ({ friend, onClose }) => {
  return (
    <div className="friend-card">
      <h2 className="friend-name">{friend.name}</h2>
      {friend.image && (
        <img src={friend.image} alt={`${friend.name}'s profile`} className="friend-image" />
      )}
      <table>
        <tbody>
          <tr>
            <td>出身地</td>
            <td>{friend.hometown}</td>
          </tr>
          <tr>
            <td>MBTI</td>
            <td>{friend.mbti}</td>
          </tr>
          <tr>
            <td>趣味</td>
            <td>{friend.hobby}</td>
          </tr>
          <tr>
            <td>好きな食べ物</td>
            <td>{friend.favoriteFood}</td>
          </tr>
          <tr>
            <td>部活</td>
            <td>{friend.club}</td>
          </tr>
        </tbody>
      </table>
      <button onClick={onClose}>閉じる</button>
    </div>
  );
};

export default FriendCard;
