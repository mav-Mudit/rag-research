# V1 Baseline Evaluation Results

These results were generated using the fixed V1 configuration and evaluation questions.

## Question 1

**Question:** What problem does Retrieval-Augmented Generation aim to address, and why can a language model's parametric knowledge be insufficient?

### Retrieved Sources

**Source 1:** Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks, page 1

> Retrieval-Augmented Generation for
Knowledge-Intensive NLP Tasks
Patrick Lewis†‡, Ethan Perez⋆,
Aleksandra Piktus†, Fabio Petroni†, Vladimir Karpukhin†, Naman Goyal†, Heinrich Küttler†,
Mike Lewis†, Wen-tau Yih†, Tim Rocktäschel†‡, Sebastian Riedel†‡, Douwe Kiela†
†Facebook AI Research;‡University College London;⋆New York University;
plewis@fb.com
Abstract
Large pre-trained language models have been shown to store factual knowledge
in their parameters, and achieve state-of-the-art results when ﬁne-tuned on down-
stream NLP tasks. However, their ability to access and precisely manipulate knowl-
edge is still limited, and hence on knowledge-intensive tasks, their performance
lags behind task-speciﬁc architectures. Additionally, providing provenance for their
decisions and updating their world knowledge remain open research problems. Pre-
trained models with a differentiable access mechanism to explicit non-parametric
memory have so far been only investigated for extractive downstream tasks. We
explore a general-purpose ﬁne-tuning recipe for retrieval-augmented generation
(RAG) — models which combine pre-trained parametric and non-parametric mem-
ory for language generation. We introduce RAG models where the parametric
memory is a pre-trained seq2seq model and the non-parametric memory is a dense
vector index of Wikipedia, accessed with a pre-trained neural retriever. We com-
pare two RAG formulations, one which conditions on the same retrieved passages

**Source 2:** Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks, page 2

> a general-purpose ﬁne-tuning approach which we refer to as retrieval-augmented generation (RAG).
We build RAG models where the parametric memory is a pre-trained seq2seq transformer, and the
non-parametric memory is a dense vector index of Wikipedia, accessed with a pre-trained neural
retriever. We combine these components in a probabilistic model trained end-to-end (Fig. 1). The
retriever (Dense Passage Retriever [26], henceforth DPR) provides latent documents conditioned on
the input, and the seq2seq model (BART [32]) then conditions on these latent documents together with
the input to generate the output. We marginalize the latent documents with a top-K approximation,
either on a per-output basis (assuming the same document is responsible for all tokens) or a per-token
basis (where different documents are responsible for different tokens). Like T5 [51] or BART, RAG
can be ﬁne-tuned on any seq2seq task, whereby both the generator and retriever are jointly learned.
There has been extensive previous work proposing architectures to enrich systems with non-parametric
memory which are trained from scratch for speciﬁc tasks, e.g. memory networks [ 64, 55], stack-
augmented networks [25] and memory layers [ 30]. In contrast, we explore a setting where both
parametric and non-parametric memory components are pre-trained and pre-loaded with extensive
knowledge. Crucially, by using pre-trained access mechanisms, the ability to access knowledge is
present without additional training.

**Source 3:** Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks, page 1

> vector index of Wikipedia, accessed with a pre-trained neural retriever. We com-
pare two RAG formulations, one which conditions on the same retrieved passages
across the whole generated sequence, and another which can use different passages
per token. We ﬁne-tune and evaluate our models on a wide range of knowledge-
intensive NLP tasks and set the state of the art on three open domain QA tasks,
outperforming parametric seq2seq models and task-speciﬁc retrieve-and-extract
architectures. For language generation tasks, we ﬁnd that RAG models generate
more speciﬁc, diverse and factual language than a state-of-the-art parametric-only
seq2seq baseline.
1 Introduction
Pre-trained neural language models have been shown to learn a substantial amount of in-depth knowl-
edge from data [47]. They can do so without any access to an external memory, as a parameterized
implicit knowledge base [51, 52]. While this development is exciting, such models do have down-
sides: They cannot easily expand or revise their memory, can’t straightforwardly provide insight into
their predictions, and may produce “hallucinations” [38]. Hybrid models that combine parametric
memory with non-parametric (i.e., retrieval-based) memories [20, 26, 48] can address some of these
issues because knowledge can be directly revised and expanded, and accessed knowledge can be
inspected and interpreted. REALM [ 20] and ORQA [ 31], two recently introduced models that

### Generated Answer

Retrieval-Augmented Generation (RAG) aims to solve the shortcomings of pre-trained language models on knowledge-intensive tasks by giving them differentiable access to an explicit (non‑parametric) memory — e.g., a retrievable text index — so generated outputs can condition on retrieved documents, be more factual, and provide inspectable provenance and updatable knowledge [Source 1], [Source 2].

A language model’s parametric knowledge can be insufficient because, although it stores substantial factual information in its weights, it has limited ability to access and precisely manipulate that knowledge; it is hard to inspect or update, it can “hallucinate,” and its performance on knowledge‑intensive tasks can lag behind retrieve‑and‑extract architectures or task‑specific models [Source 1], [Source 3].

---

## Question 2

**Question:** How does RAG combine parametric and non-parametric memory during generation?

### Retrieved Sources

**Source 1:** Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks, page 2

> a general-purpose ﬁne-tuning approach which we refer to as retrieval-augmented generation (RAG).
We build RAG models where the parametric memory is a pre-trained seq2seq transformer, and the
non-parametric memory is a dense vector index of Wikipedia, accessed with a pre-trained neural
retriever. We combine these components in a probabilistic model trained end-to-end (Fig. 1). The
retriever (Dense Passage Retriever [26], henceforth DPR) provides latent documents conditioned on
the input, and the seq2seq model (BART [32]) then conditions on these latent documents together with
the input to generate the output. We marginalize the latent documents with a top-K approximation,
either on a per-output basis (assuming the same document is responsible for all tokens) or a per-token
basis (where different documents are responsible for different tokens). Like T5 [51] or BART, RAG
can be ﬁne-tuned on any seq2seq task, whereby both the generator and retriever are jointly learned.
There has been extensive previous work proposing architectures to enrich systems with non-parametric
memory which are trained from scratch for speciﬁc tasks, e.g. memory networks [ 64, 55], stack-
augmented networks [25] and memory layers [ 30]. In contrast, we explore a setting where both
parametric and non-parametric memory components are pre-trained and pre-loaded with extensive
knowledge. Crucially, by using pre-trained access mechanisms, the ability to access knowledge is
present without additional training.

**Source 2:** Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks, page 1

> Retrieval-Augmented Generation for
Knowledge-Intensive NLP Tasks
Patrick Lewis†‡, Ethan Perez⋆,
Aleksandra Piktus†, Fabio Petroni†, Vladimir Karpukhin†, Naman Goyal†, Heinrich Küttler†,
Mike Lewis†, Wen-tau Yih†, Tim Rocktäschel†‡, Sebastian Riedel†‡, Douwe Kiela†
†Facebook AI Research;‡University College London;⋆New York University;
plewis@fb.com
Abstract
Large pre-trained language models have been shown to store factual knowledge
in their parameters, and achieve state-of-the-art results when ﬁne-tuned on down-
stream NLP tasks. However, their ability to access and precisely manipulate knowl-
edge is still limited, and hence on knowledge-intensive tasks, their performance
lags behind task-speciﬁc architectures. Additionally, providing provenance for their
decisions and updating their world knowledge remain open research problems. Pre-
trained models with a differentiable access mechanism to explicit non-parametric
memory have so far been only investigated for extractive downstream tasks. We
explore a general-purpose ﬁne-tuning recipe for retrieval-augmented generation
(RAG) — models which combine pre-trained parametric and non-parametric mem-
ory for language generation. We introduce RAG models where the parametric
memory is a pre-trained seq2seq model and the non-parametric memory is a dense
vector index of Wikipedia, accessed with a pre-trained neural retriever. We com-
pare two RAG formulations, one which conditions on the same retrieved passages

**Source 3:** Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks, page 9

> to provide a ﬁnal output. These approaches have proved successful in a number of domains including
Machine Translation [ 18, 22] and Semantic Parsing [21]. Our approach does have several differences,
including less of emphasis on lightly editing a retrieved item, but on aggregating content from several
pieces of retrieved content, as well as learning latent retrieval, and retrieving evidence documents
rather than related training pairs. This said, RAG techniques may work well in these settings, and
could represent promising future work.
6 Discussion
In this work, we presented hybrid generation models with access to parametric and non-parametric
memory. We showed that our RAG models obtain state of the art results on open-domain QA. We
found that people prefer RAG’s generation over purely parametric BART, ﬁnding RAG more factual
and speciﬁc. We conducted an thorough investigation of the learned retrieval component, validating
its effectiveness, and we illustrated how the retrieval index can be hot-swapped to update the model
without requiring any retraining. In future work, it may be fruitful to investigate if the two components
can be jointly pre-trained from scratch, either with a denoising objective similar to BART or some
another objective. Our work opens up new research directions on how parametric and non-parametric
memories interact and how to most effectively combine them, showing promise in being applied to a
wide variety of NLP tasks.
9

### Generated Answer

RAG pairs a parametric seq2seq generator (a pre‑trained model like BART) with a non‑parametric dense vector index (Wikipedia) accessed by a neural retriever (DPR). The retriever returns latent documents z conditioned on the input x, and the seq2seq generator conditions on those retrieved documents together with x to produce the output y. The model treats the retrieved documents probabilistically and marginalizes over a top‑K set of documents (using either a per‑output or per‑token top‑K approximation), and the retriever and generator can be fine‑tuned jointly end‑to‑end. RAG therefore aggregates content from several retrieved pieces of evidence while leveraging the generator’s parametric memory to produce the final text [Source 2], [Source 1].

---

## Question 3

**Question:** How does RAG differ from a traditional language model that relies only on its parameters, particularly when dealing with knowledge-intensive tasks?

### Retrieved Sources

**Source 1:** Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks, page 1

> Retrieval-Augmented Generation for
Knowledge-Intensive NLP Tasks
Patrick Lewis†‡, Ethan Perez⋆,
Aleksandra Piktus†, Fabio Petroni†, Vladimir Karpukhin†, Naman Goyal†, Heinrich Küttler†,
Mike Lewis†, Wen-tau Yih†, Tim Rocktäschel†‡, Sebastian Riedel†‡, Douwe Kiela†
†Facebook AI Research;‡University College London;⋆New York University;
plewis@fb.com
Abstract
Large pre-trained language models have been shown to store factual knowledge
in their parameters, and achieve state-of-the-art results when ﬁne-tuned on down-
stream NLP tasks. However, their ability to access and precisely manipulate knowl-
edge is still limited, and hence on knowledge-intensive tasks, their performance
lags behind task-speciﬁc architectures. Additionally, providing provenance for their
decisions and updating their world knowledge remain open research problems. Pre-
trained models with a differentiable access mechanism to explicit non-parametric
memory have so far been only investigated for extractive downstream tasks. We
explore a general-purpose ﬁne-tuning recipe for retrieval-augmented generation
(RAG) — models which combine pre-trained parametric and non-parametric mem-
ory for language generation. We introduce RAG models where the parametric
memory is a pre-trained seq2seq model and the non-parametric memory is a dense
vector index of Wikipedia, accessed with a pre-trained neural retriever. We com-
pare two RAG formulations, one which conditions on the same retrieved passages

**Source 2:** Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks, page 9

> to provide a ﬁnal output. These approaches have proved successful in a number of domains including
Machine Translation [ 18, 22] and Semantic Parsing [21]. Our approach does have several differences,
including less of emphasis on lightly editing a retrieved item, but on aggregating content from several
pieces of retrieved content, as well as learning latent retrieval, and retrieving evidence documents
rather than related training pairs. This said, RAG techniques may work well in these settings, and
could represent promising future work.
6 Discussion
In this work, we presented hybrid generation models with access to parametric and non-parametric
memory. We showed that our RAG models obtain state of the art results on open-domain QA. We
found that people prefer RAG’s generation over purely parametric BART, ﬁnding RAG more factual
and speciﬁc. We conducted an thorough investigation of the learned retrieval component, validating
its effectiveness, and we illustrated how the retrieval index can be hot-swapped to update the model
without requiring any retraining. In future work, it may be fruitful to investigate if the two components
can be jointly pre-trained from scratch, either with a denoising objective similar to BART or some
another objective. Our work opens up new research directions on how parametric and non-parametric
memories interact and how to most effectively combine them, showing promise in being applied to a
wide variety of NLP tasks.
9

**Source 3:** Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks, page 2

> knowledge. Crucially, by using pre-trained access mechanisms, the ability to access knowledge is
present without additional training.
Our results highlight the beneﬁts of combining parametric and non-parametric memory with genera-
tion for knowledge-intensive tasks—tasks that humans could not reasonably be expected to perform
without access to an external knowledge source. Our RAG models achieve state-of-the-art results
on open Natural Questions [29], WebQuestions [3] and CuratedTrec [2] and strongly outperform
recent approaches that use specialised pre-training objectives on TriviaQA [24]. Despite these being
extractive tasks, we ﬁnd that unconstrained generation outperforms previous extractive approaches.
For knowledge-intensive generation, we experiment with MS-MARCO [1] and Jeopardy question
generation, and we ﬁnd that our models generate responses that are more factual, speciﬁc, and
diverse than a BART baseline. For FEVER [56] fact veriﬁcation, we achieve results within 4.3% of
state-of-the-art pipeline models which use strong retrieval supervision. Finally, we demonstrate that
the non-parametric memory can be replaced to update the models’ knowledge as the world changes.1
2 Methods
We explore RAG models, which use the input sequencex to retrieve text documentsz and use them
as additional context when generating the target sequence y. As shown in Figure 1, our models
leverage two components: (i) a retriever pη(z|x) with parametersη that returns (top-K truncated)

### Generated Answer

Short answer: RAG augments a parametric language model with a non‑parametric retrieval component, so it consults an external memory of retrieved passages at generation time rather than relying only on knowledge stored in model weights [Source 1].

Key differences and consequences (from the provided context)
- External, inspectable memory: RAG retrieves passages (e.g., from a Wikipedia vector index) that can be inspected and updated, so knowledge can be revised or swapped at test time without retraining the model [Source 1], [Source 3].
- Better for knowledge‑intensive generation and QA: RAG sets state‑of‑the‑art on multiple open‑domain QA tasks and outperforms parametric seq2seq baselines on such tasks [Source 1].
- Generates more factual, specific and diverse text: RAG’s generations are reported as more factual, specific and diverse than a parametric-only baseline (e.g., BART) and can produce free‑form abstractive answers beyond simple extractive QA [Source 1], [Source 2], [Source 3].
- Learned/differentiable retrieval matters: training the retriever (rather than freezing it or replacing it with a fixed BM25 retriever) improves performance, and differentiable retrieval is especially important for open‑domain QA [Source 3].
- Flexible retrieval strategies: RAG can be formulated to condition on the same retrieved passages for a whole output or to use different passages per token, giving architectural flexibility [Source 1].

If you need, I can summarize how these differences show up on a specific task (e.g., open‑domain QA or MSMARCO NLG) using the cited results.

---

## Question 4

**Question:** What are the main differences between RAG-Sequence and RAG-Token, and how do they affect the documents used during generation?

### Retrieved Sources

**Source 1:** Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks, page 3

> byθ that generates a current token based on a context of the previousi− 1 tokensy1:i−1, the original
inputx and a retrieved passagez.
To train the retriever and generator end-to-end, we treat the retrieved document as a latent variable.
We propose two models that marginalize over the latent documents in different ways to produce a
distribution over generated text. In one approach, RAG-Sequence, the model uses the same document
to predict each target token. The second approach, RAG-Token, can predict each target token based
on a different document. In the following, we formally introduce both models and then describe the
pη andpθ components, as well as the training and decoding procedure.
2.1 Models
RAG-Sequence Model The RAG-Sequence model uses the same retrieved document to generate
the complete sequence. Technically, it treats the retrieved document as a single latent variable that
is marginalized to get the seq2seq probability p(y|x) via a top-K approximation. Concretely, the
top K documents are retrieved using the retriever, and the generator produces the output sequence
probability for each document, which are then marginalized,
pRAG-Sequence(y|x) ≈
∑
z∈top-k(p(·|x))
pη(z|x)pθ(y|x,z ) =
∑
z∈top-k(p(·|x))
pη(z|x)
N∏
i
pθ(yi|x,z,y 1:i−1)
RAG-Token Model In the RAG-Token model we can draw a different latent document for each
target token and marginalize accordingly. This allows the generator to choose content from several

**Source 2:** Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks, page 8

> indices is low (12% with the 2018 index and 2016 leaders, 4% with the 2016 index and 2018 leaders).
This shows we can update RAG’s world knowledge by simply replacing its non-parametric memory.
Effect of Retrieving more documents Models are trained with either 5 or 10 retrieved latent
documents, and we do not observe signiﬁcant differences in performance between them. We have the
ﬂexibility to adjust the number of retrieved documents at test time, which can affect performance and
runtime. Figure 3 (left) shows that retrieving more documents at test time monotonically improves
Open-domain QA results for RAG-Sequence, but performance peaks for RAG-Token at 10 retrieved
documents. Figure 3 (right) shows that retrieving more documents leads to higher Rouge-L for
RAG-Token at the expense of Bleu-1, but the effect is less pronounced for RAG-Sequence.
10 20 30 40 50
KR e t r i e v e dD o c s
39
40
41
42
43
44NQ Exact Match RAG-Tok
RAG-Seq
10 20 30 40 50
KR e t r i e v e dD o c s
40
50
60
70
80NQ Answer Recall @ K
RAG-Tok
RAG-Seq
Fixed DPR
BM25
10 20 30 40 50
KR e t r i e v e dD o c s
48
50
52
54
56Bleu-1 / Rouge-L score
RAG-Tok R-L
RAG-Tok B-1
RAG-Seq R-L
RAG-Seq B-1
Figure 3: Left: NQ performance as more documents are retrieved. Center: Retrieval recall perfor-
mance in NQ. Right: MS-MARCO Bleu-1 and Rouge-L as more documents are retrieved.
5 Related Work
Single-Task Retrieval Prior work has shown that retrieval improves performance across a variety of

**Source 3:** BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding, page 14

> • Learning rate (Adam): 5e-5, 3e-5, 2e-5
• Number of epochs: 2, 3, 4
We also observed that large data sets (e.g.,
100k+ labeled training examples) were far less
sensitive to hyperparameter choice than small data
sets. Fine-tuning is typically very fast, so it is rea-
sonable to simply run an exhaustive search over
the above parameters and choose the model that
performs best on the development set.
A.4 Comparison of BERT, ELMo ,and
OpenAI GPT
Here we studies the differences in recent popular
representation learning models including ELMo,
OpenAI GPT and BERT. The comparisons be-
tween the model architectures are shown visually
in Figure 3. Note that in addition to the architec-
ture differences, BERT and OpenAI GPT are ﬁne-
tuning approaches, while ELMo is a feature-based
approach.
The most comparable existing pre-training
method to BERT is OpenAI GPT, which trains a
left-to-right Transformer LM on a large text cor-
pus. In fact, many of the design decisions in BERT
were intentionally made to make it as close to
GPT as possible so that the two methods could be
minimally compared. The core argument of this
work is that the bi-directionality and the two pre-
training tasks presented in Section 3.1 account for
the majority of the empirical improvements, but
we do note that there are several other differences
between how BERT and GPT were trained:
• GPT is trained on the BooksCorpus (800M
words); BERT is trained on the BooksCor-
pus (800M words) and Wikipedia (2,500M
words).

### Generated Answer

- RAG-Sequence treats the retrieved document as a single latent variable for the whole output: the top‑K documents are retrieved, the generator computes the probability of the entire output conditioned on each document, and these sequence-level probabilities are marginalized (i.e., one document is used to generate all tokens of a given sequence) [Source 1].

- RAG-Token treats the latent document per token: for each next token the generator produces a distribution conditioned on each retrieved document and marginalizes over documents token-by-token, which allows the model to pull content from different documents across the output sequence [Source 2].

Effects on documents used during generation:
- RAG-Sequence uses one chosen retrieved document to condition every token of the generated sequence (though the model marginalizes over the top‑K documents at generation time) [Source 1].
- RAG-Token can effectively mix information from multiple retrieved documents by selecting (via marginalization) potentially different documents for different output tokens, enabling the generator to combine content from several documents in a single answer [Source 2].

(For a target sequence of length one—e.g., sequence classification—the two approaches are equivalent.) [Source 2]

Additional note: RAG-Sequence tends to produce more diverse generations than RAG-Token in the experiments reported [Source 3].

---

## Question 5

**Question:** How does GPT-3 demonstrate that large language models can perform tasks from natural-language descriptions and a few examples without gradient-based updates?

### Retrieved Sources

**Source 1:** Chain-of-Thought Prompting Elicits Reasoning in Large Language Models, page 2

> tasks, given a prompt that consists of triples:⟨input, chain of thought, output⟩. A chain of thought is
a series of intermediate natural language reasoning steps that lead to the ﬁnal output, and we refer to
this approach as chain-of-thought prompting. An example prompt is shown in Figure 1.
We present empirical evaluations on arithmetic, commonsense, and symbolic reasoning benchmarks,
showing that chain-of-thought prompting outperforms standard prompting, sometimes to a striking
degree. Figure 2 illustrates one such result—on the GSM8K benchmark of math word problems
(Cobbe et al., 2021), chain-of-thought prompting with PaLM 540B outperforms standard prompting
by a large margin and achieves new state-of-the-art performance. A prompting only approach is
important because it does not require a large training dataset and because a single model checkpoint
can perform many tasks without loss of generality. This work underscores how large language models
can learn via a few examples with natural language data about the task (c.f. automatically learning
the patterns underlying inputs and outputs via a large training dataset).
2 Chain-of-Thought Prompting
Consider one’s own thought process when solving a complicated reasoning task such as a multi-step
math word problem. It is typical to decompose the problem into intermediate steps and solve each
before giving the ﬁnal answer: “After Jane gives 2 ﬂowers to her mom she has 10... then after she

**Source 2:** Language Models are Few-Shot Learners, page 1

> Language Models are Few-Shot Learners
Tom B. Brown∗ Benjamin Mann∗ Nick Ryder∗ Melanie Subbiah∗
Jared Kaplan† Prafulla Dhariwal Arvind Neelakantan Pranav Shyam Girish Sastry
Amanda Askell Sandhini Agarwal Ariel Herbert-Voss Gretchen Krueger Tom Henighan
Rewon Child Aditya Ramesh Daniel M. Ziegler Jeffrey Wu Clemens Winter
Christopher Hesse Mark Chen Eric Sigler Mateusz Litwin Scott Gray
Benjamin Chess Jack Clark Christopher Berner
Sam McCandlish Alec Radford Ilya Sutskever Dario Amodei
OpenAI
Abstract
Recent work has demonstrated substantial gains on many NLP tasks and benchmarks by pre-training
on a large corpus of text followed by ﬁne-tuning on a speciﬁc task. While typically task-agnostic
in architecture, this method still requires task-speciﬁc ﬁne-tuning datasets of thousands or tens of
thousands of examples. By contrast, humans can generally perform a new language task from only
a few examples or from simple instructions – something which current NLP systems still largely
struggle to do. Here we show that scaling up language models greatly improves task-agnostic,
few-shot performance, sometimes even reaching competitiveness with prior state-of-the-art ﬁne-
tuning approaches. Speciﬁcally, we train GPT-3, an autoregressive language model with 175 billion
parameters, 10x more than any previous non-sparse language model, and test its performance in
the few-shot setting. For all tasks, GPT-3 is applied without any gradient updates or ﬁne-tuning,

**Source 3:** Chain-of-Thought Prompting Elicits Reasoning in Large Language Models, page 1

> Chain-of-Thought Prompting Elicits Reasoning
in Large Language Models
Jason Wei Xuezhi Wang Dale Schuurmans Maarten Bosma
Brian Ichter Fei Xia Ed H. Chi Quoc V . Le Denny Zhou
Google Research, Brain Team
{jasonwei,dennyzhou}@google.com
Abstract
We explore how generating a chain of thought—a series of intermediate reasoning
steps—signiﬁcantly improves the ability of large language models to perform
complex reasoning. In particular, we show how such reasoning abilities emerge
naturally in sufﬁciently large language models via a simple method called chain-of-
thought prompting, where a few chain of thought demonstrations are provided as
exemplars in prompting.
Experiments on three large language models show that chain-of-thought prompting
improves performance on a range of arithmetic, commonsense, and symbolic
reasoning tasks. The empirical gains can be striking. For instance, prompting a
PaLM 540B with just eight chain-of-thought exemplars achieves state-of-the-art
accuracy on the GSM8K benchmark of math word problems, surpassing even
ﬁnetuned GPT-3 with a veriﬁer.
A: The cafeteria had 23 apples originally. They used 
20 to make lunch. So they had 23 - 20 = 3. They 
bought 6 more apples, so they have 3 + 6 = 9. The 
answer is 9.
Chain-of-Thought Prompting
Q: Roger has 5 tennis balls. He buys 2 more cans of 
tennis balls. Each can has 3 tennis balls. How many 
tennis balls does he have now? 
A: The answer is 11. 
Q: The cafeteria had 23 apples. If they used 20 to

### Generated Answer

GPT-3 shows that very large autoregressive language models can do tasks from natural‑language instructions plus a few exemplars by using in‑context learning rather than parameter updates. The authors trained a 175‑billion‑parameter model and evaluated it in zero‑, one‑, and few‑shot settings; crucially, GPT‑3 was "applied without any gradient updates or fine‑tuning" and yet achieved strong performance on many NLP tasks, in some cases approaching prior fine‑tuned state of the art [Source 1][Source 2]. This scaling effect—bigger models improving task‑agnostic few‑shot performance—demonstrates that providing natural‑language descriptions and a few examples in the model input is sufficient for many tasks without gradient‑based learning [Source 1][Source 2].

---

## Question 6

**Question:** How does T5's text-to-text formulation allow the same model and training framework to be applied to different NLP tasks?

### Retrieved Sources

**Source 1:** Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer, page 41

> 4. Reflection
Having completed our systematic study, we wrap up by first recapping some of our most
significant findings. Our results provide some high-level perspective on which avenues of
research might be more or less promising. To conclude, we outline some topics we think
might provide effective approaches for further progressing the field.
4.1 Takeaways
Text-to-text Our text-to-text framework provides a simple way to train a single model
on a wide variety of text tasks using the same loss function and decoding procedure.
We showed how this approach can be successfully applied to generative tasks like
abstractive summarization, classification tasks like natural language inference, and
even regression tasks like STS-B. In spite of its simplicity, we found the text-to-
text framework obtained comparable performance to task-specific architectures and
ultimately produced state-of-the-art results when combined with scale.
Architectures While some work on transfer learning for NLP has considered architectural
variants of the Transformer, we found the original encoder-decoder form worked
best in our text-to-text framework. Though an encoder-decoder model uses twice as
many parameters as “encoder-only” (e.g. BERT) or “decoder-only” (language model)
architectures, it has a similar computational cost. We also showed that sharing the
parameters in the encoder and decoder did not result in a substantial performance
drop while halving the total parameter count.
41

**Source 2:** Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer, page 2

> data sets (Yang et al., 2019; Liu et al., 2019c; Zellers et al., 2019), benchmarks (Wang et al.,
2019b, 2018; Conneau and Kiela, 2018), fine-tuning methods (Howard and Ruder, 2018;
Houlsby et al., 2019; Peters et al., 2019), and more. The rapid rate of progress and diversity
of techniques in this burgeoning field can make it difficult to compare different algorithms,
tease apart the effects of new contributions, and understand the space of existing methods for
transfer learning. Motivated by a need for more rigorous understanding, we leverage a unified
approach to transfer learning that allows us to systematically study different approaches
and push the current limits of the field.
The basic idea underlying our work is to treat every text processing problem as a
“text-to-text” problem, i.e. taking text as input and producing new text as output. This
approach is inspired by previous unifying frameworks for NLP tasks, including casting all text
problems as question answering (McCann et al., 2018), language modeling (Radford et al.,
2019), or span extraction Keskar et al. (2019b) tasks. Crucially, the text-to-text framework
allows us to directly apply the same model, objective, training procedure, and decoding
process to every task we consider. We leverage this flexibility by evaluating performance
on a wide variety of English-based NLP problems, including question answering, document
2. http://commoncrawl.org
2

**Source 3:** Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer, page 9

> Exploring the Limits of Transfer Learning
examples is shown in Figure 1. We provide full examples of preprocessed inputs for every
task we studied in Appendix D.
Our text-to-text framework follows previous work that casts multiple NLP tasks into
a common format: McCann et al. (2018) propose the “Natural Language Decathlon”, a
benchmark that uses a consistent question-answering format for a suite of ten NLP tasks.
The Natural Language Decathlon also stipulates that all models must be multi-task, i.e.
are able to simultaneously tackle all of the tasks at once. We instead allow for separately
fine-tuning the model on each individual task and use short task prefixes instead of an explicit
question-answer format. Radford et al. (2019) evaluate the zero-shot learning capabilities of
language models by feeding some input to the model as a prefix and then autoregressively
sampling an output. For example, automatic summarization is done by feeding in a document
followed by the text “TL;DR:” (short for “too long, didn’t read”, a common abbreviation)
and then the summary is predicted via autoregressive decoding. We mainly consider models
that explicitly process an input with an encoder before generating an output with a separate
decoder and we focus on transfer learning rather than zero-shot learning. Finally, Keskar
et al. (2019b) unify many NLP tasks as “span extraction”, where text corresponding to

### Generated Answer

T5 casts every NLP problem as "text in → text out" (e.g., "translate: ...", "summarize: ...", "cola sentence: ..."), so each task is presented as feeding the model some input text and training it to generate the desired output text. Because every task shares the same input/output format, the authors can use a single Transformer model architecture and apply the same loss function, objective, training procedure, hyperparameters, and decoding process across all tasks—letting one unified model and training framework handle translation, QA, classification, summarization, etc. [Source 3][Source 2][Source 1].

---

## Question 7

**Question:** Why does LoRA argue that the changes required when adapting a large language model have low intrinsic rank, and how does its approach exploit this observation?

### Retrieved Sources

**Source 1:** LoRA: Low-Rank Adaptation of Large Language Models, page 4

> (2020) shows that the pre-trained language models have a low “instrisic dimension” and can still
learn efﬁciently despite a random projection to a smaller subspace. Inspired by this, we hypothe-
size the updates to the weights also have a low “intrinsic rank” during adaptation. For a pre-trained
weight matrix W0∈ Rd×k, we constrain its update by representing the latter with a low-rank de-
compositionW0 + ∆W =W0 +BA, whereB∈ Rd×r,A∈ Rr×k, and the rank r≪ min(d,k ).
During training,W0 is frozen and does not receive gradient updates, whileA andB contain trainable
parameters. Note both W0 and ∆W =BA are multiplied with the same input, and their respective
output vectors are summed coordinate-wise. Forh =W0x, our modiﬁed forward pass yields:
h =W0x + ∆Wx =W0x +BAx (3)
We illustrate our reparametrization in Figure 1. We use a random Gaussian initialization for A and
zero forB, so ∆W =BA is zero at the beginning of training. We then scale ∆Wx by α
r , whereα
is a constant inr. When optimizing with Adam, tuningα is roughly the same as tuning the learning
rate if we scale the initialization appropriately. As a result, we simply set α to the ﬁrst r we try
and do not tune it. This scaling helps to reduce the need to retune hyperparameters when we vary
r (Yang & Hu, 2021).
A Generalization of Full Fine-tuning. A more general form of ﬁne-tuning allows the training of
a subset of the pre-trained parameters. LoRA takes a step further and does not require the accumu-

**Source 2:** LoRA: Low-Rank Adaptation of Large Language Models, page 4

> A Generalization of Full Fine-tuning. A more general form of ﬁne-tuning allows the training of
a subset of the pre-trained parameters. LoRA takes a step further and does not require the accumu-
lated gradient update to weight matrices to have full-rank during adaptation. This means that when
applying LoRA to all weight matrices and training all biases 2, we roughly recover the expressive-
ness of full ﬁne-tuning by setting the LoRA rankr to the rank of the pre-trained weight matrices. In
other words, as we increase the number of trainable parameters 3, training LoRA roughly converges
to training the original model, while adapter-based methods converges to an MLP and preﬁx-based
methods to a model that cannot take long input sequences.
No Additional Inference Latency. When deployed in production, we can explicitly compute and
store W = W0 +BA and perform inference as usual. Note that both W0 and BA are in Rd×k.
When we need to switch to another downstream task, we can recover W0 by subtracting BA and
then adding a different B′A′, a quick operation with very little memory overhead. Critically, this
2They represent a negligible number of parameters compared to weights.
3An inevitability when adapting to hard tasks.
4

**Source 3:** LoRA: Low-Rank Adaptation of Large Language Models, page 10

> Table 6 shows that, surprisingly, LoRA already performs competitively with a very small r (more
so for{Wq,Wv} than just Wq). This suggests the update matrix ∆W could have a very small
“intrinsic rank”.6 To further support this ﬁnding, we check the overlap of the subspaces learned by
different choices of r and by different random seeds. We argue that increasing r does not cover a
more meaningful subspace, which suggests that a low-rank adaptation matrix is sufﬁcient.
6However, we do not expect a small r to work for every task or dataset. Consider the following thought
experiment: if the downstream task were in a different language than the one used for pre-training, retraining
the entire model (similar to LoRA withr =dmodel) could certainly outperform LoRA with a smallr.
10

### Generated Answer

Why they think the adaptation has low intrinsic rank
- Prior work shows overparameterized pretrained models live on a low‑dimensional manifold, so the authors hypothesize the change in weights during adaptation (ΔW) also has a low “intrinsic rank” rather than requiring full-rank updates [Source 2].  
- Empirically, LoRA finds very small ranks (e.g., r = 1 or 2 for GPT‑3 175B despite a full dimension of 12,288) are sufficient in practice, and subspace-overlap analyses show increasing r does not recover qualitatively new directions—supporting the claim that ΔW is low‑rank for many tasks [Source 2], [Source 3].

How LoRA exploits that observation
- Instead of fine‑tuning all weights, LoRA freezes the pretrained model and injects small trainable low‑rank decomposition matrices (the A and B matrices) that parameterize the weight update ΔW (i.e., a low‑rank factorization of the change) and trains only those matrices [Source 1], [Source 2].  
- This lets LoRA match or beat full fine‑tuning while using far fewer trainable parameters (up to ~10,000× reduction in reported examples), reducing GPU memory and avoiding extra inference latency; it also enables cheap task switching by swapping small LoRA modules [Source 1], [Source 2].  
- (Caveat noted by the authors: very different downstream tasks—e.g., a new language—may require larger r or full fine‑tuning) [Source 3].

---

## Question 8

**Question:** How does ReAct combine reasoning and acting, and why does this provide an advantage over approaches that perform reasoning without interacting with external environments?

### Retrieved Sources

**Source 1:** ReAct: Synergizing Reasoning and Acting in Language Models, page 3

> and diagnosability across all domains, as humans can readily distinguish information from model’s
internal knowledge versus external environments, as well as inspect reasoning traces to understand
the decision basis of model actions.
To summarize, our key contributions are the following: (1) we introduce ReAct, a novel prompt-
based paradigm to synergize reasoning and acting in language models for general task solving; (2) we
perform extensive experiments across diverse benchmarks to showcase the advantage of ReAct in a
few-shot learning setup over prior approaches that perform either reasoning or action generation in
isolation; (3) we present systematic ablations and analysis to understand the importance of acting in
reasoning tasks, and reasoning in interactive tasks; (4) we analyze the limitations ofReAct under the
prompting setup (i.e. limited support of reasoning and acting behaviors), and perform initial ﬁnetuning
experiments showing the potential of ReAct to improve with additional training data. Scaling up
ReAct to train and operate on more tasks and combining it with complementary paradigms like
reinforcement learning could further unlock the potential of large language models.
2 REAC T: S YNERGIZING REASONING + AC TING
Consider a general setup of an agent interacting with an environment for task solving. At time
stept, an agent receives an observationot∈O from the environment and takes an actionat∈A

**Source 2:** ReAct: Synergizing Reasoning and Acting in Language Models, page 2

> 2022). However, this “chain-of-thought” reasoning is a static black box, in that the model uses
its own internal representations to generate thoughts and is not grounded in the external world,
which limits its ability to reason reactively or update its knowledge. This can lead to issues like fact
hallucination and error propagation over the reasoning process (Figure 1 (1b)). On the other hand,
recent work has explored the use of pre-trained language models for planning and acting in interactive
environments (Ahn et al., 2022; Nakano et al., 2021; Yao et al., 2020; Huang et al., 2022a), with
a focus on predicting actions via language priors. These approaches usually convert multi-modal
observations into text, use a language model to generate domain-speciﬁc actions or plans, and then
use a controller to choose or execute them. However, they do not employ language models to reason
abstractly about high-level goals or maintain a working memory to support acting, barring Huang
et al. (2022b) who perform a limited form of verbal reasoning to reiterate spatial facts about the
current state. Beyond such simple embodied tasks to interact with a few blocks, there have not been
studies on how reasoning and acting can be combined in a synergistic manner for general task solving,
and if such a combination can bring systematic beneﬁts compared to reasoning or acting alone.
In this work, we present ReAct, a general paradigm to combine reasoning and acting with language

**Source 3:** ReAct: Synergizing Reasoning and Acting in Language Models, page 4

> D) Human aligned and controllable: ReAct promises an interpretable sequential decision making
and reasoning process where humans can easily inspect reasoning and factual correctness. Moreover,
humans can also control or correct the agent behavior on the go by thought editing, as shown in
Figure 5 in Section 4.
3 K NOWLEDGE -I NTENSIVE REASONING TASKS
We begin with knowledge-intensive reasoning tasks like multi-hop question answering and fact
veriﬁcation. As shown in Figure 1(1d), by interacting with a Wikipedia API, ReAct is able to
retrieve information to support reasoning, while also use reasoning to target what to retrieve next,
demonstrating a synergy of reasoning and acting.
3.1 S ETUP
Domains We consider two datasets challenging knowledge retrieval and reasoning: (1) Hot-
PotQA (Yang et al., 2018), a multi-hop question answering benchmark that requires reasoning
over two or more Wikipedia passages, and (2) FEVER (Thorne et al., 2018), a fact veriﬁcation
benchmark where each claim is annotated SUPPORTS, REFUTES, or NOT ENOUGH INFO, based
on if there exists a Wikipedia passage to verify the claim. In this work, we operate in a question-only
setup for both tasks, where models only receive the question/claim as input without access to support
paragraphs, and have to rely on their internal knowledge or retrieve knowledge via interacting with
an external environment to support reasoning.
Action Space We design a simple Wikipedia web API with three types of actions to support

### Generated Answer

ReAct interleaves verbal reasoning traces and environment actions: the LLM is prompted to both "think" (produce explicit reasoning) and "act" (issue environment queries or commands) in an ongoing loop. This lets the agent "reason to act" (use reasoning to create, maintain, and adjust high-level plans) and "act to reason" (query external sources and fold returned observations back into its reasoning) [Source 1].

That coupling gives several concrete advantages over reasoning-only approaches. By interacting with the environment, ReAct can incorporate fresh external information into its reasoning, support dynamic plan adjustment, and perform commonsense goal decomposition that purely reaction-driven or purely internal approaches miss. Empirically, an IM-style (environment-feedback-only) prompting ablation underperforms ReAct (71% vs. 53% overall success) and tended to fail at recognizing subgoal completion and locating items due to lack of high-level decomposition and commonsense reasoning—shortcomings ReAct addresses by combining internal reasoning with actions [Source 2]. ReAct also improves diagnosability (humans can distinguish internal knowledge from external observations and inspect reasoning traces) and shows advantages in few-shot settings compared to methods that do reasoning or acting in isolation [Source 3].

---

## Question 9

**Question:** What does Chain-of-Thought prompting reveal about the relationship between model scale, intermediate reasoning steps, and performance on complex reasoning tasks?

### Retrieved Sources

**Source 1:** Chain-of-Thought Prompting Elicits Reasoning in Large Language Models, page 1

> Chain-of-Thought Prompting Elicits Reasoning
in Large Language Models
Jason Wei Xuezhi Wang Dale Schuurmans Maarten Bosma
Brian Ichter Fei Xia Ed H. Chi Quoc V . Le Denny Zhou
Google Research, Brain Team
{jasonwei,dennyzhou}@google.com
Abstract
We explore how generating a chain of thought—a series of intermediate reasoning
steps—signiﬁcantly improves the ability of large language models to perform
complex reasoning. In particular, we show how such reasoning abilities emerge
naturally in sufﬁciently large language models via a simple method called chain-of-
thought prompting, where a few chain of thought demonstrations are provided as
exemplars in prompting.
Experiments on three large language models show that chain-of-thought prompting
improves performance on a range of arithmetic, commonsense, and symbolic
reasoning tasks. The empirical gains can be striking. For instance, prompting a
PaLM 540B with just eight chain-of-thought exemplars achieves state-of-the-art
accuracy on the GSM8K benchmark of math word problems, surpassing even
ﬁnetuned GPT-3 with a veriﬁer.
A: The cafeteria had 23 apples originally. They used 
20 to make lunch. So they had 23 - 20 = 3. They 
bought 6 more apples, so they have 3 + 6 = 9. The 
answer is 9.
Chain-of-Thought Prompting
Q: Roger has 5 tennis balls. He buys 2 more cans of 
tennis balls. Each can has 3 tennis balls. How many 
tennis balls does he have now? 
A: The answer is 11. 
Q: The cafeteria had 23 apples. If they used 20 to

**Source 2:** Chain-of-Thought Prompting Elicits Reasoning in Large Language Models, page 2

> tasks, given a prompt that consists of triples:⟨input, chain of thought, output⟩. A chain of thought is
a series of intermediate natural language reasoning steps that lead to the ﬁnal output, and we refer to
this approach as chain-of-thought prompting. An example prompt is shown in Figure 1.
We present empirical evaluations on arithmetic, commonsense, and symbolic reasoning benchmarks,
showing that chain-of-thought prompting outperforms standard prompting, sometimes to a striking
degree. Figure 2 illustrates one such result—on the GSM8K benchmark of math word problems
(Cobbe et al., 2021), chain-of-thought prompting with PaLM 540B outperforms standard prompting
by a large margin and achieves new state-of-the-art performance. A prompting only approach is
important because it does not require a large training dataset and because a single model checkpoint
can perform many tasks without loss of generality. This work underscores how large language models
can learn via a few examples with natural language data about the task (c.f. automatically learning
the patterns underlying inputs and outputs via a large training dataset).
2 Chain-of-Thought Prompting
Consider one’s own thought process when solving a complicated reasoning task such as a multi-step
math word problem. It is typical to decompose the problem into intermediate steps and solve each
before giving the ﬁnal answer: “After Jane gives 2 ﬂowers to her mom she has 10... then after she

**Source 3:** Chain-of-Thought Prompting Elicits Reasoning in Large Language Models, page 19

> multi-step reasoning, (2) a large language model is used, and (3) the scaling curve is relatively ﬂat.
Conversely, the beneﬁts are smaller when one or more of these conditions are not met.
These intuitions are perhaps supported by the arithmetic reasoning results. The performance gain
from chain-of-thought prompting is largest for PaLM 540B on GSM8K (challenging multi-step
problems, ﬂat scaling curve), which meets these conditions. The performance gain is small for the
subsets of MAWPS that only require one or two steps (SingleOP, SingleEq, and AddSub), for which
PaLM 540B already achieves performance of 90% or higher (and it is also generally true that there is
less headroom for improvement when performance is already strong).
Although in this paper we focused on multi-step reasoning tasks (arithmetic, commonsense, and
symbolic), chain-of-thought prompting can potentially be applied to any task for which humans use a
“chain of thought” to solve (at least in principle). We leave the empirical evaluation of chain-of-thought
prompting on such diverse tasks (e.g., machine translation, etc.) to future work.
A.4 Why is prompting with the equation only not enough for some arithmetic reasoning
datasets?
Prompting with the equation only as an intermediate step does help on many datasets, especially when
the datasets only require a few reasoning steps (SV AMP, ASDiv, MAWPS). For GSM8K, however,

### Generated Answer

Chain-of-Thought prompting shows that the ability to produce intermediate reasoning steps—and benefit from them—is an emergent property of model scale. When models are sufficiently large, prompting them to generate chains of thought yields much better performance on complex arithmetic, symbolic, and commonsense reasoning tasks (it turns otherwise flat scaling curves into dramatically increasing ones) and even helps out‑of‑distribution generalization (e.g., to longer sequences) [Source 1], [Source 3]. However, this benefit appears only above a certain scale: chain‑of‑thought prompting often hurts performance for many models smaller than ~10B parameters, and scaling up (e.g., to hundreds of billions) fixes large fractions of errors such as semantic misunderstandings and missing a reasoning step [Source 2]. A caveat is that producing human‑like intermediate steps does not by itself prove the model is “reasoning” in a cognitive sense [Source 1].

---

## Question 10

**Question:** What limitations of RAG are identified by the authors, and how do these limitations affect the reliability or usefulness of the generated answers?

### Retrieved Sources

**Source 1:** Language Models are Few-Shot Learners, page 26

> at∼ 52% (see Table 3.11).5 Human abilities to detect model generated text appear to decrease as model size increases:
there appears to be a trend towards chance accuracy with model size, and human detection of GPT-3 is close to chance.6
This is true despite the fact that participants spend more time on each output as model size increases (see Appendix E).
Examples of synthetic articles from GPT-3 are given in Figures 3.14 and 3.15.7 Much of the text is—as indicated by the
evaluations—difﬁcult for humans to distinguish from authentic human content. Factual inaccuracies can be an indicator
that an article is model generated since, unlike human authors, the models have no access to the speciﬁc facts that the
article titles refer to or when the article was written. Other indicators include repetition, non sequiturs, and unusual
phrasings, though these are often subtle enough that they are not noticed.
Related work on language model detection by Ippolito et al. [IDCBE19] indicates that automatic discriminators like
G R O V E R[ZHR+19] and GLTR [GSR19] may have greater success at detecting model generated text than human
evaluators. Automatic detection of these models may be a promising area of future research.
Ippolito et al. [IDCBE19] also note that human accuracy at detecting model generated text increases as humans observe
more tokens. To do a preliminary investigation of how good humans are at detecting longer news articles generated

**Source 2:** Chain-of-Thought Prompting Elicits Reasoning in Large Language Models, page 15

> Checklist
1. For all authors...
(a) Do the main claims made in the abstract and introduction accurately reﬂect the paper’s
contributions and scope? [Yes]
(b) Did you describe the limitations of your work? [Yes] See Section 6 and Appendix A.2.
(c) Did you discuss any potential negative societal impacts of your work? [Yes] We don’t
expect negative societal impacts as a direct result of the contributions in our paper. One
consideration, however, is that generated chain of thought is not always factual, which
is noted as a limitation in Appendix D.1 (and note that we do not suggest using such
chains of thought in a factual manner or in any real-world scenario).
(d) Have you read the ethics review guidelines and ensured that your paper conforms to
them? [Yes]
2. If you are including theoretical results...
(a) Did you state the full set of assumptions of all theoretical results? [N/A]
(b) Did you include complete proofs of all theoretical results? [N/A]
3. If you ran experiments...
(a) Did you include the code, data, and instructions needed to reproduce the main experi-
mental results (either in the supplemental material or as a URL)? [Yes] We included
inputs, outputs, and targets for LaMDA and GPT-3 in the supplementary material.
Although we use proprietary models, we GPT-3 results are fully reproducible. Repro-
ducibility is further discussed in Appendix E.1.
(b) Did you specify all the training details (e.g., data splits, hyperparameters, how they

**Source 3:** Language Models are Few-Shot Learners, page 36

> 6.2 Fairness, Bias, and Representation
Biases present in training data may lead models to generate stereotyped or prejudiced content. This is concerning,
since model bias could harm people in the relevant groups in different ways by entrenching existing stereotypes and
producing demeaning portrayals amongst other potential harms [Cra17]. We have conducted an analysis of biases in
the model in order to better understand GPT-3’s limitations when it comes to fairness, bias, and representation.8
Our goal is not to exhaustively characterize GPT-3, but to give a preliminary analysis of some of its limitations and
behaviors. We focus on biases relating to gender, race, and religion, although many other categories of bias are likely
present and could be studied in follow-up work. This is a preliminary analysis and does not reﬂect all of the model’s
biases even within the studied categories.
Broadly, our analysis indicates that internet-trained models have internet-scale biases; models tend to reﬂect stereotypes
present in their training data. Below we discuss our preliminary ﬁndings of bias along the dimensions of gender, race,
and religion. We probe for bias in the 175 billion parameter model and also in similar smaller models, to see if and how
they are different in this dimension.
6.2.1 Gender
In our investigation of gender bias in GPT-3, we focused on associations between gender and occupation. We found

### Generated Answer

Summary of limitations the authors identify, and how each affects reliability/usefulness:

- Dependence on gold (relevant) passages for some questions. The authors note their results are "impressive given that (i) those models access gold passages with specific information required to generate the reference answer" and that "many questions are unanswerable without the gold passages" — i.e., if retrieval does not surface the needed passages the model cannot produce the correct answer [Source 1]. Effect: answers are only reliable when the retriever finds the right evidence; retrieval failure makes generated answers untrustworthy or unanswerable.

- Coverage limits of the underlying corpus. The authors point out "not all questions are answerable from Wikipedia alone" [Source 1]. Effect: if the knowledge source used for retrieval lacks the needed facts, RAG cannot produce correct answers, reducing usefulness for topics outside the corpus.

- Remaining hallucination and factual errors (albeit reduced). The authors report RAG "hallucinates less and generate[s] factually correct text more often than BART," which implies hallucination is still possible even if reduced [Source 1]. Effect: some generated answers may still be incorrect or fabricated, so outputs should be verified.

- Model-variant limitations in combining evidence across documents. The paper contrasts RAG-Token and RAG-Sequence, noting RAG-Token performs better and may do so because it can combine content from several documents; by implication some variants (e.g., RAG-Sequence) are less able to integrate multiple retrieved passages effectively [Source 1]. Effect: certain model variants may produce less complete or less accurate answers when the correct response must synthesize information from multiple sources.

If you need a more exhaustive list of failure modes (e.g., specific hallucination types, retrieval error rates), the provided context does not include those detailed diagnostics.

---

