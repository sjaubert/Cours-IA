**The Perfect Prompt: A Prompt Engineering Cheat Sheet**

Aug-12th, 2024: Updated, new resources added.

[![Maximilian Vogel](media/image1.png){width="0.3333333333333333in"
height="0.3333333333333333in"}](https://medium.com/@maximilian.vogel?source=post_page---byline--d0b9c62a2bba---------------------------------------)

[Maximilian
Vogel](https://medium.com/@maximilian.vogel?source=post_page---byline--d0b9c62a2bba---------------------------------------)

Following

7 min read

·

Apr 8, 2024

4.3K

50

Large language models **can produce any sequence of characters**.
Literally any. In any idiom, data format or programming language.

And at **very different levels of quality**.

It can be one of those typically lukewarm model responses with lots of
caveats, long-winded explanations, or half-hallucinated knowledge from
the day before yesterday.

Or the first section of a best-selling novel, a proposal for a perfect
brand name, the most powerful and elegant Python function for a tricky
problem.

Or even more, more and more of that: When you are **building an
application**, the model can reliably and accurately answer millions of
questions from your customers, fully process insurance claims or
stubbornly rummage every day through the freshly filed patent filings in
search of conflicts with older ones.

There is one if - and this is a big if:** This works only, if you
specify your wish in a perfect prompt**.

And that doesn't just mean you have to avoid using ambiguous
instructions like all these guys wasting the three wishes. No, it is
much harder. To realize the full potential of our AI fairies and
genies, **you need to craft your prompts masterfully and meticulously**.

When you are using models for everyday chores, this engineering work may
be helpful.

If you are **building applications** with AI, **it is a must**.

Our Prompt Engineering Cheat Sheet is a condensed (PDF) book of spells
for this somewhat arcane and often tricky discipline of machine
learning.

Whether you're a seasoned user or just starting your AI journey, this
cheat sheet should serve as a **pocket dictionary** for many areas of
communication with large language models.

The contents:

- the **AUTOMAT** and the **CO-STAR** framework

- **output format** definition

- **few-shot learning**

- **chain of thought**

- prompt **templates**

- **RAG**, retrieval augmented generation

- **formatting and delimiters **and

- the **multi-prompt** approach.

Here are** [all example prompts easily to copy, adapt and
use](https://www.linkedin.com/pulse/perfect-prompt-engineering-cheat-sheet-snippets-part-vogel-mxkcf/)** for
yourself (external link, LinkedIn) and here is a handy [**PDF version of
the cheat
sheet**](https://big-picture.com/media/the_prompt_engineering_cheat_sheet.pdf) (external
link, BP) to take with you.

**The AUTOMAT Framework**

The AUTOMAT Framework describes the key ingredients of a perfect prompt
instruction: What you need, how to write it.

**And how not to write it**.

Press enter or click to view image in full size

![](media/image2.png){width="6.018055555555556in" height="9.725in"}

The Prompt Engineering Cheat Sheet: The AUTOMAT Framework (image credit:
Maximilian Vogel)

The acronym** AUTOMAT **stands for

**A**ct as a ...

**U**ser Persona & Audience

**T**argeted Action

**O**utput Definition

**M**ode / Tonality / Style

**A**typical Cases

**T**opic Whitelisting

By considering each element, you can guide the LLM towards the desired
outcome. Imagine you're writing a script for a chatbot. You define its
role (A), who it's interacting with (U), the goal of the interaction
(T), what information it should provide (O), how it should communicate
(M), how to handle edge cases (A), and what topics are relevant (T).
This structure ensures clear, consistent communication for your LLM.

Press enter or click to view image in full size

![](media/image3.png){width="6.3in" height="2.4069444444444446in"}

AUTOMAT Framework: An Example (image credit: Maximilian Vogel)

**The CO-STAR Framework**

A similar approach, but setting the focus a little bit differently:

- **Context:** Set the scene! Provide background details for the LLM to
  understand the situation.

- **Objective:** What do you want to achieve? Clearly define the task
  for focused results.

- **Style & Tone:** Dress it up! Specify the desired writing style and
  emotional tone for your LLM's response.

- **Audience:** Know your reader. Identify who you're targeting to
  tailor the LLM's output.

- **Response:** Pick your format. Define the output format (text, code,
  etc.) for the LLM's response.

Press enter or click to view image in full size

![](media/image4.png){width="6.3in" height="5.472222222222222in"}

The Prompt Engineering Cheat Sheet: The CO-STAR framework,
see [details](https://towardsdatascience.com/how-i-won-singapores-gpt-4-prompt-engineering-competition-34c195a93d41#10b2) by
Sheila Teo (image credit: Maximilian Vogel)

**Output Format**

The definition of the output format tells the model **how to provide the
response**. Even better than telling is showing. Provide a real-life
example of an output.

The model can mimic almost every conceivable output, any existing
format, as well as the structures you define for a specific task.
Providing an answer in an easy-to-parse format like JSON greatly
simplifies building applications and autonomous AI workers.

Press enter or click to view image in full size

![](media/image5.png){width="6.3in" height="4.378472222222222in"}

Prompt engineering: Output format (image credit: Maximilian Vogel)

Further structure the output by

- specifying **allowed values** and ranges for the AI's response

- instruct the AI what to do if **data is unavailable, if values are
  missing**

Press enter or click to view image in full size

![](media/image6.png){width="6.3in" height="3.6791666666666667in"}

The Prompt Engineering Cheat Sheet: Output format (image credit:
Maximilian Vogel)

**Few-Shot Learning**

Few-shot learning in prompts shows the model a few practical problems
and solutions before it starts with the real job:

- **Standard cases**: Weave a few examples of how the model should map
  input to output

- **Special cases**: Show the model how to answer edge cases or
  outliers. How should it answer, if data is missing, if off-topic
  questions are asked, or if a user goes rogue.

Press enter or click to view image in full size

![](media/image7.png){width="6.3in" height="5.808333333333334in"}

The Prompt Engineering Cheat Sheet: Few shot learning (image credit:
Maximilian Vogel)

**Chain of thought**

If we force the model to** think aloud** and to make some considerations
and reasoning before it gives the final answer, the results will get
better.\
\
Here, our AI is not all different from 6th graders solving math
problems. Or, let's say, humans in general.

Not my idea, by the way, but that of the [Google Brain
Team](https://arxiv.org/abs/2201.11903).

To filter the reasoning from the answer, again, use JSON in the output.

Press enter or click to view image in full size

![](media/image8.png){width="6.3in" height="5.241666666666666in"}

The Prompt Engineering Cheat Sheet: Chain of thought (image credit:
Maximilian Vogel)

**Prompt Templates**

When building AI applications, you will almost never use a **constant
prompt**.

You will use a template containing variables that are set depending on
the situation: Specific user questions, document chunks, API outputs,
the current time, content from the internet, etc.

Press enter or click to view image in full size

![](media/image9.png){width="6.3in" height="2.942361111111111in"}

The Prompt Engineering Cheat Sheet: Prompt templates (image credit:
Maximilian Vogel)

In each step or invocation of the template, the variables are then
replaced by actual content.

Press enter or click to view image in full size

![](media/image10.png){width="6.3in" height="3.2631944444444443in"}

The Prompt Engineering Cheat Sheet: Prompt templates (image credit:
Maximilian Vogel)

**RAG --- Retrieval augmented generation**

RAG is maybe the most important technique developed in the field of LLMs
in the last two years. This technique lets LLMs access your data or
documents to answer a question --- overcoming limitations like knowledge
cutoff in the pre-training data. RAG allows us to tap into an extremely
broad base of content, comprising megabytes and gigabytes of data,
leading to more comprehensive and up-to-date responses from LLMs.

Press enter or click to view image in full size

![](media/image11.png){width="6.3in" height="4.983333333333333in"}

The Prompt Engineering Cheat Sheet: Retrieval augmented generation
(RAG) - a step-by-step introduction (image credit: Maximilian Vogel)

**Formatting and delimiters**

Models don't read your prompt twice.

Either they understand at once what purpose a piece of information
serves - is it an example, an instruction, or is it context information?

Or they don\'t. Then their response will be probably wrong.

So, **make sure that the model can grasp the structure of your prompt**.
Unlike the privileged authors of Medium stories, you are limited to
characters only; you cannot use graphic highlighting such as headings,
bold, or italics. When structuring the individual sections, make friends
with hashes, quotation marks and line breaks.

Press enter or click to view image in full size

![](media/image12.png){width="6.3in" height="3.786111111111111in"}

The Prompt Engineering Cheat Sheet: Formatting and delimiters (image
credit: Maximilian Vogel)

**Assemble the parts**

Here is a real-world example of how to put it all together. I am using
the components of a prompt and the delimiters we discussed above to give
the prompt a structure. Regarding the order of appearance, start with
the core instruction, then examples, data, the output format and finally
the interaction history.

**And yes, prompts with examples and context information can get quite
long.** That's why the model providers are opening ever
increasing *context windows *for a single *inference --- *in AI lingo,
this is the maximum length of input for one answer generation by the
model.

Press enter or click to view image in full size

![](media/image13.png){width="6.3in" height="6.961805555555555in"}

The Prompt Engineering Cheat Sheet: Components of a complex prompt
(image credit: Maximilian Vogel)

**Multi-Prompt Approach**

When building a complex application like an autonomous AI worker
handling insurance claims, one prompt is often not enough. You could
build a single prompt categorizing a claim, checking the coverage,
considering the insurance policy of the customer, and calculating the
reimbursement value.

But this is not the best approach. It is both easier and returns more
accurate responses to split the prompt into smaller single task prompts
and build chains of model requests. Usually, you categorize input data
first and then select a specific chain which processes the data with
models and deterministic functions.

Press enter or click to view image in full size

![](media/image14.png){width="6.45625in" height="3.654413823272091in"}

The Prompt Engineering Cheat Sheet: Multi-prompt approach (image credit:
Maximilian Vogel)
