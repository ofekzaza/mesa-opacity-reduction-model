OURS_NAME = "ours model"

def parse_name_for_plots(name: str) -> str:
    plot_name = name.replace("ours", OURS_NAME) if "ours" in name else name
    plot_name = plot_name.replace("_reduction", "_winds")
    plot_name = plot_name.replace("_", " ")
    plot_name = plot_name.replace("-", " ")
    plot_name = plot_name.capitalize()
    return plot_name
