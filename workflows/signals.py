

from django.dispatch import Signal

#A transition named 'transition' has occured on this 'object' intitiated by this 'user'
transition_has_occured = Signal(providing_args=['object', 'transition', 'user'])

