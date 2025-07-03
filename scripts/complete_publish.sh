#!/bin/bash
# Complete the publishing process for toolkit

echo "Completing toolkit publication..."

# Navigate to the public repo
PUBLIC_REPO="../../vitals-vars-toolkits"

if [ ! -d "$PUBLIC_REPO" ]; then
    echo "❌ Public repository not found at $PUBLIC_REPO"
    exit 1
fi

cd "$PUBLIC_REPO" || exit 1

echo "📍 Current directory: $(pwd)"
echo "📊 Git status:"
git status --short

# Pull latest changes
echo -e "\n📥 Pulling latest changes..."
git pull origin main

# Push the committed changes
echo -e "\n📤 Pushing to GitHub..."
git push origin main

if [ $? -eq 0 ]; then
    echo -e "\n✅ Successfully published to GitHub!"
    echo "🔗 View at: https://github.com/mgc26/vitals-vars-toolkits/tree/main/02_ed_boarding"
else
    echo -e "\n❌ Push failed. Manual intervention may be required."
    echo "Try running these commands manually:"
    echo "  cd $(pwd)"
    echo "  git pull origin main"
    echo "  git push origin main"
fi