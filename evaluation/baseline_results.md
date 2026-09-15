# V1 Baseline Evaluation Results

These results were generated using the fixed V1 configuration and evaluation questions.

## Question 1

**Question:** What problem does Retrieval-Augmented Generation aim to address, and why can a language model's parametric knowledge be insufficient?

### Retrieved Sources

**Source 1:** Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks, page 1

> outperforming parametric seq2seq models and task-speciﬁc retrieve-and-extract
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

**Source 3:** Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks, page 1

> trained models with a differentiable access mechanism to explicit non-parametric
memory have so far been only investigated for extractive downstream tasks. We
explore a general-purpose ﬁne-tuning recipe for retrieval-augmented generation
(RAG) — models which combine pre-trained parametric and non-parametric mem-
ory for language generation. We introduce RAG models where the parametric
memory is a pre-trained seq2seq model and the non-parametric memory is a dense
vector index of Wikipedia, accessed with a pre-trained neural retriever. We com-
pare two RAG formulations, one which conditions on the same retrieved passages
across the whole generated sequence, and another which can use different passages
per token. We ﬁne-tune and evaluate our models on a wide range of knowledge-
intensive NLP tasks and set the state of the art on three open domain QA tasks,
outperforming parametric seq2seq models and task-speciﬁc retrieve-and-extract

### Generated Answer

Retrieval-Augmented Generation (RAG) aims to address the shortcomings of parametric-only language models on knowledge‑intensive tasks by combining a pre-trained seq2seq (parametric) model with an explicit non‑parametric memory (a retrieved dense index of documents) so the generator can condition on external, updatable evidence when producing text [Source 3].  

A language model’s parametric knowledge can be insufficient because such models can’t easily expand or revise what they “know,” have limited ability to precisely access or manipulate facts, may produce hallucinations, and don’t readily provide provenance for their outputs—limitations that hurt performance on knowledge‑intensive tasks and make updating or explaining their answers difficult [Source 1][Source 2].

---

## Question 2

**Question:** How does RAG combine parametric and non-parametric memory during generation?

### Retrieved Sources

**Source 1:** Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks, page 9

> approaches, where a similar training input-output pair is retrieved for a given input, and then edited
to provide a ﬁnal output. These approaches have proved successful in a number of domains including
Machine Translation [ 18, 22] and Semantic Parsing [21]. Our approach does have several differences,
including less of emphasis on lightly editing a retrieved item, but on aggregating content from several
pieces of retrieved content, as well as learning latent retrieval, and retrieving evidence documents
rather than related training pairs. This said, RAG techniques may work well in these settings, and
could represent promising future work.
6 Discussion
In this work, we presented hybrid generation models with access to parametric and non-parametric
memory. We showed that our RAG models obtain state of the art results on open-domain QA. We
found that people prefer RAG’s generation over purely parametric BART, ﬁnding RAG more factual

**Source 2:** Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks, page 2

> parametric and non-parametric memory components are pre-trained and pre-loaded with extensive
knowledge. Crucially, by using pre-trained access mechanisms, the ability to access knowledge is
present without additional training.
Our results highlight the beneﬁts of combining parametric and non-parametric memory with genera-
tion for knowledge-intensive tasks—tasks that humans could not reasonably be expected to perform
without access to an external knowledge source. Our RAG models achieve state-of-the-art results
on open Natural Questions [29], WebQuestions [3] and CuratedTrec [2] and strongly outperform
recent approaches that use specialised pre-training objectives on TriviaQA [24]. Despite these being
extractive tasks, we ﬁnd that unconstrained generation outperforms previous extractive approaches.
For knowledge-intensive generation, we experiment with MS-MARCO [1] and Jeopardy question
generation, and we ﬁnd that our models generate responses that are more factual, speciﬁc, and

**Source 3:** Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks, page 1

> trained models with a differentiable access mechanism to explicit non-parametric
memory have so far been only investigated for extractive downstream tasks. We
explore a general-purpose ﬁne-tuning recipe for retrieval-augmented generation
(RAG) — models which combine pre-trained parametric and non-parametric mem-
ory for language generation. We introduce RAG models where the parametric
memory is a pre-trained seq2seq model and the non-parametric memory is a dense
vector index of Wikipedia, accessed with a pre-trained neural retriever. We com-
pare two RAG formulations, one which conditions on the same retrieved passages
across the whole generated sequence, and another which can use different passages
per token. We ﬁne-tune and evaluate our models on a wide range of knowledge-
intensive NLP tasks and set the state of the art on three open domain QA tasks,
outperforming parametric seq2seq models and task-speciﬁc retrieve-and-extract

### Generated Answer

RAG pairs a pre-trained parametric generator (a seq2seq model) with a pre-built non‑parametric memory (a dense vector index of Wikipedia accessed by a pre-trained neural retriever) and conditions generation on retrieved documents [Source 3]. During generation the model uses the retrieved passages as evidence — either conditioning on the same retrieved passages for the whole output or allowing different retrieved passages per token — effectively aggregating content from multiple retrieved pieces and learning latent retrieval over evidence documents rather than editing single retrieved training pairs [Source 3], [Source 1]. Both the parametric and non‑parametric components are pre‑trained so access to external knowledge is available without additional training [Source 2].

---

## Question 3

**Question:** How does RAG differ from a traditional language model that relies only on its parameters, particularly when dealing with knowledge-intensive tasks?

### Retrieved Sources

**Source 1:** Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks, page 9

> approaches, where a similar training input-output pair is retrieved for a given input, and then edited
to provide a ﬁnal output. These approaches have proved successful in a number of domains including
Machine Translation [ 18, 22] and Semantic Parsing [21]. Our approach does have several differences,
including less of emphasis on lightly editing a retrieved item, but on aggregating content from several
pieces of retrieved content, as well as learning latent retrieval, and retrieving evidence documents
rather than related training pairs. This said, RAG techniques may work well in these settings, and
could represent promising future work.
6 Discussion
In this work, we presented hybrid generation models with access to parametric and non-parametric
memory. We showed that our RAG models obtain state of the art results on open-domain QA. We
found that people prefer RAG’s generation over purely parametric BART, ﬁnding RAG more factual

**Source 2:** Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks, page 1

> trained models with a differentiable access mechanism to explicit non-parametric
memory have so far been only investigated for extractive downstream tasks. We
explore a general-purpose ﬁne-tuning recipe for retrieval-augmented generation
(RAG) — models which combine pre-trained parametric and non-parametric mem-
ory for language generation. We introduce RAG models where the parametric
memory is a pre-trained seq2seq model and the non-parametric memory is a dense
vector index of Wikipedia, accessed with a pre-trained neural retriever. We com-
pare two RAG formulations, one which conditions on the same retrieved passages
across the whole generated sequence, and another which can use different passages
per token. We ﬁne-tune and evaluate our models on a wide range of knowledge-
intensive NLP tasks and set the state of the art on three open domain QA tasks,
outperforming parametric seq2seq models and task-speciﬁc retrieve-and-extract

**Source 3:** Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks, page 1

> outperforming parametric seq2seq models and task-speciﬁc retrieve-and-extract
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

### Generated Answer

Short answer: RAG augments a parameter‑only language model with an explicit retrieval mechanism that brings in external, updatable evidence at generation time, which makes it more factual, specific and better on knowledge‑intensive tasks.

Details:
- Traditional parametric models store knowledge only in their weights and so “cannot easily expand or revise their memory, can’t straightforwardly provide insight into their predictions, and may produce ‘hallucinations’” [Source 3].
- RAG combines a pre‑trained seq2seq parametric model with a non‑parametric dense vector index (Wikipedia) accessed by a neural retriever, i.e., it has differentiable access to explicit external memory rather than relying solely on parameters [Source 2].
- Architecturally RAG can condition on retrieved passages (either the same passages for the whole output or different passages per token) and is designed to aggregate content from several retrieved documents, learn latent retrieval, and retrieve evidence documents rather than just related training pairs [Source 2, Source 1].
- Empirically, this leads to state‑of‑the‑art results on open‑domain QA and to generations that are more factual, specific and diverse (and preferred by people) compared with parametric‑only seq2seq baselines [Source 2, Source 1, Source 3].

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

**Source 2:** Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks, page 6

> BART generations (see §4.5).
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

**Source 3:** Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks, page 3

> is marginalized to get the seq2seq probability p(y|x) via a top-K approximation. Concretely, the
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
documents when producing an answer. Concretely, the top K documents are retrieved using the
retriever, and then the generator produces a distribution for the next output token for each document,
before marginalizing, and repeating the process with the following output token, Formally, we deﬁne:
pRAG-Token(y|x) ≈
N∏
i
∑
z∈top-k(p(·|x))
pη(z|x)pθ(yi|x,z,y 1:i−1)

### Generated Answer

- Core difference in latent-document use:
  - RAG-Sequence treats the retrieved document as a single latent variable for the entire output: for each candidate document z the generator computes pθ(y|x,z) (a product over all tokens) and these document-level probabilities are then marginalized over the top-K retrieved docs [Source 1][Source 3].
  - RAG-Token allows a (potentially) different latent document to be chosen for each output token: for every token the model marginalizes over the top-K documents (i.e., the sum over documents is inside the product over tokens) so each token can be produced conditionally on a different retrieved passage [Source 3].

- How this affects documents used during generation:
  - RAG-Sequence effectively picks one document at a time to generate the whole sequence (marginalizing across documents only at the sequence level) [Source 3].
  - RAG-Token can mix information from multiple documents within a single generated answer because it can attend to or select different documents for different tokens; this enables combining content across documents and has been observed to improve factuality/specificity on tasks like Jeopardy question generation [Source 2][Source 3].

---

## Question 5

**Question:** How does GPT-3 demonstrate that large language models can perform tasks from natural-language descriptions and a few examples without gradient-based updates?

### Retrieved Sources

**Source 1:** Language Models are Few-Shot Learners, page 1

> a few examples or from simple instructions – something which current NLP systems still largely
struggle to do. Here we show that scaling up language models greatly improves task-agnostic,
few-shot performance, sometimes even reaching competitiveness with prior state-of-the-art ﬁne-
tuning approaches. Speciﬁcally, we train GPT-3, an autoregressive language model with 175 billion
parameters, 10x more than any previous non-sparse language model, and test its performance in
the few-shot setting. For all tasks, GPT-3 is applied without any gradient updates or ﬁne-tuning,
with tasks and few-shot demonstrations speciﬁed purely via text interaction with the model. GPT-3
achieves strong performance on many NLP datasets, including translation, question-answering, and
cloze tasks, as well as several tasks that require on-the-ﬂy reasoning or domain adaptation, such as
unscrambling words, using a novel word in a sentence, or performing 3-digit arithmetic. At the same

**Source 2:** Language Models are Few-Shot Learners, page 34

> possibly from data that is very different in organization and style than the test data. Ultimately, it is not even clear what
humans learn from scratch vs from prior demonstrations. Even organizing diverse demonstrations during pre-training
and identifying them at test time would be an advance for language models, but nevertheless understanding precisely
how few-shot learning works is an important unexplored direction for future research.
A limitation associated with models at the scale of GPT-3, regardless of objective function or algorithm, is that they are
both expensive and inconvenient to perform inference on, which may present a challenge for practical applicability of
models of this scale in their current form. One possible future direction to address this is distillation [HVD15] of large
models down to a manageable size for speciﬁc tasks. Large models such as GPT-3 contain a very wide range of skills,

**Source 3:** Language Models are Few-Shot Learners, page 40

> Algorithmic innovation in language models over the last two years has been enormous, including denoising-based
bidirectionality [DCLT18], preﬁxLM [DL15] and encoder-decoder architectures [LLG+19, RSR+19], random permu-
tations during training [YDY+19], architectures that improve the efﬁciency of sampling [DYY+19], improvements in
data and training procedures [LOG+19], and efﬁciency increases in the embedding parameters [LCG+19]. Many of
these techniques provide signiﬁcant gains on downstream tasks. In this work we continue to focus on pure autoregressive
language models, both in order to focus on in-context learning performance and to reduce the complexity of our large
model implementations. However, it is very likely that incorporating these algorithmic advances could improve GPT-3’s
performance on downstream tasks, especially in the ﬁne-tuning setting, and combining GPT-3’s scale with these
algorithmic techniques is a promising direction for future work.
8 Conclusion

### Generated Answer

GPT-3 shows this by being trained as a very large (175 billion-parameter) autoregressive language model and then evaluated in a "few-shot" protocol where tasks are given as natural-language instructions plus a small number of examples in the input prompt. Crucially, GPT-3 is applied without any gradient updates or fine‑tuning — all task behavior comes from the text interaction (in‑context learning) — and yet it achieves strong performance across many NLP tasks (translation, question answering, cloze, and on‑the‑fly reasoning/domain‑adaptation tasks such as unscrambling words, using a novel word, or 3‑digit arithmetic), in some cases rivaling prior fine‑tuned systems [Source 1]. The authors emphasize that they intentionally used a pure autoregressive model to study this in‑context, few‑shot ability and that the large scale of the model is key to its task‑agnostic few‑shot performance [Source 3]; they also note that such large models exhibit a wide range of skills, motivating this demonstration [Source 2].

---

## Question 6

**Question:** How does T5's text-to-text formulation allow the same model and training framework to be applied to different NLP tasks?

### Retrieved Sources

**Source 1:** Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer, page 3

> “T5” refers to our model, which we dub the “Text-to-Text Transfer Transformer”.
summarization, and sentiment classification, to name a few. With this unified approach,
we can compare the effectiveness of different transfer learning objectives, unlabeled data
sets, and other factors, while exploring the limits of transfer learning for NLP by scaling up
models and data sets beyond what has previously been considered.
We emphasize that our goal is not to propose new methods but instead to provide a
comprehensive perspective on where the field stands. As such, our work primarily comprises
a survey, exploration, and empirical comparison of existing techniques. We also explore the
limits of current approaches by scaling up the insights from our systematic study (training
models up to11 billion parameters) to obtain state-of-the-art results in many of the tasks
we consider. In order to perform experiments at this scale, we introduce the “Colossal Clean

**Source 2:** Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer, page 41

> with the findings in Section 3.6, we find that additional pre-training improves performance
over the baseline. Nevertheless, T5-Base substantially outperforms baseline-1T on all
downstream tasks. This suggests that scale is not the only factor that contributes to T5’s
success. We hypothesize that the larger models benefit not only from their increased size
but also from these non-scaling factors.
4. Reflection
Having completed our systematic study, we wrap up by first recapping some of our most
significant findings. Our results provide some high-level perspective on which avenues of
research might be more or less promising. To conclude, we outline some topics we think
might provide effective approaches for further progressing the field.
4.1 Takeaways
Text-to-text Our text-to-text framework provides a simple way to train a single model
on a wide variety of text tasks using the same loss function and decoding procedure.

**Source 3:** Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer, page 2

> 2019), or span extraction Keskar et al. (2019b) tasks. Crucially, the text-to-text framework
allows us to directly apply the same model, objective, training procedure, and decoding
process to every task we consider. We leverage this flexibility by evaluating performance
on a wide variety of English-based NLP problems, including question answering, document
2. http://commoncrawl.org
2

### Generated Answer

T5 casts every NLP problem as a text-to-text task — both the input and the desired output are plain text — so the same model, loss, training procedure, and decoding process can be used for all tasks. This lets a single transformer handle question answering, summarization, sentiment classification, span extraction, etc., without changing the objective or decoder across tasks [Source 3], and provides a simple unified way to train one model on a wide variety of text tasks using the same loss function and decoding procedure [Source 2; Source 1].

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

LoRA’s starting hypothesis is that the weight changes needed to adapt a very large pre-trained model occupy a much smaller (“low intrinsic”) subspace than the full parameter space. This idea is motivated by prior work showing over‑parameterized models live on a low intrinsic dimension, and by the observation that the actual adaptation delta (∆W) can be well-approximated by a low-rank matrix [Source 2], [Source 3].

LoRA exploits that observation by freezing the original pre-trained weights and learning only a low-rank decomposition of the weight updates: it injects trainable rank‑decomposition matrices into each Transformer layer and optimizes those smaller matrices instead of re‑training all parameters. This greatly reduces the number of trainable parameters while retaining performance — empirically LoRA is competitive even with very small rank r, and subspace analyses show increasing r often does not add meaningful directions beyond the low-rank update [Source 1], [Source 3]. (LoRA’s authors note a small‑r solution may not suffice for every possible downstream shift, e.g., a different language.) [Source 1], [Source 2], [Source 3].

---

## Question 8

**Question:** How does ReAct combine reasoning and acting, and why does this provide an advantage over approaches that perform reasoning without interacting with external environments?

### Retrieved Sources

**Source 1:** ReAct: Synergizing Reasoning and Acting in Language Models, page 2

> In this work, we present ReAct, a general paradigm to combine reasoning and acting with language
models for solving diverse language reasoning and decision making tasks (Figure 1). ReAct
prompts LLMs to generate both verbal reasoning traces and actions pertaining to a task in an
interleaved manner, which allows the model to perform dynamic reasoning to create, maintain, and
adjust high-level plans for acting (reason to act), while also interact with the external environments
(e.g. Wikipedia) to incorporate additional information into reasoning (act to reason).
2

**Source 2:** ReAct: Synergizing Reasoning and Acting in Language Models, page 3

> perform extensive experiments across diverse benchmarks to showcase the advantage of ReAct in a
few-shot learning setup over prior approaches that perform either reasoning or action generation in
isolation; (3) we present systematic ablations and analysis to understand the importance of acting in
reasoning tasks, and reasoning in interactive tasks; (4) we analyze the limitations ofReAct under the
prompting setup (i.e. limited support of reasoning and acting behaviors), and perform initial ﬁnetuning
experiments showing the potential of ReAct to improve with additional training data. Scaling up
ReAct to train and operate on more tasks and combining it with complementary paradigms like
reinforcement learning could further unlock the potential of large language models.
2 REAC T: S YNERGIZING REASONING + AC TING
Consider a general setup of an agent interacting with an environment for task solving. At time

**Source 3:** ReAct: Synergizing Reasoning and Acting in Language Models, page 2

> environments (Ahn et al., 2022; Nakano et al., 2021; Yao et al., 2020; Huang et al., 2022a), with
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

ReAct prompts a language model to produce verbal reasoning traces and environment-directed actions in an interleaved way — i.e., the model "reasons to act" (creates, maintains, and adjusts high‑level plans) and "acts to reason" (queries or interacts with external sources to bring new information back into its reasoning) rather than doing those steps separately [Source 1].  

This synergy helps because prior methods either only generate actions from observations or only produce reasoning traces without interaction; they typically do not use the model to reason about high‑level goals, maintain a working memory for acting, or incorporate new information from the environment. By combining reasoning and acting, ReAct can dynamically update plans based on external evidence and thus outperforms approaches that reason in isolation (empirically shown in few‑shot experiments) [Source 3][Source 2].

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
we made a preliminary attempt to shed insight into it via error analysis. This small analysis involved
manually reading 45 errors made by PaLM 62B and categorizing them into semantic understanding
(20 errors), one step missing (18 errors), and other errors (7 errors). The “other category” included

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

**Source 3:** Chain-of-Thought Prompting Elicits Reasoning in Large Language Models, page 3

> intermediate steps, which means that additional computation can be allocated to problems
that require more reasoning steps.
2. Second, a chain of thought provides an interpretable window into the behavior of the model,
suggesting how it might have arrived at a particular answer and providing opportunities
to debug where the reasoning path went wrong (although fully characterizing a model’s
computations that support an answer remains an open question).
3. Third, chain-of-thought reasoning can be used for tasks such as math word problems,
commonsense reasoning, and symbolic manipulation, and is potentially applicable (at least
in principle) to any task that humans can solve via language.
4. Finally, chain-of-thought reasoning can be readily elicited in sufﬁciently large off-the-shelf
language models simply by including examples of chain of thought sequences into the
exemplars of few-shot prompting.

### Generated Answer

Chain-of-thought (CoT) prompting shows that intermediate reasoning steps, when elicited in model outputs, interact strongly with model scale to determine performance on complex reasoning tasks:

- CoT enables the model to allocate additional computation to problems that require more reasoning steps—i.e., explicitly producing intermediate steps helps solve harder problems (supports improved performance on tasks like math, commonsense, and symbolic manipulation) [Source 3].  
- The ability to benefit from CoT emerges only at larger model scales: CoT reasoning predictably appears only above certain sizes (it often hurts performance for most models smaller than ~10B parameters), so scaling up is critical for CoT to help [Source 1].  
- When present, CoT dramatically changes scaling behavior: tasks with flat scaling under standard prompting show sharply improved (dramatically increasing) scaling curves with CoT, expanding the set of tasks large models can perform successfully; it also aids OOD generalization to longer sequences in symbolic reasoning [Source 2].  
- CoT also provides an interpretable window into model behavior and helps diagnose errors (though models even at large scale still make errors such as missing a step or semantic misunderstandings, as seen in manual error analyses) [Source 3; Source 1].  

In short, larger model scale enables effective use of intermediate reasoning steps via CoT, which in turn substantially improves performance and generalization on complex reasoning tasks and makes model reasoning more interpretable.

---

## Question 10

**Question:** What limitations of RAG are identified by the authors, and how do these limitations affect the reliability or usefulness of the generated answers?

### Retrieved Sources

**Source 1:** Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks, page 5

> 4 Results
4.1 Open-domain Question Answering
Table 1 shows results for RAG along with state-of-the-art models. On all four open-domain QA
tasks, RAG sets a new state of the art (only on the T5-comparable split for TQA). RAG combines
the generation ﬂexibility of the “closed-book” (parametric only) approaches and the performance of
"open-book" retrieval-based approaches. Unlike REALM and T5+SSM, RAG enjoys strong results
without expensive, specialized “salient span masking” pre-training [20]. It is worth noting that RAG’s
retriever is initialized using DPR’s retriever, which uses retrieval supervision on Natural Questions
and TriviaQA. RAG compares favourably to the DPR QA system, which uses a BERT-based “cross-
encoder” to re-rank documents, along with an extractive reader. RAG demonstrates that neither a
re-ranker nor extractive reader is necessary for state-of-the-art performance.
There are several advantages to generating answers even when it is possible to extract them. Docu-

**Source 2:** Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks, page 6

> even when the correct answer is not in any retrieved document, achieving 11.8% accuracy in such
cases for NQ, where an extractive model would score 0%.
4.2 Abstractive Question Answering
As shown in Table 2, RAG-Sequence outperforms BART on Open MS-MARCO NLG by 2.6 Bleu
points and 2.6 Rouge-L points. RAG approaches state-of-the-art model performance, which is
impressive given that (i) those models access gold passages with speciﬁc information required to
generate the reference answer , (ii) many questions are unanswerable without the gold passages, and
(iii) not all questions are answerable from Wikipedia alone. Table 3 shows some generated answers
from our models. Qualitatively, we ﬁnd that RAG models hallucinate less and generate factually
correct text more often than BART. Later, we also show that RAG generations are more diverse than
BART generations (see §4.5).
4.3 Jeopardy Question Generation

**Source 3:** Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks, page 7

> RAG-S This 14th century work is divided into 3 sections: "Inferno", "Purgatorio" & "Paradiso"
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

### Generated Answer

The authors identify three main limitations that affect RAG’s reliability/usefulness:

- Retrieval failures — the correct answer may not be present in retrieved documents. When this happens RAG still sometimes produces the correct answer (11.8% accuracy on NQ when no retrieved document contains the answer), but an extractive reader would get 0% in those cases, so missing evidence reduces reliability and makes outputs less verifiable [Source 2].  
- Imperfect alignment with gold evidence — the top retrieved document comes from a gold article only 71% of the time (90% within top‑10), so RAG does not always retrieve the most relevant or authoritative sources; this weakens the factual grounding of generated answers and can lower accuracy or faithfulness [Source 3].  
- Dependence on the retrieval corpus — some questions are not answerable from the knowledge source used (e.g., Wikipedia), and other systems that access gold passages have an advantage for such items; therefore RAG’s usefulness is limited when the corpus lacks the required information [Source 2].

These limitations mean RAG’s generations can be less reliable when retrieval misses or the corpus lacks needed facts, and users should be cautious about unsupported or unverifiable answers [Source 2, Source 3].

---

