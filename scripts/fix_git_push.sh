#!/bin/bash
# Fix git divergence and complete push

echo "Fixing git divergence and completing push..."

PUBLIC_REPO="../../vitals-vars-toolkits"
cd "$PUBLIC_REPO" || exit 1

echo "📍 Working in: $(pwd)"

# Configure merge strategy
echo -e "\n⚙️ Configuring merge strategy..."
git config pull.rebase false

# Pull with merge
echo -e "\n📥 Pulling and merging remote changes..."
git pull origin main --no-edit

# Now push
echo -e "\n📤 Pushing merged changes..."
git push origin main

if [ $? -eq 0 ]; then
    echo -e "\n✅ Successfully published to GitHub!"
    echo "🔗 View at: https://github.com/mgc26/vitals-vars-toolkits/tree/main/02_ed_boarding"
    
    # Show what was added
    echo -e "\n📦 Published toolkit contents:"
    ls -la 02_ed_boarding/
else
    echo -e "\n❌ Push failed."
fi