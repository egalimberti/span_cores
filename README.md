# [Mining (maximal) Span-cores from Temporal Networks](http://edoardogalimberti.altervista.org/documents/papers/Mining__maximal__Span-cores_from_Temporal_Networks.pdf)

## Folders
* datasets: datasets listed in Table 1, PrimarySchool, HighSchool
* output: destination of code's output
* span_cores: code

## Code
To use the code, first run 'python setup.py build_ext --inplace' from the folder 'span_cores/'.
This command builds the .c files created by Cython.
Alternatively, without running the mentioned command, it is possible to directly execute the Python code.

## Execution
Run the following command from the folder 'span_cores/':
  'python span_cores.py [-h] [--ver] d a'

#### Positional arguments:
  * d           dataset
    * prosper-loans
    * lastfm
    * wiki-talk
    * dblp
    * stack-overflow
    * wikipedia
    * amazon
    * epinions
    * primary_school
    * high_school
    
  * a           algorithm
    * nsc       Naive-span-cores (beginning of Section 4)
    * sc        Span-cores (Algorithm 1)
    * nmsc      Naive-maximal-span-cores (beginning of Section 5)
    * msc       Maximal-span-cores (Algorithm 2)
    * info      dataset info

#### Optional arguments:
  * -h, --help  show the help message and exit

  * --ver       verbose
  	print the results of the selected algorithm in the output folder with the format 'span    order    vertices'
  	
#### Example:
  'python span_cores.py prosper-loans sc --ver'
  
## Datasets

#### Format
  * space-separated files
  * first line specifies, respectively,
    * number of timestamps
    * number of vertices
    * number of edges
  * following lines are in the format *tij i < j*, ordered by *t*
  * timestamps' and vertices' identifiers start from 0
  
#### Contact
Mail to [edoardo.galimberti@isi.it](mailto:edoardo.galimberti@isi.it) for the datasets missing in this repository.
