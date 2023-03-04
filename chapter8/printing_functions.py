import printing_models as pm
from printing_models import print_models, show_completed_models 

unprinted_designs = [ 'toycar', 'spaceship', 'rocket' ]
completed_models = []

pm.print_models(unprinted_designs, completed_models)
pm.show_completed_models(completed_models)


