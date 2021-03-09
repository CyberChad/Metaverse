(clear-all)

(define-model sc2beacons
  ;; do not change these parameters
  ;;(sgp :esc t :bll .5 :ol t :er t :lf 0 :trace-detail high)
  (sgp :esc t :lf .05 :trace-detail high)

  ;; adjust these as needed
  ;;(sgp :v nil :ans .2 :mp 10.0 :rt -60)

  ;; need to use a mouse
  (sgp :needs-mouse t :show-focus t)

  ;; This type holds all the game info
  (chunk-type game-state beacon_x beacon_y state)
  ;;(chunk-type try-strategy strategy state)

  ;; This chunk-type should be modified to contain the information needed
  ;; for your model's learning strategy

  ;;(chunk-type learned-info action)

  ;; Declare the slots used for the goal buffer since it is
  ;; not set in the model defintion or by the productions.
  ;; See the experiment code text for more details.

   (declare-buffer-usage goal game-state :all)

  ;; Create chunks for the items used in the slots for the game information and state

  ;; (define-chunks  (move-mouse) (click-mouse)  )

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
       state play
  )

  (p find-next-beacon
   =goal>
      isa       game-state
      state     play
      beacon_x  =loc_x
      beacon_y  =loc_y
   ?manual>
       state free
  ==>
  !output! ("p find-next-beacon:")
   =goal>
      state     play
     +manual>
       cmd press-key
       key "C"

   )

)