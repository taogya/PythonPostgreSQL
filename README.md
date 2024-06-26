# PythonPostgreSQL
Pythonを使用したPostgreSQLの制御サンプル

## PostgreSQLのインストール
[Windows] 以下のライトを使用。<br>
https://sourceforge.net/projects/pgsqlportable/files/16.1/ <br>

パスに日本語を含まない場所へ展開する。<br>

## PostgreSQLにデータベース作成
```
# [Windows] サーバー起動
$ $env:INIT_SQL_PATH = "$(pwd)\src\sql\init_db.sql"
$ pushd C:\path\to\your\postgresql-16.1-1-windows-x64-lite\pgsql
$ bin\psql -f $env:INIT_SQL_PATH -U postgres
$ PostgreSQL-Start.bat
$ popd
```