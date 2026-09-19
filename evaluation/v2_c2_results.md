# Chunking Config 2 Evaluation Results


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

**Source 2:** Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks, page 9

> model that leverages bi-directional attention to achieve stronger performance on discriminative
and generative tasks. Our work aims to expand the space of possible tasks with a single, uniﬁed
architecture, by learning a retrieval module to augment pre-trained, generative language models.
Learned Retrieval There is signiﬁcant work on learning to retrieve documents in information
retrieval, more recently with pre-trained, neural language models [ 44, 26] similar to ours. Some
work optimizes the retrieval module to aid in a speciﬁc, downstream task such as question answering,
using search [46], reinforcement learning [6, 63, 62], or a latent variable approach [31, 20] as in our

**Source 3:** Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks, page 1

> edge is still limited, and hence on knowledge-intensive tasks, their performance
lags behind task-speciﬁc architectures. Additionally, providing provenance for their
decisions and updating their world knowledge remain open research problems. Pre-
trained models with a differentiable access mechanism to explicit non-parametric
memory have so far been only investigated for extractive downstream tasks. We
explore a general-purpose ﬁne-tuning recipe for retrieval-augmented generation
(RAG) — models which combine pre-trained parametric and non-parametric mem-
ory for language generation. We introduce RAG models where the parametric
memory is a pre-trained seq2seq model and the non-parametric memory is a dense

### Generated Answer

Retrieval-Augmented Generation (RAG) is designed to address shortcomings of large pre-trained language models on knowledge‑intensive tasks by augmenting them with a retrieval mechanism over external (non‑parametric) memory. It tackles the need for more accurate, up‑to‑date, and provenanceable access to facts for generation, where purely parametric models fall short [Source 1, Source 3].

Why parametric knowledge can be insufficient:
- Although large models store factual knowledge in their parameters, their ability to access and precisely manipulate that knowledge is limited, so they underperform on knowledge‑intensive tasks compared to task‑specific architectures [Source 1].  
- Parametric memory also makes it hard to provide provenance for generated answers and to update world knowledge, both open problems for purely parameter‑based models; RAG combines a pre‑trained seq2seq (parametric) model with a dense, non‑parametric retrieval store to address these issues [Source 3].  
- Hence learning a retrieval component to augment generation lets the model use explicit external evidence, improving accuracy, traceability, and updatability for knowledge‑heavy problems [Source 2, Source 3].

---

## Question 2

**Question:** How does RAG combine parametric and non-parametric memory during generation?

### Retrieved Sources

**Source 1:** Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks, page 1

> memory is a pre-trained seq2seq model and the non-parametric memory is a dense
vector index of Wikipedia, accessed with a pre-trained neural retriever. We com-
pare two RAG formulations, one which conditions on the same retrieved passages
across the whole generated sequence, and another which can use different passages
per token. We ﬁne-tune and evaluate our models on a wide range of knowledge-
intensive NLP tasks and set the state of the art on three open domain QA tasks,
outperforming parametric seq2seq models and task-speciﬁc retrieve-and-extract
architectures. For language generation tasks, we ﬁnd that RAG models generate
more speciﬁc, diverse and factual language than a state-of-the-art parametric-only
seq2seq baseline.
1 Introduction

**Source 2:** Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks, page 9

> could represent promising future work.
6 Discussion
In this work, we presented hybrid generation models with access to parametric and non-parametric
memory. We showed that our RAG models obtain state of the art results on open-domain QA. We
found that people prefer RAG’s generation over purely parametric BART, ﬁnding RAG more factual
and speciﬁc. We conducted an thorough investigation of the learned retrieval component, validating
its effectiveness, and we illustrated how the retrieval index can be hot-swapped to update the model
without requiring any retraining. In future work, it may be fruitful to investigate if the two components
can be jointly pre-trained from scratch, either with a denoising objective similar to BART or some

**Source 3:** Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks, page 2

> We endow pre-trained, parametric-memory generation models with a non-parametric memory through
a general-purpose ﬁne-tuning approach which we refer to as retrieval-augmented generation (RAG).
We build RAG models where the parametric memory is a pre-trained seq2seq transformer, and the
non-parametric memory is a dense vector index of Wikipedia, accessed with a pre-trained neural
retriever. We combine these components in a probabilistic model trained end-to-end (Fig. 1). The
retriever (Dense Passage Retriever [26], henceforth DPR) provides latent documents conditioned on
the input, and the seq2seq model (BART [32]) then conditions on these latent documents together with

### Generated Answer

RAG pairs a pre-trained parametric seq2seq generator (BART) with a non‑parametric memory (a dense vector index of Wikipedia accessed by a pre‑trained neural retriever). The retriever (DPR) returns latent documents conditioned on the input, and the seq2seq model conditions its generation on those retrieved passages; the whole setup is combined as a probabilistic model and fine‑tuned end‑to‑end. RAG can be implemented to condition on the same retrieved passages for an entire generated sequence or to use different retrieved passages per token during generation [Source 3][Source 1].

---

## Question 3

**Question:** How does RAG differ from a traditional language model that relies only on its parameters, particularly when dealing with knowledge-intensive tasks?

### Retrieved Sources

**Source 1:** Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks, page 2

> the non-parametric memory can be replaced to update the models’ knowledge as the world changes.1
2 Methods
We explore RAG models, which use the input sequencex to retrieve text documentsz and use them
as additional context when generating the target sequence y. As shown in Figure 1, our models
leverage two components: (i) a retriever pη(z|x) with parametersη that returns (top-K truncated)
distributions over text passages given a queryx and (ii) a generatorpθ(yi|x,z,y 1:i−1) parametrized
1Code to run experiments with RAG has been open-sourced as part of the HuggingFace Transform-
ers Library [66] and can be found at https://github.com/huggingface/transformers/blob/master/

**Source 2:** Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks, page 1

> edge is still limited, and hence on knowledge-intensive tasks, their performance
lags behind task-speciﬁc architectures. Additionally, providing provenance for their
decisions and updating their world knowledge remain open research problems. Pre-
trained models with a differentiable access mechanism to explicit non-parametric
memory have so far been only investigated for extractive downstream tasks. We
explore a general-purpose ﬁne-tuning recipe for retrieval-augmented generation
(RAG) — models which combine pre-trained parametric and non-parametric mem-
ory for language generation. We introduce RAG models where the parametric
memory is a pre-trained seq2seq model and the non-parametric memory is a dense

**Source 3:** Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks, page 5

> models that do not require such supervision will be applicable to a wider range of tasks. We explore
two variants: the standard 3-way classiﬁcation task (supports/refutes/not enough info) and the 2-way
(supports/refutes) task studied in Thorne and Vlachos [57]. In both cases we report label accuracy.
4 Results
4.1 Open-domain Question Answering
Table 1 shows results for RAG along with state-of-the-art models. On all four open-domain QA
tasks, RAG sets a new state of the art (only on the T5-comparable split for TQA). RAG combines
the generation ﬂexibility of the “closed-book” (parametric only) approaches and the performance of
"open-book" retrieval-based approaches. Unlike REALM and T5+SSM, RAG enjoys strong results

### Generated Answer

Traditional (parametric-only) language models keep knowledge only in their learned weights, which limits their up-to-dateness and performance on knowledge‑intensive tasks and makes provenance and updating hard [Source 2].

RAG differs by combining that parametric component (a pre‑trained seq2seq generator) with an explicit non‑parametric memory and a retriever: a retriever pη(z|x) returns relevant text passages given the input, and the generator pθ(yi|x,z,y1:i−1) conditions on those retrieved documents when producing output [Source 1], [Source 2]. Because the non‑parametric memory is external it can be replaced to update the model’s world knowledge as facts change [Source 1]. Empirically, this hybrid (“retrieval‑augmented”) approach keeps the generation flexibility of closed‑book models while gaining the accuracy of open‑book retrieval methods, yielding state‑of‑the‑art results on open‑domain QA benchmarks [Source 3].

---

## Question 4

**Question:** What are the main differences between RAG-Sequence and RAG-Token, and how do they affect the documents used during generation?

### Retrieved Sources

**Source 1:** Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks, page 3

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

**Source 2:** Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks, page 3

> pη andpθ components, as well as the training and decoding procedure.
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

**Source 3:** Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks, page 3

> byθ that generates a current token based on a context of the previousi− 1 tokensy1:i−1, the original
inputx and a retrieved passagez.
To train the retriever and generator end-to-end, we treat the retrieved document as a latent variable.
We propose two models that marginalize over the latent documents in different ways to produce a
distribution over generated text. In one approach, RAG-Sequence, the model uses the same document
to predict each target token. The second approach, RAG-Token, can predict each target token based
on a different document. In the following, we formally introduce both models and then describe the
pη andpθ components, as well as the training and decoding procedure.
2.1 Models

### Generated Answer

- Core difference:
  - RAG-Sequence uses a single retrieved document z to generate the entire output sequence (the same z is used for every target token) and marginalizes over the top-K documents at the sequence level [Source 2].
  - RAG-Token can pick a (potentially) different retrieved document for each output token: for each next token the generator considers each retrieved document and marginalizes over them, allowing different tokens to be conditioned on different documents [Source 1], [Source 3].

- Effect on documents used during generation:
  - RAG-Sequence: one document (per latent draw) conditions the whole generated sequence, so the output is produced from the content of a single chosen document (with top-K marginalization across documents) [Source 2].
  - RAG-Token: different tokens can be generated from different retrieved documents, enabling the generator to combine content from several documents when producing an answer (marginalization is performed for each token) [Source 1], [Source 3].

- Note: for sequence classification (target sequence length = 1) the two approaches are equivalent, since there is only one token to condition on [Source 1].

---

## Question 5

**Question:** How does GPT-3 demonstrate that large language models can perform tasks from natural-language descriptions and a few examples without gradient-based updates?

### Retrieved Sources

**Source 1:** Language Models are Few-Shot Learners, page 1

> tuning approaches. Speciﬁcally, we train GPT-3, an autoregressive language model with 175 billion
parameters, 10x more than any previous non-sparse language model, and test its performance in
the few-shot setting. For all tasks, GPT-3 is applied without any gradient updates or ﬁne-tuning,
with tasks and few-shot demonstrations speciﬁed purely via text interaction with the model. GPT-3
achieves strong performance on many NLP datasets, including translation, question-answering, and
cloze tasks, as well as several tasks that require on-the-ﬂy reasoning or domain adaptation, such as
unscrambling words, using a novel word in a sentence, or performing 3-digit arithmetic. At the same

**Source 2:** Language Models are Few-Shot Learners, page 40

> language models, both in order to focus on in-context learning performance and to reduce the complexity of our large
model implementations. However, it is very likely that incorporating these algorithmic advances could improve GPT-3’s
performance on downstream tasks, especially in the ﬁne-tuning setting, and combining GPT-3’s scale with these
algorithmic techniques is a promising direction for future work.
8 Conclusion
We presented a 175 billion parameter language model which shows strong performance on many NLP tasks and
benchmarks in the zero-shot, one-shot, and few-shot settings, in some cases nearly matching the performance of
40

**Source 3:** Language Models are Few-Shot Learners, page 1

> on a large corpus of text followed by ﬁne-tuning on a speciﬁc task. While typically task-agnostic
in architecture, this method still requires task-speciﬁc ﬁne-tuning datasets of thousands or tens of
thousands of examples. By contrast, humans can generally perform a new language task from only
a few examples or from simple instructions – something which current NLP systems still largely
struggle to do. Here we show that scaling up language models greatly improves task-agnostic,
few-shot performance, sometimes even reaching competitiveness with prior state-of-the-art ﬁne-
tuning approaches. Speciﬁcally, we train GPT-3, an autoregressive language model with 175 billion

### Generated Answer

GPT-3 is trained as a single, very large (175 billion parameter) autoregressive language model on a large text corpus and then applied to new tasks purely via text interaction (prompts) without any gradient updates or fine-tuning. Users give the model a natural-language task description and a few example input‑output pairs (zero‑, one‑, or few‑shot prompts), and the model completes the task from that context alone. With this in‑context learning approach, GPT‑3 achieves strong performance on many benchmarks (e.g., translation, question answering, cloze tasks) and on on‑the‑fly reasoning or domain‑adaptation tasks (e.g., unscrambling words, using a novel word, 3‑digit arithmetic), in some cases nearly matching prior fine‑tuned state‑of‑the‑art systems [Source 1][Source 3][Source 2].

---

## Question 6

**Question:** How does T5's text-to-text formulation allow the same model and training framework to be applied to different NLP tasks?

### Retrieved Sources

**Source 1:** Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer, page 3

> text as input and training it to generate some target text. This allows us to use the
same model, loss function, hyperparameters, etc. across our diverse set of tasks. It
also provides a standard testbed for the methods included in our empirical survey.
“T5” refers to our model, which we dub the “Text-to-Text Transfer Transformer”.
summarization, and sentiment classification, to name a few. With this unified approach,
we can compare the effectiveness of different transfer learning objectives, unlabeled data
sets, and other factors, while exploring the limits of transfer learning for NLP by scaling up
models and data sets beyond what has previously been considered.

**Source 2:** Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer, page 2

> and push the current limits of the field.
The basic idea underlying our work is to treat every text processing problem as a
“text-to-text” problem, i.e. taking text as input and producing new text as output. This
approach is inspired by previous unifying frameworks for NLP tasks, including casting all text
problems as question answering (McCann et al., 2018), language modeling (Radford et al.,
2019), or span extraction Keskar et al. (2019b) tasks. Crucially, the text-to-text framework
allows us to directly apply the same model, objective, training procedure, and decoding
process to every task we consider. We leverage this flexibility by evaluating performance

**Source 3:** Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer, page 4

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

### Generated Answer

By casting every task as "text in → text out" (e.g., input text and a target text to generate), T5 can use a single Transformer model, the same training objective/loss, the same hyperparameters and training procedure, and the same decoding process for all tasks. This unified text-to-text formulation therefore lets the exact same model and framework be applied across diverse NLP tasks (and makes direct comparisons and transfer learning straightforward) [Source 1][Source 2][Source 3].

---

## Question 7

**Question:** Why does LoRA argue that the changes required when adapting a large language model have low intrinsic rank, and how does its approach exploit this observation?

### Retrieved Sources

**Source 1:** LoRA: Low-Rank Adaptation of Large Language Models, page 12

> This suggests that the low-rank adaptation matrix potentially ampliﬁes the important features for
speciﬁc downstream tasks that were learned but not emphasized in the general pre-training model.
8 C ONCLUSION AND FUTURE WORK
Fine-tuning enormous language models is prohibitively expensive in terms of the hardware required
and the storage/switching cost for hosting independent instances for different tasks. We propose
LoRA, an efﬁcient adaptation strategy that neither introduces inference latency nor reduces input
sequence length while retaining high model quality. Importantly, it allows for quick task-switching
when deployed as a service by sharing the vast majority of the model parameters. While we focused

**Source 2:** LoRA: Low-Rank Adaptation of Large Language Models, page 2

> change in weights during model adaptation also has a low “intrinsic rank”, leading to our proposed
Low-Rank Adaptation (LoRA) approach. LoRA allows us to train some dense layers in a neural
network indirectly by optimizing rank decomposition matrices of the dense layers’ change during
adaptation instead, while keeping the pre-trained weights frozen, as shown in Figure 1. Using GPT-3
175B as an example, we show that a very low rank (i.e.,r in Figure 1 can be one or two) sufﬁces even
when the full rank (i.e., d) is as high as 12,288, making LoRA both storage- and compute-efﬁcient.
LoRA possesses several key advantages.
• A pre-trained model can be shared and used to build many small LoRA modules for dif-

**Source 3:** LoRA: Low-Rank Adaptation of Large Language Models, page 4

> A Generalization of Full Fine-tuning. A more general form of ﬁne-tuning allows the training of
a subset of the pre-trained parameters. LoRA takes a step further and does not require the accumu-
lated gradient update to weight matrices to have full-rank during adaptation. This means that when
applying LoRA to all weight matrices and training all biases 2, we roughly recover the expressive-
ness of full ﬁne-tuning by setting the LoRA rankr to the rank of the pre-trained weight matrices. In
other words, as we increase the number of trainable parameters 3, training LoRA roughly converges
to training the original model, while adapter-based methods converges to an MLP and preﬁx-based
methods to a model that cannot take long input sequences.

### Generated Answer

LoRA starts from the empirical observation that the weight changes needed for task adaptation lie in a low-dimensional subspace — i.e., the accumulated update matrix has a low “intrinsic rank” even when the full weight matrices are huge (for example, experiments with GPT‑3 175B show very small ranks like r=1 or 2 suffice) [Source 2].  

LoRA exploits this by parameterizing the weight update as a low‑rank decomposition (two small matrices) and keeping the pre‑trained weights frozen; only the small low‑rank factors are trained. This makes adaptation much more storage‑ and compute‑efficient, lets a single pre‑trained model be shared with many compact task modules, and still recover the expressiveness of full fine‑tuning as r is increased. The low‑rank adapter also effectively amplifies task‑relevant features that were learned but not emphasized by pretraining [Sources 2, 3, 1].

---

## Question 8

**Question:** How does ReAct combine reasoning and acting, and why does this provide an advantage over approaches that perform reasoning without interacting with external environments?

### Retrieved Sources

**Source 1:** ReAct: Synergizing Reasoning and Acting in Language Models, page 8

> On the value of internal reasoning vs. external feedback To our knowledge, ReAct is the ﬁrst
demonstration of combined reasoning and action using an LLM applied to an interactive environment
within a closed-loop system. Perhaps the closest prior work is Inner Monologue (IM), from Huang
et al. (2022b), in which actions from an embodied agent are motivated by an eponymous “inner
monologue”. However, IM’s “inner monologue” is limited to observations of the environment
state and what needs to be completed by the agent for the goal to be satisﬁed. In contrast, the
reasoning traces in ReAct for decision making is ﬂexible and sparse, allowing diverse reasoning
types (see Section 2) to be induced for different tasks.

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

> reasoning tasks, and reasoning in interactive tasks; (4) we analyze the limitations ofReAct under the
prompting setup (i.e. limited support of reasoning and acting behaviors), and perform initial ﬁnetuning
experiments showing the potential of ReAct to improve with additional training data. Scaling up
ReAct to train and operate on more tasks and combining it with complementary paradigms like
reinforcement learning could further unlock the potential of large language models.
2 REAC T: S YNERGIZING REASONING + AC TING
Consider a general setup of an agent interacting with an environment for task solving. At time
stept, an agent receives an observationot∈O from the environment and takes an actionat∈A

### Generated Answer

ReAct interleaves explicit verbal reasoning traces with concrete actions: the LLM is prompted to both "reason" (produce high‑level plans and chains of thought) and "act" (query or manipulate an external environment) in a single, closed‑loop process. This lets the model use reasoning to decide actions ("reason to act") and then use observations from those actions to update its reasoning ("act to reason") [Source 2].

This provides advantages over reasoning‑only approaches because (1) it creates a closed‑loop between internal thought and external feedback, so the model can incorporate new information from the environment into subsequent reasoning and planning [Source 2]; (2) it supports flexible, sparse, and diverse reasoning traces tailored to different tasks rather than being limited to fixed observations/goals, as in prior inner‑monologue approaches [Source 1]; and (3) it is the first demonstrated way to combine reasoning and action in an LLM for interactive tasks, enabling dynamic adjustment of plans based on environment responses [Source 1], [Source 3].

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
models, as chain of thought actually hurts performance for most models smaller than 10B parameters.
The question of why model scale improves chain-of-thought prompting is certainly multi-faceted, and

**Source 2:** Chain-of-Thought Prompting Elicits Reasoning in Large Language Models, page 9

> experiments on commonsense reasoning underscored how the linguistic nature of chain-of-thought
reasoning makes it generally applicable (Section 4). Finally, we showed that for symbolic reasoning,
chain-of-thought prompting facilitates OOD generalization to longer sequence lengths (Section 5). In
all experiments, chain-of-thought reasoning is elicited simply by prompting an off-the-shelf language
model. No language models were ﬁnetuned in the process of writing this paper.
The emergence of chain-of-thought reasoning as a result of model scale has been a prevailing theme
(Wei et al., 2022b). For many reasoning tasks where standard prompting has a ﬂat scaling curve, chain-

**Source 3:** Chain-of-Thought Prompting Elicits Reasoning in Large Language Models, page 9

> outputs of language models with a chain of thought.
8 Conclusions
We have explored chain-of-thought prompting as a simple and broadly applicable method for enhanc-
ing reasoning in language models. Through experiments on arithmetic, symbolic, and commonsense
reasoning, we ﬁnd that chain-of-thought reasoning is an emergent property of model scale that allows
sufﬁciently large language models to perform reasoning tasks that otherwise have ﬂat scaling curves.
Broadening the range of reasoning tasks that language models can perform will hopefully inspire
further work on language-based approaches to reasoning.
9

### Generated Answer

Chain-of-thought prompting shows that the ability to produce useful intermediate reasoning steps is an emergent property of model scale: sufficiently large models can use chain-of-thought to solve complex reasoning tasks that otherwise show little improvement with scale, whereas for many models below ~10B parameters chain-of-thought can even hurt performance [Source 1], [Source 3]. When elicited by prompting (no finetuning), these intermediate, language-form reasoning traces boost performance across arithmetic, symbolic, and commonsense tasks and enable out‑of‑distribution generalization (e.g., to longer sequence lengths) that standard prompting does not achieve [Source 2], [Source 3]. In short: larger scale enables reliable chain-of-thought generation, and those intermediate steps materially improve complex-reasoning performance.

---

## Question 10

**Question:** What limitations of RAG are identified by the authors, and how do these limitations affect the reliability or usefulness of the generated answers?

### Retrieved Sources

**Source 1:** Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks, page 5

> "open-book" retrieval-based approaches. Unlike REALM and T5+SSM, RAG enjoys strong results
without expensive, specialized “salient span masking” pre-training [20]. It is worth noting that RAG’s
retriever is initialized using DPR’s retriever, which uses retrieval supervision on Natural Questions
and TriviaQA. RAG compares favourably to the DPR QA system, which uses a BERT-based “cross-
encoder” to re-rank documents, along with an extractive reader. RAG demonstrates that neither a
re-ranker nor extractive reader is necessary for state-of-the-art performance.
There are several advantages to generating answers even when it is possible to extract them. Docu-

**Source 2:** Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks, page 6

> B-1 QB-1 R-L B-1 Label Acc.
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

**Source 3:** Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks, page 7

> 4.5 Additional Results
Generation Diversity Section 4.3 shows that RAG models are more factual and speciﬁc than
BART for Jeopardy question generation. Following recent work on diversity-promoting decoding
[33, 59, 39], we also investigate generation diversity by calculating the ratio of distinct ngrams to
total ngrams generated by different models. Table 5 shows that RAG-Sequence’s generations are
more diverse than RAG-Token’s, and both are signiﬁcantly more diverse than BART without needing
any diversity-promoting decoding.
Retrieval Ablations A key feature of RAG is learning to retrieve relevant information for the task.
To assess the effectiveness of the retrieval mechanism, we run ablations where we freeze the retriever

### Generated Answer

The excerpts do not present a dedicated “limitations” list, but they imply two main limitations and their effects:

- Dependence on the retriever’s initialization and supervision. RAG’s retriever is initialized from DPR, which was trained with retrieval supervision on Natural Questions and TriviaQA; this ties RAG’s retrieval capability to that retriever and its supervised domains [Source 1]. Effect: retrieval (and thus answer quality) may be constrained by the retriever’s training/data coverage.

- Reduced reliability when retrieval misses relevant documents. The authors note RAG can still produce correct answers when the correct answer is not in any retrieved document, but only at 11.8% accuracy on NQ (an extractive model would score 0% in that setting) [Source 2]. Effect: answers are less reliable if retrieval fails — RAG can sometimes hallucinate or infer correctly, but most of the time it will not recover the missing evidence.

The provided context also mentions retrieval ablations but does not give their results or other limitations in detail, so I cannot report further limitations or their effects beyond what the excerpts show [Source 3].

---

