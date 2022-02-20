# ベースイメージとして python v3.6 を使用する
FROM python:3.8

# 以降の RUN, CMD コマンドで使われる作業ディレクトリを指定する
WORKDIR /app
RUN apt-get update
RUN apt-get -y upgrade
RUN apt-get install -y libgl1-mesa-dev
# カレントディレクトリにある資産をコンテナ上の ｢/app｣ ディレクトリにコピーする
ADD ./ /app

RUN pip install -r requirements.txt --no-cache-dir
EXPOSE 8502
CMD ["streamlit","run","object_detection.py","--server.port","8502"]
