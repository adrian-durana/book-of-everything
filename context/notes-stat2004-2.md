# STAT2004 Statistical Modelling & Analysis: transcription, part 2 of 4 (HW 26–51)

_Continuation of part 1 (see `claude/notes-stat2004-1.md` for sources, legibility check and conventions)._

**This part:** goodness-of-fit tests, data fabrication and pseudo-replication, Pearson's $\chi^2$ test, Fisher's exact test, one-way ANOVA (derivation, $F$-statistic, tables, post-hoc comparisons, contrasts), two-way ANOVA, linear models (estimation, GLRT, $F$-table, polynomial example).

---

### HW 26 (`20261121_231600.jpg`): Goodness-of-fit tests (1)

**Goodness-of-fit tests**

**N.** We use goodness-of-fit tests for categorical data (i.e. non-numerical data).
Recall we use g-o-f. tests of the form:
$$\sum_{\text{cells } i}\frac{(\text{Observed}_i - \text{Expected}_i)^2}{\text{Expected}_i} \overset{\text{app.}}{\sim} \chi^2 \quad \Big\}\ \text{Pearson's } \chi^2 \text{ test}$$
We will derive this formally.

**Ex.** Suppose each component can be classified as one of $k$ categories (i.e. one of $k$ levels of a factor) (e.g. handedness $= \{L, R, A\}$, income $= \{0\text{–}6k, 6k\text{–}12k, \dots\}$).

**N.** The underlying population proportion for each level is
$$p_1, p_2, \dots, p_k \quad\text{where } p_k = 1 - \sum_{i=1}^{k-1} p_i$$
and so we have $k-1$ free parameters.

Now suppose $X_1, X_2, \dots, X_k$ are the counts in each category for a sample of $n$ units. Now
$$X_1 + X_2 + \dots + X_k = n \implies X_k = n - X_1 - X_2 - \dots - X_{k-1}$$
The pmf of $\vect X = (X_1, X_2, \dots, X_k)\T \sim \text{Multinomial}(p_1,\dots,p_k)$ is
$$p(X_1 = x_1, \dots, X_k = x_k) = \binom{n}{\vect x} p_1^{x_1} p_2^{x_2} \cdots p_k^{x_n}$$
where
$$\binom{n}{\vect x} = \frac{n!}{x_1!\,x_2!\cdots x_n!} \quad \text{is the multinomial coeff.}$$
[possible error: the last exponent and the last factorial use $x_n$; they should be $x_k$. The handwriting of $k$ is close to $h$ throughout this page; read as $k$. The "Multinomial($p_1,\dots,p_k$)" omits $n$; the book has $\Mnom(n, p_1,\dots,p_k)$.]

Suppose for example that we are interested in testing a single point null hypothesis:
$$H_0: \vect p = (p_1, p_2, \dots, p_k) = \vect p^{*} = (p_1^{*}, p_2^{*}, \dots, p_k^{*})$$
where $\vect p^{*}$ is a given set of proportions, vs. $H_1: \vect p \ne \vect p^{*}$.
[Side note with an arrow pointing to "$\ne$": "note only 1 needs be wrong".]

*Figure:* none.

---

### HW 27 (`20261121_231610.jpg`): Goodness-of-fit tests (2)

**Goodness-of-fit tests**

**N.** (continued) Consider now the GLRT statistic:
$$\Omega = \frac{\sup_{H_0} L(\vect p \given \vect x)}{\sup_{H_1} L(\vect p \given \vect x)}$$
where
$$\sup_{H_0} L(\vect p \given \vect x) = L(\vect p^{*} \given \vect x) = \binom{n}{\vect x} p_1^{*\,x_1} p_2^{*\,x_2}\cdots p_k^{*\,x_k}$$
$$\sup_{H_1} L(\vect p \given \vect x) = \binom{n}{\vect x}(\hat p_1)^{x_1}(\hat p_2)^{x_2}\cdots(\hat p_k)^{x_k} = \binom{n}{\vect x}\Bigl(\frac{x_1}{n}\Bigr)^{x_1}\Bigl(\frac{x_2}{n}\Bigr)^{x_2}\cdots\Bigl(\frac{x_k}{n}\Bigr)^{x_k}$$
so
$$\Omega = \Bigl(\frac{p_1^{*}}{\hat p_1}\Bigr)^{x_1}\Bigl(\frac{p_2^{*}}{\hat p_2}\Bigr)^{x_2}\cdots\Bigl(\frac{p_k^{*}}{\hat p_k}\Bigr)^{x_k}$$
Note that small $\Omega \iff$ small $\log\Omega \iff$ large $-\log\Omega$.
$$
\begin{aligned}
-\log\Omega &= x_1\log\Bigl(\frac{\hat p_1}{p_1^{*}}\Bigr) + x_2\log\Bigl(\frac{\hat p_2}{p_2^{*}}\Bigr) + \dots + x_k\log\Bigl(\frac{\hat p_k}{p_k^{*}}\Bigr)\\
&= x_1\log\Bigl(\frac{x_1}{np_1^{*}}\Bigr) + x_2\log\Bigl(\frac{x_2}{np_2^{*}}\Bigr) + \dots\\
&= x_1\log\Bigl(\frac{O_1}{\E_1}\Bigr) + x_2\log\Bigl(\frac{O_2}{\E_2}\Bigr) + \dots
\end{aligned}
$$
where $O_i$ is observed counts, $\E_i$ is expected counts under $H_0$.
$$= \sum_{\text{cells } i} O_i\log\Bigl(\frac{O_i}{\E_i}\Bigr)$$
This is the EXACT GLRT for categorical data.
Why do we use Pearson's $\chi^2$-test then?

[Notation: the GLRT statistic is written with a symbol that looks like $\Omega$ (as for the parameter space on HW 06); likely meant as $\Lambda$ (HW 24). Expected counts are written with a blackboard $\mathbb{E}_i$; ordinary $E_i$ is meant. Subscripts $k$ written like $n$ in places, as on HW 26.]

*Figure:* none.

---

### HW 28 (`20261121_231617.jpg`): Goodness-of-fit tests (3)

**Goodness-of-fit tests**

**N.** We use Pearson's $\chi^2$-test for the following reasons:
1. The null distribution of $-\log\Omega$ cannot be easily derived (and so cutoffs are hard to find)
2. Twice the GLRT can be shown to be asymptotically equivalent to Pearson's $\chi^2$ (i.e. the dominant term of Taylor expansion)
3. The null-distribution of Pearson's $\chi^2$ is (relatively) easy to derive. In fact, Pearson's $\chi^2 \overset{\text{app.}}{\sim} \chi^2$ dist.
   ↳ $-2\log\Omega \sim \chi^2_{[\text{blot}]}$, with "$n-1$" written below the blot
4. Pearson's $\chi^2$ is far easier to compute by hand.

[illegible: the degrees of freedom on $\chi^2$ are covered by a solid ink blot in the notebook; "$n-1$" is written under it as the replacement. By HW 26 ($k-1$ free parameters) $k-1$ is presumably meant; the $\sim$ is asymptotic. A retake won't help.]

**Rem.** When computing a p-value for this test, we say the data is <u>consistent</u> with the null hypothesis, instead of for the null hypothesis. This is because we may have two distinct, yet very similar hypotheses that would both be 'supported', though only one would be 'true' or 'more true'.

**Ex.** Claim $H_0$: $c^2 = a^2 + b^2$ for all right-angled triangles.
We can sample as many triangles as we want, but we can never prove it given enough samples (as there may still exist a counterexample).

We can only find evidence AGAINST the null or AGAINST the hypothesis — we <u>cannot</u> say the evidence SUPPORTS the null.

**Rem.** While getting a small p-value makes us suspicious about the null, an overly large p-value also makes us suspicious about either <u>data-fabrication</u> or <u>psuedo-replication</u>.

*Figure:* none.

---
### HW 29 (`20261121_231624.jpg`): Data fabrication; Pseudo-replication

**Data fabrication**

**N.** Suppose we are sampling from a population with an underlying proportion of $9/16$ of some trait.

<u>Real data</u>
$$12/16 \;\to\; 82/160 \;\to\; 847/1600 \qquad \Big\}\ \text{could diverge from } 900/1600$$
<u>Fake data</u>
$$12/16 \;\to\; 88/160 \;\to\; 901/1600 \qquad \Big\}\ \text{converge to } 9/16$$
This happens as bad [one word blotted out] scientists are bad at statistics, and do not understand the law of large numbers. In particular, they are too afraid to add variance/s to their fake data.

[The "9" in "9/16" is the writer's "a"-shaped 9 (as elsewhere); read as $9/16$, consistent with "900/1600".]

**Pseudo-replication**

Suppose we are comparing two fertilisers using $n$ trees.
We could:

*Figure (two designs):*
- Top row: two tree symbols (a vertical stem with an asterisk-like crown, drawn on a short horizontal ground line), the left one labelled $f_1$ and the right one $f_2$ at the base. Brace to the right: "sample 2 trees 100 times".
- Bottom row: six tree symbols in a row (no ground line), labelled at their bases, left to right: $f_1, f_2, f_2, f_1, f_2, f_1$ [the second label is partly cut by the stroke and reads like "$f_2$"]. Brace to the right: "sample 6 trees 33 times".

It is a lot easier to do the first experiment compared to the second experiment.

---

### HW 30 (`20261121_231630.jpg`): Pearson's $\chi^2$ test

**Pearson's $\chi^2$ test**

**N.** Pearson's $\chi^2$ (or GLRT) <u>test of independence</u> and test of homogenuity are carried out identically, but are different in the underlying hypotheses and the way the data is collected.

<u>Test of independence:</u>
- Null hypothesis is that these factors are ind.:
  $$H_0: p_{ij} = p_{i\cdot}\,p_{\cdot j} \quad \forall\, i,j \qquad \Big\}\ \text{prop. in level } i\text{, factor 1, vs. level } j\text{, factor 2}$$
  $$H_1: p_{ij} \ne p_{i\cdot}\,p_{\cdot j} \quad (\exists\, i,j)$$
- We sample from a single population and then cross-classify

<u>Test of homogeneity:</u>
- Null hypothesis is that proportions are common:
  $$H_0: \vect p_a = \vect p_b = \vect p_{\text{common}} \ \forall \text{ groups} \qquad \Big\}\ \text{proportion (vector) of groups } a \text{ vs. } b$$
  $$H_1: \exists\, i,j: \vect p_i \ne \vect p_j \ \text{ or }\ \vect p_i \ne \vect p_{\text{common}}$$
- Sample from two (or more) sub-populations and compare occurrences of a categorical factor between the two samples.

**Rem.** For a test of homogeneity, we have
- $c(r-1)$ free parameters for <u>alternative model</u>
- $(r-1)$ free parameters for <u>null model</u>
- $\text{df} = c(r-1) - (r-1) = (c-1)(r-1)$ for a test of homogeneity $\Big\}$ symmetric in rows and columns

[$r$ = number of rows (levels of the factor), $c$ = number of columns (groups), as in the HW 31 example.]

*Figure:* none.

---

### HW 31 (`20261121_231637.jpg`): Pearson's $\chi^2$ test example (1)

**Pearson's $\chi^2$ test example**

**Ex.** To plan for next year's IT intake, the computer choices of all staff across three faculties were collected.

| OS | Science | Engineering | Arts |
|---|---|---|---|
| Windows | 12 (12.51) | 17 (13.90) | 9 (11.58) |
| Mac | 8 (10.54) | 9 (11.71) | 15 (9.75) |
| Linux | 7 (3.95) | 4 (4.39) | 1 (3.66) |
| **Total** | 27 | 30 | 25 |

[Expected counts under $H_0$ in brackets, written small to the lower right of each observed count. Table drawn with a vertical rule after the OS column, a horizontal rule under the header and another above Total. Checked against $(\text{row total})(\text{column total})/82$: Arts–Windows is $11.585$ (written 11.58) and Arts–Mac is $9.756$ (written 9.75); all other entries agree to 2 d.p.]

<u>Q:</u> Is OS preference homogenous/consistent across all three faculties?
$$H_0: \vect p_{\text{sci}} = \vect p_{\text{eng}} = \vect p_{\text{art}} = \vect p_{\text{common}}$$
$$\begin{pmatrix}p_w\\p_m\\p_\ell\end{pmatrix}_{\text{sci}} = \begin{pmatrix}p_w\\p_m\\p_\ell\end{pmatrix}_{\text{eng}} = \begin{pmatrix}p_w\\p_m\\p_\ell\end{pmatrix}_{\text{art}} = \begin{pmatrix}p_w\\p_m\\p_\ell\end{pmatrix}_{\text{common}}$$
$H_1$: no restrictions on each prob. vector

Free parameters in null: 2
Free parameters in alt.: 6
$\therefore$ Free parameters / degrees of freedom of test: $6 - 2 = 4$

To carry out Pearson's $\chi^2$ test, we need to find the expected counts under the null hypothesis.

---

### HW 32 (`20261121_231641.jpg`): Pearson's $\chi^2$ test example (2)

**Ex.** (continued) Under the null, the MLE for the common vector of probabilities is:
$$\hat p_w = \frac{38}{82}, \quad \hat p_m = \frac{32}{82}, \quad \hat p_\ell = \frac{12}{82}$$
The expected counts are therefore:
<u>Science:</u>
$$
\begin{aligned}
27 \times \tfrac{38}{82} &= 12.51 && \text{prefer Windows}\\
27 \times \tfrac{32}{82} &= 10.54 && \text{prefer Mac}\\
27 \times \tfrac{12}{82} &= 3.95 && \text{prefer Linux}
\end{aligned}
$$
and we can similarly compute these for Eng. and Arts.

Pearson's $\chi^2$ statistic is:
$$\chi^2 = \frac{(12 - 12.51)^2}{12.51} + \frac{(17 - 13.90)^2}{13.90} + \dots + \frac{(1 - 3.60)^2}{3.66} = 9.66$$
[possible error: the last numerator has $3.60$; the expected count is $3.66$. The total $9.66$ is correct (computed: $9.662$).]

To find the p-value:
$$\Prob(\ChiSq{4} \ge 9.66) = 1 - \texttt{pchisq(9.66, 4)} = 0.047$$
and thus we can conclude that there is moderate evidence that OS preference differs across faculties.
[Checked: $0.0466$.]

**Rem.** Are there any caveats for using Pearson's $\chi^2$ here?
(Note that the limiting distribution $\chi^2$ is a generalisation of the normal approx. to a binomial proportion)

Recall that, for a binomial, the normal approximation holds if we have at least 10 'successes' and 10 'failures'.
For Pearson's $\chi^2$ test, we must both relax and tighten this requirement:
1. At least 80% of the cells in table have $\ge 10$ counts
2. All cells have $\ge 5$ counts

Where this fails, we use <u>Fisher's exact test</u>.
[possible error: as written, (1) is implied by (2) only if 10 is replaced by 5; CN Rem 8.1 gives the rule of thumb $np_i \ge 5$ for all $i$ (expected counts); the notes' rule is stated for counts and mixes thresholds 10 and 5. The Linux row here has expected counts below 5, which is presumably the caveat intended; not stated.]

*Figure:* none.

---
### HW 33 (`20261121_231652.jpg`): Fisher's exact test

**Fisher's exact test**

**Def.** Fisher's exact test involves the following logical arguments:
1. Argue the margins of the table can be considered fixed/given under the null hypothesis.
   (e.g. the number of staff from each faculty who needed a new computer is determined completely by when they started at UQ, and nothing to do with computer preference.)
   Thus, column totals are considered fixed.
   (e.g. if computer pref. is not associated with faculty, then the 38 staff to choose Windows anyway regardless of their faculty, and similar for Mac and Linux users.)
   Thus, row totals are considered fixed.
2. Under the null, any configuration of counts with the same given set of row and column margins would be equally likely to have occurred.
   (e.g.

   | OS | Sci. | Eng. | Arts | |
   |---|---|---|---|---|
   | Windows | 12 · 13/15 | 17 · 14/23 | 9 · 11/0 | 38 |
   | Mac | 8 · 11/0 | 9 · 11/7 | 15 · 10/25 | 32 |
   | Linux | 7 · 3/12 | 4 · 5/0 | 1 · 4/0 | 12 |
   | | 27 | 30 | 25 | 82 |
   )

   [Each cell holds the observed count (large) followed by two small numbers stacked vertically: "top/bottom" above means top number over bottom number. These are two alternative tables with the same margins. Top configuration: Sci $(13, 11, 3)$, Eng $(14, 11, 5)$, Arts $(11, 10, 4)$. Bottom configuration: Sci $(15, 0, 12)$, Eng $(23, 7, 0)$, Arts $(0, 25, 0)$. Both checked to have row totals 38, 32, 12 and column totals 27, 30, 25. The Sci–Linux bottom entry is small and could be read as 13; the margins require 12. The Arts–Mac top entry "10" has a reversed-looking 0. Table drawn as on HW 31, with an extra vertical rule before the row-total column.]

   Both top and bottom configurations of counts would be an equally likely outcome. The top would be 'less unusual', the bottom would be 'more' so.
3. By <u>simulations</u> of all tables of counts with the given fixed margins, we can determine how often we get something 'as unusual or more unusual as our observed costs'.

<u>This is Fisher's exact test.</u>

[possible error: (2) under the null with both margins fixed, tables are not equally likely; each has a (multivariate) hypergeometric probability. "observed costs" = observed counts. (3): "simulations of all tables" mixes enumeration (exact test) with simulation.]

*Figure:* the table above.

---

### HW 34 (`20261121_231702.jpg`): Derivation of ANOVA (1)

**Derivation of ANOVA**

**N.** ANOVA (Analysis of variance) is used to compare a quantitative variable across levels of one (or more) factors. ANOVA is actually a special case of linear models.

ANOVA setup: (extension of a 2-sample test for $\ge 2$ groups)
$$
\left.\begin{aligned}
Y_{11}, Y_{12}, \dots, Y_{1n} &\iid \Normal^{*}(\mu_1, \sigma^2)\\
Y_{21}, Y_{22}, \dots, Y_{2n} &\iid \Normal^{*}(\mu_2, \sigma^2)\\
&\ \vdots\\
Y_{J1}, Y_{J2}, \dots, Y_{Jn} &\iid \Normal^{*}(\mu_J, \sigma^2)
\end{aligned}\right\}\ \text{come from } J \text{ sub-pop., independent from each other}
$$
[The rows end in $Y_{jn}$ (equal group sizes) here; HW 35 uses group sizes $n_j$ and $N = \sum n_j$.]

Graphically, the data may look like this:

*Figure (dot plot of groups):* vertical axis (arrow up, no label) and horizontal axis (arrow right) with ticks labelled $1, 2, 3, \dots, J$ ("$\cdots$" between 3 and $J$). Above each tick, a vertical column of small open circles (the observations of that group) with a short horizontal bar through it marking the group mean, labelled to its right:
- group 1: 5 circles, roughly at mid height; bar labelled $\bar y_{1\cdot}$, just below the dotted line
- group 2: 3 circles close together, slightly lower; bar labelled $\bar y_{2\cdot}$
- group 3: 5 circles, the highest group; bar labelled $\bar y_{3\cdot}$, well above the dotted line
- group $J$: 3 circles near the dotted line; bar labelled $\bar y_{J\cdot}$ just above it
A horizontal dotted line across the whole plot at about the level of groups 1 and $J$, labelled $\bar y_{\cdot\cdot}$ at its right end (grand mean).

A default null hypothesis to test is whether
$$H_0: \mu_1 = \mu_2 = \dots = \mu_J \quad\text{vs.}\quad H_1: \text{at least one } \mu_i \text{ is different.}$$
How do we generalise our 2-sample t-test to $\ge 2$ groups?
We can appeal to the GLRT principle
$$\Lambda = \frac{\sup_{H_0} L(\mu_1, \mu_2, \dots, \mu_J \given \vect Y)}{\sup_{H_1} L(\mu_1, \mu_2, \dots, \mu_J \given \vect Y)}$$

---

### HW 35 (`20261121_231708.jpg`): Derivation of ANOVA (2)

**N.** The joint likelihood function is:
$$
\begin{aligned}
L(\mu_1,\mu_2,\dots,\mu_J \given \vect Y)
&= \Bigl(\frac{1}{\sqrt{2\pi\sigma^2}}\Bigr)^{n_1}\exp\Bigl\{-\frac{1}{2\sigma^2}\sum_{i=1}^{n_1}(Y_{1i}-\mu_1)^2\Bigr\}\Bigl(\frac{1}{\sqrt{2\pi\sigma^2}}\Bigr)^{n_2}\exp\Bigl\{-\frac{1}{2\sigma^2}\sum_{i=1}^{n_2}(Y_{2i}-\mu_2)^2\Bigr\}\cdots\\
&= \Bigl(\frac{1}{\sqrt{2\pi\sigma^2}}\Bigr)^{N}\exp\Bigl\{-\frac{1}{2\sigma^2}\sum_{j=1}^{J}\sum_{i=1}^{n_j}(Y_{ji}-\mu_j)^2\Bigr\}
\end{aligned}
$$
Under the null $H_0: \mu_1 = \mu_2 = \dots = \mu$, the MLE would be
$$\hat\mu_1 = \hat\mu_2 = \dots = \hat\mu_J = \hat\mu = \bar Y_{\cdot\cdot} = \sum_{j=1}^{J}\sum_{i=1}^{n_j} Y_{ji} \Big/ N$$
Therefore
$$\sup_{H_0} L(\cdots \given \vect Y) = L(\bar Y_{\cdot\cdot}, \bar Y_{\cdot\cdot}, \dots, \bar Y_{\cdot\cdot} \given \vect Y) = \Bigl(\frac{1}{\sqrt{2\pi\sigma^2}}\Bigr)^{N}\exp\Bigl\{-\frac{1}{2\sigma^2}\sum_{i=1}^{J}\sum_{i=1}^{n_j}(Y_{ji}-\bar Y_{\cdot\cdot})^2\Bigr\}$$
[The outer sum index is written $i=1$; $j=1$ is meant.]
Under the alternative $H_1: \cdots$, the MLE would be
$$\hat\mu_1 = \bar Y_{1\cdot},\ \hat\mu_2 = \bar Y_{2\cdot},\ \dots,\ \hat\mu_J = \bar Y_{J\cdot}.$$
and so
$$\sup_{H_1} L(\cdots \given \vect Y) = L(\bar Y_{1\cdot}, \bar Y_{2\cdot}, \dots, \bar Y_{J\cdot} \given \vect Y) = \Bigl(\frac{1}{\sqrt{2\pi\sigma^2}}\Bigr)^{N}\exp\Bigl\{-\frac{1}{2\sigma^2}\sum_{j=1}^{J}\sum_{i=1}^{n_j}(Y_{ji}-\bar Y_{j\cdot})^2\Bigr\}$$
[Small blots on the subscript of $\bar Y_{J\cdot}$ and on the inner index $i$; readable from context.]
We now examine the double summation of the top:
$$
\begin{aligned}
\underbrace{\sum_{j=1}^{J}\sum_{i=1}^{n_j}(Y_{ji}-\bar Y_{\cdot\cdot})^2}_{\text{Total sum of sq.}} &= \sum_{j=1}^{J}\sum_{i=1}^{n_j}(Y_{ji} - \bar Y_{j\cdot} + \bar Y_{j\cdot} - \bar Y_{\cdot\cdot})^2\\
&= \sum_{j=1}^{J}\sum_{i=1}^{n_j}(Y_{ji}-Y_{j\cdot})^2 + 2\sum_{j=1}^{J}(\bar Y_{j\cdot}-\bar Y_{\cdot\cdot})\underbrace{\sum_{i=1}^{n_j}(Y_{ji}-\bar Y_{\cdot\cdot})}_{\to\,0}\\
&\quad + \underbrace{\sum_{j=1}^{J}\sum_{i=1}^{n_j}(\bar Y_{j\cdot}-\bar Y_{\cdot\cdot})^2}_{\text{inner sum gives } n_j} = \underset{\text{(residuals)}}{SS_{\text{within}}} + \underset{\text{(groups)}}{SS_{\text{between}}}
\end{aligned}
$$
[The cross-term's inner sum is struck through with a diagonal arrow pointing to "0". possible error: the inner sum should be $\sum_i (Y_{ji}-\bar Y_{j\cdot})$ (which is 0), not $\sum_i(Y_{ji}-\bar Y_{\cdot\cdot})$; the first term drops the bar on $\bar Y_{j\cdot}$. "$= n_j$" is written under the last inner sum, meaning $\sum_{i=1}^{n_j}(\bar Y_{j\cdot}-\bar Y_{\cdot\cdot})^2 = n_j(\bar Y_{j\cdot}-\bar Y_{\cdot\cdot})^2$.]

*Figure:* none.

---

### HW 36 (`20261121_231717.jpg`): Derivation of ANOVA (3)

**Derivation of ANOVA**

**N.** Therefore, the maximal likelihood under $H_0$ is:
$$\sup_{H_0} L = \Bigl(\frac{1}{\sqrt{2\pi\sigma^2}}\Bigr)^{N}\exp\Bigl[-\frac{1}{2\sigma^2}\bigl[SS_{\text{groups}} + SS_{\text{residuals}}\bigr]\Bigr]$$
Denominator:
$$\sup_{H_1} L = \Bigl(\frac{1}{\sqrt{2\pi\sigma^2}}\Bigr)^{N}\exp\Bigl[-\frac{1}{2\sigma^2}\bigl[SS_{\text{residuals}}\bigr]\Bigr]$$
So the GLRT statistic reduces to:
$$\Lambda = \frac{\sup_{H_0}}{\sup_{H_1}} = \exp\Bigl\{-\frac{1}{2\sigma^2}\bigl[SS_{\text{groups}}\bigr]\Bigr\}$$
and so small values of $\Lambda \iff$ large values of $SS_{\text{groups}}$.

How large would 'large enough' be?
Under $H_0$, each $\bar Y_{j\cdot} \overset{\text{ind}}{\sim} \Normal(\mu, \sigma^2/n_j)$
$$
\left.\begin{aligned}
&\implies \frac{\sqrt{n_j}}{\sigma}(\bar Y_{j\cdot} - \mu) \overset{\text{ind}}{\sim} \Normal(0,1)\\
&\implies \frac{n_j}{\sigma^2}(\bar Y_j - \mu)^2 \overset{\text{ind}}{\sim} \ChiSq{1}
\end{aligned}\right\}\ \text{for } j = 1,\dots,J
$$
$$\implies \frac{1}{\sigma^2}\sum_{j=1}^{J} n_j(\bar Y_j - \mu)^2 \sim \ChiSq{J}$$
Note we do not know $\mu$, so we must use $\bar Y_{\cdot\cdot}$. Thus,
$$\sum_{j=1}^{J} n_j(\bar Y_{j\cdot} - Y_{\cdot\cdot})^2 \sim \sigma^2\ChiSq{J-1}$$
$$\implies \frac{1}{J-1}SS_{\text{groups}} \sim \frac{\sigma^2\ChiSq{J-1}}{J-1} \qquad (1)$$
[The step from $\ChiSq{J}$ to $\ChiSq{J-1}$ (replacing $\mu$ by $\bar Y_{\cdot\cdot}$) is stated, not proved. $Y_{\cdot\cdot}$ should carry a bar.]

*Figure:* none.

---
### HW 37 (`20261121_231725.jpg`): Derivation of F-statistic

**Derivation of F-statistic**

**N.** In practice the population parameter $\sigma^2$ is also unknown.
We can use the following estimator:
$$
\begin{aligned}
&= \frac{(n_1-1)S_1^2 + (n_2-1)S_2^2 + \dots + (n_J-1)S_J^2}{(n_1-1) + (n_2-1) + \dots + (n_J-1)}\\
&= S^2_{\text{pooled}}\\
&= \frac{\sum_{j=1}^{J}\sum_{i=1}^{n_j}(Y_{ji}-\bar Y_{j\cdot})^2}{N-J} \qquad \leftarrow SS_{\text{residuals}}\ \text{(numerator)}\\
&\sim \frac{\sigma^2\ChiSq{N-J}}{N-J}
\end{aligned}
$$
[The display starts with "=" and no left-hand side. The distribution line is the "(2)" referred to below.]

Surprisingly, $SS_{\text{groups}}$ and $SS_{\text{residuals}}$ are independent.
We can compare this to the intuition that each $\bar Y_{j\cdot}$ is independent of $S_j^2$ for normal data.
[This statement is presumably the "(3)" referred to below; it is not numbered on the page.]

Combining
$$\frac{SS_{\text{groups}}/(J-1)}{SS_{\text{resid.}}/(N-J)} \sim \frac{\sigma^2\ChiSq{J-1}/(J-1)}{\sigma^2\ChiSq{N-J}/(N-J)} \quad \begin{matrix}(1)\\(2)\end{matrix}\ \Big]\ \text{ind. by (3)}$$
$$=: F_{J-1,\,N-J}$$
- arrow from the denominator $SS_{\text{resid.}}/(N-J)$ to "$\hat\sigma^2$"
- arrow from the first subscript $J-1$: "difference in complexity between alternative (full) model and null model (i.e. $J-1$ gaps between groups)"
- arrow from the second subscript $N-J$: "measures how accurately we can estimate the common $\sigma^2$ (noise)"

The F-statistic (or F ratio) is also known as the signal-to-noise ratio.
[(1) is HW 36's equation (1). "alterntive" spelt "attentive"-like; read as alternative.]

*Figure:* none (the annotations above are arrows to labels).

---

### HW 38 (`20261121_231734.jpg`): ANOVA tables

**ANOVA tables**

**N.** We can summarise all steps into an ANOVA table:

| Source | df | SS | MS(S) | F | $\Prob(F)$ |
|---|---|---|---|---|---|
| groups | $J-1$ | $SS_{\text{groups}}$ | $SS_{\text{groups}}/(J-1)$ | $MS_{\text{gr}}/MS_{\text{re}}$ | $\Prob(F_{J-1,N-J} \ge F)$ |
| resids | $N-J$ | $SS_{\text{resids}}$ | $SS_{\text{resids}}/(N-J)$ | | |
| total | $N-1$ | | | | |

In practice, we use statistical software (e.g. R/MATLAB) to perform an ANOVA test.

**Ex.** Data from Rotten Tomatoes were collected as movie ratings. The means and s.d.s of movie scores, classified by genre, are tabulated below:

| Genre | mean | s.d. | $n$ |
|---|---|---|---|
| Actions | 44.97 | 25.10 | 31 |
| Comedy | 49.78 | 26.35 | 27 |
| Horror | 41.29 | 27.04 | 17 |
| Romance | 47.20 | 31.57 | 10 |
| Animated | 60.58 | 26.73 | 12 |
| Thriller | 62.58 | 28.66 | 13 |
| **Overall** | 49.55 | (26.91) | 110 |

<u>Q:</u> Are there any differences in average movie ratings across genres?

[The overall "s.d." (26.91) is in brackets: it is the pooled s.d. $\sqrt{724.4}$ from HW 39, not the overall s.d.]

---

### HW 39 (`20261121_231739.jpg`): ANOVA tables (example)

**ANOVA tables (example)**

**Ex.** (continued) The overall mean rating of movies:
$$\bar y_{\cdot\cdot} = \frac{31(44.97) + 27(49.78) + \cdots}{110} = 49.55$$
The overall variance of movie ratings:
$$S^2_{\text{pooled}} = \frac{30(25.10)^2 + 26(26.35)^2 + \cdots}{104} = \frac{75334.4}{104}\ \begin{matrix}\leftarrow SS_{\text{resid}}\\ \leftarrow N-J\end{matrix} = 724.4 = (26.91)^2$$
Finally,
$$SS_{\text{groups}} = 31(44.97 - 49.55)^2 + 27(49.78 - 49.55)^2 + \cdots = \cdots = 5466.63$$
We now construct the ANOVA table:

| source | df | SS | MS | F | $\Prob(F)$ |
|---|---|---|---|---|---|
| genre | 5 | 5466.63 | 1093.3 | $1093.3/724.4 = 1.51$ | $\Prob(F_{5,104} \ge 1.51) = 0.193$ |
| resids | 104 | 75334.4 | 724.4 | | |
| total | 109 | | | | |

[Table drawn with solid rules after "source" and under the header and above "total", and dotted vertical rules between the other columns.]

and we thus conclude there is no evidence that there is a difference.

[Checked from the summary table: $\bar y_{\cdot\cdot} = 49.57$; $SS_{\text{resid}} = 75337.4$ (notes 75334.4, rounding of the s.d.s); $S_{\text{pooled}} = 26.91$ ✓. possible error: $SS_{\text{groups}}$ computes to $5533.8$ (with $\bar y_{\cdot\cdot}$ 49.55 or 49.57), not $5466.63$; then $MS = 1106.8$, $F = 1.53$, $p = 0.18$. The conclusion is unchanged. $\Prob(F_{5,104} \ge 1.51) = 0.193$ is correct for $F = 1.51$. "The overall variance" is the pooled (within-group) variance.]

---

### HW 40 (`20261121_231746.jpg`): ANOVA tables (post-hoc comparisons)

**ANOVA tables**

**Ex.** (continued) What if, after looking at the data, we conduct a two-sample t-test is carried out on the 'best' and 'worst' genres (i.e. Horror vs. Thriller)
We use the pooled variance:
$$T = \frac{\bar Y_{6\cdot} - \bar Y_{3\cdot}}{S_{\text{pool}}\sqrt{1/13 + 1/17}} = \dots = 2.13$$
and so the p-value for this comparison is
$$\Prob(T_{104} \ge 2.13) = 0.018$$
Based on this post-hoc analysis, we COULD decide it is better to classify an upcoming horror movie as a thriller movie to 'improve' their ratings.
[Checked: $T = 21.29/(26.91\sqrt{1/13+1/17}) = 2.15$ (notes 2.13); $\Prob(T_{104} \ge 2.13) = 0.018$ ✓. The test is one-sided as written.]

**Rem.** How do we [one word blotted out] reconcile this apparent contradiction?

There will always be a 'best' and 'worst' group in an experiment. If we choose to test 'best' vs. 'worst' after looking at the data, we must account for the fact that, for example, we could have chosen any of $\binom{6}{2} = 15$ comparisons. i.e. we use <u>Bonferroni's correction</u>.

**Ex.** We should modify the two-sample t-test p-value by $\binom{6}{2}$, i.e. corrected p-value $= 0.018 \times 15 = 0.266$.
[$0.018 \times 15 = 0.27$; $0.266$ is $15 \times 0.0177$ (the unrounded p-value).]

**Rem.** We only perform post-hoc tests with a Bonferroni correction only if the ANOVA test gives a significant result.
Also note that the Bonferroni correction is conservative.
This protects us from inflated Type I errors.

*Figure:* none.

---
### HW 41 (`20261121_231754.jpg`): Contrasts (1)

**Contrasts**

**N.** Comparing 'best' vs. 'worst', or any pairwise comparison, is an example of a <u>contrast</u>: a linear combination of group means $\sum a_j\mu_j$ such that the sum of weights $\sum a_j = 0$.
["worst" is written above a blot that crosses out the original word.]

**Ex.** Compare thriller to horror movies again. This is a contrast as
$$\mu_6 - \mu_3 = \sum a_j\mu_j, \quad \text{where } \vect a = (0\ 0\ {-1}\ 0\ 0\ 1).$$
[Group order as in the HW 38 table: Action, Comedy, Horror, Romance, Animated, Thriller.]

**N.** Contrasts are useful when we want to consider particular comparisons of our group means (and not just pairwise).
There are two popular sets of constraints; sum parameterisation and contrast parameterisation.

<u>Sum parameterisation:</u> One-way ANOVA can alternatively be written by
$$Y_{ji} = \underbrace{\mu}_{1 \text{ parameter}} + \underbrace{\alpha_j}_{J \text{ parameters}} + \varepsilon_{ji}, \qquad j = 1,\dots,J \text{ groups},\quad i = 1,\dots,n_j,\quad \varepsilon_{ji} \iid \Normal^{*}(0,\sigma^2)$$
where, for identifiability, set $\sum \alpha_j = 0$.
[The constraint's symbol is written like "$a_j$"; from the model it is $\alpha_j$. The handwriting of $a$ and $\alpha$ is close on this page.]

In this case, $\mu$ is interpreted as the overall mean $\sum\mu_j/J$, where $\alpha_j$ can be interpreted as the difference between the group [mean, crossed out] $j$ and the overall mean $\mu$.
(e.g. individual mark vs. average mark)
Each $\alpha_j$ is even itself a contrast — WLOG consider
$$
\begin{aligned}
\alpha_1 = \mu_1 - \mu &= \mu_1 - \sum\mu_j/J = (1 - 1/J)\mu_1 - 1/J\,\mu_2 - \cdots\\
&= \sum a_j\mu_j \quad \text{where } \sum a_j = (J-1)/J - 1/J - \cdots = 0
\end{aligned}
$$
Sum parameterisation is useful when all groups in a study are variations of some factor, OR if the $J$ groups exhaust all possible subgroups.

*Figure:* none.

---

### HW 42 (`20261121_231804.jpg`): Contrasts (2)

**Contrasts**

**N.** <u>Contrast parameterisation:</u> one-way ANOVA can also be written by $Y_{ji} = \mu + \alpha_j + \varepsilon_{ji}$ (identical to sum para.) where now for identifiability $\alpha_1 = 0$.

Then $\mu$ is interpreted as the mean of group 1, and $\alpha_j$ represents the distance between group $j$ and group 1.
(e.g. compare individual mark to best in class/max)

Contrast parameterisation is useful when one group can be considered a baseline/reference group.

**Rem.** In R/MATLAB, the default is to alphanumerically sort the groups and set group 1 as the baseline.

**N.** Note that all three parameterisations (mean, sum, contrast) specify the exact same model.

[About the bottom third of the page is blank.]

*Figure:* none.

---

### HW 43 (`20261121_231812.jpg`): Two-way ANOVA (1)

**Two-way ANOVA**

**Ex.** (Tooth growth vs. vitamin C) See R demo

**N.** <u>Two-way ANOVA</u>
If the groups in your study are obtained by crossing two or more factors (each at two or more levels), then we should respect the study design and consider a two-way ANOVA.
Model: the most general two-way setup is given by:
$$Y_{jki} = \mu + \alpha_j + \beta_k + \gamma_{jk} + \varepsilon_{jki}, \qquad
\begin{aligned}
j &= 1,\dots,J && \text{level of factor A}\\
k &= 1,\dots,K && \text{level of factor B}\\
i &= 1,\dots,n_{jk} && \text{indiv.}
\end{aligned}$$
[A blot precedes $n_{jk}$.]
The number of parameters is: $1 + J + K + J\cdot K$
The number of groups is: $J\cdot K$
To make this model identifiable, we impose constraints:
1. 'sum parameterisation' with
   $$\sum\alpha_j = 0,\quad \sum\beta_k = 0,\quad \textstyle\sum_j\delta_{jk} = \sum_k\delta_{jk} = 0$$
   $$\iff \underbrace{\alpha_\cdot = 0}_{1},\ \underbrace{\beta_\cdot = 0}_{1},\ \underbrace{\delta_{\cdot k} = \delta_{j\cdot} = 0}_{J+K-1}$$
   $\ast$ See A4!
2. 'contrast parameterisation' with
   $$\alpha_1 = 0,\quad \beta_1 = 0,\quad \delta_{1k} = 0,\quad \delta_{j1} = 0$$

[possible error: the interaction is $\gamma_{jk}$ in the model but $\delta_{jk}$ in the constraints (and $\gamma_{jk}$ again below). The underbraces count the constraints (1, 1 and $J+K-1$). "A4" presumably = Assignment 4 (not among the uploads).]

In either parameterisation, the parameters can be interpreted as:
- $\alpha_j$: main/marginal effects of factor A
- $\beta_k$: 〃 B
- $\gamma_{jk}$: interaction effects between factors A & B

Focusing on contrast parameterisation:
- $\mu$: mean/expected response of 'first' group
- $\alpha_j$: expected change when changing factor A → level $j$ from lvl. 1
- $\beta_k$: expected change when changing factor B → level $k$ from lvl. 1
- $\gamma_{jk}$: additional change when changing both factors A, B ↑

[A blot before "from lvl. 1" in the $\alpha_j$ line, with "level $j$" written above it.]

*Figure:* none.

---

### HW 44 (`20261121_231824.jpg`): Two-way ANOVA (2)

**Two-way ANOVA**

**N.** When we have a two-way ANOVA, our first point of interest is to <u>test for interactions</u>.
If there are interactions, then it may NOT be meaningful to talk about the main effects. Only if there are no interactions can we then talk about main effects.

**Ex.** (continued) The six treatment groups can actually considered as a $2 \times 3$ design instead:
$$(\text{OJ}, \text{VC}) \times (\text{Low}, \text{Medium}, \text{High})$$
See R demo.

**Rem.** Note that in R we used `lm` to fit ANOVA models.
This is because ANOVA is a special case of a linear model.

[About the bottom third of the page is blank. The R demo (tooth growth: R's `ToothGrowth` data, presumably) is not among the uploads.]

*Figure:* none.

---
### HW 45 (`20261121_231833.jpg`): Linear models (1)

**Linear models**

**Def.** Linear models assume that the data has the structure
$$\vect Y = \mat X\vect\beta + \vect\varepsilon$$
where
- $\vect Y$ is an $(n\times 1)$ vector of responses, one row for each individual response
- $\mat X$ is an $(n\times p)$ matrix of explanatory variables / covariates / predictors
- $\vect\beta$ is a $(p\times 1)$ vector of regression parameters
- $\vect\varepsilon$ is a $(n\times 1)$ vector of random deviations
- $n$ is the sample size
- $p$ is the number of predictors

**Ex.** One-way ANOVA is a kind of linear model.
Using the default contrast parameterisation,
$$Y_{ji} = \mu + \alpha_j + \varepsilon_{ji} \quad \text{where } \alpha_1 = 0$$
Then
$$
\vect Y = \begin{pmatrix} Y_{11}\\ \vdots\\ Y_{1n_1}\\ Y_{21}\\ \vdots\\ Y_{Jn_J}\end{pmatrix},\qquad
\mat X = \begin{pmatrix} 1 & 0 & 0 & \cdots & 0\\ & & \vdots & & \\ 1 & 0 & 0 & \cdots & 0\\ 1 & 1 & 0 & \cdots & 0\\ & & \vdots & & \\ 1 & 0 & 0 & \cdots & 1\end{pmatrix},\qquad
\vect\beta = \begin{pmatrix}\mu\\ \alpha_2\\ \vdots\\ \alpha_J\end{pmatrix}
$$
[$\mat X$ as drawn: first column all 1s; the block of group-1 rows is $(1, 0, \dots, 0)$; the first group-2 row is $(1, 1, 0, \dots, 0)$; the last row is $(1, 0, \dots, 0, 1)$; vertical dots in the middle columns.]

For the usual ANOVA null (all group means identical)
$$H_0: \alpha_2 = \dots = \alpha_J = 0$$
or, alternatively,
$$H_0: \mat R\vect\beta = \vect 0 \quad\text{vs.}\quad H_1: \mat R\vect\beta \ne \vect 0$$
where
$$\mat R = \begin{pmatrix} 0 & 1 & 0 & \cdots & 0\\ 0 & 0 & 1 & 0\cdots & 0\\ \vdots & & & \ddots & \vdots\\ 0 & \cdots & & \cdots 0 & 1\end{pmatrix} \quad \text{is the } \underline{\text{restriction}} \text{ matrix.}$$
[$\mat R$ is $(J-1)\times J$: a zero first column followed by the identity.]

*Figure:* none (matrices above).

---

### HW 46 (`20261121_231843.jpg`): Linear models (2)

**Linear models**

**N.** Linear models are popular because they have a universal test for <u>any</u> restrictions on the model parameters.
In general, if we take
$$H_0: \mat R\vect\beta = \vect 0 \quad\text{vs.}\quad H_1: \mat R\vect\beta \ne \vect 0$$
we simply:
- Fit the null model, imposing restriction
- Fit the alt. model, without restriction

and then we compare the residual sum-of-squares (RSS) left over from the two model fits, by the GLRT:
$$\frac{(RSS_0 - RSS_1)/r}{RSS_1/df_1} \sim F_{r,\,df_1}$$
- arrow to the numerator from the label "how much worse the null model is, vs. alt model"
- arrow (↑) to the denominator from "how well does the alt. model fit the data"
- a bracket from the whole fraction to:
$$r = \#\text{ restrictions under } H_0 = \rank(\mat R) = df_0 - df_1$$

This test is a generalisation of ANOVA to some arbitrary restriction matrix $\mat R$ (not just default of equal means).

[The distribution under $H_0$ is stated, not derived. "$df_1$" = residual degrees of freedom of the alternative model. About the bottom fifth of the page is blank; stray pencil marks at the lower left.]

*Figure:* none (the labelled arrows above).

---

### HW 47 (`20261121_231848.jpg`): Linear model (two-way ANOVA)

**Linear model (two-way ANOVA)**

**Ex.** Consider the earlier two-way ANOVA example.
What if we are interested in
$$H_0: \bigl\{\underbrace{\mu_1 = \mu_2 = \mu_3}_{\text{orange juice}},\ \underbrace{\mu_4 = \mu_5 = \mu_6}_{\text{tablets}}\bigr\} \quad \leftarrow \text{dosage does not matter, but type of supplement does}$$
$$
\begin{aligned}
&\iff H_0: \Bigl\{\begin{matrix}\alpha_2 = 0\\ \alpha_3 = 0\end{matrix},\ \alpha_4 = \alpha_5 = \alpha_6\Bigr\}\\
&\iff H_0: \Bigl\{\begin{matrix}\alpha_2 = 0\\ \alpha_3 = 0\end{matrix},\ \begin{matrix}\alpha_4 - \alpha_5 = 0\\ \alpha_5 - \alpha_6 = 0\end{matrix}\Bigr\}\\
&\iff H_0: \mat R\vect\beta = \vect 0, \quad\text{where}
\end{aligned}
$$
$$
\mat R = \begin{pmatrix}0&1&0&0&0&0\\0&0&1&0&0&0\\0&0&0&1&-1&0\\0&0&0&0&1&-1\end{pmatrix},\qquad
\vect\beta = \begin{pmatrix}\mu\\ \alpha_2\\ \alpha_3\\ \alpha_4\\ \alpha_5\\ \alpha_6\end{pmatrix}
$$
[The six tooth-growth groups are treated here as six groups of a one-way model in the contrast parameterisation (groups 1–3 orange juice, 4–6 tablets, presumably at increasing dose). $\vect\beta$ is written "$\mathrm{B}$" in the last display. Checked: $\mat R\vect\beta = \vect 0$ encodes exactly the stated $H_0$; $\rank(\mat R) = 4$. Bottom 40% of the page blank.]

*Figure:* none (matrices above).

---

### HW 48 (`20261121_231856.jpg`): Linear model (GLRT) (1)

**Linear model (GLRT)**

**N.** Where does the universal test for linear models come from? Under our assumption $\vect\varepsilon \iid \Normal^{*}(0,\sigma^2)$,
$$\vect Y \sim \Normal_{n\times 1}(\mat X\vect\beta, \sigma^2\mat I)$$
Suppose $\sigma^2$ is known for now. Then the likelihood function for $\vect\beta$ is given by
$$L(\vect\beta \given \vect y, \mat X) = \Bigl(\frac{1}{\sqrt{2\pi\sigma^2}}\Bigr)^{n}\exp\Bigl\{-\frac{1}{2\sigma^2}(\vect y - \mat X\vect\beta)\T(\vect y - \mat X\vect\beta)\Bigr\}$$
and so the log-likelihood is
$$\ell = -\frac n2\log\sigma^2 - \frac{1}{2\sigma^2}(\vect y - \mat X\vect\beta)\T(\vect y - \mat X\vect\beta) + c$$
We now maximise the log-likelihood w.r.t. $\vect\beta$ under no restrictions (i.e. unconstrainted maximisation):
$$0 = \frac{\partial\ell}{\partial\vect\beta} = -\frac{1}{2\sigma^2}\bigl[-\mat X\T(\vect y - \mat X\vect\beta)\bigr] = \frac{1}{\sigma^2}\mat X\T(\vect y - \mat X\vect\beta)$$
[possible error: the middle expression is missing a factor 2: $\partial/\partial\vect\beta$ of the quadratic form is $-2\mat X\T(\vect y - \mat X\vect\beta)$; the right-hand side is correct.]
which implies
$$\mat X\T\vect y = \mat X\T\mat X\vect\beta \qquad \text{(orthogonal}$$
$$\iff \hat{\vect\beta}_{\text{MLE}} = (\mat X\T\mat X)^{-1}\mat X\T\vect y \qquad \text{(if } \mat X\T\mat X \text{ is invertible, i.e. } \mat X\T \text{ has full rank)}$$
We can verify that $\E(\hat{\vect\beta}_{\text{MLE}}) = \vect\beta$.
The matrix $(\mat X\T\mat X)^{-1}\mat X\T$ is a.k.a. the 'hat matrix'.

[possible error: the hat matrix is $\mat X(\mat X\T\mat X)^{-1}\mat X\T$ (it maps $\vect y$ to $\hat{\vect y}$); $(\mat X\T\mat X)^{-1}\mat X\T$ maps $\vect y$ to $\hat{\vect\beta}$. "(orthogonal" has no closing bracket or further text. "$\mat X\T$ has full rank": $\mat X$ has full column rank.]

*Figure:* none.

---
### HW 49 (`20261121_231902.jpg`): Linear model (GLRT) (2)

**N.** Therefore, the ML acheived under no restrictions is:
$$
\begin{aligned}
\sup_{\vect\beta} L(\vect\beta \given \vect y, \mat X) &= \Bigl(\frac{1}{\sqrt{2\pi\sigma^2}}\Bigr)^{n}\exp\Bigl\{-\frac{1}{2\sigma^2}(\vect y - \mat X\hat{\vect\beta})\T(\vect y - \mat X\hat{\vect\beta})\Bigr\}\\
&\overset{\text{by } \vect a\T\vect a = \sum a_i^2}{=} \Bigl(\frac{1}{\sqrt{2\pi\sigma^2}}\Bigr)^{n}\exp\Bigl\{-\frac{1}{2\sigma^2}\cdot RSS_1\Bigr\}
\end{aligned}
$$
[The justification "by $\vect a\T\vect a = \sum a_i^2$" is written at the left with a curved arrow to the "=".]

Similarly, under the restricted model, we can optimise $\vect\beta$ subject to the constraint $\mat R\vect\beta = \vect 0$, which gives the estimator $\vect\beta_{\text{restricted}}$.
Thus, the ML under $H_0$ is therefore:
$$
\sup_{H_0: \mat R\vect\beta = \vect 0} L(\vect\beta \given \vect y, \mat X) = \Bigl(\frac{1}{\sqrt{2\pi\sigma^2}}\Bigr)^{n}\exp\Bigl\{-\frac{1}{2\sigma^2}(\vect y - \mat X\hat{\vect\beta}_r)\T(\vect y - \mat X\hat{\vect\beta}_r)\Bigr\} = \Bigl(\frac{1}{\sqrt{2\pi\sigma^2}}\Bigr)^{n}\exp\Bigl\{-\frac{1}{2\sigma^2}\cdot RSS_0\Bigr\}
$$
Therefore, the GLRT for testing $H_0: \mat R\vect\beta = \vect 0$ versus $H_1: \mat R\vect\beta \ne \vect 0$ is
$$\Omega = \exp\Bigl\{-\frac{1}{2\sigma^2}(RSS_0 - RSS_1)\Bigr\}$$
Thus, the larger the difference $RSS_0 - RSS_1$, the smaller the GLRT statistic $\Omega$.
[GLRT statistic again written with an $\Omega$-like symbol, as on HW 27; $\Lambda$ on HW 24 and 36.]

How large however, is 'large'? We have that
$$
\begin{aligned}
RSS_1 &\sim \ChiSq{n-p}\,\sigma^2 && \leftarrow n \text{ is \# observations, } p \text{ is \# parameters}\\
RSS_0 &\sim \sigma^2\ChiSq{n-(p-r)} && p - r \text{ is \# parameters under null}
\end{aligned}
$$
Thus (as sum of $\chi^2$ is $\chi^2$, difference requires ind.)
$$RSS_0 - RSS_1 \sim \sigma^2\ChiSq{r}$$
$$\iff \frac{1}{\sigma^2}\Bigl(\frac{RSS_0 - RSS_1}{r}\Bigr) \sim \frac{\ChiSq{r}}{r} \quad \text{which has expectation 1. (rescaled)}$$
[The $\chi^2$ distributions of $RSS_0$, $RSS_1$ and the independence are stated, not proved; $RSS_0$'s distribution holds under $H_0$.]

*Figure:* none.

---

### HW 50 (`20261121_231908.jpg`): Linear model F-table

**Linear model F-table**

**N.** However, generally $\sigma^2$ is unknown. We can estimate $\sigma^2$ by
$$\hat\sigma^2 = \frac{RSS_1}{n-p} \underset{\text{(ANOVA)}}{=} MS_{\text{errors}} = MS_{\text{resid}}$$
Moreover, we can show
$$\frac{(RSS_0 - RSS_1)/r}{RSS_1/(n-p)} \quad \Big]\ \text{independent} \qquad \sim \frac{\ChiSq{r}/r}{\ChiSq{n-p}/(n-p)} =: F_{r,\,n-p} = F_{r,\,df_1}$$
[A bracket with two arrows links numerator and denominator, labelled "independent". "We can show": not shown.]

This can be summarised in a linear model F-table.

| | Model | df | RSS | F | $\Prob(F)$ |
|---|---|---|---|---|---|
| Group → | ⟨difference⟩ | $r$ | $RSS_0 - RSS_1$ | $\dfrac{RSS_0 - RSS_1/r}{RSS_1/n-p}$ | $\Prob(F_{r,n-p} \ge F)$ |
| Resids → | Alternative | $n-p$ | $RSS_1$ | | |
| Total → | Null | $n-(p-r)$ | $RSS_0$ | | |

[The row labels "Group → / Resids → / Total →" are written outside the table to the left, linking to the ANOVA table of HW 38. The F entry lacks brackets: $(RSS_0-RSS_1)/r \big/ \bigl(RSS_1/(n-p)\bigr)$ is meant. Table drawn with vertical rules between columns and a horizontal rule under the header and above "Null". Bottom 40% of the page blank.]

*Figure:* none (the table).

---

### HW 51 (`20261121_231913.jpg`): Linear models (example)

**Linear models (example)**

**Ex.** (Jump distance vs. heights of students)
Consider a cubic model for jump distance vs. height:
$$\text{jump}_i = \beta_0 + \beta_1\,\text{height}_i + \beta_2\,\text{height}_i^2 + \beta_3\,\text{height}_i^3 + \varepsilon_i$$
<u>Q:</u> Is this a linear model? Let
$$
\vect Y = \begin{pmatrix}\text{jump}_1\\ \vdots\\ \text{jump}_n\end{pmatrix},\quad
\mat X = \begin{pmatrix}1 & \text{height}_1 & \text{height}_1^2 & \text{height}_1^3\\ & & \vdots & \\ 1 & \text{height}_n & \text{height}_n^2 & \text{height}_n^3\end{pmatrix},\quad
\vect\beta = \begin{pmatrix}\beta_0\\ \beta_1\\ \beta_2\\ \beta_3\end{pmatrix},\quad
\vect\varepsilon = \begin{pmatrix}\varepsilon_1\\ \vdots\\ \varepsilon_n\end{pmatrix}
$$
[Arrow up to the columns of $\mat X$:] "columns must be ~~non-linear~~ / linearly independent (full rank $\mat X$)" ["non-linear" is struck through.]

Thus this is a linear model! Note this is linear in the parameters $\vect\beta$, not in the predictors.

<u>Q:</u> Is a cubic model in height necessary, or is a quadratic model enough?
(see R demo)

[The R demo is not among the uploads. Bottom 30% of the page blank. This is the last handwritten page.]

*Figure:* none.
