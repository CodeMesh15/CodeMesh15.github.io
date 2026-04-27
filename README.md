# Owais Makroo Portfolio

A personal portfolio built with HTML, Tailwind CSS, and a custom Python static site generator.

## Project Structure

- `assets/data/`: A directory containing YAML files with all the content for the portfolio (experience, research, projects, writing, etc.). Update these files to change the text and links on your website.
- `assets/template.html`: A Jinja2 HTML template. It defines the structure, layout, and styling (using Tailwind CSS) of the website.
- `build.py`: A Python script that reads the YAML files from the `assets/data/` directory and injects their content into `template.html` to generate the final `index.html`.
- `index.html`: The generated static website. **Do not edit this directly**, as your changes will be overwritten the next time you run the build script.

## How `build.py` Works

The `build.py` script acts as a minimalist static site generator. Here is a step-by-step breakdown of its process:

1. **Reads Data:** It uses the `pyyaml` library to load all the YAML files in the `assets/data/` directory and combines them into a single Python dictionary.
2. **Configures Jinja2:** It sets up a Jinja2 environment and adds custom filters (like `tojson`, which safely converts Python lists into JSON strings so they can be read by JavaScript inside the template).
3. **Loads Template:** It loads the `template.html` file from the current directory.
4. **Renders HTML:** It passes the loaded data dictionary into the Jinja2 template. The template engine replaces the `{{ variable }}` placeholders and executes logic blocks (like `{% for item in list %}`) using the provided data, generating the final HTML string.
5. **Writes Output:** It saves the resulting, fully populated HTML into `index.html`.

### Prerequisites

To run the build script, you need Python installed, along with two external libraries:

```bash
pip install pyyaml jinja2
```

### Running the Build

Whenever you update the YAML files in `data/` (to change content) or `template.html` (to change the design), run the following command in your terminal to regenerate your website:

```bash
python build.py
```

### Auto-Commit and Push

You can also use the build script to automatically add, commit, and push your changes to Git after building the website. Just pass the `-m` or `--msg` argument with your commit message:

```bash
python build.py -m "Update portfolio content"
```

## How to Modify It

You can easily adapt and extend this system to fit your evolving needs:

### 1. Adding New Simple Content Fields
- Open the relevant YAML file in the `data/` directory (e.g., `data/hero.yaml`) and add a new key-value pair. For example, if you want to add a Twitter link, add `twitter: "https://twitter.com/yourhandle"` under the `hero:` section.
- Open `template.html` and add the corresponding Jinja2 tag where you want it to appear, such as: `<a href="{{ hero.twitter }}">Twitter</a>`.

### 2. Adding Entirely New Sections
- Add a new structured block of data in a new or existing YAML file in `data/` (e.g., a list of `certifications`).
- Add a new HTML `<section>` in `template.html`.
- Use Jinja2 loops to dynamically render the content. For example:
  ```html
  {% for cert in certifications %}
    <div class="card">{{ cert.name }} - {{ cert.year }}</div>
  {% endfor %}
  ```

### 3. Modifying the Build Script (`build.py`)
- **Custom Filters:** If you need to format text in a specific way before it reaches the HTML (e.g., formatting dates, or converting Markdown text to HTML), you can write a Python function in `build.py` and register it as a custom Jinja2 filter.
- **Multiple Pages:** Currently, it only builds `index.html`. If your portfolio grows and you want separate pages (like `projects.html` or `blog.html`), you can modify `build.py` to loop through multiple templates, pass specific chunks of data to them, and write out multiple HTML files.