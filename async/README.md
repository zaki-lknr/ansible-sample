# asyncとpollを使った非同期処理

以下にまとめた。

[[Ansible] asyncとpollを使った非同期処理とループの並列実行 - zaki work log](https://zaki-hmkc.hatenablog.com/entry/2021/04/06/214645)

# ソース

- base.yml: 比較用同期処理
- async-poll.yml: async + poll を使ったtaskの非同期処理おためし
- async-loop.yml: async + poll + loop によるループの並列処理と結果の取得
