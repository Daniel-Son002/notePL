# src1.dsl
module1 concat_str foo bar baz debug=1 trace=0
module1 add_num 1 2 3 5 6 10 2 5 1 3 type=int
# module1 add_num 1 2 3.0 type=float
module1 mul_num 4 3 2 type=int
module1 mul_num 4.0 3 2 type=float
module1 mul_num 4.0 0.25 type=float
module1 mul_num 10 2 type=int
module1 div_num 9 3 type=int

module1 print_str Hello world! This my CS 252 project!!
