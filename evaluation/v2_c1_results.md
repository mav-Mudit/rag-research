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

**Source 2:** Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks, page 9

> architecture, by learning a retrieval module to augment pre-trained, generative language models.
Learned Retrieval There is signiﬁcant work on learning to retrieve documents in information
retrieval, more recently with pre-trained, neural language models [ 44, 26] similar to ours. Some
work optimizes the retrieval module to aid in a speciﬁc, downstream task such as question answering,
using search [46], reinforcement learning [6, 63, 62], or a latent variable approach [31, 20] as in our

**Source 3:** Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks, page 1

> their predictions, and may produce “hallucinations” [38]. Hybrid models that combine parametric
memory with non-parametric (i.e., retrieval-based) memories [20, 26, 48] can address some of these
issues because knowledge can be directly revised and expanded, and accessed knowledge can be
inspected and interpreted. REALM [ 20] and ORQA [ 31], two recently introduced models that
combine masked language models [8] with a differentiable retriever, have shown promising results,

### Generated Answer

Retrieval-Augmented Generation (RAG) aims to improve performance on knowledge-intensive tasks by augmenting generative language models with a retrieval module that brings in relevant external information for generation [Source 2]. This is needed because, while large pre-trained models do store factual knowledge, their parametric memory can be insufficient: it can produce “hallucinations,” and cannot be easily revised, expanded, or inspected—limitations that retrieval-based (non‑parametric) memories help address by providing directly accessible and updatable evidence [Source 1][Source 3].

---

## Question 2

**Question:** How does RAG combine parametric and non-parametric memory during generation?

### Retrieved Sources

**Source 1:** Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks, page 9

> In this work, we presented hybrid generation models with access to parametric and non-parametric
memory. We showed that our RAG models obtain state of the art results on open-domain QA. We
found that people prefer RAG’s generation over purely parametric BART, ﬁnding RAG more factual
and speciﬁc. We conducted an thorough investigation of the learned retrieval component, validating
its effectiveness, and we illustrated how the retrieval index can be hot-swapped to update the model

**Source 2:** Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks, page 1

> (RAG) — models which combine pre-trained parametric and non-parametric mem-
ory for language generation. We introduce RAG models where the parametric
memory is a pre-trained seq2seq model and the non-parametric memory is a dense
vector index of Wikipedia, accessed with a pre-trained neural retriever. We com-
pare two RAG formulations, one which conditions on the same retrieved passages
across the whole generated sequence, and another which can use different passages

**Source 3:** Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks, page 2

> and non-parametric memory to the “workhorse of NLP,” i.e. sequence-to-sequence (seq2seq) models.
We endow pre-trained, parametric-memory generation models with a non-parametric memory through
a general-purpose ﬁne-tuning approach which we refer to as retrieval-augmented generation (RAG).
We build RAG models where the parametric memory is a pre-trained seq2seq transformer, and the
non-parametric memory is a dense vector index of Wikipedia, accessed with a pre-trained neural

### Generated Answer

RAG augments a pre-trained seq2seq (parametric) generation model with a non‑parametric memory implemented as a dense vector index of Wikipedia, which is accessed by a pre-trained neural retriever; the seq2seq generator conditions its output on the retrieved passages during generation [Source 3][Source 2]. Two RAG formulations are compared: one conditions on the same retrieved passages for the entire generated sequence, and the other can use different retrieved passages at different points in the generation [Source 2].

---

## Question 3

**Question:** How does RAG differ from a traditional language model that relies only on its parameters, particularly when dealing with knowledge-intensive tasks?

### Retrieved Sources

**Source 1:** Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks, page 1

> (RAG) — models which combine pre-trained parametric and non-parametric mem-
ory for language generation. We introduce RAG models where the parametric
memory is a pre-trained seq2seq model and the non-parametric memory is a dense
vector index of Wikipedia, accessed with a pre-trained neural retriever. We com-
pare two RAG formulations, one which conditions on the same retrieved passages
across the whole generated sequence, and another which can use different passages

**Source 2:** Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks, page 7

> improves results on all other tasks, especially for Open-Domain QA, where it is crucial.
Index hot-swapping An advantage of non-parametric memory models like RAG is that knowledge
can be easily updated at test time. Parametric-only models like T5 or BART need further training to
update their behavior as the world changes. To demonstrate, we build an index using the DrQA [5]
Wikipedia dump from December 2016 and compare outputs from RAG using this index to the newer

**Source 3:** Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks, page 2

> present without additional training.
Our results highlight the beneﬁts of combining parametric and non-parametric memory with genera-
tion for knowledge-intensive tasks—tasks that humans could not reasonably be expected to perform
without access to an external knowledge source. Our RAG models achieve state-of-the-art results
on open Natural Questions [29], WebQuestions [3] and CuratedTrec [2] and strongly outperform

### Generated Answer

- RAG augments a pre-trained parametric seq2seq model with a non‑parametric memory: a dense vector index of (e.g.) Wikipedia that is accessed by a pre-trained neural retriever, so generation is conditioned on retrieved passages as well as the model parameters [Source 1].

- During generation RAG can condition on retrieved passages (either the same passages for the whole output or different passages during generation), i.e. it explicitly uses external evidence rather than relying only on what is stored in its weights [Source 1].

- That combination yields substantially better performance on knowledge‑intensive and open‑domain QA tasks (RAG achieves state‑of‑the‑art results on several QA benchmarks and improves Open‑Domain QA in particular) [Source 3][Source 2].

- Crucially, because the knowledge lives in a non‑parametric index it can be updated at test time (“index hot‑swapping”), so RAG can incorporate new or changed information without further model training — something parametric‑only models (e.g., T5 or BART) require additional training to accomplish [Source 2].

In short: unlike a parameter‑only language model, RAG combines retrieval of external documents with generation, giving more accurate, updatable responses for knowledge‑intensive tasks [Source 1][Source 2][Source 3].

---

## Question 4

**Question:** What are the main differences between RAG-Sequence and RAG-Token, and how do they affect the documents used during generation?

### Retrieved Sources

**Source 1:** Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks, page 3

> distribution over generated text. In one approach, RAG-Sequence, the model uses the same document
to predict each target token. The second approach, RAG-Token, can predict each target token based
on a different document. In the following, we formally introduce both models and then describe the
pη andpθ components, as well as the training and decoding procedure.
2.1 Models
RAG-Sequence Model The RAG-Sequence model uses the same retrieved document to generate

**Source 2:** Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks, page 6

> Table 2 shows that RAG-Token performs better than RAG-Sequence on Jeopardy question generation,
with both models outperforming BART on Q-BLEU-1. 4 shows human evaluation results, over 452
pairs of generations from BART and RAG-Token. Evaluators indicated that BART was more factual
than RAG in only 7.1% of cases, while RAG was more factual in 42.7% of cases, and both RAG and
BART were factual in a further 17% of cases, clearly demonstrating the effectiveness of RAG on

**Source 3:** Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks, page 7

> Doc 5
Figure 2: RAG-Token document posteriorp(zi|x,yi,y−i) for each generated token for input “Hem-
ingway" for Jeopardy generation with 5 retrieved documents. The posterior for document 1 is high
when generating “A Farewell to Arms" and for document 2 when generating “The Sun Also Rises".
Table 3: Examples from generation tasks. RAG models generate more speciﬁc and factually accurate
responses. ‘?’ indicates factually incorrect responses, * indicates partially correct responses.

### Generated Answer

- Core modeling difference: RAG-Sequence conditions the entire generated sequence on a single retrieved document; RAG-Token allows each target token to be generated conditioned on a (potentially) different retrieved document. [Source 1]

- Mechanism/behavior: RAG-Token computes a document posterior per token (p(zi | x, yi, y−i)) so the model can switch which retrieved document it relies on as it emits tokens. RAG-Sequence keeps the same document choice for all tokens in the output. [Source 3][Source 1]

- Effect on generation: RAG-Token can pull different facts from different documents within one output (e.g., using one document when generating “A Farewell to Arms” and another when generating “The Sun Also Rises”), enabling more specific/factual outputs; empirically RAG-Token outperforms RAG-Sequence on the reported Jeopardy question generation task. [Source 3][Source 2]

---

## Question 5

**Question:** How does GPT-3 demonstrate that large language models can perform tasks from natural-language descriptions and a few examples without gradient-based updates?

### Retrieved Sources

**Source 1:** Language Models are Few-Shot Learners, page 1

> thousands of examples. By contrast, humans can generally perform a new language task from only
a few examples or from simple instructions – something which current NLP systems still largely
struggle to do. Here we show that scaling up language models greatly improves task-agnostic,
few-shot performance, sometimes even reaching competitiveness with prior state-of-the-art ﬁne-
tuning approaches. Speciﬁcally, we train GPT-3, an autoregressive language model with 175 billion

**Source 2:** Language Models are Few-Shot Learners, page 1

> tuning approaches. Speciﬁcally, we train GPT-3, an autoregressive language model with 175 billion
parameters, 10x more than any previous non-sparse language model, and test its performance in
the few-shot setting. For all tasks, GPT-3 is applied without any gradient updates or ﬁne-tuning,
with tasks and few-shot demonstrations speciﬁed purely via text interaction with the model. GPT-3
achieves strong performance on many NLP datasets, including translation, question-answering, and

**Source 3:** Language Models are Few-Shot Learners, page 14

> Figure 3.3: On TriviaQA GPT3’s performance grows smoothly with model size, suggesting that language models
continue to absorb knowledge as their capacity increases. One-shot and few-shot performance make signiﬁcant gains
over zero-shot behavior, matching and exceeding the performance of the SOTA ﬁne-tuned open-domain model, RAG
[LPP+20]
and/or the style of their answers are out-of-distribution for GPT-3. Nevertheless, GPT-3 appears able to adapt to this

### Generated Answer

GPT-3 shows this by being used in a few‑shot setting where tasks are given as natural‑language prompts plus a few examples and the model is run "as is"—with no gradient updates or fine‑tuning. Applied purely via text interaction, GPT-3 (175B parameters) achieves strong performance on many NLP tasks (e.g., translation, question answering) [Source 2], and scaling the model improves task‑agnostic few‑shot performance [Source 1]. Empirically, one‑shot and few‑shot evaluations give large gains over zero‑shot and can match or exceed the performance of state‑of‑the‑art fine‑tuned models (e.g., on TriviaQA) [Source 3].

---

## Question 6

**Question:** How does T5's text-to-text formulation allow the same model and training framework to be applied to different NLP tasks?

### Retrieved Sources

**Source 1:** Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer, page 4

> for treating every problem as a text-to-text task and describe our “Colossal Clean Crawled
Corpus” (C4), the Common Crawl-based data set we created as a source of unlabeled text
data. We refer to our model and framework as the “Text-to-Text Transfer Transformer”
(T5).
2.1 Model
Early results on transfer learning for NLP leveraged recurrent neural networks (Peters
et al., 2018; Howard and Ruder, 2018), but it has recently become more common to use

**Source 2:** Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer, page 3

> same model, loss function, hyperparameters, etc. across our diverse set of tasks. It
also provides a standard testbed for the methods included in our empirical survey.
“T5” refers to our model, which we dub the “Text-to-Text Transfer Transformer”.
summarization, and sentiment classification, to name a few. With this unified approach,
we can compare the effectiveness of different transfer learning objectives, unlabeled data

**Source 3:** Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer, page 2

> “text-to-text” problem, i.e. taking text as input and producing new text as output. This
approach is inspired by previous unifying frameworks for NLP tasks, including casting all text
problems as question answering (McCann et al., 2018), language modeling (Radford et al.,
2019), or span extraction Keskar et al. (2019b) tasks. Crucially, the text-to-text framework
allows us to directly apply the same model, objective, training procedure, and decoding

### Generated Answer

By casting every NLP problem as a text-in → text-out task, T5 standardizes the format of inputs and outputs so the same model architecture can handle all tasks (e.g., classification, summarization, QA) without task-specific heads. This makes it possible to use the same objective, loss function, training procedure, hyperparameters, and decoding strategy across a diverse set of tasks, allowing one unified model and training framework to be applied to each task [Source 3], [Source 2]. The paper frames this as treating every problem as a “text-to-text” problem and builds the T5 model around that idea [Source 1].

---

## Question 7

**Question:** Why does LoRA argue that the changes required when adapting a large language model have low intrinsic rank, and how does its approach exploit this observation?

### Retrieved Sources

**Source 1:** LoRA: Low-Rank Adaptation of Large Language Models, page 2

> We take inspiration from Li et al. (2018a); Aghajanyan et al. (2020) which show that the learned
over-parametrized models in fact reside on a low intrinsic dimension. We hypothesize that the
change in weights during model adaptation also has a low “intrinsic rank”, leading to our proposed
Low-Rank Adaptation (LoRA) approach. LoRA allows us to train some dense layers in a neural
network indirectly by optimizing rank decomposition matrices of the dense layers’ change during

**Source 2:** LoRA: Low-Rank Adaptation of Large Language Models, page 9

> 2019; Allen-Zhu & Li, 2020a). Another theoretical result in Allen-Zhu & Li (2020b) suggests that
low-rank adaptations can be useful for adversarial training. In sum, we believe that our proposed
low-rank adaptation update is well-motivated by the literature.
7 U NDERSTANDING THE LOW-RANK UPDATES
Given the empirical advantage of LoRA, we hope to further explain the properties of the low-rank
adaptation learned from downstream tasks. Note that the low-rank structure not only lowers the

**Source 3:** LoRA: Low-Rank Adaptation of Large Language Models, page 2

> network indirectly by optimizing rank decomposition matrices of the dense layers’ change during
adaptation instead, while keeping the pre-trained weights frozen, as shown in Figure 1. Using GPT-3
175B as an example, we show that a very low rank (i.e.,r in Figure 1 can be one or two) sufﬁces even
when the full rank (i.e., d) is as high as 12,288, making LoRA both storage- and compute-efﬁcient.
LoRA possesses several key advantages.

### Generated Answer

LoRA’s argument is empirical/theoretical: prior work shows over‑parameterized, pre‑trained models lie on a low intrinsic dimension, so the authors hypothesize that the weight changes needed for task adaptation likewise have a low “intrinsic rank” (i.e., can be well approximated by a low‑rank matrix) [Source 1]. This view is also supported by related theoretical results that low‑rank adaptations can be useful (e.g., for adversarial training) [Source 2].

LoRA exploits that observation by not updating the full weight matrices. Instead it freezes the pre‑trained weights and learns a low‑rank decomposition of the weight change (optimizing small rank‑r matrices that sum to the update). Practically, very small r (e.g., 1–2) suffices even when the full layer rank is huge (e.g., 12,288 for GPT‑3 175B), making adaptation much more storage‑ and compute‑efficient [Source 3].

---

## Question 8

**Question:** How does ReAct combine reasoning and acting, and why does this provide an advantage over approaches that perform reasoning without interacting with external environments?

### Retrieved Sources

**Source 1:** ReAct: Synergizing Reasoning and Acting in Language Models, page 2

> current state. Beyond such simple embodied tasks to interact with a few blocks, there have not been
studies on how reasoning and acting can be combined in a synergistic manner for general task solving,
and if such a combination can bring systematic beneﬁts compared to reasoning or acting alone.
In this work, we present ReAct, a general paradigm to combine reasoning and acting with language
models for solving diverse language reasoning and decision making tasks (Figure 1). ReAct

**Source 2:** ReAct: Synergizing Reasoning and Acting in Language Models, page 4

> only reasoning or acting across different domains. We also show in Section 3 additional beneﬁts
when ﬁnetuning is enabled, and in Section 4 how ReAct performance is robust to prompt selections.
D) Human aligned and controllable: ReAct promises an interpretable sequential decision making
and reasoning process where humans can easily inspect reasoning and factual correctness. Moreover,
humans can also control or correct the agent behavior on the go by thought editing, as shown in

**Source 3:** ReAct: Synergizing Reasoning and Acting in Language Models, page 8

> explorations and query re-formulations that are still challenging for prompting-based methods.
On the value of internal reasoning vs. external feedback To our knowledge, ReAct is the ﬁrst
demonstration of combined reasoning and action using an LLM applied to an interactive environment
within a closed-loop system. Perhaps the closest prior work is Inner Monologue (IM), from Huang
et al. (2022b), in which actions from an embodied agent are motivated by an eponymous “inner

### Generated Answer

How ReAct combines reasoning and acting
- ReAct is a general paradigm in which a language model both generates explicit reasoning (thoughts) and issues external actions in an interactive environment, operating in a closed‑loop where actions produce feedback that the model can use next [Source 1], [Source 3].

Why this is advantageous over pure reasoning (no interaction)
- Closed‑loop feedback enables exploration and query reformulation that prompting‑only methods struggle with, so the model can adapt its plan based on what it learns from the environment rather than relying solely on internal deduction [Source 3].
- The combined approach yields systematic benefits over using only reasoning or only acting for general task solving (improving performance across domains) [Source 1].
- It also produces an interpretable sequential decision and reasoning trace that humans can inspect and intervene on (e.g., thought editing), making behavior more controllable and correctable than opaque, non‑interactive reasoning alone [Source 2].

---

## Question 9

**Question:** What does Chain-of-Thought prompting reveal about the relationship between model scale, intermediate reasoning steps, and performance on complex reasoning tasks?

### Retrieved Sources

**Source 1:** Chain-of-Thought Prompting Elicits Reasoning in Large Language Models, page 16

> A Frequently Asked Questions
A.1 Why does increasing model scale improve chain-of-thought prompting?
The ﬁnding that successful chain-of-thought reasoning predictably emerges only at certain model
scales is intriguing. Scaling up language models has been shown to confer beneﬁts such as improved
performance and sample efﬁciency (Kaplan et al., 2020), but chain-of-thought reasoning is emergent
in the sense that its success cannot be predicted only by extrapolating the performance of small scale

**Source 2:** Chain-of-Thought Prompting Elicits Reasoning in Large Language Models, page 16

> parsed, due to either repetitions or logic that never arrived at a ﬁnal answer.
In summary, the success of chain-of-thought reasoning as a result of model scale is a complicated
phenomena that likely involves a variety of emergent abilities (semantic understanding, symbol
mapping, staying on topic, arithmetic ability, faithfulness, etc). Future work could more thoroughly
investigate what properties of pretraining data, model architecture, and optimization objective causally

**Source 3:** Chain-of-Thought Prompting Elicits Reasoning in Large Language Models, page 9

> outputs of language models with a chain of thought.
8 Conclusions
We have explored chain-of-thought prompting as a simple and broadly applicable method for enhanc-
ing reasoning in language models. Through experiments on arithmetic, symbolic, and commonsense
reasoning, we ﬁnd that chain-of-thought reasoning is an emergent property of model scale that allows
sufﬁciently large language models to perform reasoning tasks that otherwise have ﬂat scaling curves.

### Generated Answer

Chain-of-Thought prompting shows that having the model produce intermediate reasoning steps can substantially improve performance on complex reasoning tasks, but this benefit is an emergent effect that only appears once models reach a sufficient scale. Larger models reliably use chains of thought to solve arithmetic, symbolic, and commonsense problems that smaller models cannot, and tasks that otherwise show flat scaling curves improve when chain-of-thought is used by sufficiently large models [Source 3].  

The emergence of chain-of-thought success with scale reflects gains in multiple underlying abilities (e.g., semantic understanding, symbol mapping, staying on topic, arithmetic, faithfulness) that larger models acquire; these properties together enable effective intermediate reasoning rather than being predictable from small-model behavior alone [Source 1][Source 2]. However, chain-of-thought reasoning can still fail in some cases (e.g., outputs that are unparsed because of repetitions or logic that never reaches a final answer), indicating the phenomenon is complex and dependent on several factors of model training and architecture [Source 2].

---

## Question 10

**Question:** What limitations of RAG are identified by the authors, and how do these limitations affect the reliability or usefulness of the generated answers?

### Retrieved Sources

**Source 1:** Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks, page 6

> RAG-Tok. 17.3 22.2 40.1 41.5 72.5 89.5RAG-Seq. 14.7 21.4 40.8 44.2
to more effective marginalization over documents. Furthermore, RAG can generate correct answers
even when the correct answer is not in any retrieved document, achieving 11.8% accuracy in such
cases for NQ, where an extractive model would score 0%.
4.2 Abstractive Question Answering
As shown in Table 2, RAG-Sequence outperforms BART on Open MS-MARCO NLG by 2.6 Bleu

**Source 2:** Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks, page 6

> BART were factual in a further 17% of cases, clearly demonstrating the effectiveness of RAG on
the task over a state-of-the-art generation model. Evaluators also ﬁnd RAG generations to be more
speciﬁc by a large margin. Table 3 shows typical generations from each model.
Jeopardy questions often contain two separate pieces of information, and RAG-Token may perform
best because it can generate responses that combine content from several documents. Figure 2 shows

**Source 3:** Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks, page 6

> As shown in Table 2, RAG-Sequence outperforms BART on Open MS-MARCO NLG by 2.6 Bleu
points and 2.6 Rouge-L points. RAG approaches state-of-the-art model performance, which is
impressive given that (i) those models access gold passages with speciﬁc information required to
generate the reference answer , (ii) many questions are unanswerable without the gold passages, and
(iii) not all questions are answerable from Wikipedia alone. Table 3 shows some generated answers

### Generated Answer

The authors identify limits mainly tied to retrieval and source coverage:

- Dependence on retrieved (or “gold”) passages: many questions cannot be answered without gold passages, so if retrieval fails to return the needed passages RAG’s ability to produce correct answers is constrained [Source 3].  
- Limited source coverage: not all evaluation questions are answerable from Wikipedia alone, so using Wikipedia as the retrieval corpus limits what RAG can reliably answer [Source 3].  
- Retrieval affects reliability of generations: although RAG can sometimes produce correct answers even when the correct answer is not present in any retrieved document (11.8% accuracy on NQ in such cases), this behavior implies that when retrieval does not supply the necessary evidence the model may be making unsupported inferences, reducing the grounding and thus the reliability of some outputs [Source 1].  
- Complexity of multi-document composition: tasks that require combining information from multiple documents (e.g., Jeopardy questions with two pieces of information) place heavier demands on the method; the need to marginalize or combine across documents affects which RAG variant works best and can impact answer quality [Source 1, Source 2].

Overall, these limitations mean RAG’s usefulness and trustworthiness depend strongly on the retrieval quality and the coverage of the retrieval corpus: when relevant source passages are missing or outside the corpus, generated answers are less reliably grounded. [Source 1][Source 3][Source 2]

---

