# Hybrid V1 Evaluation Results



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

Retrieval-Augmented Generation (RAG) targets knowledge‑intensive NLP tasks where a model needs reliable, up‑to‑date, and inspectable factual information. It does this by giving a pre‑trained seq2seq model differentiable access to an external (non‑parametric) text index that it can retrieve from and condition on when generating output [Source 1], [Source 2].

A language model’s parametric knowledge can be insufficient because stored facts in model parameters are hard to precisely access or manipulate, are difficult to update or revise, and do not provide provenance for decisions; such limitations can lead to poorer performance on knowledge‑heavy tasks and to hallucinations. Using an external retriever+index lets the model consult explicit evidence, be updated as the world changes, and produce more factual, specific outputs [Source 1], [Source 3], [Source 2].

---

## Question 2

**Question:** How does RAG combine parametric and non-parametric memory during generation?

### Retrieved Sources

**Source 1:** Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks, page 9

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

RAG uses a pre-trained seq2seq transformer as the parametric memory (BART) and a dense-vector Wikipedia index with a neural retriever (DPR) as the non-parametric memory. The retriever pη(z|x) returns top-K latent documents given the input, and the seq2seq generator conditions on those retrieved documents plus the input to produce the output. RAG marginalizes over the latent documents with a top-K approximation (either per-output or per-token), and the retriever and generator can be fine-tuned end-to-end so the components are jointly learned. [Source 2], [Source 1], [Source 3]

---

## Question 3

**Question:** How does RAG differ from a traditional language model that relies only on its parameters, particularly when dealing with knowledge-intensive tasks?

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

**Source 2:** Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks, page 4

> RAG models can go beyond simple extractive QA and answer questions with free-form, abstractive
text generation. To test RAG’s natural language generation (NLG) in a knowledge-intensive setting,
we use the MSMARCO NLG task v2.1 [ 43]. The task consists of questions, ten gold passages
retrieved from a search engine for each question, and a full sentence answer annotated from the
retrieved passages. We do not use the supplied passages, only the questions and answers, to treat
4

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

Short answer: RAG augments a parametric language model with a retrieval-based (non‑parametric) memory, so it fetches and conditions on external passages at generation time rather than relying solely on knowledge stored in its weights. This makes it more updatable, interpretable, and less prone to some failure modes of parametric‑only models, and improves performance on knowledge‑intensive tasks [Source 1][Source 3].

Key differences (from the provided context)
- Retrieval + generation: RAG combines a parametric generator with a retriever that fetches relevant passages and conditions generation on them (including formulations that can use the same passage for the whole sequence or different passages per token) — enabling free‑form, abstractive answers grounded in retrieved evidence [Source 1][Source 2].
- More factual, specific, diverse outputs: RAG produces more factual, specific and diverse language than a state‑of‑the‑art parametric seq2seq baseline (e.g., BART) on knowledge‑intensive generation tasks [Source 1][Source 3].
- Learnable and crucial retrieval: Learning the retriever (differentiable retrieval) improves results across tasks and is especially important for open‑domain QA, compared to fixed retrieval or relying only on model parameters [Source 3].
- Updatability and interpretability: Because RAG uses non‑parametric memory, its knowledge can be revised or expanded at test time (index “hot‑swapping”), and retrieved evidence can be inspected to provide insight into predictions — things parametric‑only models cannot easily do without further training [Source 1][Source 3].
- Reduced hallucination risk: By grounding generation in retrieved passages, RAG helps address hallucinations and the inability of parametric models to easily revise or explain their knowledge [Source 1].

If you want, I can summarize how the retriever vs. BM25 ablation affects different tasks or give examples from the MSMARCO or Jeopardy evaluations mentioned in the sources.

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

- Basic difference in latent-variable marginalization:
  - RAG-Sequence treats the retrieved document as a single latent variable for the whole output sequence: the model marginalizes over the top-K retrieved documents, but for any given document z it uses that same z to generate every token in y [Source 1].
  - RAG-Token marginalizes at the token level: for each next token the generator produces token distributions conditioned on each retrieved document and then marginalizes, so it can effectively draw a (potentially) different document for each token [Source 2].

- How this affects which documents are used during generation:
  - RAG-Sequence picks (via marginalization over top-K) one document per generated sequence and generates the entire sequence from that single document’s context [Source 1].
  - RAG-Token can combine information across multiple documents within a single generated sequence because each token’s probability is computed by marginalizing over the top-K documents independently; thus different tokens can be influenced by different documents [Source 2].

- Additional consequences:
  - For sequence-classification tasks with target length one, the two approaches are equivalent (only one token) [Source 2].
  - Empirically, RAG-Sequence produced more diverse generations than RAG-Token in the reported experiments [Source 3].

---

## Question 5

**Question:** How does GPT-3 demonstrate that large language models can perform tasks from natural-language descriptions and a few examples without gradient-based updates?

### Retrieved Sources

**Source 1:** Language Models are Few-Shot Learners, page 1

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

**Source 2:** Language Models are Few-Shot Learners, page 40

> a broader set of explicit tasks for multi-task learning, for example through procedural generation [TFR+17], human
interaction [ZSW+19b], or active learning [Mac92].
Algorithmic innovation in language models over the last two years has been enormous, including denoising-based
bidirectionality [DCLT18], preﬁxLM [DL15] and encoder-decoder architectures [LLG+19, RSR+19], random permu-
tations during training [YDY+19], architectures that improve the efﬁciency of sampling [DYY+19], improvements in
data and training procedures [LOG+19], and efﬁciency increases in the embedding parameters [LCG+19]. Many of
these techniques provide signiﬁcant gains on downstream tasks. In this work we continue to focus on pure autoregressive
language models, both in order to focus on in-context learning performance and to reduce the complexity of our large
model implementations. However, it is very likely that incorporating these algorithmic advances could improve GPT-3’s
performance on downstream tasks, especially in the ﬁne-tuning setting, and combining GPT-3’s scale with these
algorithmic techniques is a promising direction for future work.
8 Conclusion
We presented a 175 billion parameter language model which shows strong performance on many NLP tasks and
benchmarks in the zero-shot, one-shot, and few-shot settings, in some cases nearly matching the performance of
40

**Source 3:** Language Models are Few-Shot Learners, page 34

> humans learn from scratch vs from prior demonstrations. Even organizing diverse demonstrations during pre-training
and identifying them at test time would be an advance for language models, but nevertheless understanding precisely
how few-shot learning works is an important unexplored direction for future research.
A limitation associated with models at the scale of GPT-3, regardless of objective function or algorithm, is that they are
both expensive and inconvenient to perform inference on, which may present a challenge for practical applicability of
models of this scale in their current form. One possible future direction to address this is distillation [HVD15] of large
models down to a manageable size for speciﬁc tasks. Large models such as GPT-3 contain a very wide range of skills,
most of which are not needed for a speciﬁc task, suggesting that in principle aggressive distillation may be possible.
Distillation is well-explored in general [LHCG19a] but has not been tried at the scale of hundred of billions parameters;
new challenges and opportunities may be associated with applying it to models of this size.
Finally, GPT-3 shares some limitations common to most deep learning systems – its decisions are not easily interpretable,
it is not necessarily well-calibrated in its predictions on novel inputs as observed by the much higher variance in
performance than humans on standard benchmarks, and it retains the biases of the data it has been trained on. This

### Generated Answer

GPT-3 (an autoregressive language model with 175 billion parameters) was trained once and then evaluated by conditioning it on natural‑language task descriptions plus a few demonstration examples in its context window (zero‑, one‑, and few‑shot settings). Without any gradient updates or fine‑tuning, this in‑context approach yielded strong performance on many NLP tasks—sometimes nearly matching prior state‑of‑the‑art fine‑tuned methods—demonstrating that large LMs can learn to perform new tasks from descriptions and examples alone [Source 1], [Source 2].

---

## Question 6

**Question:** How does T5's text-to-text formulation allow the same model and training framework to be applied to different NLP tasks?

### Retrieved Sources

**Source 1:** Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer, page 4

> Raffel, Shazeer, Roberts, Lee, Narang, Matena, Zhou, Li and Liu
2. Setup
Before presenting the results from our large-scale empirical study, we review the necessary
background topics required to understand our results, including the Transformer model
architecture and the downstream tasks we evaluate on. We also introduce our approach
for treating every problem as a text-to-text task and describe our “Colossal Clean Crawled
Corpus” (C4), the Common Crawl-based data set we created as a source of unlabeled text
data. We refer to our model and framework as the “Text-to-Text Transfer Transformer”
(T5).
2.1 Model
Early results on transfer learning for NLP leveraged recurrent neural networks (Peters
et al., 2018; Howard and Ruder, 2018), but it has recently become more common to use
models based on the “Transformer” architecture (Vaswani et al., 2017). The Transformer
was initially shown to be effective for machine translation, but it has subsequently been
used in a wide variety of NLP settings (Radford et al., 2018; Devlin et al., 2018; McCann
et al., 2018; Yu et al., 2018). Due to its increasing ubiquity, all of the models we study are
based on the Transformer architecture. Apart from the details mentioned below and the
variants we explore in Section 3.2, we do not deviate significantly from this architecture as
originally proposed. Instead of providing a comprehensive definition of this model, we refer

**Source 2:** Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer, page 3

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

**Source 3:** Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer, page 2

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

### Generated Answer

T5 casts every problem as text input → text output (e.g., "translate English to German: …", "summarize: …", "cola sentence: …") so the same sequence-to-sequence Transformer can be used for all tasks [Source 2]. Because inputs and targets are all plain text, the authors can use a single model architecture, loss function, training procedure, decoding process, and hyperparameter set across diverse tasks (translation, QA, classification, summarization, etc.), which makes the model and training framework directly applicable and comparable across those tasks [Source 2][Source 3]. The models studied are all based on the Transformer architecture and implemented within this unified text‑to‑text setup (T5) [Source 1].

---

## Question 7

**Question:** Why does LoRA argue that the changes required when adapting a large language model have low intrinsic rank, and how does its approach exploit this observation?

### Retrieved Sources

**Source 1:** LoRA: Low-Rank Adaptation of Large Language Models, page 1

> LORA: L OW-R ANK ADAPTATION OF LARGE LAN-
GUAGE MODELS
Edward Hu∗ Yelong Shen∗ Phillip Wallis Zeyuan Allen-Zhu
Yuanzhi Li Shean Wang Lu Wang Weizhu Chen
Microsoft Corporation
{edwardhu, yeshe, phwallis, zeyuana,
yuanzhil, swang, luw, wzchen }@microsoft.com
yuanzhil@andrew.cmu.edu
(Version 2)
ABSTRACT
An important paradigm of natural language processing consists of large-scale pre-
training on general domain data and adaptation to particular tasks or domains. As
we pre-train larger models, full ﬁne-tuning, which retrains all model parameters,
becomes less feasible. Using GPT-3 175B as an example – deploying indepen-
dent instances of ﬁne-tuned models, each with 175B parameters, is prohibitively
expensive. We propose Low-Rank Adaptation, or LoRA, which freezes the pre-
trained model weights and injects trainable rank decomposition matrices into each
layer of the Transformer architecture, greatly reducing the number of trainable pa-
rameters for downstream tasks. Compared to GPT-3 175B ﬁne-tuned with Adam,
LoRA can reduce the number of trainable parameters by 10,000 times and the
GPU memory requirement by 3 times. LoRA performs on-par or better than ﬁne-
tuning in model quality on RoBERTa, DeBERTa, GPT-2, and GPT-3, despite hav-
ing fewer trainable parameters, a higher training throughput, and, unlike adapters,
no additional inference latency . We also provide an empirical investigation into
rank-deﬁciency in language model adaptation, which sheds light on the efﬁcacy of

**Source 2:** LoRA: Low-Rank Adaptation of Large Language Models, page 2

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

Why LoRA thinks adaptation updates are low‑rank
- Prior work shows over‑parameterized pretrained models lie on a low intrinsic dimension, so LoRA hypothesizes that the weight changes during adaptation similarly live in a low “intrinsic rank” subspace rather than filling the full parameter space [Source 2].  
- Empirically, LoRA finds very small ranks suffice (e.g., r = 1 or 2 even when the full dimension is 12,288 for GPT‑3), and experiments (Table 6) show small r performs competitively; tests of subspace overlap indicate that increasing r does not meaningfully expand the learned subspace, supporting the low‑rank hypothesis [Source 3].

How LoRA exploits that observation
- Instead of fine‑tuning all weights, LoRA freezes the pretrained weights and models the weight update ∆W as a low‑rank decomposition (trainable matrices A and B) injected into each Transformer layer. Only those small rank‑decomposition matrices are trained [Source 2].  
- This lets LoRA dramatically reduce the number of trainable parameters and GPU memory (e.g., ~10,000× fewer trainable parameters and ~3× less GPU memory in the GPT‑3 example) while matching or improving fine‑tuning quality, avoiding added inference latency, and enabling cheap task‑specific modules that can be swapped in/out [Source 1, Source 2].

---

## Question 8

**Question:** How does ReAct combine reasoning and acting, and why does this provide an advantage over approaches that perform reasoning without interacting with external environments?

### Retrieved Sources

**Source 1:** ReAct: Synergizing Reasoning and Acting in Language Models, page 2

> and if such a combination can bring systematic beneﬁts compared to reasoning or acting alone.
In this work, we present ReAct, a general paradigm to combine reasoning and acting with language
models for solving diverse language reasoning and decision making tasks (Figure 1). ReAct
prompts LLMs to generate both verbal reasoning traces and actions pertaining to a task in an
interleaved manner, which allows the model to perform dynamic reasoning to create, maintain, and
adjust high-level plans for acting (reason to act), while also interact with the external environments
(e.g. Wikipedia) to incorporate additional information into reasoning (act to reason).
2

**Source 2:** ReAct: Synergizing Reasoning and Acting in Language Models, page 8

> demonstration of combined reasoning and action using an LLM applied to an interactive environment
within a closed-loop system. Perhaps the closest prior work is Inner Monologue (IM), from Huang
et al. (2022b), in which actions from an embodied agent are motivated by an eponymous “inner
monologue”. However, IM’s “inner monologue” is limited to observations of the environment
state and what needs to be completed by the agent for the goal to be satisﬁed. In contrast, the
reasoning traces in ReAct for decision making is ﬂexible and sparse, allowing diverse reasoning
types (see Section 2) to be induced for different tasks.
To demonstrate the differences between ReAct and IM, and to highlight the importance of internal
reasoning vs. simple reactions to external feedback, we ran an ablation experiment using a thought
pattern composed of IM-like dense external feedback. As can be seen in Table 3,ReAct substantially
outperforms IM-style prompting ( ReAct-IM) (71 vs. 53 overall success rate), with consistent
advantages on ﬁve out of six tasks. Qualitatively, we observed that ReAct-IM often made mistakes
in identifying when subgoals were ﬁnished, or what the next subgoal should be, due to a lack of high-
level goal decomposition. Additionally, many ReAct-IM trajectories struggled to determine where
an item would likely be within the ALFWorld environment, due to a lack of commonsense reasoning.
Both shortcomings can be addressed in the ReAct paradigm. More details about ReAct-IM is in

**Source 3:** ReAct: Synergizing Reasoning and Acting in Language Models, page 3

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

### Generated Answer

How it combines them
- ReAct prompts a language model to produce verbal reasoning traces and environment-directed actions in an interleaved (step-by-step) fashion. This lets the model “reason to act” (use its chain-of-thought to form and adjust high‑level plans) and “act to reason” (query or interact with external sources and bring that new information back into the reasoning trace) [Source 1].

Why this helps compared with reasoning-only approaches
- Interleaving actions with reasoning lets the agent incorporate fresh, environment-derived information into its reasoning (act → reason) and use reasoning to plan better actions (reason → act), which improves dynamic planning and commonsense localization of items that pure internal reasoning can miss [Source 1], [Source 2].
- Empirically, ReAct outperforms an Inner‑Monologue–style baseline that relies mainly on external observations without flexible internal reasoning (71% vs. 53% overall success), and the paper attributes failures of the IM‑style approach to poor subgoal decomposition and lack of commonsense—shortcomings ReAct addresses by combining reasoning and acting [Source 2].
- The interleaved traces also improve diagnosability: humans can distinguish internal knowledge from external evidence and inspect the chain‑of‑thought behind actions, which aids understanding and debugging compared to opaque reasoning-only outputs [Source 3].

---

## Question 9

**Question:** What does Chain-of-Thought prompting reveal about the relationship between model scale, intermediate reasoning steps, and performance on complex reasoning tasks?

### Retrieved Sources

**Source 1:** Chain-of-Thought Prompting Elicits Reasoning in Large Language Models, page 9

> experiments on commonsense reasoning underscored how the linguistic nature of chain-of-thought
reasoning makes it generally applicable (Section 4). Finally, we showed that for symbolic reasoning,
chain-of-thought prompting facilitates OOD generalization to longer sequence lengths (Section 5). In
all experiments, chain-of-thought reasoning is elicited simply by prompting an off-the-shelf language
model. No language models were ﬁnetuned in the process of writing this paper.
The emergence of chain-of-thought reasoning as a result of model scale has been a prevailing theme
(Wei et al., 2022b). For many reasoning tasks where standard prompting has a ﬂat scaling curve, chain-
of-thought prompting leads to dramatically increasing scaling curves. Chain-of-thought prompting
appears to expand the set of tasks that large language models can perform successfully—in other
words, our work underscores that standard prompting only provides a lower bound on the capabilities
of large language models. This observation likely raises more questions than it answers—for instance,
how much more can we expect reasoning ability to improve with a further increase in model scale?
What other prompting methods might expand the range of tasks that language models can solve?
As for limitations, we ﬁrst qualify that although chain of thought emulates the thought processes of
human reasoners, this does not answer whether the neural network is actually “reasoning,” which

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

**Source 3:** Chain-of-Thought Prompting Elicits Reasoning in Large Language Models, page 9

> instructions that are prepended to inputs), our work takes the orthogonal direction of augmenting the
outputs of language models with a chain of thought.
8 Conclusions
We have explored chain-of-thought prompting as a simple and broadly applicable method for enhanc-
ing reasoning in language models. Through experiments on arithmetic, symbolic, and commonsense
reasoning, we ﬁnd that chain-of-thought reasoning is an emergent property of model scale that allows
sufﬁciently large language models to perform reasoning tasks that otherwise have ﬂat scaling curves.
Broadening the range of reasoning tasks that language models can perform will hopefully inspire
further work on language-based approaches to reasoning.
9

### Generated Answer

Chain-of-Thought (CoT) prompting causes models to produce explicit intermediate reasoning steps in their outputs, rather than just final answers, by augmenting outputs with a “chain of thought” (i.e., step‑by‑step verbal reasoning) [Source 3]. This ability is an emergent property of model scale: CoT prompting reliably helps only at sufficiently large model sizes and often hurts performance for many models smaller than ~10B parameters; success cannot be predicted from small‑model behavior alone [Source 2]. When CoT emerges, it dramatically changes scaling behavior—tasks with flat scaling under standard prompting show sharply improving performance with CoT as model size increases—expanding the set of complex reasoning problems models can solve and enabling benefits such as out‑of‑distribution generalization (e.g., to longer symbolic sequences) [Source 1, Source 3]. Error analyses further indicate that increasing scale fixes many types of mistakes that block correct chains of thought (semantic misunderstandings, missing intermediate steps, and other errors), explaining why larger models benefit more from CoT prompting [Source 2]. Finally, while CoT elicits human‑like intermediate steps and improves task performance, the papers note this does not by itself prove that the models are “reasoning” in the same sense humans do [Source 1].

---

## Question 10

**Question:** What limitations of RAG are identified by the authors, and how do these limitations affect the reliability or usefulness of the generated answers?

### Retrieved Sources

**Source 1:** Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks, page 6

> impressive given that (i) those models access gold passages with speciﬁc information required to
generate the reference answer , (ii) many questions are unanswerable without the gold passages, and
(iii) not all questions are answerable from Wikipedia alone. Table 3 shows some generated answers
from our models. Qualitatively, we ﬁnd that RAG models hallucinate less and generate factually
correct text more often than BART. Later, we also show that RAG generations are more diverse than
BART generations (see §4.5).
4.3 Jeopardy Question Generation
Table 2 shows that RAG-Token performs better than RAG-Sequence on Jeopardy question generation,
with both models outperforming BART on Q-BLEU-1. 4 shows human evaluation results, over 452
pairs of generations from BART and RAG-Token. Evaluators indicated that BART was more factual
than RAG in only 7.1% of cases, while RAG was more factual in 42.7% of cases, and both RAG and
BART were factual in a further 17% of cases, clearly demonstrating the effectiveness of RAG on
the task over a state-of-the-art generation model. Evaluators also ﬁnd RAG generations to be more
speciﬁc by a large margin. Table 3 shows typical generations from each model.
Jeopardy questions often contain two separate pieces of information, and RAG-Token may perform
best because it can generate responses that combine content from several documents. Figure 2 shows
an example. When generating “Sun”, the posterior is high for document 2 which mentions “The

**Source 2:** Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks, page 4

> RAG models can go beyond simple extractive QA and answer questions with free-form, abstractive
text generation. To test RAG’s natural language generation (NLG) in a knowledge-intensive setting,
we use the MSMARCO NLG task v2.1 [ 43]. The task consists of questions, ten gold passages
retrieved from a search engine for each question, and a full sentence answer annotated from the
retrieved passages. We do not use the supplied passages, only the questions and answers, to treat
4

**Source 3:** Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks, page 5

> retriever is initialized using DPR’s retriever, which uses retrieval supervision on Natural Questions
and TriviaQA. RAG compares favourably to the DPR QA system, which uses a BERT-based “cross-
encoder” to re-rank documents, along with an extractive reader. RAG demonstrates that neither a
re-ranker nor extractive reader is necessary for state-of-the-art performance.
There are several advantages to generating answers even when it is possible to extract them. Docu-
ments with clues about the answer but do not contain the answer verbatim can still contribute towards
a correct answer being generated, which is not possible with standard extractive approaches, leading
5

### Generated Answer

Limitations identified in the provided excerpts

- Dependence on gold (relevant) passages: the authors note that the evaluated models “access gold passages with specific information required to generate the reference answer” and that “many questions are unanswerable without the gold passages” [Source 1]. Effect: if the retriever does not return the necessary passages, RAG cannot produce the correct answer and performance will drop — i.e., reliability depends on retrieving the right evidence.

- Limited source-coverage (Wikipedia-only issues): the authors state that “not all questions are answerable from Wikipedia alone” [Source 1]. Effect: when the knowledge needed is absent from the retrieval corpus, RAG’s outputs may be incomplete or incorrect, reducing usefulness on topics outside the corpus.

- Remaining tendency to hallucinate (though less than some baselines): the authors report that RAG “hallucinate[s] less and generate[s] factually correct text more often than BART” — wording implies hallucination is reduced but not eliminated [Source 1]. Effect: generated answers can still be factually wrong in some cases, so outputs must be treated with caution and (when important) verified against sources.

If you want, I can summarize how these limitations suggest practical safeguards (e.g., improving retrieval, expanding corpora, or adding verification steps).

---

