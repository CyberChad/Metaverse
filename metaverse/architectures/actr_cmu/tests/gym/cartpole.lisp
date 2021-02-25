(clear-all)

(define-model cartpole
  ;; do not change these parameters
  ;;(sgp :esc t :bll .5 :ol t :er t :lf 0 :trace-detail high)
  (sgp :esc t :lf .05 :trace-detail high)

  ;; adjust these as needed
  ;;(sgp :v nil :ans .2 :mp 10.0 :rt -60)

  ;; This type holds all the game info

  ;; (chunk-type game-state cart_pos cart_vel pole_pos pole_vel state)
  (chunk-type game-state cart_pos cart_vel pole_pos pole_vel state)

  ;; This chunk-type should be modified to contain the information needed
  ;; for your model's learning strategy

  ;;(chunk-type learned-info action)

  ;; Declare the slots used for the goal buffer since it is
  ;; not set in the model defintion or by the productions.
  ;; See the experiment code text for more details.

   (declare-buffer-usage goal game-state :all)

  ;; Create chunks for the items used in the slots for the game information and state

  ;;(define-chunks )

  ;; Provide a keyboard for the model's motor module to use
  (install-device '("motor" "keyboard"))

  (p start
     =goal>
       isa game-state
       state start
    ==>
     !output! ("start")
     =goal>
       state play
  )

  (p go-left
     =goal>
       isa game-state
       state play
       pole_pos =pos
     cart_vel =vel
     ?manual>
       state free
     !eval! (< =pos 0)
     ;;!eval! (<= =vel 0.02)
  ==>
      !output! ("go-left")
     =goal>
       state play
     +manual>
       cmd press-key
       key "0")

     (p go-right
     =goal>
       isa game-state
       state play
        pole_pos =pos
        cart_vel =vel
     ?manual>
       state free
        !eval! (> =pos 0)
        ;;!eval! (<= =vel 0.02)
    ==>
        !output! ("go-right")
     =goal>
       state play
     +manual>
       cmd press-key
       key "1")

  (p clear-new-imaginal-chunk
     ?imaginal>
       state free
       buffer full
     ==>
     -imaginal>)
  )