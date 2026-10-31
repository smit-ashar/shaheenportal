# Shaheen chapter portal

```
class-11/
  physics/
    01-units-and-measurements/index.html   <- one self-contained deck per chapter
    02-motion-in-a-straight-line/index.html (add next)
  chemistry/  biology/
class-12/
  physics/ ...
manifest.json         <- class > subject > chapter list (edit titles/order here)
build-portal.py       <- run after adding a chapter folder; marks it "ready"
index.html            <- the folder-explorer portal (open directly or deploy)
```

**Add a chapter:** create `class-11/physics/02-motion-in-a-straight-line/` (folder name = the `id` in manifest.json), drop the deck in as `index.html`, run `python3 build-portal.py`.

**Embedding in the real portal:** each deck is a standalone page, so load it in an `<iframe>`.
- Deck → portal messages: `{source:'shaheen-deck', type:'slidechange', index, total, title, section}` and `{source:'shaheen-deck', type:'next-chapter', chapter}` (sent from the last slide).
- Portal → deck messages: `{source:'shaheen-portal', type:'goto'|'next'|'prev', index}`.
- Keyboard inside a deck: arrows/Space, Home/End, M map, N notes, F fullscreen.

## Deploying on Vercel
1. Put the **contents** of this folder at the root of the repo / upload (so `index.html` sits at the top level, not inside a sub-folder).
2. Framework Preset: **Other**. Build Command: *(empty)*. Output Directory: *(empty)* or `.`.
3. Open `https://<your-project>.vercel.app/` — it should show the portal. A single chapter lives at `/class-11/physics/01-units-and-measurements/index.html`.
If you see `404 NOT_FOUND`, `index.html` is not at the deployment root — check the Root Directory setting in Project → Settings → General.
