# ReRanker Evaluation Results


## Question 1

**Question:** What problem does Retrieval-Augmented Generation aim to address, and why can a language model's parametric knowledge be insufficient?

### Retrieved Sources

**Source 1:** Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks, page 1

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

**Source 3:** Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks, page 2

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

### Generated Answer

Retrieval-Augmented Generation (RAG) addresses the problem of performing knowledge-intensive NLP tasks when a model needs reliable, up-to-date, and inspectable factual knowledge. It does this by giving a generative model differentiable access to explicit, non‑parametric memory (e.g., a retrieval index of documents) to condition generation on retrieved texts rather than only on what is stored in its parameters [Source 1], [Source 2].

A language model’s parametric knowledge can be insufficient because, although large pre‑trained models store substantial facts in their weights, they have limited ability to access and precisely manipulate that knowledge, can’t easily be updated or provide provenance for predictions, and may “hallucinate” or produce incorrect facts. RAG remedies these limitations by combining parametric and non‑parametric memory so knowledge can be inspected, revised, and used directly at generation time [Source 1], [Source 3].

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

**Source 2:** Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks, page 2

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

**Source 3:** Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks, page 6

> best because it can generate responses that combine content from several documents. Figure 2 shows
an example. When generating “Sun”, the posterior is high for document 2 which mentions “The
Sun Also Rises”. Similarly, document 1 dominates the posterior when “A Farewell to Arms” is
generated. Intriguingly, after the ﬁrst token of each book is generated, the document posterior ﬂattens.
This observation suggests that the generator can complete the titles without depending on speciﬁc
documents. In other words, the model’s parametric knowledge is sufﬁcient to complete the titles. We
ﬁnd evidence for this hypothesis by feeding the BART-only baseline with the partial decoding "The
Sun. BART completes the generation "The Sun Also Rises" is a novel by this author of "The Sun
Also Rises" indicating the title "The Sun Also Rises" is stored in BART’s parameters. Similarly,
BART will complete the partial decoding "The Sun Also Rises" is a novel by this author of "A
with "The Sun Also Rises" is a novel by this author of "A Farewell to Arms". This example shows
how parametric and non-parametric memories work together—the non-parametric component helps
to guide the generation, drawing out speciﬁc knowledge stored in the parametric memory.
4.4 Fact Veriﬁcation
Table 2 shows our results on FEVER. For 3-way classiﬁcation, RAG scores are within 4.3% of
state-of-the-art models, which are complex pipeline systems with domain-speciﬁc architectures and

### Generated Answer

RAG pairs a parametric seq2seq transformer (BART) with a non‑parametric dense-vector index accessed by a neural retriever (DPR): the retriever pη(z|x) returns top‑K latent documents z for an input x, and the generator conditions on x plus those retrieved documents to produce the output [Source 2]. The model is formulated probabilistically and marginalizes over the retrieved documents with a top‑K approximation — either assuming one document explains the whole output (per‑output) or allowing different documents to be responsible for different tokens (per‑token) [Source 2]. Practically, RAG aggregates content from several retrieved pieces (rather than lightly editing a single retrieval), and the retriever and generator can be fine‑tuned end‑to‑end; the retrieval index can also be swapped to update knowledge without retraining the generator [Source 1][Source 2][Source 3].

---

## Question 3

**Question:** How does RAG differ from a traditional language model that relies only on its parameters, particularly when dealing with knowledge-intensive tasks?

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

**Source 3:** Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks, page 1

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

### Generated Answer

Short answer: RAG augments a parametric language model with a retrieval-based (non‑parametric) memory, so it retrieves and conditions on external passages at generation time instead of relying only on stored parameters. This makes its knowledge inspectable and updateable, and improves factuality, specificity, diversity and task performance on knowledge‑intensive tasks compared to parametric‑only models [Source 1, Source 3].

Key differences (from the provided context)
- Hybrid retrieval + generation: RAG combines a seq2seq generator with a neural retriever over an external index (e.g., Wikipedia) and can condition generation on retrieved passages (even per token), rather than producing text solely from learned parameters [Source 1].  
- Updateable, inspectable knowledge: Because RAG uses non‑parametric memory, the external index can be revised or swapped at test time (index hot‑swapping), and retrieved evidence can be inspected—unlike purely parametric models whose knowledge is locked in weights and requires retraining to change [Source 1, Source 3].  
- Better for knowledge‑intensive generation: RAG yields more factual, specific and diverse outputs than parametric seq2seq baselines (e.g., BART), and its retrieval component (especially a learned/differentiable retriever) measurably improves performance on open‑domain QA and other knowledge‑intensive tasks [Source 2, Source 3].  
- Reduced reliance on memorization: By retrieving relevant passages, RAG mitigates issues of hallucination and limited ability to expand or revise memory that affect models relying only on parameters [Source 1]. 

If you want, I can summarize specific experimental results from the paper showing the gains on open‑domain QA and NLG tasks.

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

**Source 2:** Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks, page 3

> RAG-Token Model In the RAG-Token model we can draw a different latent document for each
target token and marginalize accordingly. This allows the generator to choose content from several
documents when producing an answer. Concretely, the top K documents are retrieved using the
retriever, and then the generator produces a distribution for the next output token for each document,
before marginalizing, and repeating the process with the following output token, Formally, we deﬁne:
pRAG-Token(y|x) ≈
N∏
i
∑
z∈top-k(p(·|x))
pη(z|x)pθ(yi|x,z,y 1:i−1)
Finally, we note that RAG can be used for sequence classiﬁcation tasks by considering the target class
as a target sequence of length one, in which case RAG-Sequence and RAG-Token are equivalent.
2.2 Retriever: DPR
The retrieval componentpη(z|x) is based on DPR [26]. DPR follows a bi-encoder architecture:
pη(z|x)∝ exp
(
d(z)⊤q(x)
)
d(z) = BERTd(z), q(x) = BERTq(x)
where d(z) is a dense representation of a document produced by a BERTBASE document encoder [8],
and q(x) a query representation produced by a query encoder, also based on BERTBASE. Calculating
top-k(pη(·|x)), the list ofk documentsz with highest prior probabilitypη(z|x), is a Maximum Inner
Product Search (MIPS) problem, which can be approximately solved in sub-linear time [23]. We use
a pre-trained bi-encoder from DPR to initialize our retriever and to build the document index. This

**Source 3:** Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks, page 4

> minimize the negative marginal log-likelihood of each target,∑
j− logp(yj|xj) using stochastic
gradient descent with Adam [28]. Updating the document encoder BERTd during training is costly as
it requires the document index to be periodically updated as REALM does during pre-training [20].
We do not ﬁnd this step necessary for strong performance, and keep the document encoder (and
index) ﬁxed, only ﬁne-tuning the query encoder BERTq and the BART generator.
2.5 Decoding
At test time, RAG-Sequence and RAG-Token require different ways to approximatearg maxyp(y|x).
RAG-Token The RAG-Token model can be seen as a standard, autoregressive seq2seq genera-
tor with transition probability: p′
θ(yi|x,y 1:i−1) = ∑
z∈top-k(p(·|x))pη(zi|x)pθ(yi|x,zi,y 1:i−1) To
decode, we can plugp′
θ(yi|x,y 1:i−1) into a standard beam decoder.
RAG-Sequence For RAG-Sequence, the likelihoodp(y|x) does not break into a conventional per-
token likelihood, hence we cannot solve it with a single beam search. Instead, we run beam search for
each documentz, scoring each hypothesis usingpθ(yi|x,z,y 1:i−1). This yields a set of hypotheses
Y , some of which may not have appeared in the beams of all documents. To estimate the probability
of an hypothesis y we run an additional forward pass for each document z for which y does not
appear in the beam, multiply generator probability withpη(z|x) and then sum the probabilities across

### Generated Answer

- Latent-document granularity:
  - RAG-Sequence treats the retrieved document as a single latent variable for the whole output sequence — one document z is used to generate every token of y for that hypothesis, and the model marginalizes over the top-K retrieved documents at the sequence level [Source 1].
  - RAG-Token treats the latent document per token — for each output token the model marginalizes over the top-K documents, so different tokens can be generated conditioned on different documents [Source 2].

- How this affects which documents are used during generation:
  - RAG-Sequence picks (implicitly, via marginalization) one retrieved document to condition the entire generated sequence; each sequence hypothesis comes from a single document at a time [Source 1].
  - RAG-Token can mix information from multiple retrieved documents across the tokens of a single generated sequence, because the generator marginalizes over documents independently for each next-token prediction [Source 2].

- Additional notes:
  - For target sequences of length one the two approaches are equivalent (a single-token case) [Source 2].
  - Empirically, RAG-Sequence’s generations are reported to be more diverse than RAG-Token’s (and both are more diverse than a BART baseline) [Source 3].

---

## Question 5

**Question:** How does GPT-3 demonstrate that large language models can perform tasks from natural-language descriptions and a few examples without gradient-based updates?

### Retrieved Sources

**Source 1:** Language Models are Few-Shot Learners, page 1

> parameters, 10x more than any previous non-sparse language model, and test its performance in
the few-shot setting. For all tasks, GPT-3 is applied without any gradient updates or ﬁne-tuning,
with tasks and few-shot demonstrations speciﬁed purely via text interaction with the model. GPT-3
achieves strong performance on many NLP datasets, including translation, question-answering, and
cloze tasks, as well as several tasks that require on-the-ﬂy reasoning or domain adaptation, such as
unscrambling words, using a novel word in a sentence, or performing 3-digit arithmetic. At the same
time, we also identify some datasets where GPT-3’s few-shot learning still struggles, as well as some
datasets where GPT-3 faces methodological issues related to training on large web corpora. Finally,
we ﬁnd that GPT-3 can generate samples of news articles which human evaluators have difﬁculty
distinguishing from articles written by humans. We discuss broader societal impacts of this ﬁnding
and of GPT-3 in general.
∗Equal contribution
†Johns Hopkins University, OpenAI
Author contributions listed at end of paper.
arXiv:2005.14165v4  [cs.CL]  22 Jul 2020

**Source 2:** Language Models are Few-Shot Learners, page 5

> remove extraneous symbols from a word. Model performance improves with the addition of a natural language task
description, and with the number of examples in the model’s context,K. Few-shot learning also improves dramatically
with model size. Though the results in this case are particularly striking, the general trends with both model size and
number of examples in-context hold for most tasks we study. We emphasize that these “learning” curves involve no
gradient updates or ﬁne-tuning, just increasing numbers of demonstrations given as conditioning.
Broadly, on NLP tasks GPT-3 achieves promising results in the zero-shot and one-shot settings, and in the the few-shot
setting is sometimes competitive with or even occasionally surpasses state-of-the-art (despite state-of-the-art being held
by ﬁne-tuned models). For example, GPT-3 achieves 81.5 F1 on CoQA in the zero-shot setting, 84.0 F1 on CoQA in
the one-shot setting, 85.0 F1 in the few-shot setting. Similarly, GPT-3 achieves 64.3% accuracy on TriviaQA in the
zero-shot setting, 68.0% in the one-shot setting, and 71.2% in the few-shot setting, the last of which is state-of-the-art
relative to ﬁne-tuned models operating in the same closed-book setting.
GPT-3 also displays one-shot and few-shot proﬁciency at tasks designed to test rapid adaption or on-the-ﬂy reasoning,
which include unscrambling words, performing arithmetic, and using novel words in a sentence after seeing them

**Source 3:** Language Models are Few-Shot Learners, page 1

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

### Generated Answer

GPT-3 (an autoregressive language model with 175 billion parameters) is evaluated in zero‑, one‑, and few‑shot settings by giving it a natural‑language task description and a small number of examples as part of the input (i.e., in‑context examples) and then asking it to complete the task—without any gradient updates or fine‑tuning. This setup yields strong task performance, in some cases nearly matching prior fine‑tuned state‑of‑the‑art models, demonstrating that scaling enables task‑agnostic few‑shot learning from natural‑language prompts alone [Source 1][Source 2].

---

## Question 6

**Question:** How does T5's text-to-text formulation allow the same model and training framework to be applied to different NLP tasks?

### Retrieved Sources

**Source 1:** Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer, page 3

> Exploring the Limits of Transfer Learning
"translate English to German: That is good."
"cola sentence: The 
course is jumping well."
"summarize: state authorities 
dispatched emergency crews tuesday to 
survey the damage after an onslaught 
of severe weather in mississippi…"
"stsb sentence1: The rhino grazed 
on the grass. sentence2: A rhino 
is grazing in a field."
T5
"Das ist gut."
"not acceptable"
"six people hospitalized after 
a storm in attala county."
"3.8"
Figure 1: A diagram of our text-to-text framework. Every task we consider—including
translation, question answering, and classification—is cast as feeding our model
text as input and training it to generate some target text. This allows us to use the
same model, loss function, hyperparameters, etc. across our diverse set of tasks. It
also provides a standard testbed for the methods included in our empirical survey.
“T5” refers to our model, which we dub the “Text-to-Text Transfer Transformer”.
summarization, and sentiment classification, to name a few. With this unified approach,
we can compare the effectiveness of different transfer learning objectives, unlabeled data
sets, and other factors, while exploring the limits of transfer learning for NLP by scaling up
models and data sets beyond what has previously been considered.
We emphasize that our goal is not to propose new methods but instead to provide a
comprehensive perspective on where the field stands. As such, our work primarily comprises

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

**Source 3:** Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer, page 41

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

### Generated Answer

T5 casts every NLP problem as “text in → text out” (e.g., prefixing the input with a task prompt like "translate English to German:" or "summarize:" and training the model to generate the desired target text). Because inputs and targets are always plain text, the same Transformer model, loss, objective, training procedure, decoding process, and even hyperparameters can be used across tasks (translation, QA, classification, summarization, etc.) without task-specific architectures or heads [Source 2], [Source 3]. This unified text-to-text framing therefore enables a single, consistent training and evaluation framework for diverse NLP tasks [Source 3].

---

## Question 7

**Question:** Why does LoRA argue that the changes required when adapting a large language model have low intrinsic rank, and how does its approach exploit this observation?

### Retrieved Sources

**Source 1:** LoRA: Low-Rank Adaptation of Large Language Models, page 2

> often introduce inference latency (Houlsby et al., 2019; Rebufﬁ et al., 2017) by extending model
depth or reduce the model’s usable sequence length (Li & Liang, 2021; Lester et al., 2021; Ham-
bardzumyan et al., 2020; Liu et al., 2021) (Section 3). More importantly, these method often fail to
match the ﬁne-tuning baselines, posing a trade-off between efﬁciency and model quality.
We take inspiration from Li et al. (2018a); Aghajanyan et al. (2020) which show that the learned
over-parametrized models in fact reside on a low intrinsic dimension. We hypothesize that the
change in weights during model adaptation also has a low “intrinsic rank”, leading to our proposed
Low-Rank Adaptation (LoRA) approach. LoRA allows us to train some dense layers in a neural
network indirectly by optimizing rank decomposition matrices of the dense layers’ change during
adaptation instead, while keeping the pre-trained weights frozen, as shown in Figure 1. Using GPT-3
175B as an example, we show that a very low rank (i.e.,r in Figure 1 can be one or two) sufﬁces even
when the full rank (i.e., d) is as high as 12,288, making LoRA both storage- and compute-efﬁcient.
LoRA possesses several key advantages.
• A pre-trained model can be shared and used to build many small LoRA modules for dif-
ferent tasks. We can freeze the shared model and efﬁciently switch tasks by replacing the
matricesA andB in Figure 1, reducing the storage requirement and task-switching over-
head signiﬁcantly.

**Source 2:** LoRA: Low-Rank Adaptation of Large Language Models, page 10

> Table 6 shows that, surprisingly, LoRA already performs competitively with a very small r (more
so for{Wq,Wv} than just Wq). This suggests the update matrix ∆W could have a very small
“intrinsic rank”.6 To further support this ﬁnding, we check the overlap of the subspaces learned by
different choices of r and by different random seeds. We argue that increasing r does not cover a
more meaningful subspace, which suggests that a low-rank adaptation matrix is sufﬁcient.
6However, we do not expect a small r to work for every task or dataset. Consider the following thought
experiment: if the downstream task were in a different language than the one used for pre-training, retraining
the entire model (similar to LoRA withr =dmodel) could certainly outperform LoRA with a smallr.
10

**Source 3:** LoRA: Low-Rank Adaptation of Large Language Models, page 12

> the 48th layer of GPT-3.
We draw several conclusions from Table 7. First, ∆W has a stronger correlation withW compared
to a random matrix, indicating that ∆W ampliﬁes some features that are already in W . Second,
instead of repeating the top singular directions of W , ∆W only ampliﬁes directions that are not
emphasized in W . Third, the ampliﬁcation factor is rather huge: 21.5≈ 6.91/0.32 for r = 4 .
See Section H.4 for whyr = 64 has a smaller ampliﬁcation factor. We also provide a visualization
in Section H.3 for how the correlation changes as we include more top singular directions fromWq.
This suggests that the low-rank adaptation matrix potentially ampliﬁes the important features for
speciﬁc downstream tasks that were learned but not emphasized in the general pre-training model.
8 C ONCLUSION AND FUTURE WORK
Fine-tuning enormous language models is prohibitively expensive in terms of the hardware required
and the storage/switching cost for hosting independent instances for different tasks. We propose
LoRA, an efﬁcient adaptation strategy that neither introduces inference latency nor reduces input
sequence length while retaining high model quality. Importantly, it allows for quick task-switching
when deployed as a service by sharing the vast majority of the model parameters. While we focused
on Transformer language models, the proposed principles are generally applicable to any neural
networks with dense layers.

### Generated Answer

Why LoRA thinks adaptation updates are low-rank
- Prior work shows over-parameterized pretrained models lie on a low intrinsic dimension; LoRA extends this idea to the change in weights during adaptation and hypothesizes that the weight update matrix ΔW has a low “intrinsic rank” (i.e., can be well-approximated by a low-rank matrix) [Source 2].  
- Empirically, LoRA finds that very small ranks (r = 1 or 2) suffice even when the full layer dimensionality is very large (e.g., d = 12,288), and that subspaces learned with different r or random seeds overlap—supporting the claim that ΔW is effectively low-rank [Source 3].

How LoRA exploits that observation
- Instead of fine-tuning all weights, LoRA freezes the pretrained weights and models the required weight change as a low-rank decomposition: it injects trainable low-rank matrices (A and B) into each Transformer layer so that the effective update is A·B (a low-rank ΔW) while the original weights remain fixed [Source 1], [Source 2].  
- This lets LoRA train far fewer parameters, reduce GPU memory and storage, and keep inference cost unchanged (no added depth or latency), while matching or improving fine-tuning quality in practice because the small low-rank modules capture the task-specific update subspace [Source 1], [Source 2], [Source 3].

---

## Question 8

**Question:** How does ReAct combine reasoning and acting, and why does this provide an advantage over approaches that perform reasoning without interacting with external environments?

### Retrieved Sources

**Source 1:** ReAct: Synergizing Reasoning and Acting in Language Models, page 3

> Consider a general setup of an agent interacting with an environment for task solving. At time
stept, an agent receives an observationot∈O from the environment and takes an actionat∈A
following some policyπ(at|ct), wherect = (o1,a 1,··· ,o t−1,a t−1,o t) is the context to the agent.
Learning a policy is challenging when the mappingct↦→at is highly implicit and requires extensive
computation. For example, the agent shown in Figure 1(1c) is unable to generate the correct ﬁnal
action (Act 4) to ﬁnish the QA task as it requires complex reasoning over the trajectory context
(Question, Act 1-3, Obs 1-3). Similarly, the agent shown in Figure 1(2a) fails to comprehend from the
context that sinkbasin 1 does not contain peppershaker 1, thus keep producing hallucinating actions.
The idea of ReAct is simple: we augment the agent’s action space to ˆA =A∪L , whereL is the
space of language. An action ˆat∈L in the language space, which we will refer to as a thought or a
reasoning trace, does not affect the external environment, thus leading to no observation feedback.
Instead, a thought ˆat aims to compose useful information by reasoning over the current contextct,
and update the contextct+1 = (ct, ˆat) to support future reasoning or acting. As shown in Figure 1,
there could be various types of useful thoughts, e.g. decomposing task goals and create action plans
(2b, Act 1; 1d, Thought 1), injecting commonsense knowledge relevant to task solving (2b, Act 1),

**Source 2:** ReAct: Synergizing Reasoning and Acting in Language Models, page 2

> and if such a combination can bring systematic beneﬁts compared to reasoning or acting alone.
In this work, we present ReAct, a general paradigm to combine reasoning and acting with language
models for solving diverse language reasoning and decision making tasks (Figure 1). ReAct
prompts LLMs to generate both verbal reasoning traces and actions pertaining to a task in an
interleaved manner, which allows the model to perform dynamic reasoning to create, maintain, and
adjust high-level plans for acting (reason to act), while also interact with the external environments
(e.g. Wikipedia) to incorporate additional information into reasoning (act to reason).
2

**Source 3:** ReAct: Synergizing Reasoning and Acting in Language Models, page 2

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

### Generated Answer

How ReAct combines reasoning and acting
- ReAct prompts a language model to produce verbal reasoning traces and environment-directed actions in an interleaved (step-by-step) manner. The model both “reasons to act” (uses its reasoning traces to form and adjust high‑level action plans) and “acts to reason” (issues actions that query or change the environment and then uses the observations to continue reasoning) [Source 1].

Why this is advantageous versus reasoning-only approaches
- Interleaving actions with reasoning lets the model incorporate fresh external information into its deliberation (e.g., querying Wikipedia or an interactive environment) rather than relying solely on internal knowledge, improving the accuracy of subsequent reasoning steps [Source 1].  
- Empirically and qualitatively, ReAct outperforms prompting styles that only react to external feedback or lack sparse, high‑level reasoning (e.g., an Inner‑Monologue–style ablation): ReAct achieved substantially higher overall success (71 vs. 53) and avoided errors such as failing to decompose goals, misidentifying subgoal completion, or lacking commonsense about object locations in environments like ALFWorld [Source 2].  
- ReAct’s explicit reasoning traces also improve diagnosability: humans can distinguish what comes from the model’s internal chain of thought versus the external environment and inspect the rationale behind actions [Source 3].

Together, these factors explain why combining reasoning and acting in an interleaved way yields systematic benefits over reasoning in isolation.

---

## Question 9

**Question:** What does Chain-of-Thought prompting reveal about the relationship between model scale, intermediate reasoning steps, and performance on complex reasoning tasks?

### Retrieved Sources

**Source 1:** Chain-of-Thought Prompting Elicits Reasoning in Large Language Models, page 19

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

**Source 2:** Chain-of-Thought Prompting Elicits Reasoning in Large Language Models, page 16

> A Frequently Asked Questions
A.1 Why does increasing model scale improve chain-of-thought prompting?
The ﬁnding that successful chain-of-thought reasoning predictably emerges only at certain model
scales is intriguing. Scaling up language models has been shown to confer beneﬁts such as improved
performance and sample efﬁciency (Kaplan et al., 2020), but chain-of-thought reasoning is emergent
in the sense that its success cannot be predicted only by extrapolating the performance of small scale
models, as chain of thought actually hurts performance for most models smaller than 10B parameters.
The question of why model scale improves chain-of-thought prompting is certainly multi-faceted, and
we made a preliminary attempt to shed insight into it via error analysis. This small analysis involved
manually reading 45 errors made by PaLM 62B and categorizing them into semantic understanding
(20 errors), one step missing (18 errors), and other errors (7 errors). The “other category” included
hallucinations, repetitive outputs, and symbol mapping errors. This categorization is a coarse one
borrowed from the initial error analysis done on LaMDA in Appendix D.2, for which categories were
conceived based on what improvements were needed to make the chain of thought correct.
As shown in Figure 9, scaling PaLM to 540B parameters ﬁxed a substantial portion of errors in all
three categories. Examples of semantic understanding and one-step missing errors that were ﬁxed by

**Source 3:** Chain-of-Thought Prompting Elicits Reasoning in Large Language Models, page 8

> 540, though not for LaMDA 137B). Note that these in-domain evaluations are “toy tasks” in the
sense that perfect solution structures are already provided by the chains of thought in the few-shot
exemplars; all the model has to do is repeat the same steps with the new symbols in the test-time
example. And yet, small models still fail—the ability to perform abstract manipulations on unseen
symbols for these three tasks only arises at the scale of 100B model parameters.
As for the OOD evaluations, standard prompting fails for both tasks. With chain-of-thought prompting,
language models achieve upward scaling curves (though performance is lower than in the in-domain
setting). Hence, chain-of-thought prompting facilitates length generalization beyond seen chains of
thought for language models of sufﬁcient scale.
6 Discussion
We have explored chain-of-thought prompting as a simple mechanism for eliciting multi-step rea-
soning behavior in large language models. We ﬁrst saw that chain-of-thought prompting improves
performance by a large margin on arithmetic reasoning, yielding improvements that are much stronger
than ablations and robust to different annotators, exemplars, and language models (Section 3). Next,
3We tested 10 common names using GPT-3davinci and it got all but one correct.
4For names of length longer than 2 words, we concatenate multiple ﬁrst and last names together.
8

### Generated Answer

Chain-of-thought (CoT) prompting shows that the ability to produce and use intermediate reasoning steps is an emergent property of model scale and is tightly linked to performance on complex reasoning tasks. Specifically:

- CoT augments model outputs with intermediate reasoning steps, which helps models solve arithmetic, symbolic, and commonsense problems that standard prompting struggles with [Source 3].  
- The benefits of CoT appear only above a certain scale: for many models below ~10B parameters CoT can hurt performance, whereas sufficiently large models show dramatic, rapidly improving scaling curves when given CoT prompts [Source 2], [Source 1].  
- Increasing model size fixes substantial portions of errors (semantic understanding, missing reasoning steps, and other failures), indicating larger models can reliably generate the needed intermediate steps to reach correct answers [Source 2].  
- Overall, CoT expands the set of tasks large language models can solve (standard prompting is a lower bound), though producing human‑like chains of thought does not by itself prove the model is “reasoning” in a cognitive sense [Source 1], [Source 3].

---

## Question 10

**Question:** What limitations of RAG are identified by the authors, and how do these limitations affect the reliability or usefulness of the generated answers?

### Retrieved Sources

**Source 1:** Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks, page 6

> Table 1: Open-Domain QA Test Scores. For TQA,
left column uses the standard test set for Open-
Domain QA, right column uses the TQA-Wiki
test set. See Appendix D for further details.
Model NQ TQA WQ CT
Closed
Book
T5-11B [52] 34.5 - /50.1 37.4 -
T5-11B+SSM[52] 36.6 - /60.5 44.7 -
Open
Book
REALM [20] 40.4 - / - 40.7 46.8
DPR [26] 41.5 57.9/ - 41.1 50.6
RAG-Token 44.1 55.2/66.1 45.5 50.0
RAG-Seq. 44.5 56.8/68.0 45.2 52.2
Table 2: Generation and classiﬁcation Test Scores.
MS-MARCO SotA is [4], FEVER-3 is [68] and
FEVER-2 is [ 57] *Uses gold context/evidence.
Best model without gold access underlined.
Model Jeopardy MSMARCO FVR3 FVR2
B-1 QB-1 R-L B-1 Label Acc.
SotA - - 49.8* 49.9* 76.8 92.2 *
BART 15.1 19.7 38.2 41.6 64.0 81.1
RAG-Tok. 17.3 22.2 40.1 41.5 72.5 89.5RAG-Seq. 14.7 21.4 40.8 44.2
to more effective marginalization over documents. Furthermore, RAG can generate correct answers
even when the correct answer is not in any retrieved document, achieving 11.8% accuracy in such
cases for NQ, where an extractive model would score 0%.
4.2 Abstractive Question Answering
As shown in Table 2, RAG-Sequence outperforms BART on Open MS-MARCO NLG by 2.6 Bleu
points and 2.6 Rouge-L points. RAG approaches state-of-the-art model performance, which is
impressive given that (i) those models access gold passages with speciﬁc information required to
generate the reference answer , (ii) many questions are unanswerable without the gold passages, and

**Source 2:** Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks, page 7

> RAG-S The currency needed in Scotland is the pound sterling.
Jeopardy
Question
Gener
-ation
Washington
BART ?This state has the largest number of counties in the U.S.
RAG-T It’s the only U.S. state named for a U.S. president
RAG-S It’s the state where you’ll ﬁnd Mount Rainier National Park
The Divine
Comedy
BART *This epic poem by Dante is divided into 3 parts: the Inferno, the Purgatorio & the Purgatorio
RAG-T Dante’s "Inferno" is the ﬁrst part of this epic poem
RAG-S This 14th century work is divided into 3 sections: "Inferno", "Purgatorio" & "Paradiso"
For 2-way classiﬁcation, we compare against Thorne and Vlachos [57], who train RoBERTa [35]
to classify the claim as true or false given the gold evidence sentence. RAG achieves an accuracy
within 2.7% of this model, despite being supplied with only the claim and retrieving its own evidence.
We also analyze whether documents retrieved by RAG correspond to documents annotated as gold
evidence in FEVER. We calculate the overlap in article titles between the topk documents retrieved
by RAG and gold evidence annotations. We ﬁnd that the top retrieved document is from a gold article
in 71% of cases, and a gold article is present in the top 10 retrieved articles in 90% of cases.
4.5 Additional Results
Generation Diversity Section 4.3 shows that RAG models are more factual and speciﬁc than
BART for Jeopardy question generation. Following recent work on diversity-promoting decoding

**Source 3:** Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks, page 7

> Generation Diversity Section 4.3 shows that RAG models are more factual and speciﬁc than
BART for Jeopardy question generation. Following recent work on diversity-promoting decoding
[33, 59, 39], we also investigate generation diversity by calculating the ratio of distinct ngrams to
total ngrams generated by different models. Table 5 shows that RAG-Sequence’s generations are
more diverse than RAG-Token’s, and both are signiﬁcantly more diverse than BART without needing
any diversity-promoting decoding.
Retrieval Ablations A key feature of RAG is learning to retrieve relevant information for the task.
To assess the effectiveness of the retrieval mechanism, we run ablations where we freeze the retriever
during training. As shown in Table 6, learned retrieval improves results for all tasks.
We compare RAG’s dense retriever to a word overlap-based BM25 retriever [53]. Here, we replace
RAG’s retriever with a ﬁxed BM25 system, and use BM25 retrieval scores as logits when calculating
p(z|x). Table 6 shows the results. For FEVER, BM25 performs best, perhaps since FEVER claims are
heavily entity-centric and thus well-suited for word overlap-based retrieval. Differentiable retrieval
improves results on all other tasks, especially for Open-Domain QA, where it is crucial.
Index hot-swapping An advantage of non-parametric memory models like RAG is that knowledge
can be easily updated at test time. Parametric-only models like T5 or BART need further training to

### Generated Answer

The provided text identifies three main limitations that affect RAG’s reliability/usefulness:

- Dependence on retrieved (gold) passages: many questions are unanswerable without the gold passages the models access in evaluation, so RAG’s ability to produce correct answers depends on retrieving the right passages [Source 1], [Source 2].  
  Effect: if the retriever fails to find relevant documents, RAG cannot produce a reliable answer.

- Coverage limits of the corpus: not all questions are answerable from Wikipedia alone, so RAG’s output is limited by the knowledge available in the retrieval corpus [Source 1].  
  Effect: facts absent from the corpus cannot be generated reliably, reducing usefulness for out-of-corpus information.

- Remaining propensity to hallucinate (albeit reduced): the authors note RAG “hallucinates less and generate[s] factually correct text more often than BART,” which implies hallucination is reduced but not eliminated [Source 1].  
  Effect: generated answers can still be incorrect or unsupported, so factuality is improved but not guaranteed.

The context does not provide further detail (e.g., quantitative failure modes, error rates tied to retrieval failures, or other limitations), so I cannot provide more specifics from the provided sources.

---

