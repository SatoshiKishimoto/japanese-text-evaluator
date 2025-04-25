import streamlit as st
import language_tool_python

# 外部の LanguageTool API を使用
tool = language_tool_python.LanguageToolPublicAPI('ja-JP')

st.set_page_config(page_title="日本語チェックアプリ", layout="centered")
st.title("📝 日本語文章チェック")
st.write("日本語の文法や表現の自然さをチェックします。")

text = st.text_area("文章を入力してください", height=200)

if st.button("チェック実行"):
    if not text.strip():
        st.warning("文章を入力してください。")
    else:
        matches = tool.check(text)

        if not matches:
            st.success("✅ 美しく正しい日本語です。")
        else:
            st.error(f"❌ {len(matches)} 件の指摘が見つかりました。")
            for match in matches:
                st.markdown(f"""
                ---
                **エラー箇所**： `{text[match.offset:match.offset + match.errorLength]}`
                
                **説明**： {match.message}  
                **提案**： {', '.join(match.replacements)}
                """)

