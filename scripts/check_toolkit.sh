#!/bin/bash
# Check if a toolkit is ready to publish

if [ -z "$1" ]; then
    echo "Usage: ./check_toolkit.sh <issue_folder>"
    echo "Example: ./check_toolkit.sh 01_or_first_start_delay"
    exit 1
fi

ISSUE=$1
TOOLKIT_PATH="../issues/$ISSUE/_toolkit"

echo "🔍 Checking toolkit for: $ISSUE"
echo "================================"

# Check if _toolkit exists
if [ ! -d "$TOOLKIT_PATH" ]; then
    echo "❌ No _toolkit folder found"
    exit 1
fi

echo "✅ _toolkit folder exists"

# Check required subdirectories
for dir in sql python dashboards guides; do
    if [ -d "$TOOLKIT_PATH/$dir" ]; then
        count=$(find "$TOOLKIT_PATH/$dir" -type f | wc -l)
        echo "✅ $dir/ - $count files"
    else
        echo "⚠️  $dir/ - missing"
    fi
done

# Check for README
if [ -f "$TOOLKIT_PATH/README.md" ]; then
    echo "✅ README.md present"
else
    echo "❌ README.md missing"
fi

# Check for common issues
echo ""
echo "🔍 Checking for issues..."

# Check for internal files that shouldn't be published
internal_files=$(find "$TOOLKIT_PATH" -name "*.tmp" -o -name ".DS_Store" -o -name "_*" -o -name "*.draft.*" 2>/dev/null)
if [ -n "$internal_files" ]; then
    echo "⚠️  Found internal files that should be removed:"
    echo "$internal_files"
else
    echo "✅ No internal files found"
fi

# Summary
echo ""
echo "================================"
if [ -f "$TOOLKIT_PATH/README.md" ] && [ -d "$TOOLKIT_PATH/sql" ] && [ -d "$TOOLKIT_PATH/python" ]; then
    echo "✅ Toolkit appears ready to publish!"
    echo "Run: python publish_toolkit.py $ISSUE"
else
    echo "❌ Toolkit needs work before publishing"
fi