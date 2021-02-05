(clear-all)

(define-model sc2beacons
  ;; do not change these parameters
  (sgp :esc t :bll .5 :ol t :er t :lf 0)

  ;; adjust these as needed
  (sgp :v nil :ans .2 :mp 10.0 :rt -60)

  ;; need to use a mouse
  (sgp :needs-mouse t :show-focus t)

  ;; This type holds all the game info
  (chunk-type game-state beacon_x beacon_y state)
  (chunk-type try-strategy strategy state)

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
  ;; Provide a mouse for the model's motor module to use
  (install-device '("motor" "cursor" "mouse"))

  (p start
     =goal>
       isa game-state
       state start
    ==>
     !output! ("start")
     =goal>
       state find-beacon
  )

  (p find-next-beacon
   =goal>
      isa       try-strategy
      state     find-beacon
  ==>
   +visual-location>
      isa       visual-location
      :attended nil
      kind      beacon
      screen-y  lowest
   =goal>
      state     looking)

(p attend-beacon
   =goal>
      isa        try-strategy
      state      looking
   =visual-location>
   ?visual>
      state      free
  ==>
   =goal>
      state      attending
   +visual>
      isa        move-attention
      screen-pos =visual-location)



  (p find-beacon
   =goal>
      isa        try-strategy
      state      check-for-beacon
   =visual-location>
   ?visual>
      state      free
  ==>
   +visual>
      isa        move-attention
      screen-pos =visual-location
   =goal>
      state      read-beacon)

(p check-for-beacon
   =goal>
      isa       try-strategy
      state     read-beacon
  ==>
   =goal>
      state     prepare-move
   +visual-location>
      isa       visual-location
      value     "B")

  (p move-mouse
   =goal>
      isa        try-strategy
      state      prepare-mouse
   =visual-location>
   ?visual>
      state      free
   ?manual>
      state      free
  ==>
   +visual>
      isa        move-attention
      screen-pos =visual-location
   =goal>
      state      move-mouse
   +manual>
      ;;isa        move-cursor
      ;;loc        =visual-location)
      cmd    press-key
      key    "C"
     )

   (p click-mouse
     =goal>
       state move-mouse
     ?manual>
       state free
     ;;!eval! (< =pos 0)
     ;;!eval! (<= =vel 0.02)
  ==>
      !output! ("click")
     =goal>
       state find-beacon
     +manual>
       ;;isa    click-mouse
       cmd    press-key
       key    "C"
       )
)