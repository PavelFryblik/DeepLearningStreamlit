import uuid
import re
import base64

class Streamlit_elements():

    def mymarkdown(object, number, text):
        form = """<style type="text/css">
                .low {
                  color: #585858;
                  position: relative;
                  bottom: 1ex;
                  font-size: 60%;
                  text-align: center;
                }
                .hh1g {
                    color: green;
                    text-align: center;
                    font-size: 100%;
                }
                .hh1r {
                    color: red;
                    text-align: center;
                    font-size: 100%;
                }
          </style>"""
        try:
            if float(number.strip('%'))>=0:
                markkdown_number = '<p class="hh1g"><strong>{}</strong></p>'.format(number)
            else:
                markkdown_number = '<p class="hh1r"><strong>{}</strong></p>'.format(number)
        except:
            markkdown_number = '<p class="hh1g"><strong>{}</strong></p>'.format(number)
        markkdown_text = '<p class="low">{}</p>'.format(text)
        object.markdown(form,unsafe_allow_html=True)
        object.markdown(markkdown_number + markkdown_text ,unsafe_allow_html=True)


    def changemarkdown(object, number, text, prefix='',suffix='', change=0):
        form = """<style type="text/css">
                .sup {
                  position: relative;
                  color: #585858;
                  bottom: 1ex;
                  font-size: 100%;
                  text-align: center;
                }
                .main {
                    color: green;
                    text-align: center;
                    font-size: 175%;
                }
                .h2g {
                    color: green;
                    text-align: center;
                    font-size: 120%;
                }
                .h2r {
                    color: red;
                    text-align: center;
                    font-size: 120%;
                }
          </style>"""

        markkdown_number = '<span class="main"><strong>{}{}{}</strong></span>'.format(prefix,number,suffix)

        if float(change)==0:
            markkdown_change = '<span class="h2g"></span>'
        elif float(change)>0:
            markkdown_change = '<span class="h2g">    ({}%)</span>'.format(change)
        else:
            markkdown_change = '<span class="h2r">    ({}%)</span>'.format(change)

        markkdown_text = '<p class="sup">{}</p>'.format(text)
        object.markdown(form,unsafe_allow_html=True)
        object.markdown(markkdown_number + markkdown_change + markkdown_text ,unsafe_allow_html=True)

    def get_table_download_link(df):
        """Generates a link allowing the data in a given panda dataframe to be downloaded
        in:  dataframe
        out: href string
        """
        csv = df.to_csv(index=False)
        file_name = 'data_from_streamlit.txt'
        file_type = file_name.split('.')[-1] # e.g. txt
        b64 = base64.b64encode(csv.encode()).decode()  # some strings <-> bytes conversions necessary here
        button_uuid = str(uuid.uuid4()).replace("-", "")
        button_id = re.sub("\d+", "", button_uuid)
        custom_css = f"""
        <style>
            #{button_id} {{
                color: #fff !important;
                text-transform: uppercase;
                text-decoration: none;
                background: #ed3330;
                padding: 4px;
                border-radius: 5px;
                display: inline-block;
                border: none;
                transition: all 0.8s ease 0s;
            }}
            #{button_id}:hover {{
                    background: #434343;
                    letter-spacing: 1px;
                    -webkit-box-shadow: 0px 5px 40px -10px rgba(0,0,0,0.57);
                    -moz-box-shadow: 0px 5px 40px -10px rgba(0,0,0,0.57);
                    box-shadow: 5px 40px -10px rgba(0,0,0,0.57);
                    transition: all 0.4s ease 0s;
            }}
            #{button_id}:active {{
                color: #fff !important;
                text-transform: uppercase;
                text-decoration: none;
                background: #ed3330;
                padding: 20px;
                border-radius: 5px;
                display: inline-block;
                border: none;
                transition: all 0.4s ease 0s;
                }}
        </style> """

        dl_link = (
            custom_css
            + f'<a download="{file_name}" id="{button_id}" href="data:file/{file_type};base64,{b64}">Download data</a><br></br>'
        )
        return dl_link

    def measuresmarkdown(object, measure, text, prefix='',suffix='', format=':.0f'):
        form = """<style type="text/css">
                .sup {
                  position: relative;
                  color: #585858;
                  bottom: 1ex;
                  font-size: 100%;
                  text-align: center;
                }
                .main {
                    color: green;
                    text-align: center;
                    font-size: 175%;
                }
          </style>"""

        markdown_value = '<span class="main"><strong>{}{}{}</strong></span>'.format(prefix,measure,suffix)
        markdown_text = '<p class="sup"><strong>{}</strong></p>'.format(text)

        object.markdown(form,unsafe_allow_html=True)
        object.markdown( markdown_value + markdown_text,unsafe_allow_html=True)
