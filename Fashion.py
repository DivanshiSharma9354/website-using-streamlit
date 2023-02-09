import streamlit as st
from streamlit_option_menu import option_menu
from streamlit_extras.colored_header import colored_header
from markdownlit import mdlit
import charset_normalizer as chardet
from streamlit_chat import message


col1, mid, col2 = st.columns([5,25,5])
with mid:
    st.image("divanshi.png")
    
# Horizontal Menu
selected = option_menu(
    menu_title=None,
    options=['Home', "Fresh Arrival", "Contact"],
    icons=["house-fill", "arrow-up-right-circle-fill", "envelope-fill"],
    menu_icon="cast",
    default_index=0,
    orientation="horizontal",
    styles={
        "container": {"padding": "0!important", "background-color": "#fafafa"},
        "nav-link": {
            "text-align": "center",
            "margin": "0px",
            "--hover-color": "#eee",
            },
        "nav-link-selected": {"background-color": "#ca4bde"},
        }
)

# Home Page
if selected == "Home":
    st.image("banner.jpg")
    st.write("#")

    # Blue Jumpsuit
    colored_header(
        label="Elegant Jumpsuits",
        description=" ",
        color_name="violet-70")
    col1, mid, col2 = st.columns([1,10,10])
    with mid:
        st.image("blue250.png")
    with col2:
        c = st.container()
        c.subheader("Blue Babe Jumpsuit")
        c.markdown(":red[~₹9,500~]  **₹6,650**")
        c.caption("✅  :green[30% Off]")
        with st.expander("Description"):
            st.caption("Adorn the modern look with this lux blue twist crepe jumpsuit from Divanshi Store "
                      "crafted in polyester/spandex featuring deepneck, sleeveless, back zip, keyhole,"
                      "twist detail and two waist slip pockets.")
        with st.expander("Delivery Timeline"):
            st.caption("Estimated Delivery Time: Within 3-5 Days after order confirmation.")
        with st.expander("Available Sizes"):
            st.caption(":blue[**S**], :blue[**L**], :blue[**XL**], :blue[**XXXL**]")
        if c.button("Add To Cart  🛒"):
            c.caption("Dress Added ✔️")

    # Red Evening Dress
    st.write("#")
    colored_header(
        label="Divas Evening Dress",
        description=" ",
        color_name="violet-70")
    col1, mid, col2 = st.columns([1,10,10])
    with mid:
        st.image("red250.png")
    with col2:
        c = st.container()
        c.subheader("Red Gala Maxi")
        c.markdown(":red[~₹12,500~]  **₹9,150**")
        c.caption("✅  :green[27% Off]")
        with st.expander("Description"):
            st.caption("Adorn the evenings with this hot red halter maxi dress from Divanshi Store "
                       "crafted in polyester/elastane featuring deep neck, sleeveless and side slit. ")
        with st.expander("Delivery Timeline"):
            st.caption("Estimated Delivery Time: Within 3-5 Days after order confirmation.")
        with st.expander("Available Sizes"):
            st.caption(":blue[**S**], :blue[**L**], :blue[**XL**]")
        if c.button("Add To Cart 🛒") is True:
            c.caption("Dress Added ✔️")
    # Red Evening Dress
    st.write("#")
    colored_header(
        label="Gown Dress",
        description=" ",
        color_name="violet-70")
    col1, mid, col2 = st.columns([1,10,10])
    with mid:
        st.image("gown.jpg")
    with col2:
        c = st.container()
        c.subheader("Beautiful White Gown")
        c.markdown(":red[~₹12,500~]  **₹6,150**")
        c.caption("✅  :green[27% Off]")
        with st.expander("Description"):
            st.caption("Adorn the evenings with this hot white halter gown dress from Divanshi Store "
                       "crafted in polyester/elastane featuring deep neck, sleeveless and side slit. ")
        with st.expander("Delivery Timeline"):
            st.caption("Estimated Delivery Time: Within 4-6 Days after order confirmation.")
        with st.expander("Available Sizes"):
            st.caption(":blue[**S**], :blue[**L**], :blue[**XL**], :blue[**XXL**]")
        if c.button("Out of Stock") is True:
            c.caption("Out of Stock ❗️")



    st.write("#")
    colored_header(
        label="Gown Dress",
        description=" ",
        color_name="violet-70")
    col1, mid, col2 = st.columns([1,10,10])
    with mid:
        st.image("dressl.jpg")
    with col2:
        c = st.container()
        c.subheader("Beautiful Pink Gown")
        c.markdown(":red[~₹12,500~]  **₹9,150**")
        c.caption("✅  :green[27% Off]")
        with st.expander("Description"):
            st.caption("Adorn the evenings with this hot Pink Gown halter gown dress from Divanshi Store "
                       "crafted in polyester/elastane featuring deep neck, sleeveless and side slit. ")
        with st.expander("Delivery Timeline"):
            st.caption("Estimated Delivery Time: Within 4-6 Days after order confirmation.")
        with st.expander("Available Sizes"):
            st.caption(":blue[**S**], :blue[**L**], :blue[**XL**], :blue[**XXL**]")
        if c.button("Add to cart ☞") is True:
            c.caption("Dress Added ✔️")




# Contact Form
    st.write("#")
    col1, mid, col2 = st.columns([10, 12, 9])
    with mid:
        colored_header(
            label="Get Fashion Tips 💃",
            description=" ",
            color_name="violet-70")

    with st.form("my_form"):
        name = st.text_input("Your Name...")
        email = st.text_input("Your Email...")
        submitted = st.form_submit_button("Subscribe")
        if submitted:
            st.write("Subscribed 💜")
    video_file = open('p.mp4','rb') 
    video_bytes = video_file.read()
    st.video(video_bytes)
    message("Hi") 
    message("Hello bot!", is_user=True)
    message("I need a Your help") 
    message("Yes How May I Help You !", is_user=True)
    message("Return Policy is available?") 
    message("Yes!", is_user=True)
    message("Product Quality is  Good or Bad") 
    message("Good", is_user=True)
    message("Your Contact details?") 
    message("937674364", is_user=True)
    




# Fresh Arrival Section
elif selected == "Fresh Arrival":
    st.image("fresharrival.png")
    st.write("#")

    # Creating 4 tabs for different types of dresses.
    # Each tab will have 4 pics.
    dresses, tops, outwear, bottoms = st.tabs(["Dresses", "Tops", "Outwear", "Bottoms"])
    with dresses:
        pic1, pic2 = st.columns(2)
        with pic1:
            st.image("dress1.png")
        with pic2:
            st.image("dress2.png")
        pic3, pic4 = st.columns(2)
        with pic3:
            st.image("dress3.png")
        with pic4:
            st.image("dress4.png")
        pic5, pic6 = st.columns(2)
        with pic5:
            st.image("dress5.jpg")
        with pic6:
            st.image("dress6.jpg")    

    with tops:
        pic1, pic2 = st.columns(2)
        with pic1:
            st.image("tops1.png")
        with pic2:
            st.image("tops2.png")
        pic3, pic4 = st.columns(2)
        with pic3:
            st.image("tops3.png")
        with pic4:
            st.image("tops4.png")

    with outwear:
        pic1, pic2 = st.columns(2)
        with pic1:
            st.image("outwear1.png")
        with pic2:
            st.image("outwear2.png")
        pic3, pic4 = st.columns(2)
        with pic3:
            st.image("outwears3.png")
        with pic4:
            st.image("outwears4.png")

    with bottoms:
        pic1, pic2 = st.columns(2)
        with pic1:
            st.image("bottom1.png")
        with pic2:
            st.image("bottom2.png")
        pic3, pic4 = st.columns(2)
        with pic3:
            st.image("bottom3.png")
        with pic4:
            st.image("bottom4.png")


# Contact Section
elif selected == "Contact":
    st.markdown("Created by Divanshi Sharma")
    mdlit("@(Linkedin)(https://www.linkedin.com/in/divanshi-sharma-676401210/)")
    mdlit("@(Facebook)(https://www.fb.com/)")
    video_file = open('c.mp4','rb') 
    video_bytes = video_file.read()
    st.video(video_bytes)


