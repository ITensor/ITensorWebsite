# <img src="docs/VERSION/book/icon.png" class="largeicon">  The ITensor Book

Tensor methods are a powerful approach for problems in physics and
applied math, but keeping track of tensor indices by hand
can be tedious and make your code fragile and prone to bugs.

Inspired by diagrammatic notation for tensor networks, ITensor lets you
focus on the connectivity of tensor networks without thinking about
low-level details like index ordering and data permutation.
Indices in ITensor carry extra information so that "multiplying" 
two ITensors contracts all matching indices, similar to Einstein summation.
ITensor is very efficient despite these high level features.

The goal of this book is to quickly familiarize you with the 
main features of ITensor. Later chapters turn to advanced features and
customizing higher-level parts of the library.

# Table of Contents

- [[ITensor Library Overview|book/intro]]

### Introduction to ITensor

- [[Index Objects|book/index]]

- [[ITensor Basics|book/itensor_basics]]

- [[Contracting ITensors|book/itensor_contraction]]

- [[Factorizing ITensors (SVD Example)|book/itensor_factorizing]]

- [[Case Study: TRG Algorithm|book/trg]]

<!--
- [[Sparse ITensors (combiners, diagonal,...)|book/itensor_sparse]]
-->

### QN ITensors: Block-Sparse, Quantum Number Conserving Tensors

- [[QN ITensor Introduction|book/qnitensor_intro]]
- [[Block-Sparse Tensors|book/block_sparse]]
- [[QN Index|book/qnindex]]
- [[Quantum Number (QN) Objects|book/qn]]

<!--
- [[QN ITensor Basics|book/qnitensor_basics]]
-->

### Matrix Product States and DMRG

### Design of ITensor Library and Internals

<!--
- [[Dynamic Storage System|book/dynamic_storage]]
- [[Scale Factors (LogNum)|book/scale_factors]]
- [[TensorRef Layer|book/tensorref]]
-->

<br/>
<span style="float:right;"><img src="docs/VERSION/arrowright.png" class="icon"> 
[[ITensor Library Overview|book/intro]]
</span>
