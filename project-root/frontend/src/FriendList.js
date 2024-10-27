// frontend/src/FriendList.js
import React, { useState, useEffect } from 'react';

function FriendList({ friends, onShowCard }) {
  const [selectedFriend, setSelectedFriend] = useState(null);
  const [commonTopics, setCommonTopics] = useState([]);
  const [topicSuggestions, setTopicSuggestions] = useState([]);

  // 名刺ポップアップを閉じる関数
  const closePopup = () => setSelectedFriend(null);

  // 共通の話題を生成
  useEffect(() => {
    const calculateCommonTopics = () => {
      const topics = [];
      const hometowns = friends.map(friend => friend.hometown);
      const mbtiTypes = friends.map(friend => friend.mbti);
      const hobbys = friends.map(friend => friend.hobby);
      const favorFood = friends.map(friend => friend.favoriteFood);

      // 出身地の共通項
      if (new Set(hometowns).size === 1) {
        topics.push(`みんなの出身地: ${hometowns[0]}`);
      }

      // MBTIの共通項
      if (new Set(mbtiTypes).size === 1) {
        topics.push(`みんなのMBTIタイプ: ${mbtiTypes[0]}`);
      }

      // 趣味の共通項
      if (new Set(hobbys).size === 1) {
        topics.push(`みんなの趣味: ${hobbys[0]}`);
      }

      // 好きな食べ物の共通項
      if (new Set(favorFood).size === 1) {
        topics.push(`みんなの好きな食べ物: ${favorFood[0]}`);
      }

      setCommonTopics(topics);
    };

    calculateCommonTopics();
  }, [friends]);

  // 話題の提案を生成
  useEffect(() => {
    const generateTopicSuggestions = () => {
      if (friends.length === 0) return;

      const suggestions = [];
      const hometown = friends[friends.length - 1].hometown;
      const hobby = friends[friends.length - 1].hobby;

      suggestions.push(`出身地「${hometown}」のおすすめスポットについて話してみましょう。`);
      suggestions.push(`最近の「${hobby}」に関連する話題について語りましょう。`);
      suggestions.push("普段の生活で楽しいことについて話してみましょう！");

      setTopicSuggestions(suggestions);
    };

    generateTopicSuggestions();
  }, [friends]);

  return (
    <div>
      <h2>送信された友達</h2>
      <ul>
      {friends.map((friend, index) => (
          <li key={index}>
            <strong>名前:</strong> {friend.name}<br />
            {/* 名刺ボタンを追加することもできます */}
            <button onClick={() => onShowCard(friend)}>名刺</button>
          </li>
        ))}
      </ul>

      {selectedFriend && (
        <div style={{
          position: 'fixed', top: '20%', left: '50%', transform: 'translate(30%, -50%)',
          backgroundColor: 'white', padding: '20px', border: '1px solid black', borderRadius: '5px'
        }}>
          <h3>{selectedFriend.name}の名刺</h3>
          <p>出身地: {selectedFriend.hometown}</p>
          <p>MBTI: {selectedFriend.mbti}</p>
          <p>趣味: {selectedFriend.hobby}</p>
          <p>好きな食べ物: {selectedFriend.favoriteFood}</p>
          <button onClick={closePopup}>閉じる</button>
        </div>
      )}
      {/* 共通の話題セクション */}
      <div>
        <h3>共通の話題</h3>
        <ul>
          {commonTopics.map((topic, index) => (
            <li key={index}>{topic}</li>
          ))}
        </ul>
      </div>

      {/* 話題の提案セクション */}
      <div>
        <h3>話題の提案</h3>
        <ul>
          {topicSuggestions.map((suggestion, index) => (
            <li key={index}>{suggestion}</li>
          ))}
        </ul>
      </div>
    </div>
  );
}

export default FriendList;
