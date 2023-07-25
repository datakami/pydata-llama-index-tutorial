---
title: 'Industry dynamics in Generative AI'
date: '2023-07-07'
summary: "In Good Strategy/Bad Strategy, Richard Rumelt explores how we can take advantage of significant shifts in society to gain an edge over competitors. This works well, even for really small companies. Rumelt provides thinking points for analyzing these changes in his book. How can we apply Rumelt's ideas to generative AI?"
author: 'Judith van Stegeren'
---

I recently read a fascinating book on business strategy called [Good Strategy/Bad Strategy](https://www.goodreads.com/book/show/11721966-good-strategy-bad-strategy) by Richard Rumelt. Rumelt wants to get rid of the sloppy thinking and vagueness which often plague conversations about strategy, by teaching the reader to think about strategic decision-making in a structured way. I loved the book! If you love long-term thinking and can't stand hypes and vapid management speak, this is a great read.

I particularly liked the many case studies with which the author illustrates his points, many of them from technology companies. Rumelt discusses cases such as the rise of Cisco as a market leader in computer networks, and NVIDIA's domination in the GPU market.

The chapter "Using Dynamics" explores taking advantage of significant shifts in society to gain a competitive edge. Rumelt writes that these "waves of change" are primarily external, meaning they're beyond the control of any single organization. They arise from various factors like technological advancements, changes in costs, competition, politics, and customer perceptions.

Recognizing these waves of change as they happen can be tricky. We tend to only see their visible effects, and our view is further clouded by expectations, biases, and groupthink. Because of this mental fog of war, it's hard to understand the underlying causes and effects. However, if we can see past the surface-level impact and develop our own vision of these shifts, we can turn this into genuine competitive advantages for our business.

This chapter struck me as particularly relevant for the generative AI space, where we are currently experiencing a wave of change. So how can we apply Rumelt's ideas about dynamics to generative AI?

Rumelt provides various thinking points ("guideposts") for analyzing waves of change. Some of these can be applied to the current state of generative AI.

### Rising fixed costs

When a crucial resource or activity becomes increasingly expensive over time, it can lead to changes in consumer and company behaviors.

The costs for training a language model with average performance from scratch have significantly increased, especially since 2020. Training a model that is on par with GPT-4, and then running it in production is out of reach for most companies. OpenAI's foundational models have become too large to train (and run) on regular infrastructure, which lead to their collaboration with industry giant Microsoft.

If smaller companies want to get access to high performing AI models, they have a few options:

- build on top of proprietary foundational models, risking being dependent on their model supplier;
- find creative ways to get the same performance from smaller models or domain-specific data;
- find cheap sources of compute and storage, in-house or at cloud providers.

OpenAI has a virtual monopoly on high-performing general use LLMs at the moment, and they might raise their prices in the future. When that happens, I expect more people will consider using open source models instead, many of which are currently being developed.

### Predictable biases in forecasting

Biases in our thinking can hinder our understanding of the current situation. Rumelt gives examples: many people assume that something that has been growing in the past will continue to grow indefinitely (for example revenue, share prices). Other fallacies are: expecting that new industry developments will always result in battles between industry leaders, and assuming that industry best practices will be determined solely by current incumbents.

I see a lot of these biases and blind spots in action at the moment, ranging from rose-colored glasses ("AI will solve all our problems”) to doomsday thinking ("AI will lead to human extinction").

People seem to expect AI capabilities to increase exponentially in the future, without any interruptions or plateaus. However, AI is susceptible to hype cycles, where we alternate between periods of optimism and increased attention for AI, and periods of skepticism and lack of interest in AI applications. For example, working on neural networks in the 90s was considered career suicide in academia.

At this moment, we might be running into the limitations of Transformers-based large language models for the first time. Issues such as hallucination, limited context length, biases, and inconsistent performance need to be addressed if we want to see large-scale adoption. We don’t have any new innovations that structurally deal with these problems — yet.

In the meantime, the share prices of companies that are supposedly active in the AI domain have gone through the roof, even though most real AI companies are hemorrhaging money and struggling with user retention. I don't doubt that we will soon see the release of GPT-5, a model even more gargantuan than its predecessor. But is larger always better, for language models? (So far, [it seems the answer is yes](https://gwern.net/note/scaling), but if we can’t come up with ways to scale the quality of training data as well, we’re in for large language models that are trained on conspiracy theories, white supremacy and other toxic content.) And besides model size, should we let OpenAI determine the best practices concerning AI ethics, user data handling, LLM safety, and interface design?

### Incumbent response

How do established industry leaders react to new developments within their industry? Often, they either take no action or focus on protecting their intellectual property, falling victim to first-mover disadvantage.

AI is more a technological approach than a coherent industry, so it's hard to pinpoint which companies can be considered AI companies. There are very few "pure AI" public companies, as most are regular technology companies using AI as a tool in their toolbelt. As the sector is so new and unconsolidated, there are very few large pure AI private companies like OpenAI. So who are the industry leaders in LLMs, apart from OpenAI?

Zooming out to the technology sector at large, the renewed battle between Microsoft and Google in the search engine space is very illustrative of Rumelt's notion of "incumbent response". It has turned into a veritable arms race, where both companies try to be the first to release a new technology. This resulted in in hurried presentations of early-stage technology, that might not be quite yet ready for large-scale production release. Both OpenAI and Microsoft's infrastructure are groaning under the weight of ChatGPT and Bing inference requests, and Google had to retract the integration of their LLM Bard after it predictably made an error during the launch presentation.

### Industry attractor state

What would the industry look like if it efficiently met market demands? Which developments and business decisions move the industry closer to this state, and which hinder progress in reaching it?

Generative AI still needs to mature as an industry. We need proper tooling for understanding, building, monitoring, and maintaining generative AI systems. Businesses need to gain better control over their data, because this is a prerequisite to building proprietary unique AI systems. After all, most language models are supplied as API endpoints, and if you use the vanilla version of an LLM, your competitors can use the exact same technology as you. We also need to explore alternative business models for generative AI, beyond mobile apps and SaaS. And businesses need to address AI activism, deal with concerns about privacy and copyright, come up with an AI usage policy for employees, and make plans for responsible stewardship of customer data. All these developments are just starting.

### So... what now?

Rumelt’s guideposts raise more questions than they answer, but they provide a framework to reflect on the changes happening in the generative AI space. His case studies illustrate that small upstart companies can beat their behemoth competitors, if they manage to strategically use sweeping changes to their advantage. If this applies to inventions like microprocessors and GPU chips, it must hold for generative AI as well.

We're *in* the change as it happens, and the best we can do is try to observe it as objectively as possible, without being tricked by our biases and expectations. The generative AI domain needs our proactive thinking to grow into a mature industry. We need to think and talk about all the thorny issues of applied generative AI: from user data stewardship to model explainability, data quality to user interfaces, and scalable infrastructure to long-term model monitoring. Building and learning in public can help with that.

We are in luck: even though generative AI is high-tech, it is not solely in the hands of a few big companies. Most natural language processing techniques are described in open-access research papers, and many technologies underlying large language models are open source. As a result, open source projects, individual researcher-engineers, startups building in public, and user communities can contribute as much to the direction of generative AI as large technology companies.

### Related reads

- Bert Hubert’s [startup library](https://berthub.eu/library.html) page. Bert recommended Rumelt's book to me.
- John Kay’s [review](http://www.johnkay.com/2012/01/04/good-strategybad-strategy-richard-rumelt/) of Good Strategy/Bad Strategy
- Andreessen Horowitz report [Who owns the generative AI platform?](https://a16z.com/2023/01/19/who-owns-the-generative-ai-platform/)
