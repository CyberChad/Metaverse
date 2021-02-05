(clear-all)

(define-model count

(sgp :esc t :lf .05 :trace-detail high)

(add-dm
 (b first 1 second 2)
 (c first 2 second 3)
 (d first 3 second 4)
 (e first 4 second 5)
 (f first 5 second 6)
 (first-goal start 2 end 4)
 )

(goal-focus first-goal)

(p start
   =goal>
      start       =num1
      count       nil
 ==>
   =goal>
      count       =num1
   +retrieval>
      first       =num1
)

(P increment
   =goal>
      count       =num1
    - end         =num1
   =retrieval>
      first       =num1
      second      =num2
 ==>
   =goal>
      count       =num2
   +retrieval>
      first       =num2    !output!       (=num1)
)

(P stop
   =goal>
      count       =num
      end         =num
 ==>
   -goal>
   !output!       (=num)
)
)
