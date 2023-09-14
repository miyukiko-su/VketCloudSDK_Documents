# ブラウザウィンドウが暗転したまま動かない

ワールド入場時にブラウザウィンドウが暗転したまま動かない場合は、以下の点をチェックしてみてください。

|  原因 |  対策  |
| ----   | ---- |
| ブラウザのハードウェアアクセラレーションが無効になっている | ブラウザの設定から「ハードウェアアクセラレーション」を有効にしてください |
| PCにゲームパッドが接続されている | 該当のゲームパッドの接続を切断してください |
| ビルドエラーが発生している | [ビルドエラー](./BuildError.md)の有無を確認してください |

例として、Chromeを使用している場合は設定ページの「システム」から「ハードウェアアクセラレーションが使用可能な場合は使用する」を有効にすることでワールド入場時の暗転が解消される場合があります。

![BrowserBlackWindow](./img/BrowserBlackWindow_ja.jpg)