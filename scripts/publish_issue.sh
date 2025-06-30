#!/bin/bash
# Script to publish an issue to the public toolkit repository

# Usage: ./publish_issue.sh 01_or_first_start_delay

if [ -z "$1" ]; then
    echo "Usage: ./publish_issue.sh [issue_folder_name]"
    exit 1
fi

ISSUE_FOLDER=$1
SOURCE_PATH="../issues/$ISSUE_FOLDER"
DEST_PATH="../../vitals-vars-toolkits/$ISSUE_FOLDER"

# Check if source exists
if [ ! -d "$SOURCE_PATH" ]; then
    echo "Error: Issue folder $SOURCE_PATH not found"
    exit 1
fi

# Create destination directory
mkdir -p "$DEST_PATH"

# Copy only the public-facing content
echo "Copying issue content..."
cp -r "$SOURCE_PATH/README.md" "$DEST_PATH/"
cp -r "$SOURCE_PATH/code" "$DEST_PATH/"
cp -r "$SOURCE_PATH/toolkit" "$DEST_PATH/"
cp -r "$SOURCE_PATH/assets" "$DEST_PATH/"

# Remove any internal files that shouldn't be public
find "$DEST_PATH" -name "*.tmp" -delete
find "$DEST_PATH" -name ".DS_Store" -delete
rm -f "$DEST_PATH/linkedin_post.md"  # Remove social media drafts

echo "✅ Issue $ISSUE_FOLDER published to public repo"
echo "📁 Location: $DEST_PATH"
echo ""
echo "Next steps:"
echo "1. cd ../../vitals-vars-toolkits"
echo "2. git add $ISSUE_FOLDER"
echo "3. git commit -m 'Add Issue: $ISSUE_FOLDER'"
echo "4. git push"