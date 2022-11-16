# 3.4.4
##heliodor
- テキストチャットの色を変更出来るようにしました
- クローンリストコマンドにSetCloneGUITextMeasuredを追加しました
- sysmsgネットワークコマンドを追加しました
- ボイスミュートしていても新規ユーザーの声が聞こえてしまうバグを修正しました
- パーティクルを２回目以降再生出来ないバグを修正しました
- シングルプレイ時にメモリ範囲外アクセスバグを修正しました
- object指定のitemの高さが高くなってしまうバグを修正しました
- コミックビューワーに画像を大きくする機能を追加しました

##SDK

# 3.4.1
##heliodor
- スライダーの操作性を向上しました

##SDK
- AutoTextureCompresser追加

# 3.4.0
##heliodor
- iOSでスクリーンショットを取るとSkywayが切断されてしまう問題の回避策を導入しました
- パーティクルエディタが出力したHEPファイルに関連するテクスチャの圧縮機能を実装しました
- Intel HD Graphicsなど一部環境で色精度が下がってしまうバグを修正しました
- Sceneファイルのitem/objectにscaleが反映されるようにしました
- GUI/Buttonのクリック範囲を指定出来るようにしました
- GUI/Textのアライメントを設定出来るようにしました
- Sceneファイルのbloomにuseフラグを追加しました
- HEOTexCompを実行ファイル形式からPythonスクリプトに変更しました
- コンフィグのカメラ速度を０にしても動くようにしました
- ライセンスリストにODEを追加しました
- テクスチャを持たないHEO読み込み時にHEOTexCompの警告が出ないようにしました
- パーティクルエディタ/ファンクションカーブを追加しました
- MeshColliderとの衝突判定を最適化しました
- BoxColliderのクリック判定が正しくおこなわれない場合があるバグを修正しました
- playersのactionsから呼び出せる機能をclickablenodes等と共通化しました
- まれに動画再生開始に失敗してしまうバグを修正しました
- 動画再生中に他のプレイヤーがログインすると動画が停止してしまうバグを修正しました
- 1番目のemotionsのactionsが実行されないバグを修正しました
- FPSモードでアバターがX軸回転して他のプレイヤーから見えてしまうバグを修正しました

##SDK

# 3.3.5
- AnimationConverterを追加

# 3.3.3
- コントロールパネルのトップ画を差し替え
- コントロールパネルのチュートリアル導入ボタンを整備
- マイアバター機能を追加

# 3.3.0
- ジャンプ機能を実装しました
- JavaScriptからhel_canvas_SetGUIImageByHTMLCanvasでHTML CanvasをGUIパーツに設定する機能を実装しました
- HEOExporter／ライトマップのテクスチャ圧縮に対応しました
- GUIButtonのクリック範囲指定機能を実装しました
- iOS15でスクショが反転するバグを修正しました
- 初回ローディング中にWASDキーで移動出来てしまうバグを修正しました
- ルームURLボタンが画面縦横切り替えで表示されなくなるバグを修正しました
- コンフィグワールドタブの非表示機能が動かなくなっていたバグを修正しました
- MToonリムライトテクスチャに対応しました
- ParticleEditorがWindowsアプリからWebアプリに変わりました
- 動画スライダーの時刻表示が更新されないバグを修正しました
- Sceneファイルのavatars/idの重複チェックをおこなうようにしました
- 撮影モードを実装しました
- BoxColliderのenable設定が効いていなかったバグを修正しました
- GUIButtonのMask外を押せてしまうバグを修正しました
- glTF／PBR拡張を実装しました