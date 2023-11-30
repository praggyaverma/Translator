# Copyright (c) Streamlit Inc. (2018-2022) Snowflake Inc. (2022)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import streamlit as st
import pandas as pd
import requests
from streamlit.logger import get_logger

LOGGER = get_logger(__name__)


def run():
    st.set_page_config(
        page_title="Hi-Namaste",
        page_icon="🗣",
    )

    st.write("# What are you saying!? 🗣")
    st.write("This website converts English text to Japanese")
    st.write("\n\n\n")

    query = st.text_input("Enter your text:")
    if not query:
        st.write("Please enter some text.")
        return
    
    url = "https://google-translate113.p.rapidapi.com/api/v1/translator/text"

    payload = {
        "from": "en",
        "to": "ja",
        "text": query
    }
    headers = {
        "content-type": "application/x-www-form-urlencoded",
        "X-RapidAPI-Key": "3b12f85ebamsh6d9bbe02db68b56p1bee67jsn8012f0c52329",
        "X-RapidAPI-Host": "google-translate113.p.rapidapi.com"
    }

    response = requests.post(url, data=payload, headers=headers)
    response_json = response.json()
    japanese_text = response_json.get("trans", "")

    st.write(japanese_text)


if __name__ == "__main__":
    run()

