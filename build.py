import yaml
from jinja2 import Environment, FileSystemLoader
import json
import os
import argparse
import subprocess

def build():
    data = {}
    data_dir = 'assets/data'
    
    # Load all YAML files from the data directory
    if os.path.exists(data_dir):
        for filename in os.listdir(data_dir):
            if filename.endswith('.yaml') or filename.endswith('.yml'):
                with open(os.path.join(data_dir, filename), 'r', encoding='utf-8') as file:
                    file_data = yaml.safe_load(file)
                    if file_data:
                        data.update(file_data)
    else:
        # Fallback to data.yaml if data dir doesn't exist
        if os.path.exists('data.yaml'):
            with open('data.yaml', 'r', encoding='utf-8') as file:
                data = yaml.safe_load(file)
    
    env = Environment(loader=FileSystemLoader('assets'))
    env.filters['tojson'] = json.dumps
    
    template = env.get_template('template.html')
    rendered_html = template.render(**data)
    
    with open('index.html', 'w', encoding='utf-8') as file:
        file.write(rendered_html)
        
    print("Successfully built index.html from data files")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Build the portfolio website.")
    parser.add_argument('-m', '--msg', type=str, help="Commit message for git. If provided, will automatically commit and push.", default=None)
    args = parser.parse_args()
    
    build()
    
    if args.msg:
        print(f"Committing and pushing with message: '{args.msg}'")
        try:
            subprocess.run(['git', 'add', '.'], check=True)
            subprocess.run(['git', 'commit', '-m', args.msg], check=True)
            subprocess.run(['git', 'push'], check=True)
            print("Successfully pushed to git.")
        except subprocess.CalledProcessError as e:
            print(f"Error during git operations: {e}")