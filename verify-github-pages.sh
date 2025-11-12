#!/bin/bash

echo "=== GitHub Pages Deployment Verification ==="
echo ""

# Check git status
echo "1. Git Status:"
git status --short

echo ""
echo "2. Current Branch:"
git branch --show-current

echo ""
echo "3. Remote Configuration:"
git remote -v

echo ""
echo "4. Recent Commits:"
git log --oneline -n 5

echo ""
echo "5. Files in Root:"
ls -la | grep -E "(index\.html|\.nojekyll|CNAME)"

echo ""
echo "6. Push any pending changes:"
if [[ -n $(git status --porcelain) ]]; then
    echo "   Uncommitted changes detected!"
else
    echo "   No uncommitted changes"
fi

echo ""
echo "=== Next Steps ==="
echo "1. Enable GitHub Pages at:"
echo "   https://github.com/drgnman7777-maker/humainaintegration/settings/pages"
echo ""
echo "2. Select: Deploy from branch → master → / (root)"
echo ""
echo "3. Your site will be available at:"
echo "   https://drgnman7777-maker.github.io/humainaintegration/"
echo ""
echo "4. If using custom domain (humainaintegration.ai):"
echo "   - Add CNAME file with domain name"
echo "   - Configure DNS records"