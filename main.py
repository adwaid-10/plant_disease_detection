#Streamlit Web App

import streamlit as st
import tensorflow as tf
import numpy as np


#Tensorflow Model Prediction

def model_prediction(test_image):
    model = tf.keras.models.load_model("trained_model.keras")
    image = tf.keras.preprocessing.image.load_img(test_image,target_size=(128,128))
    input_arr = tf.keras.preprocessing.image.img_to_array(image)
    input_arr = np.array([input_arr]) #convert single image to batch
    predictions = model.predict(input_arr)
    return np.argmax(predictions)


#Sidebar

st.sidebar.title("Dashboard")
app_mode= st.sidebar.selectbox("Seletct Page",["Home","Prediction","About Project"])

#Main Page
if(app_mode=="Home"):
    st.markdown("<h2 style='text-align: center; color: white;'>PLANT DISEASE DETECTION SYSTEM </h2>", unsafe_allow_html=True)
    image_path="photos\pexels-muhammad-khairul-iddin-adnan-808510.jpg"
    st.image(image_path)
    st.subheader('Plants That Can Be Predicted', divider='rainbow')
    columns1 = st.columns([1, 1, 1, 1, 1])
    with columns1[0]:
        apple=st.button("Apple:apple:")
    if apple:
        st.image("photos\pexels-photo-206959.jpeg")
        st.write("Apples are not only delicious but also packed with nutrients! They're a great source of fiber and vitamin C. Plus, they come in so many varieties, each with its own unique flavor and texture.Apple plants can be susceptible to several diseases, including:")
        st.write("***Apple scab:***  A fungal disease that causes dark, scabby lesions on the fruit and leaves, leading to reduced yield and quality.")
        st.write("***Apple black rot:*** A fungal disease that creates dark, sunken spots on apples, which can spread to the leaves and branches. These spots look like rotting areas, hence the name 'black rot'. It reduces the quantity and quality of the fruit, affecting the overall yield of the apple tree.")
        st.write("***Cedar apple rust:*** A fungal disease that affects both cedar and apple trees. It shows up as orange or rust-colored spots on apple leaves and fruit, eventually turning black. This weakens the apple tree, causing leaf loss and reducing fruit quality and yield. It needs both cedar and apple trees to complete its life cycle. Spores from infected cedar trees spread to apple trees, leading to infection.")
    with columns1[1]:
        blueberry=st.button("Blueberry")
    if blueberry:
        st.image("photos\Blueberry.jpg")
        st.write("Blueberries are such a delightful fruit! They're not only tasty but also packed with antioxidants and nutrients. Whether you enjoy them fresh, frozen, or in baked goods like muffins or pancakes, they always add a burst of flavor. Plus, their vibrant blue color makes them visually appealing too.")

    with columns1[2]:
        cherry=st.button("Cherry:cherries:")
    if cherry:
        st.image("photos\cherry.jpg")
        st.write("Cherries are another fantastic fruit! They come in various varieties, like sweet cherries and tart cherries, each with its own distinct flavor profile. Sweet cherries are perfect for snacking on their own, while tart cherries are often used in baking or making preserves. Cherry season is always a treat, and nothing beats the taste of ripe, juicy cherries in the summertime. Plus, they're not just delicious but also packed with vitamins and antioxidants.Cherries can be susceptible to various diseases, including:")
        st.write("***Cherry Powdery Mildew:*** Cherry powdery mildew is a fungal disease that affects cherry trees, appearing as a white powdery substance on leaves, stems, and fruit. It thrives in warm, humid conditions. ")


    with columns1[3]:
        corn=st.button("Corn:corn:")
    if corn:
        st.image("photos\corn3.jpg")
        st.write("Corn, also known as maize, is a staple crop cultivated for its edible seeds, which are commonly consumed as a vegetable or processed into various food products. It is a member of the grass family and is one of the most widely grown cereal crops globally.Corn is susceptible to various diseases, including fungal, bacterial, and viral infections. Some common corn diseases include:")
        st.write("***Cercospora Leaf Spot:*** This disease is caused by the fungus Cercospora zeae-maydis. It appears as small, grayish-brown spots with a reddish-purple border on corn leaves. Severe infections can lead to premature death of leaves, reducing photosynthesis and potentially affecting yield.")
        st.write("***Gray Leaf Spot:*** Caused by the fungus Cercospora zeae-maydis, gray leaf spot manifests as rectangular, grayish lesions with yellow borders on corn leaves. It can lead to significant yield loss if not managed properly.")
        st.write("***Common Rust:*** Common rust of corn is caused by the fungus Puccinia sorghi. It appears as small, reddish-brown pustules on the leaves, stems, and husks of corn plants. Severe infections can reduce photosynthesis and yield.")
        st.write("***Northern Leaf Blight:*** This disease is caused by the fungus Exserohilum turcicum. It presents as long, elliptical lesions with wavy margins on corn leaves. Severe infections can lead to premature death of leaves, reducing photosynthesis and yield.")

    columns2 = st.columns([1, 1, 1, 1, 1])
    with columns2[0]:
        grape=st.button("Grape:grapes:")
    if grape:
        st.image("photos\grapes.jpg")
        st.write("Grapes are a type of fruit that grow in clusters on vines belonging to the genus Vitis. They are widely cultivated around the world for fresh consumption as well as for making wine, juice, jams, and raisins. Grapevines can be affected by various diseases, including fungal, bacterial, and viral infections. Here are some common grape diseases:")
        st.write("***Black Rot:*** Black rot, caused by the fungus Guignardia bidwellii, is a common disease affecting grapes. It manifests as dark lesions on leaves, stems, and fruit. Infected berries often shrivel and become mummified, leading to significant crop losses if left untreated.")
        st.write("***Esca (Black Measles):*** Esca is a complex disease syndrome affecting grapevines, caused by multiple fungi including Phaeoacremonium spp., Phaeomoniella chlamydospora, and others. It presents as dark streaks in the wood (black measles), leaf chlorosis, and eventual vine decline. Esca is challenging to manage due to its complex nature.")
        st.write("***Leaf Blight (Isariopsis Leaf Spot):***  Isariopsis Leaf Spot, caused by the fungus Isariopsis (=Mycosphaerella) leaf spot, manifests as small, circular lesions on grape leaves, which can coalesce to form larger spots. Severe infections can lead to defoliation and reduced vine vigor, affecting yield and quality.")

    with columns2[1]:
        orange=st.button("Orange:tangerine:")
    if orange:
        st.image("photos\orange.jpg")
        st.write("Oranges are vibrant citrus fruits known for their refreshing flavor and bright color. They belong to the Rutaceae family and are native to subtropical and tropical regions.Oranges can be affected by various diseases, including fungal, bacterial, and viral infections. Here are some common diseases that can affect orange trees:")
        st.write("***Citrus Huanglongbing (HLB), or Citrus Greening:*** HLB is a devastating bacterial disease caused by Candidatus Liberibacter spp. It affects the vascular system of citrus trees, leading to stunted growth, yellowing of leaves (mottled appearance), and bitter, misshapen fruit. HLB can eventually kill the tree.")


    with columns2[2]:
        peach=st.button("Peach:peach:")
    if peach:
        st.image("photos\peach.jpg")
        st.write("The peach is a fruit known for its juicy, sweet flavor and fuzzy skin. It belongs to the genus Prunus and is native to Northwest China. Peaches are commonly consumed fresh as a snack or used in various culinary applications, including desserts, salads, jams, and beverages. They are rich in vitamins A and C, as well as dietary fiber and antioxidants. Peaches come in different varieties, ranging from yellow to white flesh and freestone to clingstone varieties. They are typically in season during the summer months in many regions.Peaches are susceptible to various diseases, including fungal, bacterial, and viral infections. Some common diseases that affect peach trees include:")
        st.write("***Peach Bacterial Spot:*** It is a plant disease caused by the bacterium Xanthomonas arboricola pv. pruni. It affects peach trees and other members of the Prunus genus, causing characteristic symptoms such as dark spots or lesions on leaves, fruits, and stems. These spots may ooze bacterial exudate, and severe infections can lead to defoliation, fruit rot, and reduced yield. ")

    with columns2[3]:
        pepper=st.button("Pepper bell:hot_pepper:")
    if pepper:
        st.image("photos\Bell-peppers.jpg")
        st.write("The pepper bell, more commonly known as the bell pepper or sweet pepper, is a fruit of the Capsicum annuum species, which is native to Central and South America. Unlike other peppers in the Capsicum family, such as chili peppers, bell peppers are not spicy and have a sweet, mild flavor. They come in various colors, including green, red, yellow, and orange, and are commonly used in cooking for their crisp texture, vibrant colors, and versatility. Bell peppers are often used raw in salads, sandwiches, and dips, as well as cooked in stir-fries, soups, stews, and as a topping for pizzas and pasta dishes. They are also rich in vitamins A and C, making them a nutritious addition to meals.Bell peppers can be susceptible to various diseases, which can affect their growth, yield, and overall health. Some common diseases that affect bell peppers include:")
        st.write("***Bacterial spot:*** Bacterial spot is a common disease affecting bell peppers, caused by the bacterium Xanthomonas campestris pv. vesicatoria. It leads to dark, water-soaked lesions on leaves, stems, and fruits, which may enlarge and become necrotic with a yellow halo. Severe infections can result in defoliation, fruit drop, and reduced yield. ")

    columns3 = st.columns([1, 1, 1, 1, 1])
    with columns3[0]:
        potato=st.button("Potato")
    if potato:
        st.image("photos\potato.jpg")
        st.write("Potato (Solanum tuberosum) is a starchy tuberous crop that is widely cultivated and consumed worldwide. It is a member of the Solanaceae family, which also includes tomatoes, peppers, and eggplants. Potatoes are native to the Andes region of South America and have been a staple food crop for thousands of years.Potatoes are susceptible to various diseases, which can affect their growth, yield, and quality. Some common potato diseases include:")
        st.write("***Late Blight (Phytophthora infestans):*** This fungal disease causes dark, water-soaked lesions on leaves, stems, and tubers, leading to rapid defoliation and rotting of tubers, particularly in wet and humid conditions.")
        st.write("***Early Blight (Alternaria solani):*** Another fungal disease, early blight causes dark, concentric lesions on potato leaves, leading to defoliation and reduced yield. It is more common in warm and humid conditions.")

    with columns3[1]:
        Raspberry=st.button("Raspberry")
    if Raspberry:
        st.image("photos\Raspberry.jpg")
        st.write("Raspberry is a delicious and nutritious fruit that belongs to the rose family (Rosaceae). It is botanically classified as a member of the Rubus genus, which also includes blackberries. Raspberries are known for their sweet and tangy flavor, vibrant color, and delicate texture. They are widely cultivated and consumed around the world, both fresh and in processed forms such as jams, jellies, syrups, and baked goods.")

    with columns3[2]:
        soyabean=st.button("Soyabean")

    if soyabean:
        st.image("photos\soyabean.jpg")
        st.write("Soybean (Glycine max) is a leguminous plant that is widely cultivated for its edible beans, which are high in protein, healthy fats, vitamins, and minerals. It is native to East Asia and has been a staple food crop in many cultures for thousands of years. Soybeans are versatile and used in various forms, including whole beans, soybean oil, tofu, tempeh, soy milk, and soy sauce.")


    with columns3[3]:
        strawberry=st.button("Strawberry:strawberry:")
    if strawberry:
        st.image("photos\strawberry.jpg")
        st.write("Strawberry (Fragaria × ananassa) is a sweet and juicy fruit known for its vibrant red color, succulent texture, and delightful flavor. It belongs to the rose family (Rosaceae) and is a hybrid species derived from the crossbreeding of several wild strawberry species. Native to temperate regions of the Northern Hemisphere, strawberries are cultivated worldwide for their delicious fruit. Strawberries can sometimes be affected by leaf scorch.")
        st.write("***Strawberry leaf scorch*** is a symptom that can occur due to various factors, including environmental stressors, diseases, and nutrient deficiencies. It typically manifests as browning or yellowing of leaf margins and tips, which may progress inward toward the leaf veins. The affected leaves may become dry, crispy, and wilted.")


    with columns3[4]:
        tomato=st.button("Tomato:tomato:")
    if tomato:
        st.image("photos\Tomato.jpg")
        st.write("Tomato (Solanum lycopersicum) is a popular and versatile fruit that is botanically classified as a berry, though it is commonly used as a vegetable in cooking. Native to western South America, tomatoes are now cultivated worldwide for their edible fruits, which come in various shapes, sizes, and colors, including red, yellow, orange, pink, and purple.Tomatoes are susceptible to various diseases that can affect their growth, yield, and fruit quality. Some common tomato diseases include:")
        st.write("***Early Blight (Alternaria solani):*** Early blight is a fungal disease that causes dark, concentric lesions on tomato leaves, starting from the lower leaves and progressing upwards. It can lead to defoliation, reduced yield, and sunscald of fruits.")
        st.write("***Late Blight (Phytophthora infestans):*** Late blight is a fungal disease that affects both foliage and fruit, causing dark, water-soaked lesions on leaves and stems. It can spread rapidly during periods of cool, wet weather and lead to complete crop loss if left untreated.")
        st.write("***Septoria Leaf Spot (Septoria lycopersici):*** Septoria leaf spot is a fungal disease characterized by small, circular lesions with gray centers and dark margins on tomato leaves. It can cause defoliation and reduce fruit yield if severe.")
        st.write("***Tomato Leaf Mold (Fulvia fulva):*** Leaf mold is a fungal disease that primarily affects tomato leaves, causing yellowing, wilting, and the development of fuzzy, grayish-brown mold on the underside of leaves. It thrives in warm, humid conditions and can lead to defoliation and reduced fruit quality.")
        st.write("***Tomato Spider Mites (Tetranychus urticae):*** Two-spotted spider mites are tiny arachnids that feed on the undersides of tomato leaves, sucking out plant juices and causing stippling, yellowing, and webbing. Severe infestations can lead to leaf drop and reduced yield.")
        st.write("***Target Spot (Corynespora cassiicola):*** Target spot is a fungal disease that affects tomato leaves, stems, and fruit, causing circular lesions with dark centers and yellow halos. It can lead to defoliation, fruit rot, and reduced yield, especially in warm, humid conditions.")
        st.write("***Tomato Mosaic Virus (ToMV):*** Tomato mosaic virus is a viral disease that affects tomato plants, causing mosaic patterns, leaf curling, and stunted growth. It can reduce fruit yield and quality and is transmitted through infected plant material, sap-sucking insects, and mechanical means.")
        st.write("***Tomato Yellow Leaf Curl Virus (TYLCV):*** TYLCV is a viral disease transmitted by whiteflies, causing yellowing, curling, and stunted growth of tomato leaves. It can significantly reduce yield and affect fruit development, leading to distorted, discolored fruits.")


#About Project

if(app_mode=="About Project"):
    st.header("About Project",divider="red")
    st.subheader("About Dataset",divider='blue')
    st.write("This dataset consists of about 87K rgb images of healthy and diseased crop leaves which is categorized into 38 different classes. The total dataset is divided into 80/20 ratio of training and validation set preserving the directory structure. A new directory containing 33 test images is created later for prediction purpose.")
    st.text("Dataset taken from:")
    st.code("https://www.kaggle.com/datasets/vipoooool/new-plant-diseases-dataset/data")
    st.subheader("Project Objective",divider='blue')
    st.write("The objective of this project is to develop a machine learning model capable of accurately classifying plant diseases based on images of plant leaves. By leveraging computer vision techniques and deep learning algorithms, the model aims to assist farmers and agricultural practitioners in early detection and diagnosis of plant diseases, thereby enabling timely interventions to mitigate crop losses and improve agricultural productivity.")



#Prediction
    

if(app_mode=="Prediction"):
    st.header("Model Prediction")
    test_image=st.file_uploader("Choose an Image:")
    if(st.button("Show Image")):
        st.image(test_image)
    
    #Predict Button
    if(st.button("Predict")):
        st.write("Our Prediction")
        with st.spinner("Please wait..."):
            result_index = model_prediction(test_image)
            with open('label.txt') as f:
                content=f.readlines()
            label = []
            for i in content:
                label.append(i[:-1])
            
        st.success("Model is Predicting it's {}".format(label[result_index]))
