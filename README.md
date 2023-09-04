# StreamWise
Welcome to Streamwise, your trusted companion in shaping your educational and career journey

## Inspiration

Our inspiration for creating "StreamWise" stemmed from the desire to provide students completing 12th and 10th grades with a comprehensive and personalized course recommendation system. We aimed to combine the power of artificial intelligence, personality assessment, and mental health prediction to assist students in making informed decisions about their educational and career paths.

## What it does

"StreamWise" is a full-stack web application that empowers users to make well-informed decisions about their education and career choices. It begins by collecting basic user details and then guides them through a personality test consisting of 30 thoughtfully designed questions. Leveraging OpenAI's ChatGPT and the BM25 model, our system processes this information to provide personalized course recommendations for undergraduate programs. Additionally, it recommends suitable streams for students after completing the 10th grade, all based on their personalities, interests, and hobbies. Users can also inquire about specific details, such as entrance exams, through our integrated chatbot.

## Step-by-Step Code Execution Instructions:

- Clone the repository.
- Open the terminal
- Run the command " pip install -r requirements.txt"
- Run the command "python manage.py makemigrations"
- Run the command "python manage.py migrate"
- Run the command "python manage.py runserver"
- The server would have been started at your local host.

## How I built it

We built "StreamWise" using Django as our web development framework. The personality test is a central component, and it's carefully designed to extract valuable insights about the user. OpenAI's ChatGPT is employed to summarize the user's input and facilitate course recommendations. The BM25 model enhances our recommendation engine, ensuring that the suggested undergraduate programs align with the user's profile. We also integrated an OpenAI API-powered chatbot to provide instant answers to user queries.

## Challenges I ran into

While developing "StreamWise," we encountered several challenges. These included designing an effective personality test that accurately reflects the user's traits and preferences. Additionally, integrating the BM25 model and ChatGPT to provide precise recommendations required significant effort. Overcoming these technical hurdles and ensuring a seamless user experience was a key challenge.

## Accomplishments that I'm proud of

We are proud of creating a holistic solution that combines artificial intelligence, personality assessment, and mental health prediction to benefit students. "StreamWise" empowers users to make informed decisions about their educational paths, and we are thrilled to have developed a tool that can positively impact students' lives.

## What I learned

Throughout the development of "StreamWise," we learned the importance of effective user interaction and the value of AI-driven recommendations in the education sector. We also gained insights into working with APIs, building recommendation systems, and ensuring the scalability and reliability of a web application.

## What's next for our project

In the future, we plan to expand "StreamWise" by incorporating more advanced AI techniques and additional features. This includes refining the personality assessment process, enhancing the chatbot's capabilities, and providing even more accurate course and college recommendations. We aim to make "StreamWise" a comprehensive educational companion for students, assisting them at every step of their academic journey.
