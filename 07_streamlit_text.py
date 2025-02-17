
import streamlit as st
import openai

##### 기능 구현 함수 #####
##### 기능 구현 함수 #####
def askGpt(prompt, apikey):
    # OpenAI API 클라이언트를 초기화합니다.
    client = openai.OpenAI(api_key=apikey)

    # GPT 모델에 프롬프트를 보내어 응답을 요청합니다.
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    # 응답에서 요약된 텍스트를 추출하여 반환합니다.
    gptResponse = response.choices[0].message.content
    return gptResponse



def main():
    st.set_page_config(page_title="요약 프로그램")
    st.header("📃요약 프로그램")
    st.markdown('---')
    text = st.text_area("요약 할 글을 입력하세요")
    # 요약 기능 실행
    with st.sidebar:
        open_apikey = st.text_input(
            label='OPENAI API 키', 
            placeholder='Enter Your API Key', 
            value='', 
            type='password')


    if st.button("요약"):
            # 요약을 요청할 프롬프트를 구성합니다.
            prompt = f'''
            **Instructions** :
            - You are an expert assistant that summarizes text into **Korean language**.
            - Your task is to summarize the **text** sentences in **Korean language**.
            - Your summaries should include the following :
                - Omit duplicate content, but increase the summary weight of duplicate content.
                - Summarize by emphasizing concepts and arguments rather than case evidence.
                - Summarize in 3 lines.
                - Use the format of a bullet point.
            -text : {text}
            '''
            if open_apikey:
                try:
                    # API 키가 유효한 경우 요약 작업을 수행합니다.
                    response = askGpt(prompt, open_apikey)
                    st.info(response)
                except Exception as e:
                    # 에러가 발생한 경우 에러 메시지를 표시합니다.
                    st.error(f"요약 작업 중 에러가 발생했습니다: {str(e)}")
    return 0

if __name__=="__main__":
    main()

