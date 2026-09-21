# RRF Evaluation Results

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

Retrieval-Augmented Generation (RAG) addresses the problem of performing knowledge-intensive NLP tasks when a model needs reliable, up‑to‑date, and inspectable factual knowledge. It does this by augmenting a pre‑trained seq2seq (parametric) model with a non‑parametric retrieval component that pulls in relevant documents as context for generation, improving accuracy on tasks that require external facts [Source 1], [Source 2].

A language model’s parametric knowledge can be insufficient because the facts it stores implicitly in its parameters are hard to inspect, update, or precisely manipulate; this leads to poorer performance on knowledge‑intensive tasks, difficulty providing provenance for outputs, and a tendency to “hallucinate.” Parametric memory thus can’t be easily expanded or revised, motivating the use of an explicit retrieval memory alongside the model [Source 1], [Source 3].

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

RAG uses a retriever to fetch non‑parametric evidence documents for the input and a pre‑trained seq2seq transformer as the parametric generator; the generator conditions on both the input and the retrieved documents to produce the output. The retriever (DPR) provides latent documents pη(z|x) and the seq2seq model (BART) conditions on those documents together with x to generate y; RAG marginalizes over the top‑K retrieved documents (either treating one document as responsible for the whole output or allowing different documents to influence different tokens) and can be fine‑tuned end‑to‑end so the retriever and generator are learned jointly [Source 2]. The approach aggregates content from several retrieved pieces (evidence documents) rather than relying only on parametric memory, and the retrieval index can be swapped to update knowledge without retraining the generator [Source 1][Source 3].

---

## Question 3

**Question:** How does RAG differ from a traditional language model that relies only on its parameters, particularly when dealing with knowledge-intensive tasks?

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

- Memory architecture: traditional LMs store knowledge only in model parameters (a “parametric” implicit KB), whereas RAG is hybrid — it augments a parametric generator with a non‑parametric retrieval component that fetches external passages to condition generation [Source 1].

- Inspectability and updatability: because RAG retrieves explicit passages, the accessed knowledge can be inspected and the external index can be revised or “hot‑swapped” at test time; purely parametric models cannot easily expand or revise their memory without further training [Source 1, Source 3].

- Robustness to factual errors: parametric models “may produce ‘hallucinations’” and can’t easily show the evidence behind outputs; RAG can address some of these issues by grounding generation in retrieved evidence, improving factuality and specificity on knowledge‑intensive tasks [Source 1, Source 3].

- Generation behavior: RAG can perform free‑form, abstractive answers (not just extractive QA) and has been shown to generate more factual, specific and more diverse text than a state‑of‑the‑art parametric seq2seq baseline on NLG and QA benchmarks [Source 2, Source 3].

- Learned retrieval matters: RAG’s differentiable/dense retriever improves performance over freezing the retriever or replacing it with a simple BM25 retriever for most tasks (with some task‑dependent exceptions), and is especially important for open‑domain QA [Source 3].

In short: unlike a parameter‑only language model, RAG combines retrieval from an external knowledge store with generative modeling, yielding more inspectable, updatable, and often more factual and diverse outputs on knowledge‑intensive tasks [Source 1, Source 2, Source 3].

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

**Source 2:** Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks, page 4

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

**Source 3:** Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks, page 17

> Appendices for Retrieval-Augmented Generation for
Knowledge-Intensive NLP Tasks
A Implementation Details
For Open-domain QA we report test numbers using 15 retrieved documents for RAG-Token models.
For RAG-Sequence models, we report test results using 50 retrieved documents, and we use the
Thorough Decoding approach since answers are generally short. We use greedy decoding for QA as
we did not ﬁnd beam search improved results. For Open-MSMarco and Jeopardy question generation,
we report test numbers using ten retrieved documents for both RAG-Token and RAG-Sequence,
and we also train a BART-large model as a baseline. We use a beam size of four, and use the Fast
Decoding approach for RAG-Sequence models, as Thorough Decoding did not improve performance.
B Human Evaluation
Figure 4: Annotation interface for human evaluation of factuality. A pop-out for detailed instructions
and a worked example appear when clicking "view tool guide".
Figure 4 shows the user interface for human evaluation. To avoid any biases for screen position,
which model corresponded to sentence A and sentence B was randomly selected for each example.
Annotators were encouraged to research the topic using the internet, and were given detailed instruc-
tions and worked examples in a full instructions tab. We included some gold sentences in order to
assess the accuracy of the annotators. Two annotators did not perform well on these examples and
their annotations were removed from the results.

### Generated Answer

- Conditioning / marginalization:
  - RAG-Sequence treats the retrieved document as a single latent variable for the whole output and marginalizes over the top‑K documents at the sequence level. The generator uses the same chosen document to produce every token in the sequence [Source 1].
  - RAG-Token marginalizes at each token: for every next token the model can draw (and marginalize over) a possibly different document from the top‑K. Thus each token’s distribution is a mixture over documents [Source 2].

- Effect on which documents are used during generation:
  - RAG-Sequence forces the generator to rely on one retrieved document for the entire generated sequence (though that document is chosen via marginalization over the top‑K) [Source 1].
  - RAG-Token allows the generator to pick content from different retrieved documents across tokens, enabling the answer to draw information from several documents [Source 2].

- Practical consequence noted in the paper:
  - RAG-Sequence tends to produce more diverse generations than RAG-Token (and both are more diverse than a non-retrieval baseline like BART) [Source 3].

(For target sequences of length one, the two approaches are equivalent because marginalizing per-token vs per-sequence collapses to the same computation [Source 2].)

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

**Source 3:** Language Models are Few-Shot Learners, page 40

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

### Generated Answer

GPT-3 is trained as a very large (175 billion parameter) autoregressive language model and is evaluated by conditioning it on natural-language task descriptions plus a few exemplar input–output pairs in the prompt (zero‑, one‑, and few‑shot settings). For all tasks it is applied without any gradient updates or fine‑tuning; simply providing the description and examples in context lets the model perform the task. Scaling the model to this size produces strong, sometimes near state‑of‑the‑art, few‑shot performance, demonstrating that large LMs can learn to follow natural‑language instructions from a handful of examples in context rather than via gradient‑based training on task‑specific data [Source 1][Source 2].

---

## Question 6

**Question:** How does T5's text-to-text formulation allow the same model and training framework to be applied to different NLP tasks?

### Retrieved Sources

**Source 1:** Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer, page 2

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

**Source 2:** Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer, page 41

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

T5 casts every NLP problem as a text-to-text task — the model always takes text as input and is trained to generate target text as output (e.g., "translate English to German: …", "summarize: …", or a label string for classification) [Source 3], [Source 2]. Because inputs and outputs are all plain text, the same Transformer model, loss/objective, training procedure, decoding process, and even hyperparameters can be used across tasks, letting one unified model and training framework be applied to translation, QA, classification, summarization, etc. [Source 2], [Source 3].

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

**Source 3:** LoRA: Low-Rank Adaptation of Large Language Models, page 4

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

### Generated Answer

Why LoRA thinks adaptation updates are low-rank
- Prior work shows over‑parameterized, pre‑trained models lie on a low intrinsic dimension, so the authors hypothesize the weight changes during task adaptation also live in a low‑rank subspace rather than requiring full‑rank updates [Source 2].  
- Empirical results support this: LoRA finds very small ranks (r = 1 or 2) can suffice even when the full layer dimensionality is very large (e.g., 12,288), and experiments (Table 6) show low‑r updates perform competitively, especially for certain projection matrices like Wq and Wv [Source 2][Source 3].

How LoRA exploits that observation
- Instead of fine‑tuning all weights, LoRA freezes the pretrained weights and injects trainable low‑rank decomposition matrices (A and B) that parameterize the weight change ΔW = B A. Only these small matrices are trained, drastically reducing trainable parameters and GPU memory while retaining or improving quality [Source 1][Source 2].  
- This design makes it cheap to store and switch task‑specific modules (replace A and B), avoids added inference latency, and leverages the low intrinsic rank of the required update to be both storage‑ and compute‑efficient [Source 2][Source 1].

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

**Source 3:** ReAct: Synergizing Reasoning and Acting in Language Models, page 2

> and if such a combination can bring systematic beneﬁts compared to reasoning or acting alone.
In this work, we present ReAct, a general paradigm to combine reasoning and acting with language
models for solving diverse language reasoning and decision making tasks (Figure 1). ReAct
prompts LLMs to generate both verbal reasoning traces and actions pertaining to a task in an
interleaved manner, which allows the model to perform dynamic reasoning to create, maintain, and
adjust high-level plans for acting (reason to act), while also interact with the external environments
(e.g. Wikipedia) to incorporate additional information into reasoning (act to reason).
2

### Generated Answer

How ReAct combines reasoning and acting
- ReAct prompts a language model to produce both explicit verbal reasoning traces and environment-directed actions in an interleaved manner (reasoning steps and actions alternate), so the model both plans (“reason to act”) and executes/interacts (“act to reason”) as it solves a task [Source 1].

Why this helps compared to reasoning without interaction
- The interleaving creates a closed loop where actions bring back observations that are incorporated into ongoing reasoning, enabling dynamic creation, maintenance, and adjustment of high‑level plans based on external information [Source 1].  
- This integration yields better task performance than approaches that only react to external feedback or only reason internally; in experiments ReAct substantially outperformed an IM‑style (inner‑monologue) prompting baseline (71% vs. 53% overall success), with advantages on most tasks [Source 2].  
- ReAct addresses shortcomings of pure reaction or pure reasoning: it supports high‑level goal decomposition and commonsense inference that IM‑style prompts lacked (leading IM to miss when subgoals were finished or where items likely were), and it provides diagnosability because one can distinguish internal knowledge from external evidence by inspecting the reasoning traces [Source 2, Source 3].

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

**Source 2:** Chain-of-Thought Prompting Elicits Reasoning in Large Language Models, page 9

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

- Chain-of-thought prompting asks models to produce intermediate reasoning steps (a “chain of thought”) and this augmentation of outputs substantially improves performance on complex reasoning tasks that otherwise show flat scaling under standard prompting [Source 1], [Source 3].

- The ability to benefit from chain-of-thought is emergent with model scale: successful chain-of-thought prompting typically appears only above certain model sizes, can hurt performance for many models below ~10B parameters, and cannot be predicted by extrapolating small-model behavior [Source 2].

- Scaling up models both increases the effectiveness of chain-of-thought and reduces specific error types (e.g., semantic-understanding errors and “one-step missing” errors); for example, scaling PaLM to 540B fixed a substantial portion of such errors [Source 2].

- Chain-of-thought also enables better out-of-distribution generalization (e.g., to longer sequence lengths in symbolic reasoning) and thus broadens the set of tasks large language models can solve [Source 1].

- A caution: producing human-like intermediate steps does not by itself prove the model is truly “reasoning” in a cognitive sense [Source 1].

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

**Source 2:** Language Models are Few-Shot Learners, page 26

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

**Source 3:** Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks, page 4

> RAG models can go beyond simple extractive QA and answer questions with free-form, abstractive
text generation. To test RAG’s natural language generation (NLG) in a knowledge-intensive setting,
we use the MSMARCO NLG task v2.1 [ 43]. The task consists of questions, ten gold passages
retrieved from a search engine for each question, and a full sentence answer annotated from the
retrieved passages. We do not use the supplied passages, only the questions and answers, to treat
4

### Generated Answer

Limitations identified in the provided text, and their effects:

- Dependence on gold / relevant retrieved passages: the authors note that many questions are unanswerable without the gold passages provided for the task, and that the models’ strong results are “impressive” only given access to those gold passages [Source 1]. Effect: if retrieval fails or the retrieved documents don’t contain the necessary information, RAG cannot reliably produce a correct answer.

- Coverage limits of the source corpus: the authors point out that “not all questions are answerable from Wikipedia alone” (the corpus used for some evaluations) [Source 1]. Effect: RAG’s usefulness is constrained by the knowledge available in the retrieval corpus — missing coverage leads to unanswerable or incorrect generations.

- Need for informative retrieved documents (not just exact spans): the paper emphasizes that generating answers can leverage documents that contain clues rather than verbatim answers, implying that when such clues are absent the model cannot assemble a correct answer as an extractive system might [Source 3]. Effect: reliability depends on retrieval returning documents with sufficient clues; otherwise the generated answer may be incorrect or incomplete.

The provided context does not list other potential limitations (e.g., computational cost, latency, or remaining hallucination rates in absolute terms), so I cannot report on those from these sources.

---

