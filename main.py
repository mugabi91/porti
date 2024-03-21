

import subprocess

# Install matplotlib using pip
subprocess.run(["pip", "install", "matplotlib"])
subprocess.run(["pip", "install", "numpy"])
subprocess.run(["pip", "install", "seaborn"])
subprocess.run(["pip", "install", "Pillow"])

subprocess.run(["pip", "install", "Pandas"])


############### start of imports ################################################################################################
import pandas as pd 
import streamlit as st 
import time 
import numpy as np 
from PIL import Image

import matplotlib.pyplot as plt
import seaborn as sns
############### end of import ##############################################################################################

  
##########paths &  data frames ################################################################################
path =r"workspaces\Datasets\star_wars.csv"
df=pd.read_csv(path)
##########  end of paths &  data frames ################################################################################
 

######################## start of page set up ###############################################################################################
st.set_page_config(layout="wide")

###################################
starwars_pic =r"workspaces\images\vader.jpg"

############################## end of background styling #############################################
##########general functions#########################

def stream_data(body):
    for word in body.split(" "):
        yield word + " "
        time.sleep(0.02)

############### end of page lay out#################################

with st.sidebar:
   
    st.title("Navigation")
    page = st.radio("Go to", ("Home", "EDA"))

########################### start of page content###############################################
if page == "Home":
    #title 
    st.write("# lmt data analysis portifolio" .upper())
    #BIO
    bio = """ ###### By. L Mugabi Trevor. 
             Welcome to my portifolio.
             """
    st.write(bio)
    
    
    #intro of page
    intro = """ #### Introduction to the Star Wars Franchise Dataset:

    The Star Wars franchise is one of the most iconic and beloved series in the history of popular culture. It encompasses a vast universe filled with memorable characters, epic battles, and intricate lore. For those unfamiliar with the franchise, Star Wars began as a groundbreaking film created by George Lucas in 1977, titled "Star Wars: Episode IV - A New Hope". Since then, it has expanded into a multimedia phenomenon, including movies, TV shows, books, comics, video games, and more.

    The Star Wars franchise dataset provides a comprehensive collection of data related to various aspects of this expansive universe. It includes information about characters, planets, starships, vehicles, species, and much more. This dataset offers valuable insights into the rich tapestry of the Star Wars universe, allowing fans and researchers alike to explore and analyze different elements of the franchise.

    Whether you're interested in learning about the iconi"""

    
    st.image(starwars_pic, caption="Darth Vader illustration")
    #function to create type write effect

    st.write_stream(stream_data(intro))
        

    st.write("#### Original dataset:".capitalize())
    time.sleep(0.2)
    st.dataframe(df, use_container_width=True)
    st.write_stream(stream_data(f"Dataset holds {df.shape[0]} rows and {df.shape[1]} columns"))
    st.write_stream(stream_data("#### The dataset also holds data on star trek:"))
    startrek_pic =r"workspaces\images\startrek.jpg"
    startrek_bio = """The Star Trek franchise is a beloved and iconic science fiction universe that has captivated audiences worldwide for decades. It originated as a television series created by Gene Roddenberry in the 1960s and has since expanded into a vast multimedia phenomenon including TV shows, movies, books, games, and more.

At its core, Star Trek is known for its optimistic vision of the future, exploring themes of exploration, diversity, cooperation, and the quest for knowledge. Set in the distant future, it follows the adventures of Starfleet, a space-exploration organization representing the United Federation of Planets. The franchise features a diverse cast of characters from different species and backgrounds, working together aboard starships like the iconic USS Enterprise to discover new worlds, encounter alien civilizations, and tackle moral and ethical dilemmas.

Star Trek is renowned for its groundbreaking representation, including one of the first multicultural casts on television and addressing social issues through allegorical storytelling. It has inspired generations of fans (known as Trekkies or Trekkers) and has become a cultural touchstone for its exploration of humanity's potential, the wonders of space exploration, and the importance of cooperation and understanding in a vast and diverse universe."""
    st.image(startrek_pic,caption="Star Trek Enterprise illustration")
    st.write_stream(stream_data(startrek_bio))
    st.divider()



elif page == "EDA":
    st.write("# Exploratory Data Analysis (EDA)")
    # Load the image
    image = Image.open(r".\images\glob.jpg")  #

    # Resize the image
    max_width = 1800  # Maximum width for display
    if image.width > max_width:
        aspect_ratio = image.height / image.width
        new_width = max_width
        new_height = int(max_width * aspect_ratio)
        image = image.resize((new_width, new_height))

# Display the resized image
    st.image(image, caption='image', use_column_width=True)

    df.drop_duplicates()
    
    df.drop(['Unnamed: 4','Unnamed: 5','Unnamed: 6','Unnamed: 7','Unnamed: 8','Unnamed: 10','Unnamed: 11','Unnamed: 12','Unnamed: 13','Unnamed: 14',
            'Unnamed: 16','Unnamed: 17','Unnamed: 18','Unnamed: 20','Unnamed: 19','Unnamed: 20','Unnamed: 21','Unnamed: 22','Unnamed: 23','Unnamed: 24','Unnamed: 25',
            'Unnamed: 26','Unnamed: 27','Unnamed: 28'],axis=1,inplace=True)

    ro, wi = df.shape
    total_slots = ro*wi
    

    df.rename(columns={
        'Have you seen any of the 6 films in the Star Wars franchise?':"watched_starwars",
    'Do you consider yourself to be a fan of the Star Wars film franchise?':"starwars_fan",
    'Which of the following Star Wars films have you seen? Please select all that apply.':'watched_starwars_films',
    'Please rank the Star Wars films in order of preference with 1 being your favorite film in the franchise and 6 being your least favorite film.':'ranking',
    'Please state whether you view the following characters favorably, unfavorably, or are unfamiliar with him/her.':"taste_character",
    'Which character shot first?':'fired_first',
    'Are you familiar with the Expanded Universe?':'knowledge_of_expanded_universe',
    'Do you consider yourself to be a fan of the Expanded Universe?æ':'Expanded_universe_fan',
    'Do you consider yourself to be a fan of the Star Trek franchise?':'star_trek_fan',
    'Location (Census Region)':"Location",
        
        
    },inplace=True)
    
    
    des={
    'Have you seen any of the 6 films in the Star Wars franchise?':"watched_starwars",
    'Do you consider yourself to be a fan of the Star Wars film franchise?':"starwars_fan",
    'Which of the following Star Wars films have you seen? Please select all that apply.':'watched_starwars_films',
    'Please rank the Star Wars films in order of preference with 1 being your favorite film in the franchise and 6 being your least favorite film.':'ranking',
    'Please state whether you view the following characters favorably, unfavorably, or are unfamiliar with him/her.':"taste_character",
    'Which character shot first?':'fired_first',
    'Are you familiar with the Expanded Universe?':'knowledge_of_expanded_universe',
    'Do you consider yourself to be a fan of the Expanded Universe?æ':'Expanded_universe_fan',
    'Do you consider yourself to be a fan of the Star Trek franchise?':'star_trek_fan',
    'Location (Census Region)':"Location"
    }
    st.divider()
    
    st.write_stream(stream_data(""" #### Data cleaning:
            My Process
            Dropped the useless variables
            Dropped the duplicated entries
            Renamed the long Variable names as below 
            Did data type convertions
            Did some exploring after
            
             """))
    
    variable_names = pd.DataFrame(list(des.items()), columns=['OLD VARiABLE NAME', 'NEW VARIABLE NAME'])
    time.sleep(0.2)
    st.dataframe(variable_names)
    st.divider()
    
    total_nulls = df.isna().sum().reset_index()
    total_nulls.columns = ['Variable','Null_total']
    loss_percentage =  (np.sum(total_nulls["Null_total"])/total_slots)*100
    
    st.divider()
    st.write_stream(stream_data("#### The total number of nulls in each variable in the DataSet are below:"))
    time.sleep(0.2)
    st.dataframe(total_nulls)
    st.write_stream(stream_data(f"{loss_percentage:.2f}% of the data will be lost if all nulls are dropped"))
    
    
    
    
    
    
    
    
    
    st.divider()
    st.write_stream(stream_data('### Observation'))
    st.divider()

    st.write_stream(stream_data('''#### What is the make up of the fans by franchise ?'''))

    columns = [feature for feature in df.columns if feature != "RespondentID"] 
    
   
    df.drop(df[df['RespondentID'].isna()].index,inplace=True)
    df.reset_index(drop=True,inplace=True)
    df['RespondentID'] = pd.to_numeric(df['RespondentID'],errors="coerce")
    df['RespondentID'] = df['RespondentID'].astype(object)
    
    



    
    for col in columns:
        df[col] = df[col].astype("category")
        
    df.info()
    sns.set_theme(style='darkgrid')
    sns.set_palette('Accent')


    categories = ['starwars_fan', 'star_trek_fan', 'Expanded_universe_fan']
    titles = ['Number of Star Wars fans', 'Number of Star Trek fans', 'Number of Expanded Universe fans']






   
    fig1, axes = plt.subplots(3, 3, figsize=(15, 12))


    for i, (category, title) in enumerate(zip(categories, titles)):
        sns.countplot(data=df, x=category, ax=axes[i, 0])
        axes[i, 0].set_title(title.upper())
        
        sns.countplot(data=df, hue=category, x='Gender', ax=axes[i, 1])
        axes[i, 1].set_title(f'by Gender for {title}'.upper())
        
        sns.countplot(data=df, hue=category, x='Age', ax=axes[i, 2])
        axes[i, 2].set_title(f'by Age for {title}'.upper())

    plt.tight_layout()
    st.pyplot(fig1)
    
    st.write_stream(stream_data(''' #### INSIGHTS
As seen above starwars has got the highest number of fans followed by star trek and last the expanded universe

The fan make up by gender shows its mostly Males interested in the franchises

For starwars it has mostly a fan base of people aged 30 to 60 yrs of age

For star_trek, it has mostly a fan base of people 45 to 60 yrs of age

For the expanded universe, it has a fan base mainly of younger people of ages 18 to 44 yrs

Looking at the female fan base of all the franchises, starwars has the highest female base compared to the others. star trek comes in second and the expanded universe comes in last

Looking at the male fan base of all the franchises, starwars has the highest male fan base compared to the others. star trek comes in second and the expanded universe comes in last'''))






    st.divider()
    st.divider()
    st.write_stream(stream_data("### Where are most fans from ?"))
    fig2,ax =plt.subplots(4,1, figsize=(15,15))

    sns.countplot(data=df, x="Location",ax=ax[0])
    ax[0].set_title("fans location".upper())

    sns.countplot(data=df, x="Location",hue="starwars_fan",ax=ax[1])
    ax[1].set_title("starwars fans Location".upper())

    sns.countplot(data=df, x="Location", hue="star_trek_fan",ax=ax[2])
    ax[2].set_title("star trek fans location".upper())

    sns.countplot(data=df, x="Location", hue="Expanded_universe_fan",ax=ax[3])
    ax[3].set_title("Expanded universe fans location".upper())

    plt.tight_layout()
    plt.show()
    st.pyplot(fig2)
    
    st.write_stream(stream_data("""#### INSIGHTS
Most fans are from the East North Central followed bythe pacific and then the north Atlantic

Inspect the graphs  above for the rest and more insight on location of fans and non fans locations

 """))
    

    st.divider()
    
    
    categories = ['starwars_fan', 'star_trek_fan', 'Expanded_universe_fan']
    titles = [' levels of Star Wars fans', 'levels Star Trek fans', ' levels of Expanded Universe fans']







    st.divider()
    st.write_stream(stream_data("### What are the income and Education levels of the FAN bases?"))
    fig3, axes = plt.subplots(3, 2, figsize=(15, 15))

    for i, (category, title) in enumerate(zip(categories, titles)):
    
        sns.countplot(data=df, hue=category, x='Household Income', ax=axes[i, 0])
        axes[i, 0].set_title(f'income {title}'.upper())
        
        sns.countplot(data=df, hue=category, x='Education', ax=axes[i, 1])
        axes[i, 1].set_title(f'Education  {title}'.upper())
        axes[i, 1].tick_params(axis='x', rotation=45)


    plt.tight_layout()
    plt.show()
    st.pyplot(fig3)
    
    st.write_stream(stream_data("""#### INSIGHTS

Inspect the graphs  above for the income and edcation levels of the fans and non fans

 """))
    st.divider()
    st.write_stream(stream_data(" #### Thanks for viewing PART 1 of the EDA."))
    st.divider()
    
    

########################### end of page content###############################################

######################## end of page set up#################################################################################################################333




#
