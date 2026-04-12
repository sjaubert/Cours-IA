## If You Understand These 5 AI Terms, You’re Ahead of 90% of People
Master the core ideas behind AI without getting lost
Shreyas Naphad
Shreyas Naphad


AI-Generated Image
For Non-Members link to the full story

Let me be frank.

Most people who talk about AI either sound like they’re giving textual definitions, or they’re completely clueless when someone mentions terms like LLMs or neural networks.

You don’t have to be either of them.

I believe that there are these 5 terms, 5 concepts that, if you actually understand them (not just memorise), you’ll be miles ahead of almost everyone else in the room. Whether you’re in tech, business, education, or just someone curious about where the world is heading.

Let’s start.

1. Tokens
The very first thing that you must register in your brain is that AI models don’t read words. They don’t even read letters. They read tokens.

So what’s a token?

Imagine you’re reading a book, but instead of reading all the words, you’re reading chunks of words. Sometimes a chunk is a complete word like “cat.” Sometimes it’s part of a word like “un” or “tion.” Sometimes it’s punctuation. That piece of text (chunk) is a token.

For example, the sentence “I love pizza” can be broken into 3tokens: “I”, “ love”, “ pizza”.

Why does this matter to you?

Because every AI product you use such as ChatGPT, Claude, Gemini, is counting tokens behind the scenes. The more tokens you send in your message, the more the model has to process. The more tokens it generates in its reply, the more expensive it gets to run.

When you hear people talk about a model’s context window (more on that in a second), they’re talking about how many tokens it can hold in memory at once. Some older models could handle 4,000 tokens. Newer ones can handle over a million.

This is why AI at times forgets earlier parts of a long conversation. Once the conversation fills up the context window, the oldest tokens are dropped just like when your RAM fills up and your computer starts lagging.

Tokens are the atoms of AI language. Once you understand that, you start to see why some prompts work better than others, why AI gets forgets in long chats, and why API pricing is measured in tokens per thousand.

2. Context window
Imagine you’re talking to someone, but they have a very specific kind of memory. They can only remember the last X minutes of a conversation. Everything before that? Gone. Forgotten.

That’s a context window.

It’s the total amount of text measured in tokens that an AI model can see and consider at one time. This includes everything: your instructions, the conversation history, any documents you’ve shared, and the model’s own replies.

Think of it like a whiteboard. The context window is the size of the whiteboard. You can write whatever you want on it. But once it’s full, you have to erase something old to write something new.

You know what is more interesting?

A small context window (like 4K tokens) means the AI can only work with a few pages of text at a time. Give it a long document, and it can only read chunks of it. A large context window (like 200K tokens) means you can literally paste an entire book and ask questions about it.

This is why people got so excited when Claude announced a 200,000-token context window. Or when Gemini pushed towards 1 million. This thing fundamentally changes what you can do with the model.

What is the practical lesson? If you’re working on something important like summarizing a long document or analyzing data, always be aware that your AI might be forgetting earlier parts of your conversation. That’s not a bug. That’s just the whiteboard running out of space.

3. Temperature
This one is my personal favourite to explain, because once people hear it, they never forget it.

When you ask an AI to write something, there’s a setting known as temperature, that decides how random or predictable the output will be.

Low temperature (closer to 0) = the AI plays it safe. It picks the most likely, most expected word every single time. The output is consistent, accurate, and a little boring. Like that one guy who always sends the same email template.

High temperature (closer to 1 or beyond) = the AI takes risks. It chooses surprising words, unusual turns, interesting ideas. Sometimes brilliant. But not always.

Here’s a real example. Ask an AI to “complete the sentence: The cat sat on the…”

At low temperature, it almost always says “mat” or “floor.” Predictable. Safe.

At high temperature, it might say “philosophical dilemma” or “crumbling empire of Tuesday.”

Creative? Yes. Useful for a legal brief? Absolutely not.

So here’s the unwritten rule that most people don’t know:

If you’re using AI for factual tasks such as summarizing, coding, extracting information, you want low temperature. The AI should be precise, not creative.

If you’re using AI for creative tasks such as writing fiction, brainstorming, generating marketing copy, increase the temperature. You want the unexpected.

Most consumer apps like ChatGPT don’t let you touch this dial directly. They’ve set it to a middle ground. But if you ever use an AI API or a developer tool, you’ll see this setting. And now you actually know what to do with it.

4. Hallucination
This is the term everyone has heard, but not everyone understands why it happens and that’s the important part.

Hallucination is when an AI gives out wrong answers with absolute confidence. No hesitation. A wrong, answer stated as fact.

Example: You ask an AI about a book. It gives you a title, an author, a year, a plot summary all made up. The book doesn’t exist. But the AI states it as if it’s reading from Wikipedia.

Why does this happen?

Here’s the thing most people miss. AI language models are not databases. They don’t look up facts. They predict the next most likely token based on patterns they learned during training. They’re autocomplete on a massive scale.

So when an AI doesn’t know something, it doesn’t say “I don’t know.” It generates what sounds like a correct answer because that’s literally what it was trained to do.

The danger isn’t that AI makes mistakes. All tools make mistakes. The danger is that AI makes mistakes with the exact same confidence it uses when it’s right. It just answers.

The practical lesson here is that never blindly trust AI for facts, statistics, medical advice, legal information, or anything where being wrong has real consequences. Use it as a starting point. Then verify.

The people who understand hallucination don’t stop using AI. They just use it smarter.

5. RAG
This is the most misunderstood concept of the five. And honestly? Once you get it, you’ll see it everywhere.

RAG stands for Retrieval-Augmented Generation. It’s actually a very simple idea.

Here’s the problem it solves. A regular AI model was trained on data up to a certain date. It knows nothing about your company’s internal documents. It knows nothing about events from last week. It knows nothing about that PDF you uploaded.

So how does a product like “Chat with your PDF” or “Ask questions about this document” actually work?

This is RAG.

When you upload a document, the system doesn’t feed the whole thing into the AI’s brain. Instead, it breaks the document into chunks and stores them in a special kind of database called vector database that understands meaning rather than just keywords.

Then, when you ask a question, the system first searches this database for the most relevant chunks. It retrieves those chunks. And then it feeds them to the AI along with your question, saying: “Here’s some relevant context. Now answer the question using this.”

That’s it. Retrieve relevant stuff. Feed it to the AI. Generate an answer. RAG.

Why does this matter?

Because it’s the backbone of almost every useful AI product built in the last two years. Customer support bots that know your company’s policies. AI assistants that can answer questions from your legal documents. Tools that summarize research papers. All of it is built on RAG.

And knowing this changes how you think about AI products. When an AI knows your documents, it’s not actually learned anything. It’s just performing a very smart search and feeding the results to a language model. The model is still the same. The context just changed.

So why does any of this matter?
Because AI is not going away. And the gap between people who vaguely use AI and people who actually understand how it works even at a basic level is going to matter more and more in the next few years.

You don’t need to be an engineer. You don’t need to write code. But understanding tokens means you’ll write better prompts. Understanding context windows means you’ll know why your AI assistant is acting confused. Understanding temperature means you’ll know which settings to use for which task. Understanding hallucination means you won’t blindly trust the AI. And understanding RAG means you’ll know exactly what’s happening when any AI product claims to know your data.

That’s it. Five terms. Real understanding. And honestly? That puts you ahead of most people who are out here vaguely using AI without understanding what’s happening internally.

Welcome to the top 10%.
__________________________

Before You Learn Machine Learning, Understand These 5 Basics
5 foundational concepts that will save you hours of confusion
Shreyas Naphad
Shreyas Naphad


AI-Generated Image
I started learning Machine Learning back in 2022. Back then there was no GPT or Gemini to get help from.

I was watching a YouTube tutorial on machine learning. The guy on the screen was typing fast and lines of code were flying. And I wasn’t sure what’s going on.

What is actually happening here?

I didn’t have much idea. I typed the code. I ran it. Something worked. And I felt… nothing. Because I didn’t understand what I had just done or why it worked.

Sounds familiar?

Here’s the thing nobody tells you at the start: most beginners find machine learning hard because they skip the basics. The basics that make everything else click.

You can watch a hundred tutorials. You can copy a thousand lines of code. But if you don’t understand the ideas behind what you’re doing, you’ll always feel lost.

So before you write a single line of ML code, I want you to read this first.

These are 5 things I genuinely want you to understand, before you start your journey in Machine Leaning. Not math. Not theory. Just ideas. This will stay in your head and make you go, oh, now it makes sense.

Let’s get into it.

1. Data Is Everything
Here’s the biggest myth in machine learning: model is everything

People obsess over algorithms. They argue about which model is better. They spend hours picking the right one. But the truth? The model is almost never the problem.

The data is.

Think about it like cooking. Imagine you hand a world-class chef the worst, stale, rotten ingredients. What do you get? A bad meal. It doesn’t matter how skilled the chef is. You cannot cook something great with bad ingredients.

Machine learning works exactly the same way.

The model, that is your chef learns from data. It studies the examples you give it. It finds patterns. It makes decisions based on what it has seen. So if the data is messy, incomplete, or misleading, the model will be too.

This is why the best ML engineers don’t spend most of their time writing model code. They spend it cleaning data. Exploring it. Understanding it. Finding out what’s missing, what’s wrong, what doesn’t make sense.

A simple model trained on clean data will almost always beat a fancy model trained on bad data.

So the next time you’re tempted to jump straight into building a model, please stop. Look at your data first. Really look at it. Ask what it’s telling you. Ask what it’s hiding.

That’s where the real work is.

2. Features = What the Model Actually Sees
Here’s something that should be registered in your head.

The model doesn’t see reality. It doesn’t see the world the way you do. It only sees numbers. Specifically, it sees features i.e. the columns, values, and measurements you decide to give it.

Age, Salary, Number of clicks, Pixel values in an image, Words in a sentence, all these are features. And whatever you feed in, that’s all the model has to work with.

Imagine someone is trying to decide if you’d be a good employee. But they can’t meet you. They can’t talk to you. All they can see is your resume, a fixed list of fields. Name. Years of experience. Skills. Degree.

They’re making a huge decision with limited information. And they can only work with what’s on the page.

That’s your model. It can only work with what you give it.

This is why feature selection matters so much. If you give the model the wrong information, or leave out something important, it will perform bad. Not because it’s bad at finding patterns. But because you didn’t give it what it needed.

And the other side is also true. Give the model the right, clean, relevant features, and even a simple model can do surprisingly powerful things.

So when you’re building anything with ML, always ask: what am I actually feeding this model? Does it get what it needs? Is there something missing that would help it understand better?

Better features not only improve accuracy but make the whole model smarter.

3. Training vs. Testing
You Must Know the Difference

This one is very important. Because it looks fine on the surface. But it breaks everything underneath.

The idea is when you build an ML model, you teach it using a set of data called the training set. The model studies this data. It learns the patterns. It gets good at it.

But here’s the problem. You can’t test the model on the same data it trained on. That would be like giving a student the exact exam questions ahead of time, and then being shocked when they score 100%.

Did they actually learn? Or did they just memorize the answers?

That’s what happens when you test on training data. The model looks amazing on paper. But in the real world, when it sees new, unseen data, it fails. Because it never actually learned. It just memorized.

This is why you always keep a separate test set. Data the model has never seen. Data it cannot prepare for. When you evaluate the model on this set, you get a true picture of how it actually performs.

Think of it like school. You study all semester, that’s your training. Then you sit the final exam with questions you’ve never seen before, that’s your test. The exam is what actually tells you if you understood the subject.

If your model scores well on training data but poorly on test data, that’s a red flag. It means something went wrong. And the next point explains exactly what.

4. Overfitting vs. Underfitting
This is the concept where most people struggle. But I will be explaining it in a way that you will never forget it.

Imagine two students before a big exam.

Student A studied too specifically. He memorized every practice paper, word for word. He knows the exact phrasing of every past question. But the real exam has slightly different questions, and they freeze. He can’t adapt. All that memorizing was useless.

Student B barely studied at all. She glanced at the material once. She walks into the exam and just couldn’t get the right answers. Predictably, she fails.

Now, your model is one of these students.

Overfitting is Student A. The model has memorized the training data so well that it even memorized the noise i.e. the irrelevant details, the random patterns that don’t actually mean anything. It performs great on training data. Terrible on new data.

Underfitting is Student B. The model is too simple. It didn’t learn enough from the training data. It makes bad predictions on everything, training data and new data.

The goal is to find the model that studied well. Not too much. Not too little. A model that learned the real patterns, the ones that actually performs good in the real world.

This is called generalization. And it’s the whole point of machine learning.

You don’t want a model that’s great at one specific dataset. You want a model that actually understands the problem, and performs well on data it has never seen.

Balance is everything. Too complex → overfitting. Too simple → underfitting. Right in the middle → a model that actually works.

5. Models Don’t Understand, They Predict
This is the mindset shift that changes how you think about everything.

When you see a chatbot answer a question, we feel like it knows the answer. When you see a model classify images, it feels like it sees what’s in the photo. But it doesn’t. Not really.

Machine learning models do not think. They do not understand. They do not have knowledge.

What they have is patterns. Billions of patterns learned from data and the ability to match new inputs to those patterns.

Ask a language model: “What is the capital of France?” It will say “Paris.” But it didn’t know Paris is the capital. It learned that when the words “capital of France” appear, the word “Paris” follows. It’s a very well-trained prediction.

So, if the model learned from biased data, it will make biased predictions. If it learned from incomplete data, it will have gaps. It cannot reason its way out of a bad pattern. It can only predict based on what it has seen.

And that’s actually a powerful thing to understand. Because it means every problem with a model can be traced back to something solid such as the data, the features, the training process. Nothing is random.

ML is probability, not thinking. And when you understand this, you start seeing it as a very clever system for finding and applying patterns.

You’re More Ready Than You Think
You don’t need a maths degree to understand machine learning. You don’t need to memorize algorithms or be the best at calculus before you’re allowed to start.

What you need and what most tutorials skip is the intuition. The clarity. The simple ideas that make everything else make sense.

And now you have five of them.

You know that data is more important than the model. You know that features are what the model actually sees. You know why training and testing must be separate. You know the difference between a model that memorized and a model that actually learned. And you know that models predict and not understand.

That’s it. That’s the foundation.

Now go build something. Start small. Make a mess and learn from it. The best way to make these ideas stick is to see them fail and then fix them.

It’s all about learning patterns from data to make predictions.
____________________

Stop Using Accuracy: 5 ML Metrics You Must Understand
Accuracy could be lying to you



AI-Generated Image
For Non-Members link to the full story

The Accuracy Trap
Let me guess, when you built your first machine learning model, you trained it, ran the evaluation, saw an accuracy of 97% and thought you’ve made a fantastic model.

Well honestly, we’ve all been there.

The only problem is that the accuracy is lying to you. Not always, but often enough. And blindly trusting it has caused real damage in real products.

Here’s a classic example. Imagine you’re building a model to detect a rare disease. In your dataset, 99% of people are healthy and 1% are actually sick. Now imagine a model so dumb it doesn’t even look at the data and just predicts “healthy” for every single person. What’s the accuracy? 99%. Sounds brilliant. But it missed every sick person. Zero. That model is completely useless, and yet the accuracy score is fantastic.

This is called the imbalanced dataset problem, and it’s more common than you think. It’s found in fraud detection, cancer screening, spam filters. Accuracy fails in all of them.

So what do you use instead? Let’s go through the 5 metrics that actually tell you the truth.

Before the Metrics: The Confusion Matrix
Every metric in this article comes from one place and that is confusion matrix. Think of it as a scoreboard that shows exactly what your model got right and wrong.

There are four outcomes when your model makes a prediction:

True Positive (TP): Model said positive. It was actually positive.
True Negative (TN): Model said negative. It was actually negative.
False Positive (FP): Model said positive. It was actually negative. (a “false alarm”)
False Negative (FN): Model said negative. It was actually positive. (a “missed catch”)
Every metric below is just a different way of combining these four numbers. Once this clicks, everything else becomes easy to understand.

Metric 1: Precision
Are Your Positive Predictions Trustworthy?

The question Precision answers: Out of all the positive predictions made by the model, how many were actually positive?

Precision=TPTP+FPPrecision = \frac{TP}{TP + FP}Precision=TP+FPTP​

Think of it this way. Your model is pointing fingers and saying “that one’s spam, that one’s spam.” Precision asks: how often is your model right when it points?

When does Precision matter most? When a False Positive is costly.

Take spam detection. If your model wrongly flags a real email as spam (False Positive), your user might miss a job offer, a bank notice, an important update. That’s a real cost. You don’t want your model pointing “spam!” unless it’s very sure.

High Precision = when the model says positive, you can trust it.

from sklearn.metrics import precision_score
precision = precision_score(y_true, y_pred)
Metric 2: Recall
Is Your Model Finding All the Positives?

The question Recall answers: Out of all the actual positives, how many did the model find?

Recall=TPTP+FNRecall = \frac{TP}{TP + FN}Recall=TP+FNTP​

Recall is about coverage. It doesn’t care if your model throws a few false alarms. It cares about whether anything slipped through.

When does Recall matter most? When a False Negative is costly.

Take cancer screening. If the model misses a sick patient (False Negative), that patient goes home thinking they’re fine. That’s devastating. In this case, you’d rather flag a healthy person for more tests (False Positive) than miss a sick one. The inconvenience of extra tests is nothing compared to a missed diagnosis.

Same with fraud detection. Let a fraudulent transaction slip through? You’re losing money. Flag a legitimate one for review? Can be annoying, but it’s still fine.

High Recall = the model is thorough. It tries not to miss anything.

from sklearn.metrics import recall_score
recall = recall_score(y_true, y_pred)
Metric 3: F1-Score
What If You Care About Both?

The reality is such that Precision and Recall are often in tension with each other.

If you lower your threshold for calling something positive, you catch more positives (Recall goes up) but you also throw more false alarms (Precision goes down). It’s a seesaw.

So what do you do when you can’t just optimize one? You use the F1-Score.

F1=2×Precision×RecallPrecision+RecallF1 = 2 \times \frac{Precision \times Recall}{Precision + Recall}F1=2×Precision+RecallPrecision×Recall​

This is the harmonic mean of Precision and Recall and there’s a reason we don’t use a simple average here.

If your Precision is 1.0 and your Recall is 0.0, a simple average gives you 0.5. Sounds okay. But the F1-Score gives you 0. Why? Because a model that never predicts positive is completely broken, and the F1-Score correctly punishes that.

The harmonic mean punishes extreme values. It forces both Precision and Recall to be decent before the score looks good.

When to use F1: When you’re working with imbalanced data and you want a single number to compare different models, without ignoring either type of error.

from sklearn.metrics import f1_score
f1 = f1_score(y_true, y_pred)
Metric 4: ROC-AUC
The Big Picture View

Here’s something most beginners don’t realize: your model isn’t really outputting a 1 or a 0.

It’s outputting a probability. Something like 0.87, which means “I’m 87% sure this is positive.” You then pick a threshold (usually 0.5) and convert that to a hard label.

But what if 0.5 is the wrong threshold for your problem? What if you should be flagging anything above 0.3 to maximize Recall? Or maybe 0.7 to keep Precision high?

The ROC curve answers this by plotting your model’s performance at every possible threshold:

The x-axis is the False Positive Rate (how often you catch the wrong thing)
The y-axis is the True Positive Rate (how often you catch the real thing)
The AUC (Area Under the Curve) summarizes that whole curve into one number.

AUC = 1.0 → Perfect model. Always ranks real positives above negatives.
AUC = 0.5 → Your model is literally guessing. Flip a coin, same result.
AUC = 0.85 → Good enough. The model is meaningfully better than chance.
AUC is especially powerful because it’s threshold-independent. It tells you how well your model separates the two classes overall, not just at one specific cutoff.

from sklearn.metrics import roc_auc_score
auc = roc_auc_score(y_true, y_pred_proba)
Note: pass in the raw probabilities (y_pred_proba), not the hard 0/1 predictions.

Metric 5: Log Loss
Confidence Is Everything

Here’s a scenario. There are two models that predict the correct class. Model A says “I’m 51% sure.” Model B says “I’m 99% sure.” Accuracy gives them the same score.

That’s wrong. A model that barely goes past 50% is not the same as one that’s highly confident and correct. And if a model is confidently wrong, such as saying 95% sure about something that turns out to be false, that should be penalized hard.

That’s what Log Loss (also called Cross-Entropy Loss) does.

LogLoss=−1N∑i=1N[yilog⁡(pi)+(1−yi)log⁡(1−pi)]Log Loss = -\frac{1}{N} \sum_{i=1}^{N} [y_i \log(p_i) + (1-y_i) \log(1-p_i)]LogLoss=−N1​i=1∑N​[yi​log(pi​)+(1−yi​)log(1−pi​)]

Don’t let the formula scare you. The intuition is simple:

Correct prediction + high confidence → tiny penalty
Correct prediction + low confidence → moderate penalty
Wrong prediction + high confidence → massive penalty
Lower Log Loss is better. A perfect model has Log Loss of 0.

When to use it: When you’re not just classifying things but you care about the quality of the probabilities. Like in deep learning, medical risk scores, or any application where the probability output itself matters, not just the final yes/no answer.

from sklearn.metrics import log_loss
loss = log_loss(y_true, y_pred_proba)
How to Pick the Right Metric
Here’s a quick cheat sheet you can save:

Press enter or click to view image in full size

Source: Image By Author
The honest answer is, in most real projects, you should look at multiple metrics together. Precision and Recall tell different parts of the story. AUC gives you the overall picture. Log Loss keeps you honest about your model’s confidence. They work together.

Accuracy isn’t useless but it’s just incomplete. It’s a starting point, not a finish line.

Final Thought
The goal of a machine learning model isn’t just to score well on a metric. It’s to solve a real problem in the real world where mistakes have real consequences. The metric you choose should reflect that.

Before you train your next model, ask yourself: what’s the actual cost of a false positive here? What’s the cost of a false negative? That answer will tell you exactly which metric to optimize for.

I m curious, what metric do you rely on most in your current projects? Drop it in the comments. And if you’re working on something where picking the right metric was genuinely tricky, I’d love to hear about it.

__________________________

What is an API? A Simple Guide for Beginners (With Real Examples)
Understand REST, HTTP requests, and real-time APIs in minutes


AI-Generated Image
For Non-Members link to the full story

The every day apps you use such as Google Maps, Spotify, Instagram, your bank is held together by something you’ve probably never seen but absolutely depend on. It’s called an API. And it’s about time you master this topic.

If you’re just starting out as beginner, API is one of those terms that you might hear a lot, like everyone already knows what it means. But a lot of people don’t.

By the end of this article, you’ll understand how API works, what the different parts mean, and you’ll have a mental model to actually start building with them. That’s the goal of this article

The Restaurant Analogy
You enter a restaurant. You don’t go into the kitchen yourself, pull out the ingredients, and cook your own food. That would be a chaos! Instead, you sit at the table, look at the menu, and tell the waiter what you want. The waiter goes to the kitchen, passes your order along, the kitchen makes it, and the waiter brings it back to your table.

You never see the kitchen. You don’t know how the food was made. You just got what you asked for.

The API version of this

You are the the developer. The server is the kitchen that holds all the data and logic. The API is the waiter. It takes your request, goes to where the data lives, and brings back exactly what you asked for. You never touch the server directly. The waiter i.e. the API handles everything in between.

That’s it. That’s the entire game. An API (Application Programming Interface) is a middleman that allows two different systems talk to each other in a structured way.

Real Examples
Think about how Zomato shows you a restaurant’s location on a map. Zomato doesn’t have its own mapping system. Building one from scratch is not feasible. Instead, it uses Google Maps through an API.

When you open a restaurant page, Zomato’s app sends a request to Google’s Maps API: “Give me the map for this address.” Google’s API responds with the map data. Zomato displays it. You never touch the Google’s actual database, algorithm, and code. The API was the secure messenger in between.

When you open a weather app on your phone, here’s what actually happens. Your app doesn’t have the weather data sitting inside it. It sends a message to a weather service asking: “What’s the weather in London right now?” The weather service receives that request, looks up the data, and sends back a response: temperature, humidity, wind speed. Your app reads that response and displays it on your screen.

That entire conversation of your app asking and the server answering happened through an API.

An API is just a contract. Your app agrees to ask in a specific way, and the server agrees to respond in a specific way. Both sides trust the format.

How a request actually works
When your app talks to an API, it sends something called an HTTP request. Think of it like a structured letter. It has a specific format, and the server knows exactly how to read it. Here’s the basic flow:

Press enter or click to view image in full size

Source: Image By Author
A request has a few important parts. First is the endpoint which is the specific URL address you’re hitting. Second is the method i.e. what action you want to perform. Third are headers, which carry extra information. And sometimes there’s a body, the actual data you’re sending. The four HTTP methods you’ll use constantly are:

GET

Read something. Fetch data. “Give me a list of songs.” You’re just reading and not modifying.

POST

Create something Send data to create a new record. “Add this new song to the database.”

PUT

Update something. Replace an existing record. “Change the title of song 10.”

DELETE

Remove something. Delete an existing record. It is irreversible, so be careful with this one.

These four together are what engineers call CRUD: Create, Read, Update, Delete.

Types of APIs
API is not a single thing. It’s a category. Like a vehicle. It could be a bicycle, a truck, and a Formula 1 car. All are vehicles but they work very differently and you will use them in completely different situations. APIs are the same. There are several types, and knowing which one to use and why is crucial.

Let’s go through each one.

1) REST
REST (Representational State Transfer) is the most popular API style. It uses standard HTTP methods (GET, POST, PUT, DELETE), returns data in JSON, and is straightforward to build and understand. When someone says we have an API, they most likely mean a REST API. The only real issue is that sometimes it over-fetches. This means it gives you more data than you actually need, like getting the whole pizza menu when you just wanted to know if they have garlic bread.

2) GraphQL
GraphQL, developed by Facebook, fixes the above problem. Instead of the server deciding what data you get, you tell the server exactly what you want. Nothing more, nothing less. If you only want a user’s name and profile photo, you ask for just those two things. It’s a single endpoint where you write a query describing exactly what you need.

3) SOAP
SOAP (Simple Object Access Protocol) is older, stricter, and uses XML instead of JSON. It has rigid rules about message format and requires much more setup. You’ll rarely build with it from scratch today, but you may encounter it if you ever work with banking systems, government services, or enterprise software where security and strict standards matter more than speed.

4) gRPC
gRPC (Google Remote Procedure Call) is built for speed. Instead of sending human-readable JSON, it sends data in binary format that machines process much faster. This makes it perfect for microservices, where dozens of internal services talk to each other thousands of times per second.

Request-response APIs are great when you’re the one initiating the conversation. But what about situations where the server needs to notify you, like a new message arriving, or a stock price changing? That’s where real-time APIs come in.

5) Webhook
A webhook reverses the normal model. Instead of your app asking “did anything happen?” every few seconds, you give the server your address and say “whenever something happens, just notify.” The server then pushes a notification to your app the moment an event occurs, such as a payment going through, or a form being submitted.

6) WebSocket
A WebSocket opens a two-way channel between your app and the server. Both sides can send messages to each other at any time, without either one having to ask first. This is how real-time chat apps work, how live sports scoreboards update, and how multiplayer games stay in sync.

7) WebRTC
WebRTC (Web Real-Time Communication) takes things one step further. Instead of having a server in the middle, it allows two browsers talk directly to each other . This is how video calls in Google Meet and browser-based calls work. The server only helps the two sides find each other initially. After that, the data flows directly between them, making it extremely fast and low-latency for audio and video.

The Netflix example
Here’s something that surprises a lot of people. APIs aren’t just for fetching lists of songs or showing maps. They’re also used in how machine learning models get deployed and used in the real world.

Think about how Netflix recommends your next show. There’s a powerful ML model running somewhere in the cloud that has learned your viewing patterns. When you open Netflix, your app sends a POST request to an API which contains a JSON payload with your user ID, watch history, and maybe the time of day. The API passes that to the model, the model runs its prediction, and the API sends back a list of recommended shows. The Netflix home screen shall render the. All this happens within a second.

What that request looks like

Your app → POST request with JSON data (who you are, what you’ve watched) → hits the API → goes to ML model in the cloud → model runs prediction → API sends back recommended shows → your screen updates.

This is why Python frameworks like Flask and Django are so popular in data science teams as they’re used to wrap ML models in an API so the rest of the engineering team can actually use them. The data scientist builds the model. API makes it accessible to the app. And because these APIs are hosted on cloud infrastructure, the same architecture scales to handle millions of users globally, routing each request to whichever server is available and closest.

Status codes
When the server responds, it sends a three-digit status code along with the data. Learning these early will save you hours of debugging. Just understand this rough rule: 2xx is good news, 4xx means you made a mistake, 5xx means the server made a mistake.

Press enter or click to view image in full size

AI-Generated Image
How to start working with APIs
Theoretical knowledge is important. Practical implementation is what makes you a master. Here’s a practical starting path:

1) Download Postman: It’s a free tool that lets you send API requests without writing any code. It’s the fastest way to see how requests and responses work in real time.
2) Choose a free public API to play with. OpenWeatherMap, the GitHub API, or PokeAPI are all great starting points.
3) Send your first GET request. Fetch some data. Look at the status code. Read the JSON that comes back. Get comfortable with it.
4) Try a POST request. Create something. See the 201 response. Then GET what you just created.
5) Try a webhook services like Stripe or GitHub let you set up webhooks in their dashboards.
6) Read the documentation for whatever API you’re using. Good docs are the best teacher. Get comfortable reading them as that will help in the long term.
The one thing to remember
APIs are how the modern internet works. Every app you use such as Swiggy, Instagram, is constantly making API calls in the background, routing through REST endpoints, firing webhooks, maintaining WebSocket connections. Your job as an engineer is to understand how to talk to those APIs, how to build them yourself, and how to debug them when things go wrong.

You now know what an API is. You know the difference between REST, GraphQL, SOAP, gRPC, Webhooks, WebSockets, and WebRTC. You know what endpoints, status codes, API keys, and JSON are. You now have a good understanding needed to work with APIs.

That’s more than most people know when they land in their first job. Go check out Postman and send your first request. That’s where the real learning begins.
_____________________________
After This, You’ll Be Able to Explain Generative AI to Anyone
A beginner friendly guide to GenAI


Photo by Deng Xiang on Unsplash
For Non-Members link to the full story

At some point this year, you’ve come across the term “generative AI.”
Maybe it showed up in a headline. Maybe someone mentioned it casually in a conversation.

But what does it actually mean?

If you had to explain it to someone in one sentence… could you?

It’s about time we fix that!

Here’s what this article covers:

What AI actually is and how generative AI is different from everything that came before it
How these models learned to write, answer questions, and generate images
The six terms you’ll keep hearing
Why understanding this even at a surface level gives you a real edge right now
Think of this as a real conversation about what this thing actually is, how it works, and why it matters to you. Whether you’re a student, a working professional, or someone who just wants to understand what’s happening in the world. Let’s get into it.

What is AI?
Before we study generative AI, let’s quickly make sure we’re on the same page about AI.

Artificial Intelligence, in very simple terms, is just a software that can make decisions or predictions on its own without us telling it exactly what to do at every step. You’ve been using AI for years without realising it. The way Netflix knows you’ll like that show? AI. Your phone recognising your face? Also AI.

Traditional AI is mostly about recognising or classifying things. It looks at something and gives you a decision.

Think of traditional AI as a judge. It looks at something and gives a verdict. It’s not creating anything new. It just classifies.

Generative AI is different. And that difference is a big deal.

So what is Generative AI?
Generative AI is AI that generates. It doesn’t just look at things, rather it generates new things such as text, images, music, code, videos. When you give an instruction, it produces something that didn’t exist before.

A simple example.

Think of it like this. Old AI was like a librarian where you ask a question, it finds the right book and shows you the right page. Generative AI is more like a writer. You give it a topic, and it sits down and writes something brand new.

That might sound complicated. But it’s really not complicated, it’s just pattern recognition taken to an extreme level. And once you understand this, the whole thing becomes easy to grasp.

How did AI learn this?
Here’s where it gets interesting. Generative AI models that you’ve heard of, like ChatGPT or Gemini or Claude were trained on vast amounts of text. We’re talking about a significant chunk of everything ever written on the internet, academic papers, forums, articles, code repositories.

During training, the model’s job was really simple: predict the next word. That’s it. Given the sentence “The sky is very,” what word comes next? “Blue.” Given “Two plus two equals,” what comes next? “Four.”

But when you do that billions of times, across billions of sentences, on every topic, something maginificient happens. The model starts to understand the actual structure of language, the logic behind ideas, relationships, context.

It’s like learning to cook by tasting a million dishes. Eventually, you stop memorising recipes and start actually understanding flavour.

I won’t say it’s conscious. It doesn’t understand things the way you and I do. But it has seen so much human-written text that it has developed a really good understanding about how language works, and what kind of response fits what kind of situation.

The key concepts
There are a few terms you’ll come across. Here’s what they actually mean:

Large Language Model (LLM)
The brain behind AI. “Large” just means it was trained on a huge amount of data with billions of internal parameters. ChatGPT, Claude, Gemini, all these are LLMs.

2. Prompt

Prompts are the instructions you give to the AI. The thing you type in. The better your prompt, the better the output. Think of it as the direction you give to your assistant.

3. Training

The process of feeding the model with large amount of data so it can learn patterns. This happens once (or periodically), before you ever use the product.

4. Parameters

The internal numbers the model adjusts during training to get better at predictions. More parameters generally means a more capable model.

5. Context window

How much text the AI can see at once during a conversation. A larger context window means it can remember more of what you said earlier.

6. Hallucination

When the AI confidently gives wrong answer. It sounds real, but it’s wrong. Always verify important facts.

A quick timeline on how we got here
This didn’t come out of nowhere. There’s a real story behind how we arrived here:

1950s–90s

Early AI was mostly rule-based. Programmers manually wrote the logic: “if this, then that.”

2000s–2010s

Machine learning takes over. Instead of hard-coded rules, models learn from data.

2017

Google researchers publish a paper called “Attention Is All You Need.” It introduces the Transformer architecture which is the engine that makes modern LLMs possible.

2020–2022

GPT-3, DALL·E, Stable Diffusion. AI can now write essays, generate images, and write code. The outputs start to surprise people.

Nov 2022

ChatGPT launches. One million users in five days. One hundred million in two months. The general public got access to generative AI for the first time.

2023–today

Claude, Gemini, Llama, Mistral and dozens of others arrive.

What can it actually do and where it struggles?
Let’s be honest about both sides, because the hype can make it hard to see clearly.

What it does well: Writing, summarising, explaining, brainstorming, drafting emails, translating languages, answering questions, writing and debugging code, generating images from descriptions, and having useful conversations about any topic.

Where it struggles: Maths that requires actual reasoning (it can make mistakes), real-time information (it doesn’t browse the internet unless specifically built to do so), local context it wasn’t trained on.

The most important thing to remember is that generative AI is a tool. It improves what you’re trying to do. It doesn’t replace your judgment, your creativity, or your responsibility.

Why does any of this matter to you?
You might be thinking, okay interesting, but why should I care? If I’m not a developer. I’m not building anything.

The thing is, this technology is showing up in the tools you already use. In email clients, search engines, design software, spreadsheets, customer service chatbots, medical platforms, legal tools, education apps. You don’t have to build anything. You’re going to face it anyways.

And people who understand what it is, even at a basic level will use it more effectively, find out mistakes more easily, and make better decisions about when to trust it and when not to.
_______
MCP Explained Like You’ll Never Forget It
Shreyas Naphad
Shreyas Naphad

Following
3 min read
·
Dec 15, 2025
198


5





A complete beginner guide

Press enter or click to view image in full size

AI-Generated Image
👉For Non-Members link to the full story

Most people hear MCP (Model Context Protocol) and immediately feel confused.

Is it:

a tool framework?
an agent system?
part of LangChain?
The truth is much simpler.

And once you understand it, MCP becomes one of the easiest GenAI concepts.

This article is written for:

people confused about MCP
people preparing for GenAI interviews
people who want real practical exposure (along with theory)
No paid APIs.
No cloud.

Let’s begin.

The One Line That Explains MCP Forever
MCP is a protocol that standardizes how tools are exposed to LLM-driven systems.

That’s it.

It is just a protocol layer. Their only job is to defines how tools are exposed, discovered, and invoked by LLM-driven systems.

Why MCP Exists (The Real Problem)
LLMs are great at:

understanding language
reasoning
planning steps
but they cannot perform actions.

They can’t:

read your files
query your database
call your APIs
So we need to give them tools.

The Problem Before MCP
Each framework had its own tool format
Tools were tightly coupled to prompts
Tool logic and reasoning logic were mixed
Hard to switch LLMs
There was no single standard. It became messy.

MCP’s Core Idea (The Heart of Everything)
Separate decision-making from execution.

LLM decides what needs to be done
MCP handles how it gets done
This separation is what makes MCP powerful.

MCP Is a Protocol, Not a Framework
This distinction is important to understand.

MCP is:
a communication standard
a contract between models and tools
a reusable interaction layer
MCP is not:
an agent framework
a tool library
a replacement for LangChain
Think of MCP like HTTP:

HTTP doesn’t define business logic
it defines how systems talk to each other
MCP does the same for LLMs and tools.

MCP Architecture (Understand Once, Remember Forever)
At a high level:

User
 ↓
LLM (or LLM client)
 ↓
MCP Server
 ↓
Tools
Key Points:
LLM never talks to tools directly
tools live inside the MCP server
MCP server executes tools on request
This design makes systems:

modular
secure
easier to maintain
Who Decides Which Tool to Call?
This is a common interview question.

Answer:
Not MCP.

Tool selection is decided by:

the LLM
or an orchestration / agent layer
MCP only executes the tool that was requested.

What Is an MCP Server?
An MCP server:

exposes tools
describes their inputs and outputs
executes tools
returns structured results
It does not:

reason
plan
choose tools
Think of it as:

a controlled execution environment for tools

What Are MCP Tools?
This is where most confusion happens.

MCP tools are:
custom functions
defined by developers
exposed with metadata
They can represent:

calculators
file readers
database queries
Important Truth:
MCP does not provide built-in tools.

MCP standardizes how tools are exposed, not what tools exist.

How MCP Understands Tools
Each tool is described by:

name
description
input schema
output schema
MCP uses this information to:

allow tool discovery
validate requests
return structured responses
The internal logic of the tool does not matter to MCP.

Can MCP Work Without an LLM?
Yes.

MCP is model-agnostic (isn’t tied to a specific model).

Any client that understands the protocol can:

discover tools
invoke tools
receive results
LLMs are just one type of client.

MCP Request–Response Lifecycle
Press enter or click to view image in full size

AI-Generated Image
Client asks MCP: “What tools are available?”
MCP returns tool metadata
Client requests a tool execution
MCP validates inputs
Tool is executed
MCP returns structured result
This flow never changes.

MCP vs Tool Calling
Tool calling is a capability
MCP is a standardized protocol for tool calling
MCP makes tool usage:

portable
reusable
independent of models or frameworks
When Should You Use MCP?
Use MCP when:

tools must be reusable
models may change
clean architecture matters
Avoid MCP for:

quick demonstrations
single-prompt short experiments
One Sentence That You Should Remember
“MCP standardizes how tools are exposed and invoked by LLM-driven systems, separating model reasoning from tool execution.”

Final Mental Model (Never Forget This)
LLM → decides
MCP → executes
Tools → do the work
That’s MCP in a nutshell.

__________________________
Why Agentic AI Is the #1 Skill To Learn

AI-Generated Image
For Non-Members link to the full story

Let me get straight to the point.

I’m not here to tell you AI is coming for your job. You’ve heard that a hundred times already, and frankly, nobody wants to here the same thing again.

You’ve also probably read the top skills to learn in 2026. Learn Python. Learn AI. Learn prompt engineering. Sure all those are valid. But here’s the thing: everyone is saying that. And when everyone is saying the same thing, the real opportunity is usually one step ahead.

So what’s that step?

Agentic AI. And hang on, it’s not some buzzword to add to your LinkedIn bio. It’s a fundamental shift in what AI does, how it thinks, how it works, and what it’s capable of. Right now, very few people understand it deeply enough to actually build with it.

That gap is exactly where opportunity lives.

What Is an AI Agent?
Here’s the super way to understand it.

Regular AI: you ask → it answers. You give input → you get output. It waits for you every single step.

An AI agent: you give it a goal → it figures out the steps → it uses tools → it checks its own work → it finishes the job. You come back to a result.

Think hiring a consultant who gives you a report vs. a team that actually executes on it. That’s the difference.

A real example
You ask a normal AI: “Research my top 5 competitors and summarize their pricing.”
It gives you a generic answer based on the training data. It might as well hallucinate some part (confidently giving wrong answer).

You give the same task to an agent:
It searches the web. Navigates each pricing page. Extracts the data. Flags anything behind a paywall. Builds you a comparison table. Done.

That’s not a better chatbot. That’s a different category of tool.

The 5 things that make an agent work
A language model: The reasoning brain that decides what to do next
Tools: Web search, Calling APIs, Email, Query a database (how it interacts with the world)
Memory: Short-term (this task) and long-term (across tasks)
Planning: Breaking a big goal into smaller steps
Feedback loops: Observe results, adjust, try again
Why This Skill, Why Now
Couple of years ago, building reliable agents was complicated. Models weren’t capable enough. Frameworks were new. It was mostly a research-lab thing.

2026 is different. Models are better. Frameworks like LangGraph, CrewAI, and AutoGen are production-ready. The gap between doing a cool experiment and thing that gets you a job has closed fast.

And here’s the part people miss: this compounds with what you already know. A marketer who can build a research agent is 10x more effective. A developer who automates code review is invaluable to their team. A Product Manager who understands agentic workflows thinks about what’s possible.

It’s a multiplier to your expertise.

How to Actually Learn This Step by Step
Here’s a roadmap I’d actually follow.

Week 1: Build the mental model
Understand how LLMs work, just enough to know their limits
Read about tool use and function calling (Anthropic and OpenAI both have good docs)
Talk to these models and pay attention to when they fail , that’s more educational than most courses
Week 2–5: Learn the building blocks
Python basics that are enough to call APIs, handle JSON, write simple loops
Call the Anthropic or OpenAI API directly, just understand what’s happening
Learn function calling / tool use as this is non-negotiable
Build one agent by hand, no framework. One tool (web search or calculator), one loop, raw API calls. A weekend project. Worth every minute.
Why build it by hand first? Most people dive into LangChain and have no idea what’s happening when something breaks. Building from scratch means you understand the abstraction — not just how to use it.

Week 5–8: Learn the frameworks
LangGraph — best for production-grade, stateful agents. My honest top pick.
CrewAI — great for multi-agent systems with different roles
AutoGen (Microsoft) — solid for experimentation and research-style workflows
LangChain — largest ecosystem, most community resources
Pick one, go deep.

Month 2+: Build something real
This is where most people do not invest much. Courses will only take you so far.

Build a project that solves an actual problem you have. A research assistant. A monitoring agent that alerts you when something changes. An automated pipeline for a task you hate doing.

You’ll hit things no tutorial teaches you. It may be rate limits, model edge cases, memory management, cost optimization, graceful error handling. Those problems only become real when the project is real.

One useful agent you built and shipped beats ten certificates.

Advanced Work (when you’re ready)
Multi-agent systems — specialized agents coordinating together
RAG (Retrieval Augmented Generation) — giving agents access to large knowledge bases
Agent evaluation — how do you actually measure if it’s working well?
Human-in-the-loop design — knowing when to pause and ask a human is a skill
What If You’re Not Technical?
You can start with understanding what agents can and can’t do, designing agentic workflows, knowing how to evaluate them. Learning python would definitely help you. Even if you’re a non-tech, you still have a chance to learn and become a strong strategist.

There are also no-code options: Make, n8n, and various AI workflow builders allow you chain AI capabilities without deep coding. They have limits, but they’re real and improving.

If you have any interest in the technical side, get into it. The combination of domain expertise and the ability to actually build is rare and is of the highest value.

The Real Talk
Agents fail in unexpected ways. They can fail miserably. They can take expensive actions if you’re not careful. Reliability is still a problem that is yet to be completely solved.

The best builders in this space have a clear sight about where it breaks. Learn the limitations as deeply as you learn the capabilities.

And don’t let the speed of change make you feel panic. Yes, frameworks will upgrade. But the core concepts i.e. how agents reason, how tools work, how to design reliable systems will stay consistent.

Your Next Step, Based on Where You Are
If you’re brand new: Don’t start with a course. Open Claude or GPT-4, describe the most repetitive task in your work, and ask how an agent would handle it. Just start building intuitions.

If you have some technical background: Build an agent this week. Llama API, one tool, one loop. Before you start using a framework.

If you’re already in the space: Go deeper on evaluation. Most agent builders ignore this. What’s your testing strategy? What are your evaluation methods? This is what makes you a serious developer in this space.
_______
12 AI Terms You Must Know in 2026
Explained so simply you’ll never forget them


AI content today feels overwhelming.
One minute you’re hearing LLMs, the next it’s RAG, agents, vector databases, and MCP.
Everyone expects you to know these terms.

But here’s the truth:

Most explanations are either:

Too academic
Too vague
Or written for people who already know AI
This guide is different.

What This Article Promises
Press enter or click to view image in full size

AI-Generated Image
By the end of this article, you will understand 11 core AI terms that appear in every AI job post, blog, and product

You will be able to use this article as a revision cheat sheet before interviews.

No equations. No research-paper language.

Just clear intuition + real-world analogies.

This guide is for beginners entering AI / ML / Data Science, developers building apps with LLMs, RAG, or agents and anyone reading AI blogs and thinking: “I kind of get it… but not fully”

This is your one solid revision article you can come back to anytime

If you understand these 12 concepts clearly,
you’ll be ahead of 80% of people learning AI online.

Let’s start.

1) LLM (Large Language Model)
An LLM is a neural network trained on huge amounts of text. It learns how words usually follow each other.

It does not think or understand like humans. It predicts the next best word again and again. Chatbots, AI writers, and assistants are powered by LLMs.

2) Tokenization
AI does not read full sentences like us. It breaks text into small pieces called tokens.
A token can be a word, part of a word, or a symbol. More tokens = more cost and more time.

Example: [“Hello, this is Mark”] -> “Hello”, “this”, “is”, “Mark”. This is how tokens would be made.

This is why shorter prompts are faster and cheaper.

3) Transformer
A transformer is the brain behind LLMs. It helps AI look at all words of the sentence at once using the attention mechanism, not one by one.

The idea behind the attention mechanism is not only focus on a particular word but also look at the relation of that word with all others.

This makes understanding context much better. That’s why AI can write long, meaningful text.
Almost all modern AI models use transformers.

4) Embeddings
Models don’t understand text but numbers. So embeddings turn text into meaningful numbers. Similar words having similar meanings get similar numbers.

This helps AI compare meaning, not exact words. Used for search, recommendations, and RAG.
Think of it as converting text into coordinates.

So words like King and Prince would have nearby numbers associated. Whereas King and Pizza would have completely faraway numbers.

5) Vector Database
A vector database stores these embeddings.
It helps find similar meaning, not exact matches. Used when you search documents with questions.
Much faster than normal databases for AI tasks. Common in chatbots and AI search systems.

6) RAG (Retrieval-Augmented Generation)
RAG allows AI to search for data before answering. It fetches relevant documents containing relevant data using embeddings to answer your queries.
This reduces wrong answers.
RAG is used in most serious AI apps today.

7) Hallucination
Hallucination means AI confidently gives a wrong answer.
It sounds correct, but is actually false.

Happens when AI has no real data to rely on.
RAG helps reduce hallucinations. Never blindly trust AI answers.

8) Prompt Engineering
Prompt engineering is how you talk to AI.
Clear instructions = better answers.
You can specify the tone, format, and behaviour.
It’s about clarity. Good prompts save time and tokens.

9) Fine-Tuning
Fine-tuning means training AI on your own data.
The generalized model learns your style or domain.

For example, I have a language model that can write, but I want it to write in Shakespeare style. So I trained that model on his writings.

Used when prompts are not enough. More control, but more cost.
Not always needed for small apps.

10) Latency
Latency is how long AI takes to respond.
Lower latency = faster answers. High latency feels slow and annoying.

Depends on the model size and the tokens used. Important for user experience.

11) Agent
An agent is an AI that takes actions, not just answers.
An agent can call tools, APIs, or other models.
It follows the goals step by step. Used in automation and AI workflows.

Example: An agent that reads a Google Sheet and sends the email to the recipient.
Agents are the future of AI apps.

12) Evaluation
Evaluation checks how good AI answers are.
You don’t trust AI blindly. You measure quality and accuracy.

Needed for improvement. Without evaluation, AI apps may fail.

Common LLM Evaluation Methods
Human Evaluation: A person checks AI answers. Slow and costly. Yet important. Good for small datasets.
BLEU / ROUGE: Compares AI answered text with the reference text. Checks word overlap. Used in summarization. Does not check the meaning fully.
Old but still useful.
BERTScore: Checks meaning similarity. Uses embeddings instead of words. Better than BLEU/ROUGE. Slower to compute. Popular in NLP tasks.
LLM-as-a-Judge: One AI evaluates another AI. Fast and scalable.
Used in modern systems. Can be biased. Still very practical.

______
