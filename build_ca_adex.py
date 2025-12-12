import nest

from pynestml.frontend.pynestml_frontend import generate_nest_target


def generate_code(with_alt_version=False):
    if with_alt_version:
        generate_nest_target(input_path=["ca_adex.nestml", "ca_adex_alt.nestml"],
                             target_path="target",
                             logging_level="INFO",
                             module_name="ca_adex_module")
    else:
        generate_nest_target(input_path="ca_adex.nestml",
                             target_path="target",
                             logging_level="INFO",
                             module_name="ca_adex_module")


if __name__ == "__main__":
    with_alt_version = True
    generate_code(with_alt_version)
