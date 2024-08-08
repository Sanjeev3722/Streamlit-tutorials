import streamlit as st

st.write("Hello World: Getting Bore, Hello Brother!!")
st.title("Display Title use st.title()")
st.write("To Write text use st.write()")
st.header("I am header to write header use st.header use st.header()")
st.subheader("I am subheader To write subheader use st.subheader()")
st.text("Hey I am simple text to write simple text use st.text")
# To create hyperlink
st.markdown("[Steramlit](https://share.streamlit.io/)")
st.markdown("[Steramlit]CheatSheet(https://docs.streamlit.io/develop/quick-reference/cheat-sheet)")
st.success("success!")
st.info("Information")
st.warning("This is warning")
st.error("This is an error!")


from PIL import Image
img = Image.open("satyamev-jayate.jpg")
st.image(img, width=300, caption="Satyamev Jayte")


video_file = open("vid.mp4","rb")
video_bytes = video_file.read()
st.video(video_bytes)

st.video("https://youtu.be/ToxLVE-88y4?si=IkUkQLls0-jxmmWI")


audio_file = open("song.mp3", "rb")
audio_bytes = audio_file.read()
st.audio(audio_bytes, format="audio/mp3")

st.button("play")

st.header("Button Widgets")

if st.button("play2"):
    st.text("Enjoy Music")
    st.video("https://www.youtube.com/watch?v=2v8urSwf8TI")
    
if st.checkbox("Checkbox"):
    st.text("Checkbox selected")
    
