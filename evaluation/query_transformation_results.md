# Query Transformation Evaluation Results

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

Retrieval-Augmented Generation (RAG) is designed to address the shortcomings of purely parametric language models on knowledge‑intensive tasks: namely their limited ability to access and precisely manipulate factual knowledge, to provide provenance for answers, and to update or revise stored information. Purely parametric models store knowledge in their parameters, which makes that knowledge hard to inspect or change and can lead to “hallucinations” or degraded performance on tasks that require up‑to‑date or verifiable facts. RAG remedies this by coupling a pre‑trained generative model with a non‑parametric (retrieval) memory so the model can retrieve and condition on explicit external documents when generating answers [Source 1][Source 3].

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

RAG pairs a parametric seq2seq generator (a pre‑trained transformer like BART) with a non‑parametric dense document index (retrieved via a neural retriever such as DPR) [Source 2]. At generation time the retriever pη(z|x) returns top‑K latent documents z conditioned on the input x, and the seq2seq generator conditions on the input plus those retrieved documents to produce y [Source 2], using the retrieved texts as additional context [Source 3]. RAG marginalizes over the latent documents with a top‑K approximation (either per‑output or per‑token), and the retriever and generator can be fine‑tuned end‑to‑end so the model effectively aggregates evidence from several retrieved documents rather than just editing a single retrieved item [Source 2][Source 1].

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

**Source 3:** Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks, page 4

> RAG models can go beyond simple extractive QA and answer questions with free-form, abstractive
text generation. To test RAG’s natural language generation (NLG) in a knowledge-intensive setting,
we use the MSMARCO NLG task v2.1 [ 43]. The task consists of questions, ten gold passages
retrieved from a search engine for each question, and a full sentence answer annotated from the
retrieved passages. We do not use the supplied passages, only the questions and answers, to treat
4

### Generated Answer

In contrast to a traditional parametric-only language model (whose “knowledge” is fixed in its parameters), RAG is a hybrid that augments a generator with a non‑parametric, retrieval-based memory. Concretely:

- RAG retrieves relevant passages from an external index at generation time rather than relying solely on stored parameters, so its knowledge can be inspected, revised, or expanded without re‑training [Source 1].  
- It can produce free‑form, abstractive answers grounded in retrieved documents (not just extractive outputs) and was evaluated on NLG tasks like MSMARCO NLG to test this capability [Source 2].  
- RAG comes in formulations that either condition on the same retrieved passages for the whole output or allow different passages per token, giving flexible ways to incorporate retrieved evidence [Source 1].  
- Empirically, RAG outperforms parametric seq2seq baselines on open‑domain QA and generates more specific, diverse, and factual language than parametric‑only models [Source 1, Source 3].  
- Its differentiable (learned) retriever improves performance over a fixed retriever and is especially important for open‑domain QA; and because retrieval is non‑parametric, the index can be hot‑swapped/updated at test time (whereas parametric models require further training to change their knowledge) [Source 3].

If you need examples or a concise comparison table, say so.

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

- RAG-Sequence: treats the retrieved document as a single latent variable and uses the same retrieved document to generate the entire output sequence. The model marginalizes over the top-K retrieved documents, but for any given sampled document z the generator conditions every token on that same z [Source 1].

- RAG-Token: marginalizes a document per output token, i.e., for each next token the generator computes a distribution over the top-K documents and can effectively condition different tokens on different documents. This lets the generator pick content from several documents while producing an answer [Source 2].

Effects on documents used during generation
- RAG-Sequence forces one document to supply the evidence for the whole sequence (though the final output probability marginalizes over the top-K docs) [Source 1].
- RAG-Token allows the generator to draw on multiple documents across tokens, combining information from different retrieved passages when producing an answer [Source 2].

Additional notes
- For single-token targets (e.g., sequence classification where the target is length one) the two approaches are equivalent [Source 1].
- Empirically, RAG-Sequence produces more diverse generations than RAG-Token (both are more diverse than a non-retrieval baseline) [Source 3].

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

**Source 3:** Language Models are Few-Shot Learners, page 1

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

### Generated Answer

GPT-3 was trained as a very large (175 billion parameter) autoregressive language model and then evaluated by giving tasks as natural‑language instructions plus a few example input–output pairs in the model prompt (zero‑, one‑, and few‑shot settings). Crucially, the authors applied GPT‑3 “without any gradient updates or fine‑tuning,” and showed that simply conditioning the model on the task description and examples in context yields strong, task‑agnostic few‑shot performance—sometimes competitive with prior fine‑tuned approaches—demonstrating that large LMs can learn to perform new tasks from natural‑language descriptions and a few examples via in‑context learning rather than gradient‑based updates [Source 1][Source 2].

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

**Source 3:** Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer, page 42

> all models completely separately, though fine-tune-only ensembling still substantially
outperformed a single model.
Pushing the limitsWe combined our above insights and trained substantially larger
models (up to11 billion parameters) to achieve state-of-the-art results across many of
the benchmarks we considered. For unsupervised training, we extracted text from our
C4 data set and applied a denoising objective that corrupts contiguous spans of tokens.
We pre-trained on a multi-task mixture before fine-tuning on individual tasks. Overall,
our models were trained on over1 trillion tokens. In the interest of facilitating the
replication, extension, and application of our results, we release our code, the C4 data
set, and pre-trained model weights for each T5 variant.1
42

### Generated Answer

T5 casts every NLP problem as a text-in / text-out task (e.g., "translate ...", "summarize ...", "cola sentence: ..."), so inputs and desired outputs for translation, QA, classification, summarization, etc., are all plain text strings [Source 2]. Because every task is formulated this way, the same Transformer model, loss function, training procedure, decoding process, and hyperparameters can be applied unchanged across tasks — i.e., one unified text-to-text objective and framework is used for all tasks [Source 3]. (All models in the study are Transformer-based, so the architecture is consistent as well.) [Source 1]

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

Why LoRA thinks adaptation updates are low-rank
- Prior work shows large, overparameterized models effectively lie on a low intrinsic dimension; LoRA extends that hypothesis to the *change* in weights during adaptation, i.e., the weight-update matrix ΔW is likely low “intrinsic rank” rather than full rank [Source 2].  
- Empirically, LoRA finds very small ranks (r = 1 or 2) already perform competitively even when the full layer dimension d is large (e.g., d = 12,288), and different runs learn highly overlapping subspaces—supporting that ΔW is low-rank in practice [Source 2], [Source 3].

How LoRA exploits that observation
- Instead of fine-tuning all weights, LoRA freezes the pretrained weights and models the required change as a low-rank decomposition ΔW = A·B (two much smaller matrices) that are the only trainable parameters injected into each Transformer layer [Source 1], [Source 2].  
- This lets LoRA train far fewer parameters (e.g., up to 10,000× fewer for GPT-3 175B), reduce GPU memory needs, avoid added inference latency, and enable small, swappable task-specific modules (A and B) while keeping the shared model frozen [Source 1], [Source 2].  
- Empirical checks (subspace overlap and performance with small r) further support that a low-rank adapter suffices for many adaptation tasks, though they note small r may not work for every possible downstream scenario [Source 3].

---

## Question 8

**Question:** How does ReAct combine reasoning and acting, and why does this provide an advantage over approaches that perform reasoning without interacting with external environments?

### Retrieved Sources

**Source 1:** ReAct: Synergizing Reasoning and Acting in Language Models, page 8

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

**Source 2:** ReAct: Synergizing Reasoning and Acting in Language Models, page 2

> and if such a combination can bring systematic beneﬁts compared to reasoning or acting alone.
In this work, we present ReAct, a general paradigm to combine reasoning and acting with language
models for solving diverse language reasoning and decision making tasks (Figure 1). ReAct
prompts LLMs to generate both verbal reasoning traces and actions pertaining to a task in an
interleaved manner, which allows the model to perform dynamic reasoning to create, maintain, and
adjust high-level plans for acting (reason to act), while also interact with the external environments
(e.g. Wikipedia) to incorporate additional information into reasoning (act to reason).
2

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

ReAct interleaves verbal reasoning traces with concrete actions: the model writes short chain-of-thought style reasoning (“reason”) and then issues actions (e.g., environment queries or moves) in the same trajectory, using observations from actions to update its reasoning and plans (reason → act and act → reason) [Source 1]. This lets the agent do dynamic, high-level plan creation, maintenance, and adjustment while incorporating external information from environments (e.g., Wikipedia or embodied simulators) into its reasoning [Source 1].

That synergy gives practical advantages over approaches that only reason without interacting (or that only react to dense external feedback). ReAct’s flexible, sparse reasoning traces support diverse reasoning types and high‑level goal decomposition, while actions supply external evidence and situational information that corrects or refines those plans. In ablations, a prompting variant that mimicked dense external-feedback “inner monologue” underperformed ReAct (71% vs. 53% overall success), with failures traced to poor subgoal identification and lack of commonsense about where items are—shortcomings ReAct’s interleaving of reasoning and acting addresses [Source 2]. ReAct also improves diagnosability because its explicit reasoning traces separate internal inferences from external observations, helping humans inspect the decision basis of actions [Source 3].

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

**Source 2:** Chain-of-Thought Prompting Elicits Reasoning in Large Language Models, page 9

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

**Source 3:** Chain-of-Thought Prompting Elicits Reasoning in Large Language Models, page 16

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

### Generated Answer

Chain-of-thought (CoT) prompting shows that eliciting intermediate, language-like reasoning steps can substantially boost a model’s ability to solve complex reasoning tasks — but this benefit depends strongly on model scale. CoT is an emergent property of scale: sufficiently large models gain dramatically improving (rather than flat) scaling curves with CoT prompting, expanding the set of tasks they can solve; smaller models often do not benefit and CoT can even hurt performance for models below roughly 10B parameters [Source 1][Source 3][Source 2]. Empirically, scaling to much larger sizes (e.g., from 62B to 540B) corrected many semantic- and one-step–missing errors, indicating that larger models better produce correct intermediate steps and thus better final answers [Source 2]. CoT prompting also enables out‑of‑distribution generalization (e.g., to longer sequence lengths) and achieves these gains without model finetuning — it works by augmenting outputs with intermediate reasoning rather than changing the model weights [Source 1][Source 3].

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

The authors note a few limitations (and evaluation caveats) that affect RAG’s reliability/usefulness:

- Dependence on retrieved/gold passages: in their evaluations the models often access gold passages that contain the specific information needed for the reference answer, and many questions are unanswerable without those gold passages. Also, not all questions are answerable from a single source like Wikipedia. This means RAG’s performance depends strongly on retrieval coverage and the available corpus; if the required passages aren’t retrieved or don’t exist in the corpus, the model cannot reliably produce the correct answer [Source 1].

- Remaining hallucination risk: although RAG “hallucinates less and generate[s] factually correct text more often than BART,” hallucination is still a concern (the comparison implies it is reduced but not eliminated), so some generated answers can still be incorrect or unsupported by retrieved documents [Source 1].

- Variation across RAG variants: different RAG formulations perform differently (e.g., RAG-Token outperforms RAG-Sequence on Jeopardy question generation). Choice of variant therefore affects factuality and specificity of outputs, so reliability can vary by model configuration [Source 1].

These limitations imply that RAG’s answers are only as useful as the retrieval step and corpus coverage, and that while RAG reduces but does not remove hallucination, outputs should still be checked against source passages when high factual reliability is required.

---

