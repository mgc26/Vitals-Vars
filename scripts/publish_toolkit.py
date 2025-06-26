#!/usr/bin/env python3
"""
Publish toolkit from private repo to public repo
Usage: python publish_toolkit.py 01_or_first_start_delay
"""

import os
import sys
import shutil
import subprocess
import yaml
from pathlib import Path

def load_config(issue_path):
    """Load publishing config from _meta.yaml"""
    meta_path = issue_path / "_meta.yaml"
    if meta_path.exists():
        with open(meta_path) as f:
            return yaml.safe_load(f)
    return {"publish": True}  # Default config

def prepare_toolkit(issue_name, source_repo, temp_dir):
    """Copy and prepare toolkit files"""
    issue_path = source_repo / "issues" / issue_name
    toolkit_path = issue_path / "_toolkit"
    
    if not toolkit_path.exists():
        print(f"❌ No _toolkit folder found in {issue_name}")
        return False
    
    # Load config
    config = load_config(issue_path)
    if not config.get("publish", True):
        print(f"⏭️  Issue {issue_name} marked as do-not-publish")
        return False
    
    # Copy toolkit contents
    dest_path = temp_dir / issue_name
    shutil.copytree(toolkit_path, dest_path)
    
    # Clean up any internal files
    for pattern in ["*.tmp", ".DS_Store", "_*", "*.draft.*"]:
        for file in dest_path.rglob(pattern):
            file.unlink()
    
    print(f"✅ Prepared toolkit: {issue_name}")
    return True

def publish_to_github(issue_name, temp_dir, public_repo_path):
    """Push toolkit to public GitHub repo"""
    source_path = temp_dir / issue_name
    dest_path = public_repo_path / issue_name
    
    # Remove existing if present
    if dest_path.exists():
        shutil.rmtree(dest_path)
    
    # Copy new version
    shutil.copytree(source_path, dest_path)
    
    # Git operations
    os.chdir(public_repo_path)
    subprocess.run(["git", "add", issue_name])
    subprocess.run(["git", "commit", "-m", f"Update toolkit: {issue_name}"])
    subprocess.run(["git", "push"])
    
    print(f"📤 Published to GitHub: {issue_name}")

def main():
    if len(sys.argv) < 2:
        print("Usage: python publish_toolkit.py <issue_name>")
        print("Example: python publish_toolkit.py 01_or_first_start_delay")
        sys.exit(1)
    
    issue_name = sys.argv[1]
    
    # Paths
    script_dir = Path(__file__).parent
    source_repo = script_dir.parent
    public_repo_path = source_repo.parent / "vitals-vars-toolkits"
    temp_dir = Path("/tmp/vitals_vars_publish")
    
    # Validate public repo exists
    if not public_repo_path.exists():
        print(f"❌ Public repo not found at {public_repo_path}")
        print("Please clone the public repo next to this one")
        sys.exit(1)
    
    # Clean temp directory
    if temp_dir.exists():
        shutil.rmtree(temp_dir)
    temp_dir.mkdir()
    
    try:
        # Prepare and publish
        if prepare_toolkit(issue_name, source_repo, temp_dir):
            publish_to_github(issue_name, temp_dir, public_repo_path)
            print(f"\n✨ Successfully published {issue_name}")
            print(f"🔗 View at: https://github.com/mgc26/vitals-vars-toolkits/tree/main/{issue_name}")
        
    finally:
        # Cleanup
        if temp_dir.exists():
            shutil.rmtree(temp_dir)

if __name__ == "__main__":
    main()