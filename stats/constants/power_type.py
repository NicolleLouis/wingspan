class PowerType:
    HUNT = 'HUNT'
    HUNT_HUMAN = 'Chasse'
    FOOD = 'FOOD'
    FOOD_HUMAN = 'Nourriture'
    REPRODUCTION = 'REPRODUCTION'
    REPRODUCTION_HUMAN = 'Reproduction'
    EGG = 'EGG'
    EGG_HUMAN = 'Oeuf'
    CARD_DRAW = 'CARD_DRAW'
    CARD_DRAW_HUMAN = 'Pioche'
    CARD_BONUS = 'CARD_BONUS'
    CARD_BONUS_HUMAN = 'Piocher des carte bonus'
    HATCH_BIRD = 'HATCH_BIRD'
    HATCH_BIRD_HUMAN = 'Poser un autre oiseau'
    MOVING = 'MOVING'
    MOVING_HUMAN = 'Déplacement'
    OTHER = 'OTHER'
    OTHER_HUMAN = 'Autre'
    choices = (
        (HUNT, HUNT_HUMAN),
        (FOOD, FOOD_HUMAN),
        (REPRODUCTION, REPRODUCTION_HUMAN),
        (EGG, EGG_HUMAN),
        (CARD_DRAW, CARD_DRAW_HUMAN),
        (CARD_BONUS, CARD_BONUS_HUMAN),
        (HATCH_BIRD, HATCH_BIRD_HUMAN),
        (MOVING, MOVING_HUMAN),
        (OTHER, OTHER_HUMAN),
    )
