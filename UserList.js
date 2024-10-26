// UserList.js

import React from 'react';

function UserList({ users }) {
  return (
    <div>
      <h2>ユーザー一覧</h2>
      <ul>
        {users.map((user, index) => (
          <li key={index}>
            名前: {user.name}, 出身地: {user.hometown}, MBTI: {user.mbti}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default UserList;