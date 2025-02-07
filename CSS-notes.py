import streamlit as st
import pandas as pd
import plotly.express as px
#%%
#set up title and navigation pane

st.set_page_config(layout="wide")
st.title("Coding Summer School Report")

st.markdown("""
         The Coding Summer School (CSS) is jointly organised by the Centre for High Performance Computing (CHPC) of the CSIR and the 
         National Institute for Theoretical Computational Science (NITheCS). This joint effort was specifically motivated by a concept 
         paper of the South African Department of Science and Innovation (DSI) that explores the possibility to broaden the scope of 
         NITheP into a national institute/centre for theoretical and computational science. This is the 15th year an event of this kind 
         has happened through the CHPC and 7th year in collaboration with NITheCS.\\
             \\
        This website was written to report the main lessons from the school to my research group. This is not a tutorial or a complete 
        summary of the school, but rather a demonstration of some of the things that were taught that would be useful in our specific context.
         """)


st.write("Website made by Sarah Burnett")

tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8, tab9= st.tabs(["General", "Pandas", "Seaborn", "Streamlit", "Web scraping", 
                                                               "Bashcrawl", "Resources", "About the author", "Website code"])

#%%
#make the pages

with tab1:
    st.title("General")
    
    st.header("Tips")
    st.write("These are listed in no particular order. They are little tips that don't fit into any of the other categories")
    
    st.markdown("""
             - You can group files that are used together into Projects in Spyder. They are like folders, but open all your .py files at 
             once and keep any other files you need to import together
             - If you want to comment out multiple lines of data, enclose them in three sets of quotation marks `''' This text is ignored'''`
             - Letters are ordered like numbers, so a<b
             - `replace()` will replace a substring with a given value
             - A `try except` loop is a way to test your code without breaking it if there is an error. The code you want to run goes into
             the `try` block, and you specify the type of error you expect in the `except` block, as well as what needs to happen if that 
             error is encountered
             - fstrings are a very useful string manipulation tool. You can reference variables inside a string using `{}`
             - You can extract all elements of a list before or after an index using `:`. For example `list[3:]` will extract the elements 
             after index 3
             """)
             
    st.header("Libraries that were used")
    st.markdown("""
                - pandas (pd) allows for easy data manipulation and processing for table-style data
                - seaborn (sns) plots statistical plots like heatmaps
                - os interacts with operating system
                - requests (req) allows you to make requests to URLs
                - pubchempy (pcp) allows you to access the PubChem database from a python file
                - plotly (px) creates interactive plots
                - shutil allows you to do operations on files such as copying them
                - streamlit (st) allows you to make Streamlit web apps
                - datetime lets you work with datetime data formats
                - scikitlearn (sklearn) is a machine learning library
                - tensorflow (ts) is a machine learning library
                """)
    
with tab2:
    st.title("Pandas")
    
    st.write("""
             Pandas is a tool for efficient data analysis in python. Data is stored in tables called dataframes. The rows are indexed and the 
             columns have labels, which allows you to reference specific data to filter, sort and manipulate your data.  
             Some introductory tutorials can be found here: https://pandas.pydata.org/docs/getting_started/intro_tutorials/index.html.
             """)
    st.header("Introductory Examples")
    
    st.write("This is what a dataframe looks like")
    st.code("""
            df=pd.DataFrame({"Location": ['Park', 'Business', 'Business', 'Park', 'Park'],
                             "Price": [28,35,35,32,35],
                             "Sales": [64,17,22,30,27],
                             "Profit": [544,-324,-184,-50,-44]
                             })
            """)
 
    df=pd.DataFrame({"Location": ['Park', 'Business', 'Business', 'Park', 'Park'],
                     "Price": [28,35,35,32,35],
                     "Sales": [64,17,22,30,27],
                     "Profit": [544,-324,-184,-50,-44]
                     })
    st.write(df)
    
                
    st.write('Select one column')

    st.code("df['Location']")
    st.write(df['Location'])
    
    st.write('Add columns')
    st.code("""df["Price+Sales"]=df["Price"]+df["Sales"]""")
    df["Price+Sales"]=df["Price"]+df["Sales"]
    st.write(df)
    
    
    st.header("Useful tools that were new to me")
    
    st.write('Create a list of the unique entries in a column')
    st.code("""
            df['Location'].unique()
            """)
    unique=df['Location'].unique()
    st.write(unique)
    
    
    st.write('Filter data using `query()` to find columns with a negative profit')
    st.code("df.query('Profit<0')")
    loss=df.query('Profit<0')
    st.write(loss)
    
    st.write('Use `groupby()` to group data. Displaying mean profit for each location')
    st.code('df.groupby("Location")["Profit"].mean()')
    groups=df.groupby("Location")["Profit"].mean()
    st.write(groups)
    
    
with tab3:
    st.title("Seaborn")
    
    st.markdown('Good things coming soon :wink:')
    
with tab4:
    st.title("Streamlit")
    st.write("""
             Streamlit is a very powerful tool to create web apps. It was used to create this website! It can host pages locally or via Github. You write the code for the 
             website in a .py file, which is then run by Streamlit. If you don’t use a website for a while, it will sleep. It just needs 
             to be reactivated from your account again.    
             Their website says 'Streamlit turns data scripts into shareable web apps in minutes. All in pure Python. No front‑end 
             experience required.'  
             There is a large range of interactive features that can be added to the website, all with very easy functions. It can also 
             display data in tables and interactive graphs. Some examples are given below.
             """ )
             
    st.header("Display data")

    data = pd.DataFrame({"x": [ -10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 
                         "y": [298, 241, 190, 145, 106, 73, 46, 25, 10, 1, -2, 1, 10, 25, 46, 73, 106, 145, 190, 241, 298]})

    # Display the data in the Streamlit app
    st.write(data)

    # Create a Plotly figure
    fig = px.line(data, x="x", y="y", title="Simple Plotly Example")
    
    # Display the plot in the Streamlit app
    st.plotly_chart(fig)
    st.code("""
            data = pd.DataFrame({"x": [ -10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 
                                 "y": [298, 241, 190, 145, 106, 73, 46, 25, 10, 1, -2, 1, 10, 25, 46, 73, 106, 145, 190, 241, 298]})

            # Display the data in the Streamlit app
            st.write(data)

            # Create a Plotly figure
            fig = px.line(data, x="x", y="y", title="Simple Plotly Example")
            
            #display the plot
            st.plotly_chart(fig)
            """)

    
    
    st.header("Other features")
    
    st.subheader('Upload a file and filter the results')
    uploaded_file = st.file_uploader("Upload a CSV of sale data", type="csv")

    if uploaded_file:
        publications = pd.read_csv(uploaded_file)
        st.dataframe(publications)

        # Add filtering for year or keyword
        keyword = st.text_input("Filter by keyword", "")
        if keyword:
            filtered = publications[
                publications.apply(lambda row: keyword.lower() in row.astype(str).str.lower().values, axis=1)
            ]
            st.write(f"Filtered Results for '{keyword}':")
            st.dataframe(filtered)
        else:
            st.write("Showing all sales")
            
    st.code("""
            uploaded_file = st.file_uploader("Upload a CSV of sale data", type="csv")

            if uploaded_file:
                publications = pd.read_csv(uploaded_file)
                st.dataframe(publications)

                # Add filtering for year or keyword
                keyword = st.text_input("Filter by keyword", "")
                if keyword:
                    filtered = publications[
                        publications.apply(lambda row: keyword.lower() in row.astype(str).str.lower().values, axis=1)
                    ]
                    st.write(f"Filtered Results for '{keyword}':")
                    st.dataframe(filtered)
                else:
                    st.write("Showing all sales")
            """)
        
    st.subheader('Take text input')
    text=st.text_area('Write some text here')
    st.write(f"You wrote: {text}")
    
    st.code("""
            text=st.text_area('Write some text here')
            st.write(f"You wrote: {text}")
            """)

    st.subheader('Take input from a slider')
    number = st.slider("Pick a number", 1, 100)
    st.write(f"You picked: {number}")
    
    st.code("""
            number = st.slider("Pick a number", 1, 100)
            st.write(f"You picked: {number}")
            """)
    
    st.subheader('A noughts and crosses game developed by one of the students from the coding school')
    st.link_button('Noughts and crosses', 'https://css2025app-noughtsandcrosses-9rqynctvxelsbvsk76ih5q.streamlit.app/', type='primary')
    
    
with tab5:
    st.title("Web scraping")
    
    st.markdown("""Web scraping is the process of automatically extracting data from a website. We used the `request` library to do this.
                We did very basic examples where the URL we requested was to download a file. We did not learn how to navigate to copy 
                specific information from a website. This file then had to be saved. Our code is shown below.""")
    web_code="""
    import requests as req
    
    res = req.get(https://phytochem.nal.usda.gov/biological-activities-chemicals-csv-export/2/all?page&_format=csv')
    
    csv = open(f"bioact/2.csv", "wb") #wb means write binary because request comes back in binary
    csv.write(res.content)
    csv.close()
    """
    st.code(web_code, language='python')
    st.write("The main takeaway is that you use `req.get()` to access a URL")
    
    
    
with tab6:
    st.title("Bashcrawl")
    st.markdown("""Bashcrawl is a fun DnD style game to teach you basic bash commands. You explore rooms, fight monsters and solve puzzles. 
                Bash is a command-line interface that allows users to interact with the system using text commands""")
    
    st.markdown('Run the following commands in your terminal to begin')
    st.code('git clone https://gitlab.com/slackermedia/bashcrawl.git bashcrawl', language='bash')
    st.code('cd bashcrawl', language='bash')
    st.code('cat README.me', language='bash')
    st.write('Then follow the instructions in the README.me file')
    
    st.header('Screenshots from the game')
    
    st.image('bashcrawl entrance.png')
    st.caption('First room in the game')
    
    st.write('')
    st.write('')
    
    st.image('bashcrawl ghost.png')
    st.caption('Fighting a monster')
    
    
    
    
with tab7:
    st.title("Resources")
    
    st.link_button('Automate the Boring Stuff', 'https://automatetheboringstuff.com/', type='primary', 
                   help='A website with tutorials for automating common tasks')
    
    st.link_button('Software Carpentry', 'https://software-carpentry.org/lessons/ ', type='primary', 
                   help='A website with tutorials for a few different languages')
    
    st.link_button('Data Carpentry', 'https://datacarpentry.org/lessons/  ', type='primary', 
                   help='A website with tutorials for a few different languages')
    
    st.link_button("Streamlit documentation", 'https://docs.streamlit.io/develop/api-reference', type='primary', 
                   help="Documentation for all the elements you can add to Streamlit")
    
with tab8:
    st.write("""
             Sarah Burnett is a MSc student in the Biophysics Research Group at the University of Pretoria.\\
             \\
             Her project aims to investigate the growth response of wheat to high temperature stress, using hyperspectral imaging and 
             chlorophyll fluorescence. Climate change has caused extreme heat waves to increase in intensity and frequency. This has a 
             severe negative impact on crop yield and therefore food production. She aims to identify the physiological and quantum 
             mechanical mechanisms of the plant’s response to heat stress. This knowledge can be used to inform the development of 
             adaptive cultivation techniques to mitigate yield loss in high temperature conditions. This project is an exciting look into 
             the intersection between physics, biology and chemistry and will investigate the effects of non-trivial physics in the 
             context of a complex biological system.
             """)
    st.subheader("What is biophysics?")
    col1, col2 = st.columns([4,1], gap='large')
    
    with col1:
        st.write("""
                 Biophysics is a vibrant, interdisciplinary field that brings together scientists from fields such as physics, biology, 
                 chemistry, maths, and material science to share their skills and develop new tools for understanding how biology works. 
                 Biophysicists study life at every level, from the molecular level up to entire ecosystems. They develop new experimental 
                 and computational methods to understand all aspects of biological systems at a fundamental level, solving scientific 
                 mysteries in the process. Biophysicists push the scientific envelope to answer questions that have remained unanswered and 
                 solve the problems of the future.\\
                     \\
                The Biophysics Research Group at the University of Pretoria studies the light-harvesting protein complexes of organisms that 
                photosynthesize. Using state-of-the-art optical techniques, they investigate the energy and structural dynamics of these 
                complexes.All of this is done to understand the properties of these intriguing molecular machines - especially the transport 
                and regulation of excitation energy.
                 """)
    with col2:
        st.link_button("Group website", 'https://biophysicsup.netlify.app/', type='primary')
        st.link_button("Follow us on Instagram", "https://www.instagram.com/biophysics.up/", type='primary')
        st.link_button("Follow us on LinkedIn", "https://www.linkedin.com/company/biophysics-research-group-tuks/", type='primary')

with tab9:
    code="""
    import streamlit as st
    import pandas as pd
    #%%
    #set up title and navigation pane
    st.set_page_config(page_title="CSS summary", layout="wide")


    st.sidebar.title("Navigation")
    menu = st.sidebar.radio(
        "Go to:",
        ["General tips and info", "Pandas", "Seaborn", "Streamlit", "Web scraping", "Bashcrawl", "Resources", "Website code"],
    )

    #%%
    #make the pages

    if menu == "General tips":
        st.header("General tips")
        
    elif menu == "Pandas":
        st.header("Pandas")
        
    elif menu == "Seaborn":
        st.header("Seaborn")
        
    elif menu == "Streamlit":
        st.header("Streamlit")
        
    elif menu == "Web scraping":
        st.header("Web scraping")
        
    elif menu == "Bashcrawl":
        st.header("Bashcrawl")
        st.markdown('Bashcrawl is a fun DnD style game to teach you basic bash commands. You explore rooms, fight mosnters and solve 
                    puzzles. Bash is a command-line interface that allows users to interact with the system using text commands')
        
        st.markdown('Run the following commands in your terminal to begin')
        st.code('git clone https://gitlab.com/slackermedia/bashcrawl.git bashcrawl', language='bash')
        st.code('cd bashcrawl', language='bash')
        st.code('cat README.me', language='bash')
        st.write('Then follow the instructions in the README file')
        
        st.subheader('Screenshots from the game')
        
        st.image('bashcrawl entrance.png')
        st.caption('First room in the game')
        
        st.write('')
        st.write('')
        
        st.image('bashcrawl ghost.png')
        st.caption('Fighting a monster')
        
        
        
        
    elif menu == "Resources":
        st.header("Resources")
        
        st.link_button('Automate the Boring Stuff', 'https://automatetheboringstuff.com/', type='primary', 
                       help='A website with tutorials for automating common tasks')
        
        st.link_button('Software Carpentry', 'https://software-carpentry.org/lessons/ ', type='primary', 
                       help='A website with tutorials for a few different languages')
        
        st.link_button('Data Carpentry', 'https://datacarpentry.org/lessons/  ', type='primary', 
                       help='A website with tutorials for a few different languages')
        
    elif menu==="Website code":
        code = <Type code here>
        st.code(code, language='python')
    """
    st.code(code)

