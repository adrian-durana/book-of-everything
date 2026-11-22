# STAT2004 Statistical Modelling & Analysis: transcription, part 1 of 4 (HW 01–25)

_Transcription phase. Nothing here is book text yet. No dates are recorded (lecture and assignment dates in the sources are omitted); only the semester would be given if a source needed identifying._

## Sources (all four parts)
| Code | Source | Role | Where transcribed |
|---|---|---|---|
| **HW nn** | 51 photos of the handwritten notes, one notebook page per photo, numbered in shooting order (file name under each heading). They cover the **second half** of the course only: confidence intervals → hypothesis testing → GLRT → goodness of fit → ANOVA → linear models. | **Main source, second half** | Parts 1–2, in full |
| **PE** | *STAT2004: Notes on Point Estimation*, typed, 28 pp., written by the author and a classmate from the lecturer's notes. | **Main source, first half** (estimation) | Part 3: section/page index, items, suspected errors |
| **CN** | STAT2004 course notes (the lecturer's typed background notes), 146 pp., Part I Probability (Ch 1–3) and Part II Statistics (Ch 4–10). | Supplement, whole course | Part 3: section/page index, figure descriptions, content found only here |
| **R Lnn** | Later iteration (tutored by the author), first-half lecturer: 12 handwritten lecture PDFs (L01–L12, 54 pp.): sampling distributions, estimation, likelihood, information, asymptotics, multiple regression, diagnostics, Gauss–Markov, logistic regression. | Supplement | Part 4: page-by-page summary with content found nowhere else |
| **A WwLl** | Later iteration, second-half lecturer: handwritten lecture PDFs Weeks 7–13 (67 pp.; Weeks 7–8 sit in the `STAT2004_Ross` folder, Weeks 9–13 in `STAT2004_Alan`). Closely parallel to HW. | Supplement | Part 4: page-by-page summary |
| **AC w / Tut w** | Later iteration: applied-class sheets Weeks 2–6 with solutions, Week 7 solutions; tutorial sheets Weeks 8–9 with solutions. Exercises only. | Example/exercise pool | Part 3: question index |
| — | `Cheatsheet.pdf` and `Lab08-State Machines.pdf` (in `STAT2004_Ross.zip`) are **CSSE2010** (digital logic, AVR assembly), not STAT2004. | Out of scope | Not used |

Page counts: HW 51 pages; PE 28 pp.; CN 146 pp.; R lectures 54 pp.; A lectures 67 pp.; applied classes/tutorials 22 sheets.

## Legibility check (HW photos)
All 51 photos were read in order at full resolution. **No retakes are needed.** Every photo has a broad diagonal shadow from the phone across the page, but the ink is readable through it on every page; sharpness and exposure are fine (the two lowest sharpness scores, HW 27 and HW 29, are sparse pages and read cleanly). No page is cut off.
Content that cannot be read is in the notebook itself, so a retake won't help:
- **HW 04**: the last line of the CI for $\mu$ has a solid ink blot at the start of both denominators (`[illegible]` marked; the intended $s/\sqrt n$ is clear from the line above).
- **HW 27**: the degrees of freedom on $\chi^2$ are covered by an ink blot, with "$n-1$" written beneath (`[illegible]` marked).
- **HW 29**: one word blotted out ("bad [·] scientists"); doesn't affect content.
Small ambiguities are resolved in brackets where they occur (HW 14 "109.5", HW 26 $k$ vs $h$, HW 33 table entries; each checked against margins or arithmetic).

## Conventions
Wording, structure and labels (Def., Thm., Proof, Ex., Rem., N. = note) follow the notes. Maths uses `notation.tex` macros (`\Prob`, `\E`, `\Var`, `\Normal`, `\ChiSq`, `\iid`, `\vect`, `\mat`, `\T`, `\Bin`, `\Pois`, `\Mnom`, …). Square brackets [ ] hold transcriber's notes; `[possible error: …]` flags a suspected mistake (nothing is silently corrected; arithmetic was re-computed where marked "Checked"); `[illegible]` marks unreadable text. Crossed-out text is noted only where it carries meaning. Figures are described in enough detail to redraw in TikZ. Cross-references: "CN §x.y" = course notes section, "A W9L1-2" etc. = the later iteration's lecture (part 4).

**This part:** confidence intervals, pivots, hypothesis testing (errors, power, Neyman–Pearson, LRT, p-values, duality), GLRT and its two-sample examples.

---

### HW 01 (`20261121_231336.jpg`): Confidence intervals

**Confidence intervals**

**N.** The question we want to answer is:
How *confident* can we be that our sample statistic is *close* to our population parameter?

Closeness can be formalised as a 'margin of error'.
Confidence can be formalised as a 'level of confidence'.

Recall that a confidence interval for a proportion $p$ can be constructed by:
$$
\underbrace{\hat p}_{\text{point estimate}} \pm \underbrace{z_{\alpha/2}\,\underbrace{\sqrt{p(1-p)/n}}_{\text{(sample) standard error of estimate}}}_{\text{margin of error}} \;=\; \underbrace{1-\alpha}_{\text{level of confidence}}
$$
[The "$= 1-\alpha$" is written to the right of the interval, as shorthand for "this interval has confidence level $1-\alpha$".] [possible error: the standard error is labelled "(sample) standard error of estimate" but written with $p$, not $\hat p$; the computable interval uses $\sqrt{\hat p(1-\hat p)/n}$ (CN §6.3, (6.4)).]

Also recall that:
- a confidence interval changes from sample to sample, but the population parameter remains constant
- the *critical values* $z_{\alpha/2}$ come from the standard normal distribution $\Normal(0,1)$. (WHY?)
- the critical values do NOT depend on the underlying parameter $p$. (WHY?)

These questions are answered by pivot variables.

*Figure:* none (underbraces only, reproduced above).

---

### HW 02 (`20261121_231340.jpg`): Pivot variables

**Pivot variables**

**Def.** *Pivot variables.* A pivot variable is a theoretical (and often non-computable) transformation of a random variable such that the distribution no longer depends on unknown parameters.

**Ex.** Let $X_1,\dots,X_n \iid \Normal(\mu,\sigma^2)$, where $\mu$ unknown, $\sigma^2$ known.
We know the distribution of $\bar X$: $\bar X \sim \Normal(\mu, \sigma^2/n)$.
Thus a theoretical transformation is
$$\frac{\bar X - \mu}{\sigma/\sqrt n} \sim \Normal(0,1) \quad \Big\}\ \text{no longer depends on unknown parameters}$$
Hence 'standardisation' is an example of a pivot.

Pivot variables can be used to:
- construct confidence intervals
- construct hypothesis testing

**Ex.** (continued) The 95% CI, for example, is:
$$
\begin{aligned}
0.95 &= \Prob\bigl(-1.96 \le \Normal(0,1) \le 1.96\bigr) && \Big\}\ \text{purely prob. statement about normal dist.}\\
&= \Prob\Bigl(-1.96 \le \frac{\bar X - \mu}{\sigma/\sqrt n} \le 1.96\Bigr) && \leftarrow \text{pivot}\\
&= \dots = \Prob\Bigl(\bar X - 1.96\frac{\sigma}{\sqrt n} \le \mu \le \bar X + 1.96\frac{\sigma}{\sqrt n}\Bigr)
\end{aligned}
$$
which is how the confidence interval is derived.
Thus we can be 95% confident that the interval $\bar X \pm 1.96\,\sigma/\sqrt n$ contains the population mean $\mu$.

*Figure:* none.

---

### HW 03 (`20261121_231348.jpg`): Normal distribution: one sample ($\mu$)

**Normal distribution: one sample ($\mu$)**

**N.** The concept of pivot variables are even more useful in more complex / realistic scenarios, like when $\mu$ and $\sigma^2$ are both unknown.

**Ex.** Let $X_1,\dots,X_n \iid \Normal(\mu,\sigma^2)$ where $\mu,\sigma^2$ unknown.
We know that the MLE of $\mu$ is $\bar X = \frac1n\sum X_i$, which has a distribution $\bar X \sim \Normal(\mu,\sigma^2/n)$.
We also know that the (bias-corrected) MLE of $\sigma^2$ is $s^2 = \frac{1}{n-1}\sum (X_i - \bar X)^2$ with distribution $(n-1)s^2/\sigma^2 \sim \ChiSq{n-1}$.
Moreover, $\bar X$ and $s^2$ are independent (WHY?).

Consider the following transformation:
$$
T = \frac{\bar X - \mu}{s/\sqrt n} = \frac{\Bigl(\dfrac{\bar X - \mu}{\sigma/\sqrt n}\Bigr)}{s/\sigma}
\quad \begin{matrix} \}\ \sim \Normal(0,1) \\[2pt] \}\ \sqrt{\ChiSq{n-1}/(n-1)} \end{matrix}
\quad \Big\}\ \text{independent}
$$
which, by definition, is the $T_{n-1}$ distribution.
Thus $T$ is a theoretical transformation of our data that has a distribution that no longer depends on unknown parameters, so $T$ is a pivot variable.

To construct a $1-\alpha$ confidence interval for $\mu$ given unknown $\sigma^2$, we again start with a probabilistic statement:
$$
\begin{aligned}
1-\alpha &= \Prob\bigl(-t^{(1-\alpha/2)} \le T_{n-1} \le t^{(1-\alpha/2)}\bigr)\\
&= \Prob\Bigl(-t^{(1-\alpha/2)} \le \frac{\bar X - \mu}{s/\sqrt n} \le t^{(1-\alpha/2)}\Bigr) && \leftarrow \text{pivot}\\
&= \dots = \Prob\Bigl(\bar X - \frac{t^{(1-\alpha/2)}\,s}{[\text{blotted}]/\sqrt n} \le \mu \le \bar X + \frac{t^{(1-\alpha/2)}\,s}{[\text{blotted}]/\sqrt n}\Bigr)
\end{aligned}
$$
which is how the CI is formally derived.

[illegible: in the last line both denominators begin with a solid ink blot (a crossed-out symbol) followed by "$/\sqrt n$". In the notebook itself; a retake won't help.] [possible error: as written, the bounds read $\bar X \pm t^{(1-\alpha/2)} s/(\,\cdot/\sqrt n)$; from the line above they should be $\bar X \pm t^{(1-\alpha/2)}\, s/\sqrt n$ (CN §6.1.1, (6.2)).]
[Notation: $t^{(1-\alpha/2)}$ is the $1-\alpha/2$ quantile of $T_{n-1}$; the subscript $n-1$ is omitted on the quantile.]

*Figure:* none.

---

### HW 04 (`20261121_231354.jpg`): Normal distribution: one sample ($\sigma^2$)

**Normal distribution: one sample ($\sigma^2$)**

**N.** Not all confidence intervals are symmetric.
In fact, not all confidence intervals are additive in their margins of error — some are multiplicative!

**Ex.** Let $X_1,\dots,X_n \iid \Normal(\mu,\sigma^2)$, where $\mu,\sigma^2$ unknown.
We already know that
$$\frac{(n-1)s^2}{\sigma^2} \sim \ChiSq{n-1} \quad \Big\}\ \text{does not depend on unknown parameters}$$
and so it is a pivot.
Note that $\chi^2$ are not symmetric and is left-leaning.
We again start with a probabilistic statement (as we have a pivot):
$$
\begin{aligned}
1-\alpha &= \Prob\bigl(\chi^{2\,(\alpha/2)} \le \ChiSq{n-1} \le \chi^{2\,(1-\alpha/2)}\bigr)\\
&= \Prob\Bigl(\chi^{2\,(\alpha/2)} \le \frac{(n-1)s^2}{\sigma^2} \le \chi^{2\,(1-\alpha/2)}\Bigr)\\
&= \dots = \Prob\Bigl(\frac{(n-1)s^2}{\chi^{2\,(1-\alpha/2)}} \le \sigma^2 \le \frac{(n-1)s^2}{\chi^{2\,(\alpha/2)}}\Bigr)
\end{aligned}
$$
Thus an $(1-\alpha)$ CI for $\sigma^2$ can be constructed by:
$$\left(\frac{(n-1)s^2}{\chi^{2\,(1-\alpha/2)}_{n-1}},\ \frac{(n-1)s^2}{\chi^{2\,(\alpha/2)}_{n-1}}\right)$$
Note that: $\chi^{2\,(\alpha/2)}_{n-1}$ $\}$ a quantile of $\ChiSq{n-1}$ and thus a known number.

["left-leaning": the notes' word for the skew of the $\chi^2$ density (mass to the left, long right tail). Kept as written.]

*Figure:* none.

---
### HW 05 (`20261121_231401.jpg`): Binomial distribution: one sample

**Binomial distribution: one sample**

**N.** Recall the motivation for a binomial distribution:
A random sample of size $n$ is taken, and the number of successes $X$ is recorded. Recall
$$X \sim \Bin(n,p) \quad \Big\}\ p \text{ is pop}^{\text{n}}\text{ proportion of success}$$
["popn" is written over a crossed-out "popo".]

In general, there are no pivot transformations for discrete random variables do not exist. However, we can still construct asymptotic pivots.
[Wording as written (double negative); the meaning is "pivot transformations for discrete random variables do not exist in general".]

Recall the sample proportion has expected value $p$ with a standard error $\sqrt{p(1-p)/n}$. We also know from the central limit theorem that $\hat p$ has an asymp. normal distribution. This gives the following transformation:
$$\frac{\hat p - p}{\sqrt{\hat p(1-\hat p)/n}} \longrightarrow \Normal(0,1) \quad \text{for large } n$$
which is an asymptotic pivot.

To construct a $1-\alpha$ confidence interval for $p$, we again start
$$
\begin{aligned}
1-\alpha &= \Prob\bigl(z_{\alpha/2} \le \Normal(0,1) \le z_{1-\alpha/2}\bigr)\\
&= \Prob\Bigl(z_{\alpha/2} \le \frac{\hat p - p}{\sqrt{\hat p(1-\hat p)/n}} \le z_{1-\alpha/2}\Bigr)\\
&= \dots = \Prob\Bigl(\hat p - z_{\alpha/2}\sqrt{\tfrac{\hat p(1-\hat p)}{n}} \le p \le \hat p + z_{\alpha/2}\sqrt{\tfrac{\hat p(1-\hat p)}{n}}\Bigr)
\end{aligned}
$$
[possible error: the first two lines use $z_{\alpha/2}$ as the lower ($\alpha/2$) quantile, which is negative; the last line uses $z_{\alpha/2}$ as the positive upper critical value (as on HW 01). With the first convention the bounds would be $\hat p \pm z_{1-\alpha/2}\sqrt{\cdot}$. Notation is inconsistent within the page.]

This method is only an approximation as the CLT requires $n$ to be sufficiently large. (HOW LARGE?)
A general rule of thumb is that $n$ has to be large enough to observe at least ten successes and failures.
If $n$ is not large enough, use alternative methods (e.g. simulations, invert hypothesis tests, …)

*Figure:* none.

---

### HW 06 (`20261121_231405.jpg`): General confidence intervals

**General confidence intervals**

**N.** The general [one word crossed out] definition of a confidence interval

Let $X_1,\dots,X_n$ be data from a population depending on some parameter $\theta$. Then $(T_1(\vect x), T_2(\vect x))$ is an exact $1-\alpha$ confidence interval if $T_1, T_2$ are functions of the data alone, and that
$$\Prob\bigl(T_1(\vect x) \le \theta \le T_2(\vect x)\bigr) = 1-\alpha \qquad \forall\, \theta \in \Omega$$
If $\Prob\bigl(T_1(\vect x) \le \theta \le T_2(\vect x)\bigr) \ge 1-\alpha$, $\forall\, \theta\in\Omega$ then this is called a conservative CI with level (at least) $1-\alpha$.
[The $x$ in $T_i(x)$ is underlined (vector notation), lower case; inside $\Prob$ it should be the random $\vect X$ (CN Def 6.1 uses $T_1(\vect X), T_2(\vect X)$). Kept as written: possible error.]

**Rem.** Here are some remarks on confidence intervals:
- Interval estimates are often more useful than a point estimate, as they provide a measure of uncertainty about your estimate alongside a level of confidence. This is one of the key differences between machine learning and statistics.
- Confidence intervals for comparing two samples exist — see reference notes
- Confidence intervals can be considered as a set of plausible parameter values that are consistent with the observed data. In this sense, CIs can be considered to be the inverse of hypothesis testing.

*Figure:* none.

---

### HW 07 (`20261121_231411.jpg`): Hypothesis testing

**Hypothesis testing**

**N.** Both point and interval estimates are important tools for obtaining a 'best guess' for an unknown parameter.
However in applied settings, we need to make decisions between two competing hypotheses $H_0$ versus $H_1$ about the underlying population parameter.

A hypothesis test (or simply, test) is a decision rule that specifies when to reject $H_0$ in favour of $H_1$.
We can construct many hypothesis tests on the same scenario.

**Ex.** Consider we are testing a new drug to lower LDL cholesterol and that we record the difference in LDL levels before and after taking the drug. Some decision rules could be:

| | Rule | Underlying pop. para. | Hypo. test |
|---|---|---|---|
| (1) | $\bar X \ge c_1$ for some $c_1 > 0$ | $\mu$ (avg. improvement of pop.) | $H_0: \mu = 0$, $H_1: \mu > 0$ |
| (2) | $\operatorname{med}(\vect X) \ge c_2$ for some $c_2 > 0$ | $m$ (pop. median) | $H_0: m = 0$, $H_1: m > 0$ |
| (3) | $\min(\vect X) \ge c_3$ | min (population) | $H_0: \dots = 0$, $H_1: \dots > 0$ |
| (4) | $X_7 \ge 1.5$ | $\sim$ | |

[Row (4): the parameter column holds only a tilde ("~", i.e. none / not applicable); the test column is blank.]

There is no unique decision rule for a given scenario, but intuitively some decision rules are more sensible.

*Figure:* none (the table above).

---

### HW 08 (`20261121_231415.jpg`): Null and alternative hypotheses

**Null and alternative hypotheses**

**Def.** Null hypothesis vs. alternative hypothesis
- two competing claims about population parameter
- null hypothesis ($H_0$) claims nothing happens
- alternative hypothesis ($H_1$) is 'interesting' in the sense that something did happen

Mathematically, the two hypotheses are symmetric.
However, historically and practically speaking, there are good reasons to treat them asymmetrically (e.g. testing drugs before clearance, innocence until proven guilty).

We start with a single point null hypothesis i.e. $H_0: \theta = \theta_0$, where $\theta_0$ is a specified null value.
The alternative hypothesis is either:
- composite i.e. $H_1: \theta > \theta_0$ or $H_1: \theta < \theta_0$
- two-sided i.e. $H_1: \theta \ne \theta_0$

[possible error: "composite" is used for the one-sided alternatives; a two-sided alternative is also composite. CN §7.1.1 calls them left/right one-sided and two-sided; HW 10 uses "one-sided".]

**Ex.** Suppose we are measuring the acceleration due to gravity, which is accepted to be $g = 9.807\,\mathrm{ms^{-2}}$. You suggest the machine (to measure gravity) is miscalibrated. The null & alternative hypotheses are:
$$H_0: \mu = g \quad\text{vs.}\quad H_1: \mu \ne g$$

Note that the two hypotheses have nothing to do with the data — we dispute a parameter of a population.

*Figure:* none.

---
### HW 09 (`20261121_231422.jpg`): Test statistics and critical regions

**Test statistics and critical regions**

**Def.** *Test statistic.* The decision rule for deciding between our hypotheses $H_0, H_1$ must be based on the data $X_1,\dots,X_n$ observed. We consider some statistic $T(X_1,\dots,X_n)$. While the choice of the statistic is arbitrary, we can use statistical principles to suggest a suitable statistic.

The method of moments suggests:
- $\bar X$ for testing $\mu$
- $s^2$ for testing $\sigma^2$
  (and so on)

Maximum likelihood estimation suggests:
- $\bar X$ for testing $\mu$ if $X \sim \Normal(\mu,\sigma^2)$
- $1/\bar X$ for testing $\lambda$ if $X \sim \Expo(\lambda)$
- $\max(\bar X)$ for testing $\theta$ if $X \sim \Unif(0,\theta)$

$\Big\}$ given the model is known!

[possible error: "$\max(\bar X)$" should be $\max(\vect X) = X_{(n)}$, the MLE of $\theta$ for $\Unif(0,\theta)$.]

Or we can use a more general (and powerful) approach by appealing to the likelihood ratio principle.

**Def.** *Critical regions.* Once we identify a parameter of interest, formulated hypotheses and chosen the test statistic $T(\vect X)$, we can propose a decision rule based on the outcome of $T$:

$\ast$ Reject $H_0$ in favour of $H_1$ if $T$ falls in some critical/rejection region $C$

This can be one or two-sided depending on the hypothesis.
- One-sided: $[c,\infty)$ if $T \ge c$ OR $(-\infty,c]$ if $T \le c$
- Two-sided: $(-\infty,c] \cup [c_2,\infty)$ if $T \ne c$

[possible error: the two-sided region mixes $c$ and $c_2$ (presumably $(-\infty,c_1]\cup[c_2,\infty)$); "if $T \ge c$" etc. are shorthand for the alternative's direction.]

*Figure:* none.

---

### HW 10 (`20261121_231426.jpg`): Errors (Type I)

**Errors (Type I)**

**N.** How do we judge the merits of a particular rule?
How does it compare to competing rules?
For example, consider the three tests:
- Reject $H_0$ in favour of $H_1$, if $\bar x \ge 0.3$;
- 〃 if $\bar x \ge 0.5$; less Type I error, less power
- 〃 if $\bar x \ge 0.2$; [one word scribbled out] more Type I, more power

[Context, "the exposition": the LDL-drug example of HW 07, rule (1), $H_0: \mu = 0$ vs $H_1: \mu > 0$. The ditto marks "^" under "Reject $H_0$ in favour of $H_1$" are reproduced as 〃.]

When we make a decision based on some sort of rule, we may possibly make one of two types of errors:
- Accidentally reject $H_0$ when it is true (Type I)
- Accidentally retain $H_0$ when it is false (Type II)

**Def.** *Type I error.* The probability of a Type I error is given by
$$\alpha = \underbrace{\Prob\bigl(T(\vect X) \in C \given H_0\bigr)}_{\text{reject } H_0 \text{, given } H_0 \text{ is true}} = \underbrace{\Prob_{H_0}\bigl(T(\vect X) \in C\bigr)}_{\text{prob. 'under } H_0\text{'}}$$
This $\alpha$ is also called the 'significance level' of the test.
To compute $\alpha$ we must know the dist. of $T(\vect X)$ under $H_0$.
- We can assume a model outright for $\vect X$
- We can apply limit theorems (e.g.) CLT to approx.

**Ex.** Consider the decision rule from the exposition. Suppose $\sigma = 1.1$. What is the Type I error?
$$
\alpha = \Prob_{H_0}(\bar X \ge 0.3) = \Prob_{H_0}\Bigl(\frac{\bar X - 0}{1.1/\sqrt{27}} \ge \frac{0.3 - 0}{1.1/\sqrt{27}}\Bigr) \quad \Big\}\ \text{given } n = 27
$$
$$\overset{\text{CLT}}{\approx} \Prob_{H_0}(Z \ge 1.417) = 0.078$$

For reference, $\alpha$ for the other two tests are $0.009$, $0.172$.
We want to restrict Type I error to at most 5%.
The value of $c$ for this case would be $0.348$.
[The "$c$" is written above an ink blot that crosses out the original symbol.]
[Checked: $0.3\sqrt{27}/1.1 = 1.417$, $\Prob(Z\ge 1.417)=0.078$; $c=0.5$: $0.009$; $c=0.2$: $0.172$; $1.645 \times 1.1/\sqrt{27} = 0.348$. All correct.]

*Figure:* none.

---

### HW 11 (`20261121_231432.jpg`): Errors (Type II)

**Errors (Type II)**

**N.** It seems tempting to minimise Type I error. However, the only test that acheives this is to always accept $H_0$. This lacks power — i.e. the ability to detect an effect if one exists.

**Def.** *Type II error and power.* The probability of a Type II error is given by
$$
\begin{aligned}
\beta &= \underbrace{\Prob\bigl(T(\vect X) \notin C \given H_1\bigr)}_{\text{accept } H_0\text{, given } H_0 \text{ is false } (H_1 \text{ true})} = \underbrace{\Prob_{H_1}\bigl(T(\vect X) \notin C\bigr)}_{\text{prob. 'under' } H_1}\\
&= 1 - \underbrace{\Prob_{H_1}\bigl(T(\vect X) \in C\bigr)}_{\text{accept } H_1\text{, given } H_1 \text{ is true (i.e. power)}}
\end{aligned}
$$
The power of a test is the probability of rejecting $H_0$ when it is in fact false. It is related to Type II error via:
$$\text{power} = \Prob_{H_1}\bigl(T(\vect X) \in C\bigr) = 1 - \beta$$

**N.** As $H_1$ is typically a composite hypothesis (e.g. $H_0: \mu > 0$) there are many parameter values in the alternative. We can compute the power for each value and graph it as a function of the parameter. This is called a power curve.
[possible error: the example should read $H_1: \mu > 0$.]

*Figure:* none.

---

### HW 12 (`20261121_231437.jpg`): Power

**Power**

**Ex.** Consider the situation in the exposition. We know that the test $\{\bar X \ge 0.35\}$ has $\alpha = 0.05$. What is the power of the test?
$$
\begin{aligned}
\text{power} &= \Prob_{\mu=0.1}(\bar X \ge 0.35)\\
&= \Prob_{\mu=0.1}\Bigl(\frac{\bar X - 0.1}{1.1/\sqrt{27}} \ge \frac{0.35 - 0.1}{1.1/\sqrt{27}}\Bigr)\\
&\approx \Prob(Z \ge 1.181)\\
&= 0.119
\end{aligned}
$$
Thus the test $\{\bar X \ge 0.35\}$ will correctly detect the drug is effective 11.9% of the time if the effect of the drug is $0.1\,\mathrm{mmol/L}$.
[$c = 0.348$ from HW 10 is rounded to $0.35$; with $c=0.35$, $\alpha \approx 0.049$. Arithmetic checked: $0.25\sqrt{27}/1.1 = 1.181$, $\Prob(Z \ge 1.181) = 0.119$.]

**Hw.** Use software to plot the power curve for all values of $\mu \in [0, 0.7]$.

*Figure:* none (the power curve is set as homework, not drawn).

---
### HW 13 (`20261121_231443.jpg`): Neyman–Pearson lemma, LRT (1)

**Neyman–Pearson lemma, LRT**

**N.** We discuss the Neyman–Pearson paradigm.
Aim for a test that:
- restricts Type I error to a small $\alpha$
  (e.g. medicine $\alpha = 0.01$, biological $\alpha \approx 0.05$, social sci. $\alpha = 0.10$)
- maximises power under the alternatives

We can prove that such a test exists and is unique.
We can also construct such a test based on the likelihood ratio principle.

**Def.** *Likelihood ratio test.* Let $L(\theta;\vect x) = f_\theta(\vect x)$ be the likelihood function evaluated at $\theta$ given data $\vect x$. Suppose (for now) that we are deciding between a single null hypothesis ($H_0: \theta = \theta_0$) vs. a single alternative hypothesis ($H_1: \theta = \theta_1$).
Consider the likelihood ratio:
$$\frac{L(\theta_0 \given \vect x)}{L(\theta_1 \given \vect x)} \quad \begin{matrix}\leftarrow \text{likelihood of obs. } \vect x \text{ under } H_0\\ \leftarrow \text{likelihood of obs. } \vect x \text{ under } H_1\end{matrix}$$
This leads us to the likelihood ratio test (LRT):
$$\text{Reject } H_0: \theta = \theta_0 \text{ in favour of } H_1: \theta = \theta_1 \quad \text{if} \quad \frac{L(\theta_0 \given \vect x)}{L(\theta_1 \given \vect x)} \le c$$
[Notation switches from $L(\theta;\vect x)$ to $L(\theta \given \vect x)$ within the definition.]

**Rem.** The LRT often simplifies to familiar tests.
Moreover, the LRT is the <u>most powerful</u> test possible.

$\ast$ (↳) [This block is the continuation of the $\ast$ at the foot of HW 14, which derives $\{\bar x \ge a\}$.]
If we want to restrict Type I to at most $\alpha$ then
$$
\begin{aligned}
\alpha &= \Prob_{H_0}(\bar X \ge a)\\
&\overset{\text{CLT}}{\approx} \Prob_{H_0}\bigl(Z \ge z^{(1-\alpha)}\bigr)\\
&= \Prob_{H_0}\bigl(\bar X \ge \mu_0 + z^{(1-\alpha)}\sigma/\sqrt n\bigr)
\end{aligned}
$$
["Type I" and "$\alpha$" are written above two ink blots that cross out the original words. The "CLT" label sits under the first "=" and the second line uses "≈"; for normal data (HW 14) the result is exact. Kept as written.]

*Figure:* none.

---

### HW 14 (`20261121_231448.jpg`): Neyman–Pearson lemma, LRT (2)

**Neyman–Pearson lemma, LRT**

**Def.** *Neyman–Pearson lemma.* Suppose we have a test such that the LRT that rejects $H_0: \theta = \theta_0$ in favour of $H_1: \theta = \theta_1$ if
$$\frac{L(\theta_0 \given \vect x)}{L(\theta_1 \given \vect x)} \le c$$
such that our test has level $\alpha$. Then any other test (with level $\alpha$) must have power <u>no larger</u> than the LRT.
[Labelled "Def." in the margin although it is a theorem (lemma).]

**P.** See STAT2904
[As written: the digits read "2904" (the second digit is the writer's "9", as in "0.119" on HW 12). STAT2904 is the advanced stream of this same course (the later lectures are headed "STAT2004/2904/7004"). Proof not given in these notes.]

**Ex.** *LRT for normal mean.* Consider $X_1,\dots,X_n \iid \Normal^{*}(\mu,\sigma^2)$. We assume (for now) that $\sigma^2$ is known, while $\mu$ is unknown.
[The asterisk on $\Normal^{*}$ is picked up on HW 16 ("how critical is the normal* assumption?").]
Suppose we are testing two point hypotheses about $\mu$:
$$H_0: \mu = \mu_0 \quad\text{vs.}\quad H_1: \mu = \mu_1$$
Recall the likelihood function for normal data is:
$$L(\mu \given \vect x) = \Bigl(\frac{1}{\sqrt{2\pi\sigma^2}}\Bigr)^{n} e^{-\frac{1}{2\sigma^2}\sum (x_i - \mu)^2}$$
The LRT statistic is
$$\frac{L(\theta_0 \given \vect x)}{L(\theta_1 \given \vect x)} = \frac{e^{-\frac{1}{2\sigma^2}\sum(x_i-\mu_0)^2}}{e^{-\frac{1}{2\sigma^2}\sum(x_i-\mu_1)^2}} = e^{\frac{1}{2\sigma^2}\left(\sum(x_i-\mu_1)^2 - \sum(x_i-\mu_0)^2\right)}$$
[In the numerator of the middle fraction the subscript of $\mu$ is unclear (looks like $\mu_1$ written over); from the right-hand side it must be $\mu_0$.]
If we wish to minimise the exponent (show $H_1$):
$$
\begin{aligned}
&\sum(x_i - \bar x + \bar x - \mu_1)^2 - \sum(x_i - \bar x + \bar x - \mu_0)^2\\
&= \sum(x_i - \bar x)^2 + \dots - n(\bar x - \mu_0)^2 && \leftarrow \text{expand } (a+b)^2\\
&= n(\bar x - \mu_1)^2 - n(\bar x - \mu_0)^2 && \leftarrow \textstyle\sum(x_i - \bar x) = 0
\end{aligned}
$$
so we minimise $(\bar x - \mu_1)^2 - (\bar x - \mu_0)^2$.

Thus
$$\Bigl\{\frac{L(\theta_0 \given \vect x)}{L(\theta_1 \given \vect x)} \le c\Bigr\} \iff \{\bar x \ge a\} \qquad \ast\ \text{(↲ continued at the foot of HW 13)}$$
[The equivalence assumes $\mu_1 > \mu_0$, as in the figure; not stated in words. "(show $H_1$)" as written.]

*Figure (number line):* a horizontal line with arrowheads at both ends. Two tick marks labelled below: $\mu_0$ (left, about a quarter of the way along) and $\mu_1$ (right, near the right end). Above the line, just right of $\mu_0$, the label "$\bar x$" with a short downward arrow pointing onto the line, and a dotted arrow "$\cdots\!>$" from $\bar x$ pointing right (towards $\mu_1$), showing that larger $\bar x$ favours $H_1$.

---

### HW 15 (`20261121_231454.jpg`): Remarks on the LRT

**Remarks on the LRT**

**Rem.** The LRT is the most powerful test possible because it does not depend on our alternative hypothesis mean value $\mu_1$.
[possible error: independence of $\mu_1$ is what makes the one-sided test *uniformly* most powerful over all $\mu_1 > \mu_0$; it is most powerful for a single $\mu_1$ by the Neyman–Pearson lemma.]

**Rem.** If we are testing $H_0: \mu = \mu_0$ vs. $H_1: \mu = \mu_1 < \mu_0$, the LRT reduces to $\{\bar x < a \text{ for some } a\}$.
Thus to control the level to some $\alpha$, the test is explicitly
$$\bigl\{\bar X \le \mu_0 - z^{(1-\alpha)}\sigma/\sqrt n\bigr\}$$

If we are testing $H_0: \mu = \mu_0$ vs. $H_1: \mu \ne \mu_0$, the LRT reduces to $\{\bar x \le d_1 \cup \bar x \ge d_2\}$ [an ink blot before "∪"]
$$\iff \bigl\{\bar X \le \mu_0 - z^{(1-\alpha/2)}\sigma/\sqrt n \ \cup\ \bar X \ge \mu_0 + z^{(1-\alpha/2)}\sigma/\sqrt n\bigr\}$$
Note the two sided test requires more evidence in either direction as $\abs{z^{(1-\alpha/2)}} > \abs{z^{(1-\alpha)}}$.
This implies that in general, a two sided test cannot be UMP as a correctly chosen one sided test will always have more power than a two sided test.

*Figure:* none.

---

### HW 16 (`20261121_231500.jpg`): LRT with unknown variance

**LRT with unknown variance**

**N.** We see that for normal* data, the LRT for testing $\mu$ reduces to large and/or small values of $\bar X$. To set our critical values for the test, we used the result
$$\frac{\bar X - \mu_0}{\sigma/\sqrt n} \overset{\text{app.}}{\sim} \Normal(0,1) \quad \text{under } H_0: \mu = \mu_0$$
What if we do not know $\sigma^2$? Then we can use $S^2$ to estimate $\sigma^2$. The LRT thus reduces to large and/or small values of the pivot
$$\frac{\bar X - \mu_0}{S/\sqrt n} \sim t_{n-1} \quad \text{under } H_0: \mu = \mu_0$$
To control Type I error of the test to at most $\alpha$, we thus use the $t$-cutoff instead of $z$-cutoff.
$$
\begin{aligned}
&\bigl\{\bar X \ge \mu_0 + t^{1-\alpha}_{n-1} S/\sqrt n\bigr\} && H_0: \mu = \mu_0 \text{ vs. } H_1: \mu > \mu_0\\
&\bigl\{\bar X \le \mu_0 - t^{1-\alpha}_{n-1} S/\sqrt n\bigr\} && H_0: \mu = \mu_0 \text{ vs. } H_1: \mu < \mu_0\\
&\Bigl\{X \le \mu_0 - t^{1-\alpha/2}_{n-1}\tfrac{S}{\sqrt n} \ \cup\ X \ge \mu_0 + t^{1-\alpha/2}_{n-1}\tfrac{S}{\sqrt n}\Bigr\} && H_0: \mu = \mu_0 \text{ vs. } H_1: \mu \ne \mu_0
\end{aligned}
$$
[possible error: the two-sided line drops the bars: $X$ should be $\bar X$. The "app." on the first display: for normal data it is exact.]

Finally, how critical is the normal* assumption?
The $t$-methods are very robust against deviations from normality (see Poisson exercise in tutorial).
However, $t$-tests are not the most powerful test for non-normal data, as the likelihood functions for different functions differ, but they can still be <u>asymptotically most powerful</u>!
["for different functions differ": as written; presumably "for different distributions".]

*Figure:* none.

---
### HW 17 (`20261121_231505.jpg`): LRT example

**LRT example**

**Ex.** Let $X_1,\dots,X_n \sim \Pois(\lambda)$. Suppose we are testing between $H_0: \lambda = \lambda_0$ (e.g. 7.3) vs. $H_1: \lambda = \lambda_1 > \lambda_0$.
Construct the LRT for the scenario:
Recall the likelihood function for a Poisson is:
$$
L(\lambda; \vect x) = \prod_{i=1}^{n} e^{-\lambda}\frac{\lambda^{x_i}}{x_i!} \quad \Big\}\ \frac{\lambda^x}{x!} = e^x,\ \text{normalise}
\qquad = \frac{e^{-n\lambda}\lambda^{\sum x_i}}{\prod x_i!}
$$
[possible error: the side note "$\lambda^x/x! = e^x$, normalise" presumably means $\sum_x \lambda^x/x! = e^{\lambda}$, which is why the factor $e^{-\lambda}$ normalises the pmf.]

So the LRT statistic is
$$
\frac{L(\lambda_0;\vect x)}{L(\lambda_1;\vect x)} = \frac{e^{-n\lambda_0}\lambda_0^{\sum x_i}}{e^{-n\lambda_1}\lambda_1^{\sum x_i}} = \underbrace{e^{n(\lambda_1-\lambda_0)}}_{>0}\ \underbrace{\Bigl(\frac{\lambda_0}{\lambda_1}\Bigr)}_{<1}{}^{\sum x_i}
$$
[A small ink blot precedes the $n$ in the exponent.]
As $\lambda_1 > \lambda_0$, the LRT is small if $\sum x_i$ is large (i.e. increased sample size).
["(i.e. increased sample size)" as written; possible error: $\sum x_i$ being large is not the same as a larger sample size ($n$ is fixed).]

So the LRT for testing $H_0$ vs. $H_1$ reduces to:
$$\Bigl\{\sum x_i \ge d \text{ for some critical value } d\Bigr\}$$
Note this is the UMP for $H_0$ vs. $H_1$ for Poisson data.
Recall for Poisson data $X_i$:
$$X_1 + X_2 + \dots + X_n \sim \Pois(n\lambda).$$
This can be proved by induction (exercise).
To control Type I error to $\alpha$, we find $d$ such that
$$
\alpha \ge \Prob_{H_0}(X_1 + X_2 + \dots + X_n \ge d) = \Prob_{H_0}\bigl(\Pois(n\lambda) \ge d\bigr)
$$
[An ink blot after $X_n$.]
e.g. Suppose $n = 15$, $\lambda_0 = 7.3$, set $\alpha = 0.05$. Then
$$0.05 \ge \Prob_{H_0}\bigl(\Pois(15 \cdot 7.3) \ge d\bigr) = \Prob\bigl(\Pois(109.5) \ge d\bigr)$$
Start with (in R)
```r
> qpois(0.95, 109.5)        [1] 127
> 1 - ppois(127, 109.5)     [1] 0.04536    # <- P(... >= 128)
> 1 - ppois(126, 109.5)     [1] 0.05473    # <- P(... >= 127)
```
[In the photo the "109.5" in the R calls is written loosely and can look like "104.5"; 109.5 is meant ($15 \times 7.3$). Checked: `qpois(0.95,109.5)` = 127, $\Prob(\ge 128) = 0.04537$, $\Prob(\ge 127) = 0.05473$. Correct.]

*Figure:* none.

---

### HW 18 (`20261121_231510.jpg`): Comparing tests: LRT vs. t-test

**Comparing tests: LRT vs. t-test**

**Ex.** Thus our rule to reject $H_0: \lambda = 7.3$ in favour of $H_1: \lambda > 7.3$ is $\{X_1 + \dots + X_{15} \ge 128\}$ or $\{\bar X \ge 128/15 = 8.53 \text{ over } n = 15\}$.

Suppose we ignore the fact that this comes from a Poisson distribution, and we use the t-test:
$$\bigl\{\bar X \ge 7.3 + t^{0.95}_{14} S/\sqrt n\bigr\} = \bigl\{\bar X \ge 7.3 + 1.76\, S/\sqrt{15}\bigr\}$$
These two rules are both qual. and quant. different.
What is better?
- <u>Type I</u>: both at approx. $\alpha$
- <u>Power</u>: if data are truly Poisson, the Poisson LRT has higher power than the t-test (by Neyman–Pearson lemma). If not Poisson, the Type I error may not even be close to $\alpha$, and the power may be lower. The t-test is more robust, and always has approx. Type I error with asymp. highest power.

Thus knowing the correct model / likelihood for the data, the LRT leads to optimal decision rules.
However in practice we never know the exact distribution, and so asymptotically optimal methods (that are robust) to model misperfection is important.
"Some models are useful, but all are wrong"
[The quotation is written in this order (the usual form is "All models are wrong, but some are useful"); kept as written, no attribution in the notes.]
[Checked: $128/15 = 8.53$; $t^{0.95}_{14} = 1.761$.]

*Figure:* none.

---

### HW 19 (`20261121_231519.jpg`): P-values (1)

**P-values**

**N.** Note that we have not currently looked at an example with purely numerical data yet. This is because:
1. Identifying population parameters of interest.
2. Formulating null and alternative hypotheses of the parameter.
3. Choose the test statistic $T(\vect X)$ and region $\{T(\vect X) \in C\}$
4. Setting Type I error of test
5. Assessing power of test

must be carried out <u>BEFORE</u> collecting numerical data. These are properties of the testing procedure and not specific to any sample of data (do not cherry pick!)

Once the experiment has been completed and we have numerical data, we can then go ahead and make a decision based on our decision rule. We can also supplement our decision with a p-value, which quantifies the strength of evidence against the null in favour of the alt.

**N.** <u>General threshholds & terminology used for p-values:</u>

*Figure (p-value scale):* a horizontal axis from $0$ (left end, vertical tick) to an unlabelled right end (vertical tick, standing for 1). Interior ticks, labelled below, at $0.01$, $0.05$ and $0.10$; spacing is not to scale (the three ticks sit in the left third, roughly evenly spaced, the gap from $0.10$ to the end is about twice the length of $0$ to $0.10$). Labels, each with a brace-like bracket marking its interval:
- above the axis, between $0.01$ and $0.05$: "re. strong" (reasonably strong evidence)
- below, from $0$ to $0.01$: "very strong evidence"
- below, from $0.05$ to $0.10$: "some / weak evidence"
- below, from $0.10$ to the right end: "no evidence against $H_0$"

NOTE: there is NO dichotomy in p-values.
As p-values are often misinterpreted (e.g. [one word crossed out] the chance $H_0$ is true), a journal actually banned p-values in favour of confidence intervals. However CIs are equally misinterpreted (e.g. chance that true value in interval is 95%) and there is a duality anyways.

---

### HW 20 (`20261121_231524.jpg`): P-values (2)

**P-values**

**N.** Suppose we have realisations $x_1,\dots,x_n$ of $X_1,\dots,X_n$ from the outcome of some random experiment.
We can compute the observed value of our statistic (test) $t_{\text{obs}} = T(\vect x)$ and make a decision based on the value.
Whatever decision we make, we can supplement this by computing the p-value:
$$
\begin{aligned}
\text{p-val.} &= \Prob_{H_0}\bigl(T(\vect X) \ge t_{\text{obs}}\bigr) && H_1: \theta > \theta_0\\
\text{p-val.} &= \Prob_{H_0}\bigl(T(\vect X) \le t_{\text{obs}}\bigr) && H_1: \theta < \theta_0\\
\text{p-val.} &= 2 \times \min\Bigl\{\Prob_{H_0}\bigl(T(\vect X) \ge t_{\text{obs}}\bigr),\ \Prob_{H_0}\bigl(T(\vect X) \le t_{\text{obs}}\bigr)\Bigr\} && H_1: \theta \ne \theta_0
\end{aligned}
$$
[A hatched blot (crossed-out text) precedes "$2\times\min$".]
In all three cases, the p-value is always the probability under $H_0$ that we observe the test statistic.
[possible error: incomplete; the p-value is the probability under $H_0$ of a test statistic at least as extreme as the one observed (CN §7.1.4).]

**Ex.** (continued) Suppose $n = 15$ Poi. are collected, with observed data $7, 11, 10, \dots, 9, 6, 18$, and we test $H_0: \lambda = 7.3$ vs. $H_1: \lambda > 7.3$. Recall our decision rule at the 5% level was $\{\sum X_i \ge 128\}$. After collecting the data, we observe $\sum x_i = 132$.
[The "3" in both "7.3"s is written above an ink blot. The data list is elided in the notes ("…").]
Based on our decision rule, we decide to reject $H_0$ i.f.o. $H_1$.
Supplement decision by computing & interpreting p-value:
$$\text{p-val.} = \Prob_{H_0}\Bigl(\sum X_i \ge 132\Bigr) = \dots = 0.02 \quad \Longrightarrow \quad \text{Given } H_0\text{, prob. of sample is } 0.02.$$
Thus there is reasonably strong evidence against $H_0$ i.f.o. $H_1$.
[Checked: $\Prob(\Pois(109.5) \ge 132) = 0.0200$. possible error: the interpretation "prob. of sample is 0.02" should be "prob. of a sum at least as large as 132".]

*Figure:* none.

---
### HW 21 (`20261121_231530.jpg`): Duality

**Duality**

**N.** We start with a recap:
- <u>CI:</u> range of parameter values where data likely to have occurred, given data set
- <u>HT:</u> given a parameter value, specifies range of data that would be unlikely to be observed

We can see CIs and HTs are inverses of each other.
More precisely,
- Two-sided CIs are a set of parameter values that would have been accepted
- One-sided CIs
[The "One-sided CIs" item is left unfinished: nothing follows it, and about a quarter of the page below it is blank.]

**Ex.** Consider a CI for $\mu$ where $\sigma^2$ is unknown.
Recall for testing $H_0: \mu = \mu_0$ vs. $H_1: \mu \ne \mu_0$, the <u>rejection</u> region for a t-test
$$\bigl\{\bar X \le \mu_0 - t^{1-\alpha/2}_{n-1} S/\sqrt n \ \cup\ \bar X \ge \mu_0 + t^{\alpha/2}_{n-1} S/\sqrt n\bigr\}$$
The acceptance region is therefore
$$\bigl\{\mu_0 - t^{1-\alpha/2}_{n-1} S/\sqrt n \le \mu_0 \le \mu_0 + t^{\alpha/2}_{n-1} S/\sqrt n\bigr\}$$
$$\iff \bigl\{\bar X - t^{1-\alpha/2}_{n-1} S/\sqrt n \le \mu_0 \le \bar X + t^{\alpha/2}_{n-1} S/\sqrt n\bigr\}$$
That is, $\mu_0$ would be accepted as the null hypothesis if it lies within the confidence interval.

Thus when pivot variables cannot be constructed, we can always construct a CI by inverting hypothesis tests.

[possible error: the quantile superscripts mix $1-\alpha/2$ (left) and $\alpha/2$ (right); with HW 16's convention both should be $t^{1-\alpha/2}_{n-1}$. The middle term of the acceptance region is written $\mu_0$; it should be $\bar X$ ($\mu_0 - t\,S/\sqrt n \le \bar X \le \mu_0 + t\,S/\sqrt n$).]

*Figure:* none.

---

### HW 22 (`20261121_231535.jpg`): Generalised likelihood ratio test (GLRT)

**Generalised likelihood ratio test (GLRT)**

**N.** The GLRT can be used to unify all of the methods from §7 and §8 of the reference notes.
(e.g. one/two sample t-test, F-test, binom., $\chi^2$ GoF)

LRTs can be generalised to scenarios where both the null and alternative hypotheses are NOT single point hypotheses. These are of particular interest when a parameter is multidimensional, etc.

Suppose the null hypothesis $H_0: \theta \in \Theta_0$, where $\Theta_0$ is some subset of the full parameter space $\Omega$, and the alt. hypothesis is $H_1: \theta \in \Theta_1$, where $\Theta_1$ is another subset disjoint of $\Theta_0$.
(If we consider a 'two-sided' test, it generalises to an 'insided' or 'outsided' alternative)

Consider the GLRT statistic:
$$\frac{\sup_{\theta\in\Theta_0} L(\theta \given \vect x)}{\sup_{\theta\in\Theta_1} L(\theta \given \vect x)} \quad \begin{matrix}\leftarrow \text{best l.i.h.d. under null}\\ \leftarrow \text{best l.i.h.d. under alt.}\end{matrix}$$
If the ratio is 'small', the data is more likely observed under alt. $\Theta_1$ compared to $\Theta_0$ null.
How 'small' depends on the Type I error we fix.

["l.i.h.d." = likelihood. "§7 and §8 of the reference notes" = CN Ch 7 (hypothesis testing) and Ch 8 ($\chi^2$ GoF).]

*Figure:* none.

---

### HW 23 (`20261121_231542.jpg`): GLRT example (motivation for ANOVA) (1)

**GLRT example (motivation for ANOVA)**

**Ex.** Comparing two group means.
Let $\vect X_1 = (X_{11}, X_{12}, \dots, X_{1n_1}) \iid \Normal^{*}(\mu_1, \sigma^2)$
Let $\vect X_2 = (X_{21}, X_{22}, \dots, X_{2n_2}) \iid \Normal^{*}(\mu_2, \sigma^2)$
be two independent samples, where $\mu_1, \mu_2$ are unknown.
Assume for now that $\sigma^2$ is known.

We may want to test $H_0: \mu_1 = \mu_2$ vs. $H_1: \mu_1 \ne \mu_2$.

*Figure (parameter space):* axes with $\mu_1$ horizontal (arrow right) and $\mu_2$ vertical (arrow up), origin at the lower left. A solid straight line from the origin rising to the upper right at 45°, labelled "$H_0: \mu_1 = \mu_2$" at its upper end. The region on both sides of the line (above-left and below-right, within the quadrant) is filled with short dashed hatching, labelled "$\leftarrow H_1: \mu_1 \ne \mu_2$" with the arrow pointing into the hatched region. Brace to the right: "the null is a line, alt. is a space. 'outside' alternative".

To use the GLRT, we first write the likelihood function:
$$L(\mu_1,\mu_2 \given \vect x) = \Bigl(\frac{1}{\sqrt{2\pi\sigma^2}}\Bigr)^{n_1+n_2} \exp\Bigl\{-\frac{1}{2\sigma^2}\sum_{i=1}^{n_1}(x_{1i}-\mu_1)^2 - \frac{1}{2\sigma^2}\sum_{i=1}^{n_2}(x_{2i}-\mu_2)^2\Bigr\}$$
For the numerator of the GLRT, we wish to maximise $L(\mu_1,\mu_2 \given \vect x)$ [small blot], under the null $H_0: \mu_1 = \mu_2$. The MLE of the common mean is
$$\hat\mu_1 = \hat\mu_2 = \frac{\sum_{i=1}^{n_1} x_{1i} + \sum_{i=1}^{n_2} x_{2i}}{n_1 + n_2} = \bar x_{\cdot\cdot} \quad \Big\}\ \text{grand mean, '}\cdot\cdot\text{' denotes averaging over both indices}$$
So the ML acheivable under $H_0$ is therefore
$$\sup_{\mu_1=\mu_2} L(\mu_1,\mu_2 \given \vect x) = L(\bar x_{\cdot\cdot}, \bar x_{\cdot\cdot} \given \vect x) = \Bigl(\frac{1}{\sqrt{2\pi\sigma^2}}\Bigr)^{n_1+n_2}\exp\Bigl\{-\frac{1}{2\sigma^2}\Bigl(\sum_{i=1}^{n_1}(x_{1i}-\bar x_{\cdot\cdot})^2 + \sum_{i=1}^{n_2}(x_{2i}-\bar x_{\cdot\cdot})^2\Bigr)\Bigr\}$$
Looking at the exponand:
$$
\begin{aligned}
SS_{\text{Total}}\ \Big\{\ &\sum(x_{1i}-\bar x_{\cdot\cdot})^2 + \sum(x_{2i}-\bar x_{\cdot\cdot})^2 = \sum(x_{1i} - \bar x_{1\cdot} + \bar x_{1\cdot} - \bar x_{\cdot\cdot})^2 + \dots\\
&= \sum(x_{1i}-\bar x_{1\cdot})^2 + 2(x_{1i}-\bar x_{1\cdot})\underbrace{\sum_{i=1}^{n_1}(x_{1i}-\bar x_{1\cdot})}_{=0} + n_1(\bar x_{1\cdot} - \bar x_{\cdot\cdot})^2 + \dots\\
&= \sum(x_{1i}-\bar x_{1\cdot})^2 + n_1(\bar x_{1\cdot}-\bar x_{\cdot\cdot})^2 + \sum(x_{2i}-\bar x_{2\cdot}) + n_2(\bar x_{1\cdot}-\bar x_{\cdot\cdot})^2\\
&= \text{'within group' SS} + \text{'between group' SS}
\end{aligned}
$$
[Two arrows at the bottom point from "'between group' SS" up to the $n_1(\cdot)^2$ and $n_2(\cdot)^2$ terms.]
[possible error: (i) the cross term is written $2(x_{1i}-\bar x_{1\cdot})\sum(x_{1i}-\bar x_{1\cdot})$; it should be $2(\bar x_{1\cdot}-\bar x_{\cdot\cdot})\sum(x_{1i}-\bar x_{1\cdot})$. (ii) In the third line, $\sum(x_{2i}-\bar x_{2\cdot})$ is missing its square, and the last term should be $n_2(\bar x_{2\cdot}-\bar x_{\cdot\cdot})^2$. HW 24's $\Lambda$ has the correct $n_2(\bar x_{2\cdot}-\bar x_{\cdot\cdot})^2$.]

---

### HW 24 (`20261121_231548.jpg`): GLRT example (motivation for ANOVA) (2)

**GLRT example (motivation for ANOVA)**

**Ex.** (ANOVA breakdown)
[About a fifth of the page below this heading is blank.]

For the denominator, where $\mu_0 \ne \mu_1$, using intuition what would the MLEs be for $\hat\mu_1 = \bar x_{1\cdot}$, $\hat\mu_2 = \bar x_{2\cdot}$, and what is
$$
\sup_{\mu_1\ne\mu_2} L(\mu_1,\mu_2 \given \vect x) = L(\bar x_{1\cdot}, \bar x_{2\cdot} \given \vect x)
= \Bigl(\frac{1}{\sqrt{2\pi\sigma^2}}\Bigr)^{n_1+n_2}\exp\Bigl\{-\frac{1}{2\sigma^2}\sum_{i=1}^{n_1}(x_{1i} - x_{1\cdot})^2 - \frac{1}{2\sigma^2}\sum_{i=1}^{n_2}(x_{2i}-x_{2\cdot})^2\Bigr\}
$$
[possible error: "where $\mu_0 \ne \mu_1$" should be $\mu_1 \ne \mu_2$; the subtracted means lose their bars ($\bar x_{1\cdot}$, $\bar x_{2\cdot}$). An ink blot precedes the second exponent term.]

So the GLRT simplifies to
$$\Lambda = \exp\Bigl\{-\frac{1}{2\sigma^2}\bigl[n_1(\bar x_{1\cdot}-\bar x_{\cdot\cdot})^2 + n_2(\bar x_{2\cdot}-\bar x_{\cdot\cdot})^2\bigr]\Bigr\}$$
The ratio $\Lambda$ is small when the between group sum of squares is large $\iff \bar x_{1\cdot}, \bar x_{2\cdot}$ are far apart.
Thus we reject $H_0$ in favour of $H_1$ if
$$\bigl\{\bar X_{1\cdot} - \bar X_{2\cdot} \le d_1 \ \cup\ \bar X_{1\cdot} - \bar X_{2\cdot} \ge d_2 \text{ for some } d_1, d_2\bigr\}$$
Finally how do we set $d_1$ and $d_2$? We wish to control Type I error to e.g. 0.05. Recall that
$$\bar X_{1\cdot} - \bar X_{2\cdot} \sim \Normal\bigl(\mu_1-\mu_2,\ \sigma^2/n_1 + \sigma^2/n_2\bigr)$$
and so under the null $H_0: \mu_1 - \mu_2 = 0$, we set
$$
\left.\begin{aligned}
d_1 &= 0 - z^{(1-\alpha/2)}\sigma\sqrt{1/n_1 + 1/n_2}\\
d_2 &= 0 + z^{(1-\alpha/2)}\sigma\sqrt{1/n_1 + 1/n_2}
\end{aligned}\right\}\ \text{2-sample z-test}
$$

*Figure:* none.

---
### HW 25 (`20261121_231554.jpg`): GLRT example (motivation for 2-sample t-test)

**GLRT example (motivation for 2-sample t-test)**

**Ex.** (continued) In practice, we rarely know $\sigma^2$. What would the best estimate be for $\sigma^2$?
$$\hat\sigma^2 = \frac{(n_1-1)S_1^2 + (n_2-1)S_2^2}{(n_1+n_2-2)} = S^2_{\text{pooled}}$$
This $\hat\sigma^2$ is just a weighted average of $S_1^2$ and $S_2^2$.
We use the t-quantiles instead of the z-quantiles:
$$
\left.\begin{aligned}
d_1 &= \Delta_0 - t^{(1-\alpha/2)}_{n_1+n_2-2}\, S_{\text{pooled}}\sqrt{1/n_1 + 1/n_2}\\
d_2 &= \Delta_0 + t^{(1-\alpha/2)}_{n_1+n_2-2}\, S_{\text{pooled}}\sqrt{1/n_1 + 1/n_2}
\end{aligned}\right\}\ \text{2-sample t-test}
$$
How do we extend this to $n$ groups? ANOVA (§10).
[$\Delta_0$ is not defined on this page; HW 24 used $0$ (the null $\mu_1 - \mu_2 = 0$), so $\Delta_0$ is the null value of $\mu_1 - \mu_2$ (CN §7.3.1 writes the null as $H_0: \mu_1 - \mu_2 = \delta_0$). "§10" = CN Ch 10 (ANOVA). The rest of the page (about half) is blank.]

*Figure:* none.

---

