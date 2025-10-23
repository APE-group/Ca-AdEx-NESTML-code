import nest

from pynestml.frontend.pynestml_frontend import generate_nest_target

generate_nest_target(input_path="ca_adex.nestml",
                     target_path="target",
                     logging_level="INFO",
                     module_name="ca_adex_module")
