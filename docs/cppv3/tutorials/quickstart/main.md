<span class='article_title'>ITensor Basics Quick Start</span>

<span class='article_sig'>Thomas E. Baker &amp; Miles Stoudenmire &mdash; May 4, 2016</span>

Let's create the simplest possible program involving an ITensor.

If you need help compiling the program below, there is a set of codes in the 
`tutorial/project_template` folder included in the ITensor source directory which you can
use as a template for your own program. See the README file in `tutorial/project_template`
for instructions.

<!--(For a similar guide oriented towards DMRG calculations, see [[DMRG Quick Start|tutorials/DMRGquickstart]].)-->

Here is our program `hello_itensor.cc`.

    #include "itensor/all.h"
    using namespace itensor;

    int main()
    {
    auto i = Index(4,"index i");
    auto j = Index(6,"index j");
    auto T = ITensor(i,j);

    T.set(i=3,j=2,3.14159);

    PrintData(T);

    return 0;
    }


To understand what this program does, let us start at the top. The line

    #include "itensor/all.h"

pulls in _all_ of the ITensor library's classes and functions.

The next line of the program 

    using namespace itensor;

says to not require explicitly writing the itensor namespace in front 
of function and type names.
Otherwise you would have to type things like `itensor::Index` instead of
just `Index`.


Now we reach the actual code our program will run.
C++ requires that all programs have
a function named `main` which is the first function
to run when your program is executed

    int main()
    {

    //...rest of code here

    return 0;
    }

Now let us look at the body of the code. 
First we define tensor indices i and j, of type `Index`.

    auto i = Index(4,"index i");
    auto j = Index(6,"index j");

Each Index has a name and a size. Using these indices, we can define
an ITensor

    auto T = ITensor(i,j);

which starts out with all elements zero. To change an element, we
can call

    T.set(i=3,j=2,3.14159);

which sets the i=3, j=2 element to the value 3.14159. 

The `PrintData` macro conveniently prints information about the
ITensor T (such as its indices) and shows all of its non-zero elements:
 
    PrintData(T);


