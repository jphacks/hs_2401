import React from 'react';
import ReactDOM from 'react-dom/client'; // 'react-dom/client'からインポート
import App from './App'; // アプリケーションのメインコンポーネント

// root要素を取得
const rootElement = document.getElementById('root');

// createRootを使用してReactアプリケーションを描画
const root = ReactDOM.createRoot(rootElement);
root.render(
    <React.StrictMode>
        <App />
    </React.StrictMode>
);
