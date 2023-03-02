
## Feasibility

Consider a set of constraints of the form 
$$\begin{array}\\ 
g_i(x)=0, i\in \mathcal{E}\\
g_i(x) \geq 0, i\in \mathcal{I} 
\end{array}$$
- Here, $\{g_i\}$ are set of given functions
- $\mathcal{E}$ is an index set for the equality constraints
- $\mathcal{I}$ is an index set for the inequality constraints

>[!Note] Defininition: Feasibility
>  - Points that satisfy all the constraints are said to be *feasible*.
>  - The **set** of all feasible points is termed the *feasible region* or *feasible set*.
>  - Denoted by $S$.

> [!Important] Active and inactive constraints
>  - At a feasible point $\bar{x}$, an inequality constriant $g_i(x)\geq 0$ is said to be *binding* or *active* if $g_i(\bar{x})=0$. The point is said to be on the boundary of the constriant.
>  - The feasible point is *non-binding* or *inactive* if $g_i(\bar{x})>0$.
>  - All *equality constraints* are regarded as active at any feasible point.

- The *active set* at a feasible point is defined as the set of all constraints that are active at that point.
- The set of feasible points for which atleast one inequality is binding is called the *boundary* of the feasible region. All other feasible points are *interior points*.

## Optimality

For an $n$-dimensional problem
$$\begin{array}\\
\underset{x\in S}{\text{minimize}} & f(x)
\end{array}$$
> [!Note]
> The set $S = \mathbb{R}^n$ for an *unconstriant problem* and $S \subseteq \mathbb{R}^n$ for a *constriant problem*.

The point $x^*$ is a *global minimizer* of $f(.)$ if 
$$
\begin{array}\\
f(x^*) \leq f(x) & \forall x \in S
\end{array}
$$
In addition if $x^*$ satisfies
$$
\begin{array}\\
	f(x^*) < f(x) & \forall x\in S
\end{array}$$
then $x^*$ is a *strict global minimizer* of $f(.)$.
![[Pasted image 20230302184356.png]]

If global solution cannot be found, then we would try to find a local solution, i.e., a *local minimizer*. A local minimizer of $f$ in $S$ is point that satisfies, 
$$
\begin{array}\\
	f(x^*) \leq f(x) && \forall x\in S & \text{such that } ||x-x^*|| < \epsilon 
\end{array}$$
Similarly a *strict local minimizer* would satisfy
$$
\begin{array}\\
	f(x^*) < f(x) && \forall x\in S & \text{such that} & x\neq x^* & \text{and}&||x-x^*|| < \epsilon 
\end{array}$$
> [!Note] Stationary points
> - Points for which the first derivative of the function is zero. This is defined for unconstraint problems. Constraint problems have different definition.
> - All minimizers are stationary point, but not vice-versa.
> - Some algorithms use stationary points to find the minimizers.

> A *global solution* will be both a *local solution* and a *stationary point*.

## Convexity
> [!Important] Convex set
> - A set $S$ is *convex*, if for any element $x$ and $y$ of $S$,$$\begin{array}\\ \lambda x + (1-\lambda)y\in S & \forall & 0 \leq \lambda \leq 1\end{array}$$
> - This is a convex combination.
> - Sets that violet this property are *non-convex*.

- A function $f$ is *convex* on set $S$ if it satisfies$$f(\lambda x + (1-\lambda)x) \leq \lambda f(x) + (1-\lambda)f(x)$$
- A function is *concave* on set $S$ if it satisfies $$f(\lambda x + (1-\lambda)x) \geq \lambda f(x) + (1-\lambda)f(x)$$

A global solution can be found if the objective function is a convex function an the feasible set is a convex set.
> [!Note] Convex optimisation problem
> - A problem is called a convex optimisation problem if $S$ is a convex set and $f$ is a convex function for a problem stated as
$$\begin{array}\\ \underset{x\in S}{\text{minimize}} & f(x) \end{array}$$
> - A problem $$\begin{array}\\ \text{minimize} & f(x)\\ \text{subject to} & g_i(x), &i = 1, 2, \dots, n \\ \end{array}$$is a *Convex optimization problem* if $f$ is **convex** and $\{g_i\}$ are **concave**.


