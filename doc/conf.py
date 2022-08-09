import datetime

extensions = [
    "sphinx_copybutton",
    "sphinx_rtd_theme",
]

project = "Разработка на review.elvees.com"

source_encoding = "utf-8"
master_doc = "index"

language = "ru"
exclude_patterns = ["README.rst", "build", ".*"]
highlight_language = "none"
templates_path = ["_templates"]

copyright = '2021-{} АО НПЦ "ЭЛВИС"'.format(datetime.datetime.now().year)

pygments_style = "sphinx"
numfig = True

html_theme = "sphinx_rtd_theme"
html_static_path = []

html_domain_indices = False
html_use_index = False
html_show_sourcelink = False
html_show_sphinx = False
html_show_copyright = True
html_file_suffix = None
html_search_language = language

html_theme_options = {
    "collapse_navigation": False, # Can expand and collapse sidebar entries
    "prev_next_buttons_location": "both", # Top and bottom of the page
    "style_external_links": True # Display an icon next to external links
}
