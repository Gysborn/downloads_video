import streamlit as st
import yt_dlp
import os
from utils import get_names_files
st.set_page_config(
    page_title='Parsing book store',
    layout="wide",
    initial_sidebar_state="expanded",
    page_icon=":shark:",
    menu_items={
    'Get Help': 'https://www.extremelycoolapp.com/help',
    'Report a bug': "https://www.extremelycoolapp.com/bug",
    'About': "# This is a header. This is an *extremely* cool app!"})

placeholder = st.empty()

def cs_sidebar():
    st.sidebar.header('Загружаем видео')
    output_file = st.sidebar.radio(
    "Choice quality video",
    [":rainbow[1080i]", ":rainbow[720i]", ":rainbow[480i]", ":rainbow[360i]", ":rainbow[240i]"],
    index=None,
    )


def display_file(path):
    with open(path, "rb") as file:
        st.sidebar.download_button(
                label=f"[Download] {path}",
                data=file,
                file_name=path,
                mime="video"
            )


def download(link, name='%(title)s'):
    ydl_opts = {
        # 'format': 'bestvideo+bestaudio/best', #берем самое лучшее качество видео и фото
        'outtmpl': '{}.%(ext)s'.format(name), #наше выбраное имя, если его не было, то стандартное - название видео на самом сайте
    }
    with st.spinner('Загрузка...'):
        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info_dict = ydl.extract_info(link, download=True)
                downloaded_file_path = ydl.prepare_filename(info_dict)
        except Exception as e:
            st.html("<strong>Не корректная ссылка, попробуй другую</strong>")
            st.error(f"Подробнее: {e}")
            return None
    return downloaded_file_path


def get_video(url):
  placeholder.empty()
  file_path = download(url)
  if file_path:
    res = display_file(file_path)
    if res == None:
        os.remove(file_path)


def app():
    cs_sidebar()
    url = st.text_input('Введите url')
    if url == 'data':
        st.write(get_names_files())
        st.write(st.secrets['LOGIN'])
    if url:
      st.button('Загрузить', on_click=get_video, args=(url,))
    else:
      st.write('Пустая строка')

if __name__ == '__main__':
    app()
