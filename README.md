# Our Journey Creating Sage: The First-Aid Chatbot

## Inspiration

Our inspiration for Sage stemmed from a common concern: the need for quick and accurate first-aid advice. In many situations, timely first-aid can be the difference between a minor injury and a serious one. We wanted to leverage AI to create a tool that could provide immediate, reliable first-aid suggestions, helping people to manage injuries effectively until professional help arrives.

## What We Learned

Throughout this project, we learned a great deal about both the technical and practical aspects of building an AI chatbot:

1. **Medical Knowledge**: We delved into first-aid practices and guidelines to ensure our chatbot provided accurate and helpful advice.
2. **Natural Language Processing (NLP)**: Understanding user input accurately is critical for our chatbot. We explored various NLP techniques to enhance Sage's comprehension abilities.
3. **User Experience (UX)**: We learned the importance of designing an intuitive and user-friendly interface. Ensuring that users can easily interact with Sage was a priority.

## Building Sage

<div align="center">
    <img src="./SAGE.jpeg" alt="SAGE" width="300" height="300"/>
</div>

### Step 1: Research and Data Collection

We started by researching common injuries and their first-aid treatments. We gathered data from reputable sources such as the Red Cross and medical journals. This data formed the basis of the knowledge Sage would use to provide first-aid suggestions.

### Step 2: Developing the NLP Engine

We used Mistral 7B for Sage's NLP engine. This involved:

- **Training the Model**: Fine-tuning Mistral 7B on our curated dataset of first-aid instructions.
- **Intent Recognition**: Implementing algorithms to accurately identify the type of injury and the relevant first-aid advice.

### Step 3: Building the Chat Interface

We developed the chat interface using Streamlit for its simplicity and effectiveness in creating interactive web apps. The interface needed to be clean, responsive, and easy to use.

<div align="center">
    <img src="./Sage_UI.jpeg" alt="SAGE" width="1000" height="500"/>
</div>

### Step 4: Integration with Medical Data

We integrated our NLP engine with the medical data to ensure that Sage could provide contextually accurate first-aid suggestions. This involved setting up a database and creating APIs for seamless data retrieval.

### Step 5: Testing and Iteration

Testing was crucial. We conducted extensive tests to ensure Sage's responses were accurate and helpful. Feedback from users helped us refine and improve the bot's performance.

## Award Won
### 🏆 Wolfram Award

![Wolfram Logo](https://upload.wikimedia.org/wikipedia/commons/e/eb/WolframCorporateLogo.svg)

I am honored to have received the **Wolfram Award**, recognizing excellence in computational programming and innovation.

> *"The most exciting phrase to hear in science, the one that heralds new discoveries, is not 'Eureka!' but 'That's funny...'"*  
> — Isaac Asimov

---

## Challenges We Faced

1. **Data Accuracy**: Ensuring the accuracy of medical data was paramount. We had to cross-reference multiple sources to verify information.
2. **Understanding Context**: Training the NLP engine to understand the context and nuances of different injuries was challenging. We had to iterate multiple times to achieve satisfactory results.
3. **User Interaction**: Designing an interface that was both functional and user-friendly required careful planning and continuous feedback from potential users.
4. **Real-Time Processing**: Ensuring Sage could process and respond to queries in real-time without lag was a technical challenge that required optimizing our code and infrastructure.

📝 **Note:**  
This app will remain available until my current API credits are exhausted. At this time, I am unable to provide an option for users to connect their own API to the app. I apologize for the inconvenience and appreciate your understanding.


## Conclusion

Participating in this hackathon has been an enriching experience. Creating Sage not only allowed us to explore the fascinating world of AI and chatbots but also gave us the satisfaction of building something that can genuinely help people. We are proud of what we've achieved and excited about the potential impact of Sage in providing timely first-aid advice.
<div align="center">
    <a href="https://sage-health-chatbot.streamlit.app/" target="_blank">
        <img src="https://img.shields.io/badge/Sage%20App-Click%20Here-brightgreen?style=for-the-badge" alt="Sage App">
    </a>
</div>

<div align="center">
    <a href="https://www.youtube.com/watch?v=KW_vmMp5Tuw" target="_blank">
        <img src="https://img.shields.io/badge/Watch%20Video-Click%20Here-red?style=for-the-badge" alt="Watch Video">
    </a>
</div>
