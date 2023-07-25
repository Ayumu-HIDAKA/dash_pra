# dash_pra
dashの簡単なデモです。
sqliteからデータをもってきてプロットします。

デモprepro_praで作成したdb.sqliteをapp.pyと同じディレクトリにおいてください

# setup
```
docker-compose up
```
コンテナにはいる(dash_praにサフィックスがついていると思います)
```
docker exec -it コンテナ名 bash
```
ディレクトリの変更

```
cd src
```
アプリの起動
```
python3 app.py
```
ブラウザ
```
http://localhost:5050/
```